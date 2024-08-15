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
@Time       : 2023/7/4 17:40
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, List

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import VIEW, AuthSourceType, DataSourceType
from superset.v2.datasources.dao import DataSourceDAO

logger = logging.getLogger(__name__)


class APIDataSourceCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> dict:
        self.validate()
        return self._model.api_datasource_data

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(VIEW)


class APIDataSourceListCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        res = DataSourceDAO.find_by_type(DataSourceType.API)
        if self._actor.is_admin:
            return [
                {
                    "id": item.id,
                    "name": item.name,
                    "d_type": item.d_type,
                } for item in res
            ]

        data_auth = DataSourceDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASOURCE, self._actor.id, VIEW)
        return [
            {
                "id": item.id,
                "name": item.name,
                "d_type": item.d_type,
            } for item in res if item.id in data_auth
        ]


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
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(VIEW)


class TokenAPIListCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        res = DataSourceDAO.find_by_api_tables_by_type(
            DataSourceType.TOKEN_API)
        if self._actor.is_admin:
            return [
                {
                    "api_table_id": item[0],
                    "name": item[2],
                } for item in res
            ]

        data_auth = DataSourceDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASOURCE, self._actor.id, VIEW)
        return [
            {
                "api_table_id": item[0],
                "name": item[2],
            } for item in res if item[1] in data_auth
        ]
