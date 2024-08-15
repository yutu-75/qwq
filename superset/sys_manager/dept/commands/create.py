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
@Time       : 2023/3/17 13:49
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Dict, Any

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import MenuName
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.sys_manager.dept.dao import SysDeptDAO, SysDeptUsersDAO
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.sys_manager.permission.dao import SysAuthDAO
from superset.v2.user.dao import UserV2DAO


class CreateSysDeptCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self):
        self.validate()
        dept = SysDeptDAO.create(self._properties)
        if dept.top_id == 0:
            dept.top_id = dept.id
            SysDeptDAO.save(dept)
        return dept

    def validate(self) -> None:
        """校验组织是否存在"""
        menu = SysMenuDAO.find_by_name(MenuName.DEPT_MANAGEMENT)
        menu.can_access()
        if self._properties["pid"] == 0:
            self._properties["level"] = 0

        else:
            parent_dept = SysDeptDAO.find_by_id(self._properties["pid"])
            if parent_dept is None:
                raise HTTPError(Messages.PARENT_DEPT_NOT_EXIST, 400)

            self._properties["level"] = parent_dept.level + 1
            self._properties["top_id"] = parent_dept.top_id

        # 校验当前组织是否存在
        dept = SysDeptDAO.get_by_pid_title(
            self._properties["pid"], self._properties["title"])
        if dept is not None:
            raise HTTPError(Messages.DEPT_EXIST, 400)


class CreateSysDeptUsersCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._model = None
        self._properties = data

    def run(self):
        self.validate()
        SysDeptUsersDAO.bulk_save_dept_users(self._model,
                                             self._properties["user_ids"])
        SysAuthDAO.del_user_auth(self._properties["user_ids"][0])

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.DEPT_MANAGEMENT)
        menu.can_access()

        self._model = SysDeptDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        top_id = self._model.top_id
        users = UserV2DAO.find_by_ids(self._properties["user_ids"])
        for user in users:
            for dept in user.depts:
                if dept.top_id == top_id:
                    raise HTTPError("同一组织只可加入一次", 400)
