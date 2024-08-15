# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import json
import logging
import uuid
from typing import Dict, Any

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User
from werkzeug.datastructures import FileStorage

from superset import conf, db
from superset.commands.base import BaseCommand
from superset.constants import DatasetType
from superset.constants import MANAGE, GRANT, VIEW
from superset.datasets.commands.refresh import RefreshDatasetCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.sql_parse import ParsedQuery
from superset.utils.read_file import formdata_to_df
from superset.v2.databases.dao import DatabaseV2DAO
from superset.v2.datasets.dao import DatasetV2DAO
from superset.v2.datasets.group.dao import DatasetGroupDAO
from superset.v2.datasources.dao import DataSourceDAO
from superset.v2.utils.data_save_db import get_save_default_db, df_to_sql

logger = logging.getLogger(__name__)


class CreateDatasetV2Command(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self) -> Model:
        self.validate()
        dataset = DatasetV2DAO.create(self._properties, commit=False)

        def get_label_columns() -> dict:
            """从数据库字段说明获取字段别名， mongobi需特殊处理"""
            columns = self._properties["database"].get_columns(
                self._properties['table_name'],
                self._properties['schema']
            )
            cols = {}
            if not columns:
                return cols

            for item in columns:
                comment = item.get("comment")
                if not comment:
                    comment = item["name"]

                elif comment.startswith("{"):
                    try:
                        comment = json.loads(comment).get("name", comment)
                    except Exception as ex:
                        logger.error(ex)

                cols[item["name"]] = comment

            return cols

        label_columns = get_label_columns()
        dataset.fetch_metadata(label_columns=label_columns)
        dataset.add_user_permission(GRANT)
        return dataset

    def validate(self) -> None:
        group = DatasetGroupDAO.find_by_id(self._properties["table_group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        group.can_access(MANAGE)
        if not DatasetV2DAO.validate_uniqueness(
            self._properties["table_name"],
            self._properties["table_group_id"]
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

        datasource = DataSourceDAO.find_by_database_id(self._properties["database"])
        if datasource is None:
            raise HTTPError(Messages.IS_EXIST, 400)

        datasource.can_access(VIEW)
        self._properties["database"] = datasource.database
        if self._properties["database"] is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._properties["type_classify"] = DatasetType.DATABASE
        self._properties["custom_name"] = self._properties["table_name"]
        if self._properties.get("sql", False):
            self._properties['sql'] = 'SELECT * FROM ' + \
                                      self._properties['schema'] + '.' + \
                                      self._properties['table_name']


class CreateSQLDatasetCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self) -> Model:
        self.validate()
        dataset = DatasetV2DAO.create(self._properties, commit=False)
        db.session.flush()
        dataset.add_user_permission(GRANT)
        RefreshDatasetCommand(dataset.id).run()
        return dataset

    def validate(self) -> None:
        group = DatasetGroupDAO.find_by_id(self._properties["table_group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        group.can_access(MANAGE)
        database = DatabaseV2DAO.find_by_id(self._properties["database_id"])
        if database is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._properties["database"] = database
        if not DatasetV2DAO.validate_uniqueness(
            self._properties["table_name"],
            self._properties["table_group_id"]
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

        self._properties["type_classify"] = DatasetType.SQL
        self._properties["is_sqllab_view"] = True
        self._properties["custom_name"] = self._properties["table_name"]
        self._properties["sql"] = ParsedQuery(self._properties["sql"]).stripped()
        self._properties["columns"] = []


class CreateFileDatasetCommand(BaseCommand):
    def __init__(self, user: User, upload: FileStorage, data: Dict[str, Any]):
        self._actor = user
        self._upload = upload
        self._df = None
        self._properties = data

    def run(self, **kwargs) -> Model:
        df = formdata_to_df(self._upload)
        if isinstance(df, dict):
            sheet_name = kwargs.get("sheet_name")  # excel多个sheet时
            df = df.get(sheet_name, None)
            if df is None:
                raise HTTPError("请选择一个sheet", 400)

        self.validate()
        df_to_sql(
            df,
            self._properties["database"],
            self._properties["table_name"],
            self._properties["schema"],
        )
        # Creates SqlaTable (Dataset)
        dataset = DatasetV2DAO.create(self._properties, commit=False)
        # Updates columns and metrics from the dataset
        dataset.fetch_metadata()
        dataset.add_user_permission(GRANT)
        return dataset

    def validate(self) -> None:
        group = DatasetGroupDAO.find_by_id(self._properties["table_group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        group.can_access(MANAGE)
        if not self._properties["custom_name"]:
            raise HTTPError(Messages.DATASET_NAME_ERROR, 400)

        if not DatasetV2DAO.validate_uniqueness(
            self._properties["custom_name"],
            self._properties["table_group_id"]
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

        if DatasetV2DAO.find_by_table_name(self._properties["table_name"]):
            raise HTTPError('表名已存在，请重新命名', 400)

        if not isinstance(self._upload, FileStorage):
            raise HTTPError(Messages.FILE_NOT_UPLOADED, 400)

        self._properties["type_classify"] = DatasetType.EXCEL
        self._properties["database"] = get_save_default_db(self._actor)
        self._properties["schema"] = conf["UPLOAD_SCHEMA"]
        self._properties['sql'] = 'SELECT * FROM ' + \
                                  self._properties['schema'] + '.' + \
                                  self._properties['table_name']
