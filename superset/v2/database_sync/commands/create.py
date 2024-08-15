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

from datetime import datetime
from typing import Dict, Any

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import CreateMixin, BaseCommand
from superset.constants import MANAGE, GRANT
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.database_sync.database.dao import DataBaseSyncDAO
from superset.v2.database_sync.group.dao import DatabaseSyncGroupDAO


class DatabaseSyncName(CreateMixin, BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self, **kwargs):
        self.validate()
        database = DataBaseSyncDAO.create(self._properties)
        database.add_user_permission(GRANT)  # 写入权限
        return database

    def validate(self) -> None:
        group = DatabaseSyncGroupDAO.find_by_id(self._properties["group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        group.can_access(MANAGE)  # 验证当前分组是否有新建权限
        if not DataBaseSyncDAO.validate_uniqueness(
            self._properties["name"],
            self._properties["group_id"],
        ):
            raise HTTPError(Messages.DUPLICATE_NAME, 400)





