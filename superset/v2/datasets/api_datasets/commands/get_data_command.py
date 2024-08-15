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
@Time       : 2023/7/27 13:48
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Any, List

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import VIEW, MANAGE
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.datasets.api_datasets.dao import TableTaskDAO, TableTaskLogDAO
from superset.v2.datasets.dao import DatasetV2DAO
from superset.v2.datasources.api_datasources.dao import APITablesDAO
from superset.v2.utils.data_save_db import api_data_to_df


class APITableDataCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        df = api_data_to_df(
            self._model.configuration,
            self._model.data_path
        )
        limit = kwargs.get("limit", 20)
        df.head(int(limit))
        return df.to_dict(orient="records")

    def validate(self) -> None:
        self._model = APITablesDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.datasource.can_access(VIEW)


class DatasetTaskListCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        return [item.to_json() for item in self._model.table_tasks]

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)


class DatasetTaskLogInfoCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        page = int(kwargs.get("page", 1))
        limit = int(kwargs.get("limit", 20))
        return TableTaskLogDAO.search(
            self._model_id,
            self._model.name,
            page=page,
            limit=limit
        )

    def validate(self) -> None:
        self._model = TableTaskDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.table.can_access(MANAGE)
