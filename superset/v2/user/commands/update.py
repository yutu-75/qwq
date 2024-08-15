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

from superset.commands.base import BaseCommand, UpdateMixin
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import MenuName
from superset.models.user import UserV2
from superset.sys_manager.dept.dao import SysDeptDAO
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.sys_manager.permission.dao import SysAuthDAO
from superset.v2.role.dao import RoleV2DAO, RoleDAO
from superset.v2.user.dao import UserV2DAO

logger = logging.getLogger(__name__)


class UpdateUserV2Command(UpdateMixin, BaseCommand):
    def __init__(self, user: UserV2, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[UserV2] = None
        self._properties = data.copy()

    def run(self):
        self.validate()
        self._properties["roles"] = RoleDAO.find_by_ids(
            self._properties["roles"])
        if self._properties.get("password", False):
            self._properties["password"] = UserV2DAO.generate_password_hash(
                self._properties["password"])

        dept_ids = self._properties.pop("dept_id", [])
        if len(dept_ids) > 0:
            depts = SysDeptDAO.find_by_ids(dept_ids)
            dept_set = set()
            for dept in depts:
                if dept.top_id in dept_set:
                    raise HTTPError("同一组织只可加入一次", 400)
                else:
                    dept_set.add(dept.top_id)
            self._model.depts = depts

        UserV2DAO.update(self._model, self._properties)
        SysAuthDAO.del_user_auth(self._model.id)

    def validate(self):
        menu = SysMenuDAO.find_by_name(MenuName.USER_MANAGEMENT)
        menu.can_access()

        self._model = UserV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        # 判断是否编辑自生, 自身无法编辑超级管理员权限
        if self._model.id == self._actor.id:
            if self._properties["is_admin"] != self._model.is_admin:
                raise HTTPError(Messages.CLOSE_SUPERADMIN_ERROR, 400)

        if not self._actor.is_admin:
            del self._properties["is_admin"]

        if UserV2DAO.validate_uniqueness(
            self._properties["username"],
            self._properties["email"],
            self._model.id,
        ):
            raise HTTPError(Messages.USERNAME_OR_EMAIL_USED, 400)

        if not self._properties.get("first_name"):
            self._properties["first_name"] = self._properties["cn_name"][1:]
            self._properties["last_name"] = self._properties["cn_name"][:1]


class UpdateUserActiveCommand(UpdateMixin, BaseCommand):
    def __init__(self, user: UserV2, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._model: UserV2 = None
        self._properties = data

    def run(self):
        self.validate()
        return UserV2DAO.update(self._model, self._properties)

    def validate(self):
        menu = SysMenuDAO.find_by_name(MenuName.USER_MANAGEMENT)
        menu.can_access()

        self._model = UserV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)
