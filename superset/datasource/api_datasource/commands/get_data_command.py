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

# -*- coding: utf-8 -*-

"""
@Time       : 2023/7/4 17:40
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, List

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.datasource.api_datasource.dao import DataSourceDAO
from superset.exceptions import HTTPError

logger = logging.getLogger(__name__)


class APIDataSourceInfoCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> dict:
        self.validate()
        return {
            "tables": [
                {
                    "name": item.name,
                    "configuration": item.configuration,
                    "data_path": item.data_path,
                } for item in self._model.api_tables
            ],
            **self._model.to_json()
        }

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if self._model is None:
            raise Exception('Dataset does not exist')


class APIDataSourceListCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[dict]:
        res = DataSourceDAO.find_by_type()
        return [item.to_json() for item in res]


class APIDataSourceTableListCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        return [item.to_json() for item in self._model.api_tables]

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if self._model_id is None:
            raise HTTPError('The datasource does not exist', 400)
