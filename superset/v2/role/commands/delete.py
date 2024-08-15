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
from typing import Optional

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import AuthTargetType, MenuName
from superset.migrations.shared.security_converge import Role
from superset.models.user import UserV2
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.v2.role.dao import RoleV2DAO, UserRoleDAO

logger = logging.getLogger(__name__)


class RoleV2DeleteCommand(BaseCommand):
    def __init__(self, user: UserV2, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[Role] = None

    def run(self):
        self.validate()
        UserRoleDAO.delete_by_role_id(self._model.id, False)
        RoleV2DAO.delete(self._model, False)
        RoleV2DAO.delete_auth_by_target({
            "auth_target": self._model_id,
            "auth_target_type": AuthTargetType.ROLE,
        }, commit=False)
        self.archiving()

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.ROLE_MANAGEMENT)
        menu.can_access()

        self._model = RoleV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        if self._actor.is_admin:
            return

        if not self._model.is_creator(self._actor.id):
            raise HTTPError(Messages.DEL_ROLE_ERR, 400)

    def archiving(self):
        """将删除的role归档"""
        doc_json = {
            "id": self._model.id,
            "name": self._model.name,
            "creator_id": self._model.creator_id
        }
        RoleV2DAO.archiving_docs("role", doc_json)
