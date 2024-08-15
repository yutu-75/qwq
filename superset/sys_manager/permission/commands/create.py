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
from superset.constants import MenuName, MANAGE, AuthType, DatabaseAuthType
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.sys_manager.permission.dao import SysAuthDAO, DatabaseAuthDAO


class CreateSysAuthCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self):
        self.validate()
        SysAuthDAO.save_auth(self._properties["perm"])

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.PERMISSION_MANAGEMENT)
        menu.can_access(MANAGE)


class CreateDatabaseAuthCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self):
        self.validate()
        DatabaseAuthDAO.save_auth(self._properties["perm"])
        item = self._properties["perm"][0]
        max_auth = dict()
        if item.get("auth_target_type") == AuthType.USER.value:
            max_auth = DatabaseAuthDAO.find_perm_by_user_id(
                user_id=item["auth_target"],
                database_id=item["database_id"],
                schema=item["schema"]
            )
        return max_auth

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.PERMISSION_MANAGEMENT)
        menu.can_access(MANAGE)
