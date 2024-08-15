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
@Time       : 2023/3/29 13:40
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Dict, Any, Optional

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.dashboard import Dashboard
from superset.constants import MANAGE
from superset.v2.dashboards.dao import DashboardV2DAO
from superset.v2.dashboards.group.dao import DashboardGroupDAO


class DashboardV2MoveCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[Dashboard] = None

    def run(self) -> Dashboard:
        self.validate()
        dashboard = DashboardV2DAO.update(self._model, self._properties)
        return dashboard

    def validate(self):
        self._model = DashboardV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
        # 校验重名
        if not DashboardV2DAO.validate_uniqueness(
            self._properties["dashboard_title"],
            self._properties["dashboard_group_id"]
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

        # 重命名事件
        if self._properties["dashboard_group_id"] == self._model.dashboard_group_id:
            return

        # 移动到顶层
        if self._properties["dashboard_group_id"] == 0:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        # 查询分组是否存在
        group = DashboardGroupDAO.find_by_id(self._properties["dashboard_group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)
