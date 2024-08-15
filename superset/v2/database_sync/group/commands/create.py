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

import logging
from typing import Any, Dict

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand, CreateMixin
from superset.constants import GRANT, MANAGE, AuthType
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.v2.database_sync.group.dao import DatabaseSyncGroupDAO

logger = logging.getLogger(__name__)


class CreateDatabaseSyncGroupCommand(CreateMixin, BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data.copy()

    def run(self):
        self.validate()
        group = DatabaseSyncGroupDAO.create(self._properties)
        # 写入权限
        group.add_user_permission(GRANT)
        return group

    def validate(self) -> None:
        # 验证父ID是否存在
        pid = self._properties["pid"]
        if pid == 0:
            menu = SysMenuDAO.find_by_name(AuthType.DATABASE_SYNC)
            menu.can_access(MANAGE)
            level = 0

        else:
            group = DatabaseSyncGroupDAO.find_by_id(pid)
            if group is None:
                raise HTTPError(Messages.PARENT_NOT_EXIST, 400)

            group.can_access(MANAGE)
            level = group.level + 1

        self._properties["level"] = level
        self._properties["type"] = None
        # 检查当前分组是否存在
        if DatabaseSyncGroupDAO.validate_uniqueness(
            self._properties["pid"],
            self._properties["name"],
        ):
            raise HTTPError(Messages.GROUP_IS_EXIST, 400)
