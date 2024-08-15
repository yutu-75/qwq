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
from typing import Any, Dict
import pandas as pd
from flask_sqlalchemy import Model

from werkzeug.datastructures import FileStorage

from superset.commands.base import BaseCommand, CreateMixin
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import MenuName
from superset.models.user import UserV2
from superset.sys_manager.dept.dao import SysDeptDAO
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.v2.role.dao import RoleV2DAO, RoleDAO
from superset.v2.user.dao import UserV2DAO
from superset.v2.utils.password_strength import PasswordStrength

logger = logging.getLogger(__name__)


class CreateUserV2Command(CreateMixin, BaseCommand):
    def __init__(self, user: UserV2, data: Dict[str, Any]):
        self._actor = user
        self._properties = data.copy()

    def run(self) -> Model:
        self.validate()
        self._properties["roles"] = RoleDAO.find_by_ids(
            self._properties["roles"])
        self._properties["password"] = UserV2DAO.generate_password_hash(
            self._properties["password"])
        user = UserV2DAO.create(self._properties)
        return user

    def validate(self) -> None:
        if not PasswordStrength(self._properties['password']).check_pwd_strength:
            raise HTTPError(Messages.PWD_STRENGTH_ERROR, 400)

        menu = SysMenuDAO.find_by_name(MenuName.USER_MANAGEMENT)
        menu.can_access()

        if UserV2DAO.validate_uniqueness(
            self._properties["username"],
            self._properties["email"],
        ):
            raise HTTPError(Messages.USERNAME_OR_EMAIL_USED, 400)

        if not self._actor.is_admin:
            del self._properties["is_admin"]

        dept_ids = self._properties.pop("dept_id", [])
        if len(dept_ids) > 0:
            depts = SysDeptDAO.find_by_ids(dept_ids)
            dept_set = set()
            for dept in depts:
                if dept.top_id in dept_set:
                    raise HTTPError("同一组织只可加入一次", 400)
                else:
                    dept_set.add(dept.top_id)
            self._properties["depts"] = depts

        if not self._properties.get("first_name"):
            self._properties["first_name"] = self._properties["cn_name"][1:]
            self._properties["last_name"] = self._properties["cn_name"][:1]


class ImportUsersCommand(CreateUserV2Command):
    def __init__(self, user: UserV2, upload: FileStorage):
        self._actor = user
        self._upload = upload

    def run(self) -> None:
        df = pd.read_excel(io=self._upload)
        UserV2DAO.mulk_insert_users(df, self._actor)
