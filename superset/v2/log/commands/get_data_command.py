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
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any

from flask_appbuilder import Model

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.user import UserV2
from superset.constants import AuthSourceType
from superset.v2.log.dao import LogV2DAO
from superset.v2.user.dao import UserV2DAO

logger = logging.getLogger(__name__)


class LogV2ListCommand(BaseCommand):
    def __init__(self, user: UserV2, data: dict = None):
        self._actor = user
        self._properties = data or dict()

    def run(self, **kwargs: Any) -> Model:
        data = LogV2DAO.get_all(self._properties)
        return data

    def validate(self) -> None:
        if not self._actor.is_admin:
            if not UserV2DAO.validate_auth_source(
                    auth_source=7,
                    auth_source_type=AuthSourceType.MENU,
                    user_id=self._actor.id,
                    privilege_value=4,
            ):
                raise HTTPError(Messages.FORBIDDEN, 403)


class LogV2InfoCommand(BaseCommand):
    def __init__(self, user: UserV2, model_id: str):
        self.model_id = model_id
        self._actor = user

    def run(self, **kwargs: Any):
        self.validate()
        obj = LogV2DAO.find_by_id(self.model_id)
        data = {
            "id": obj.id,
            "dashboard_id": obj.dashboard_id,
            "slice_id": obj.slice_id,
            "duration_ms": obj.duration_ms,
            "action": obj.action,
            "referrer": obj.referrer,
            "json": obj.json,
            "dttm": obj.dttm,
            "user_id": obj.user_id,
            "user": {
                'username': obj.user.username,
                'cn_name': obj.user.cn_name,
                'first_name': obj.user.first_name,
                'last_name': obj.user.last_name,
            },
        }
        return data

    def validate(self) -> None:
        if not self._actor.is_admin:
            if not UserV2DAO.validate_auth_source(
                    auth_source=7,
                    auth_source_type=AuthSourceType.MENU,
                    user_id=self._actor.id,
                    privilege_value=4,
            ):
                raise HTTPError(Messages.FORBIDDEN, 403)
