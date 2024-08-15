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
from typing import Any, List, Optional

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User

from superset.constants import MenuName
from superset.sys_manager.dept.dao import SysDeptDAO
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.utils.cache import memoized_func

from superset.commands.base import BaseCommand
from superset.models.user import UserV2
from superset.v2.user.dao import UserV2DAO

logger = logging.getLogger(__name__)


class UserV2ListCommand(BaseCommand):
    def __init__(self, user: UserV2, **kwargs: Any):
        self._actor = user
        self._properties = kwargs

    def run(self, **kwargs: Any) -> Model:
        self.validate()
        if self._actor.is_admin:
            return UserV2DAO.get_all_user(self._properties)

        self._properties["depts_id"] = SysDeptDAO.find_depts_id_by_user(self._actor)
        return UserV2DAO.get_all_user(self._properties)


class UserV2InfoCommand(BaseCommand):
    def __init__(self, user: UserV2, model_id: str):
        self.model_id = model_id
        self._actor = user

    def run(self, **kwargs: Any):
        self.validate()
        user = UserV2DAO.find_by_id(self.model_id)
        data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "cn_name": user.cn_name,
            "is_admin": user.is_admin,
            "email": user.email,
            "active": user.active,
            "roles": [
                {
                    "id": role.id,
                    "name": role.name,
                } for role in user.roles
            ],
            "depts": [
                {
                    "id": dept.id,
                    "title": dept.title,
                } for dept in user.depts
            ],
            "last_login": user.last_login,
            "login_count": user.login_count,
            "fail_login_count": user.fail_login_count,
            "created_on": user.created_on,
            "changed_on": user.changed_on,
            "created_by_fk": user.created_by_fk,
            "changed_by_fk": user.changed_by_fk,
        }
        return data

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.USER_MANAGEMENT)
        menu.can_access()


class UserAuthDetailCommand(BaseCommand):
    def __init__(self, user: User, data: dict):
        self._actor = user
        self._properties = data

    def run(self, **kwargs: Any) -> List[dict]:
        if self._actor.is_admin:
            data_auth = UserV2DAO.find_target_perm_by_source(**self._properties)
            return UserV2DAO.find_auth_detail(
                data_auth=data_auth,
                auth_source=self._properties["auth_source"],
                auth_source_type=self._properties["auth_source_type"],
                **kwargs)

        depts_id = SysDeptDAO.find_depts_id_by_user(self._actor)
        data_auth = UserV2DAO.find_users_perm(depts_id=depts_id, **self._properties)
        return UserV2DAO.find_auth_detail(
            data_auth=data_auth,
            auth_source=self._properties["auth_source"],
            auth_source_type=self._properties["auth_source_type"],
            depts_id=depts_id,
            **kwargs)
