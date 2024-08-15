# -*- coding: utf-8 -*-
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

"""
@Time       : 2023/5/9 16:59
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, List, Dict, Optional

import simplejson
from flask_appbuilder.security.sqla.models import User
from werkzeug.datastructures import FileStorage

from superset.charts.commands.exceptions import ChartDataQueryFailedError
from superset.charts.data.commands.get_data_command import ChartDataCommand
from superset.commands.base import BaseCommand
from superset.common.query_context import QueryContext
from superset.common.query_context_factory import QueryContextFactory
from superset.connectors.sqla.models import SqlaTable
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import AuthSourceType, VIEW, MANAGE
from superset.utils.core import json_int_dttm_ser
from superset.utils.read_file import formdata_to_df
from superset.v2.datasets.dao import DatasetV2DAO

logger = logging.getLogger(__name__)


class DatasetListDataCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[Dict]:
        name = kwargs.get("name", False)
        database_id = kwargs.get("database_id", None)
        schema = kwargs.get("schema", None)
        if self._actor.is_admin:
            return DatasetV2DAO.get_admin_datasets(name, database_id, schema)

        data_auth = DatasetV2DAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASET, self._actor.id, VIEW)
        data_auth = set(data_auth.keys())
        return DatasetV2DAO.get_user_datasets(name, data_auth, database_id, schema)


class DatasetDataCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> dict:
        self.validate()
        cls_filter_ids = self._model.cls_filter_columns_ids
        column_name_list = []
        columns = []
        for item in self._model.columns:
            if item.id not in cls_filter_ids:
                columns.append(item.data)
                column_name_list.append(item.column_name)

        query_context = self.create_query_context(column_name_list, **kwargs)
        try:
            res = ChartDataCommand(query_context).run()
        except ChartDataQueryFailedError as ex:
            raise HTTPError(str(ex), 400)

        # pd.Timestamp转日期时间字符串
        data = simplejson.dumps(
            res["queries"][0]["data"],
            default=json_int_dttm_ser,
            ignore_nan=True,
            encoding=None,
        )
        return {
            "table_info": columns,
            "data": simplejson.loads(data)
        }

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(VIEW)

    def create_query_context(self, column_name_list, **kwargs: Any) -> QueryContext:
        force = kwargs.get("force", 1)
        limit = int(kwargs.get("limit", 20))

        datasource = {
            "id": self._model_id,
            "type": self._model.datasource_type
        }

        queries = [{
            "columns": column_name_list,
            "row_limit": limit
        }]
        return QueryContextFactory().create(
            datasource=datasource,
            queries=queries,
            force=force
        )


class DatasetInfoCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> dict:
        self.validate()
        cls_filter_ids = self._model.cls_filter_columns_ids
        column_name_list = []
        columns = []
        for item in self._model.columns:
            if item.id not in cls_filter_ids:
                columns.append(item.data)
                column_name_list.append(item.column_name)

        data = self._model.to_json()
        data.update({"columns": columns})
        return data

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(VIEW)


class DatasetChartsListCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[SqlaTable] = None

    def run(self) -> List[dict]:
        self.validate()
        return [{
            "id": item.id,
            "title": item.slice_name
        } for item in self._model.slices]

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)


class DatasetTableColumnsDataCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> dict:
        self.validate()

        # 调用database get_columns查询
        columns = self._model.database.get_columns(self._model.table_name)
        for col in columns:
            col["type"] = col["type"].compile()
        return columns

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(VIEW)


class FileDataCommand(BaseCommand):
    def __init__(self, user: User, upload: FileStorage):
        self._actor = user
        self._upload = upload

    def run(self, **kwargs) -> List[Dict]:
        try:
            df = formdata_to_df(self._upload)
        except UnicodeDecodeError as ex:
            logger.error(dir(ex))
            raise HTTPError(str(ex), 400)

        if isinstance(df, dict):
            return [{
                "sheet": sheet,
                "result": _.to_dict(orient="records")
            } for sheet, _ in df.items()]

        return df.to_dict(orient="records")
