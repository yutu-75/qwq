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
@Time       : 2023/3/29 12:55
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Dict, Any

from flask_appbuilder.security.sqla.models import User
from flask_sqlalchemy import Model

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import GRANT, MANAGE, AuthType
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.v2.dashboards.group.dao import DashboardGroupDAO


class CreateDashboardGroupCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self) -> Model:
        self.validate()
        group = DashboardGroupDAO.create(self._properties)
        # 写入权限
        group.add_user_permission(GRANT)
        return group

    def validate(self) -> None:
        if self._properties["pid"] == 0:
            menu = SysMenuDAO.find_by_name(AuthType.DASHBOARD)
            menu.can_access(MANAGE)
            self._properties["level"] = 0

        else:
            parent_group = DashboardGroupDAO.find_by_id(self._properties["pid"])
            if parent_group is None:
                raise HTTPError(Messages.PARENT_NOT_EXIST, 400)

            parent_group.can_access(MANAGE)
            self._properties["level"] = parent_group.level + 1

        # 检查当前分组是否存在
        if DashboardGroupDAO.validate_uniqueness(
            self._properties["pid"],
            self._properties["name"],
        ):
            raise HTTPError(Messages.GROUP_IS_EXIST, 400)
