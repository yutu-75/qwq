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
from typing import Any, Dict, Optional

from flask_appbuilder.security.sqla.models import Role

from superset.commands.base import BaseCommand, UpdateMixin
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import MenuName
from superset.models.user import UserV2
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.v2.role.dao import RoleV2DAO

logger = logging.getLogger(__name__)


class RoleV2UpdateCommand(UpdateMixin, BaseCommand):
    def __init__(self, user: UserV2, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._properties = data.copy()
        self._model = None

    def run(self):
        self.validate()
        RoleV2DAO.update(self._model, self._properties)

    def validate(self):
        menu = SysMenuDAO.find_by_name(MenuName.ROLE_MANAGEMENT)
        menu.can_access()

        self._model = RoleV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        if self._model.name == self._properties["name"]:
            return

        if RoleV2DAO.validate_name_exist(self._properties["name"]):
            raise HTTPError(Messages.IS_EXIST, 400)


class RoleV2RemoveUserCommand(UpdateMixin, BaseCommand):
    def __init__(self, user: UserV2, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[Role] = None

    def run(self) -> None:
        self.validate()
        RoleV2DAO.delete_role_users(self._model, self._properties["user_ids"])

    def validate(self):
        menu = SysMenuDAO.find_by_name(MenuName.ROLE_MANAGEMENT)
        menu.can_access()

        self._model = RoleV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

    @staticmethod
    def archiving(model_list):
        """将删除的user role归档"""
        data = [{
            'role_id': model.role_id,
            'user_id': model.user_id,
            'id': model.id,
        } for model in model_list
        ]
        RoleV2DAO.archiving_docs("user_role", {"data": data})
