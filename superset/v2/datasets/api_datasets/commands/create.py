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
@Time       : 2023/7/12 13:57
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from datetime import datetime
from typing import Dict, Any

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User

from superset import conf, db
from superset.commands.base import BaseCommand
from superset.constants import DatasetType, MANAGE, GRANT, VIEW
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.datasets.api_datasets.dao import TableTaskDAO, TableTaskLogDAO
from superset.v2.datasets.dao import DatasetV2DAO
from superset.v2.datasets.group.dao import DatasetGroupDAO
from superset.v2.datasources.api_datasources.dao import APITablesDAO
from superset.v2.utils.data_save_db import api_data_to_df, get_save_default_db, \
    df_to_sql


class CreateAPIDatasetCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._api_table = None

    def run(self) -> Model:
        self.validate()
        df = api_data_to_df(
            self._api_table.configuration,
            self._api_table.data_path
        )
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
        self._api_table = APITablesDAO.find_by_id(self._properties["api_table_id"])
        datasource = self._api_table.datasource
        if datasource is None:
            raise HTTPError(Messages.IS_EXIST, 400)

        datasource.can_access(VIEW)
        if not DatasetV2DAO.validate_uniqueness(
            self._properties["custom_name"],
            self._properties["table_group_id"],
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

        self._properties["type_classify"] = DatasetType.API
        self._properties["database"] = get_save_default_db(self._actor)
        self._properties["schema"] = conf["UPLOAD_SCHEMA"]
        self._properties["table_name"] = self._api_table.table_name
        self._properties['sql'] = 'SELECT * FROM ' + \
                                  self._properties['schema'] + '.' + \
                                  self._properties['table_name']


class CreateAPIDatasetTaskCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._model = None
        self._properties = data

    def run(self) -> Model:
        self.validate()
        self._properties["table_id"] = self._model_id
        self._properties["api_table_id"] = self._model.api_table_id
        self._properties["status"] = 1  # 任务默认为等待执行
        task = TableTaskDAO.create(self._properties)
        if self._properties["rate"] == 0:
            task.status = 0
            self.update_api_dataset(self._model, self._model.api_table, task)

        return task

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        if self._model.type_classify != DatasetType.API:
            raise HTTPError(Messages.API_DATASET_DEFINE_TASKS, 400)

        self._model.can_access(MANAGE)
        if TableTaskDAO.validate_uniqueness(
            self._properties["name"],
            self._model_id
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

    def update_api_dataset(self, table: Model, api_table: Model, task: Model):
        dt = datetime.now()
        task.last_exec_time = dt
        log = {
            "table_task_id": task.id,
            "task_id": "",
            "start_time": int(dt.timestamp() * 1000)
        }
        if api_table is None:
            log["info"] = "API数据源不存在或已被删除"
            log["status"] = 0
            task.last_exec_status = "Failed"
            task.status = log["status"]
            return
        try:
            # 获取默认上传数据库
            database = get_save_default_db(self._actor)
            # 将数据集指向写入的默认数据库
            DatasetV2DAO.update(table, {"database_id": database.id}, commit=False)
            df = api_data_to_df(
                api_table.configuration,
                api_table.data_path
            )
            df_to_sql(
                df,
                database,
                api_table.table_name,
                conf["UPLOAD_SCHEMA"],
                if_exists=self._properties["update_type"]
            )
            log["info"] = "Completed"
            log["status"] = 1
            task.last_exec_status = "Completed"
        except Exception as ex:
            log["info"] = str(ex)
            log["status"] = 0
            task.last_exec_status = "Failed"
            task.status = log["status"]
            return

        log["end_time"] = int(datetime.now().timestamp() * 1000)
        db.session.merge(task)
        TableTaskLogDAO.create(log)


class RunAPIDatasetTaskCommand(CreateAPIDatasetTaskCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._table = None
        self._properties = dict()

    def run(self) -> Model:
        self.validate()
        self.update_api_dataset(self._table, self._model.api_table, self._model)
        return self._model

    def validate(self) -> None:
        self._model = TableTaskDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._table = self._model.table
        self._table.can_access(MANAGE)
        self._properties["update_type"] = self._model.update_type
