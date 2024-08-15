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
@Time       : 2023/3/29 14:10
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Dict, Any

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.dashboard import Dashboard
from superset.constants import GRANT, MANAGE
from superset.v2.dashboards.dao import DashboardV2DAO
from superset.v2.dashboards.group.dao import DashboardGroupDAO


class DashboardV2CreateCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self) -> Dashboard:
        self.validate()
        dashboard = DashboardV2DAO.create(self._properties)
        dashboard.add_user_permission(GRANT)  # 写入权限
        return dashboard

    def validate(self) -> None:
        group = DashboardGroupDAO.find_by_id(self._properties["dashboard_group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        group.can_access(MANAGE)
        if not DashboardV2DAO.validate_uniqueness(
            self._properties["dashboard_title"],
            self._properties["dashboard_group_id"],
        ):
            raise HTTPError(Messages.IS_EXIST, 400)
