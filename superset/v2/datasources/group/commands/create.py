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

from superset.commands.base import BaseCommand, CreateMixin
from superset.constants import MANAGE, AuthType
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.v2.datasources.group.dao import DataSourceGroupDAO


class CreateDataSourceGroupCommand(CreateMixin, BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._model = None
        self._properties = data.copy()

    def run(self):
        self.validate()
        group = DataSourceGroupDAO.create(self._properties)
        # 写入权限
        group.add_user_permission(8)
        return group

    def validate(self) -> None:
        pid = self._properties["pid"]
        if pid == 0:
            menu = SysMenuDAO.find_by_name(AuthType.DATASOURCE)
            menu.can_access(MANAGE)
            level = 0

        else:
            group = DataSourceGroupDAO.find_by_id(pid)
            if group is None:
                raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

            group.can_access(MANAGE)
            level = group.level + 1

        # 检查当前分组是否存在
        if DataSourceGroupDAO.validate_uniqueness(
            self._properties["pid"],
            self._properties["name"],
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

        self._properties["level"] = level
