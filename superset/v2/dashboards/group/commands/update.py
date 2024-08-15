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
@Time       : 2023/3/29 12:59
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Dict, Any, Optional

from flask_appbuilder.security.sqla.models import User, Model

from superset import db
from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.dashboard import DashboardGroup
from superset.constants import MANAGE
from superset.v2.dashboards.group.dao import DashboardGroupDAO


class UpdateDashboardGroupCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[DashboardGroup] = None

    def run(self) -> Model:
        self.validate()
        group = DashboardGroupDAO.update(self._model, self._properties, commit=False)
        if hasattr(self._properties, "level"):
            DashboardGroupDAO.update_children_level(
                self._model_id, self._properties["level"])

        db.session.commit()
        return group

    def validate(self):
        self._model = DashboardGroupDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        self._model.can_access(MANAGE)
        # 验证是否重名
        if DashboardGroupDAO.validate_uniqueness(
            self._properties["pid"],
            self._properties["name"],
        ):
            raise HTTPError(Messages.GROUP_IS_EXIST, 400)

        # 重命名事件
        if self._properties["pid"] == self._model.pid:
            return

        # 移动到自身
        if self._properties["pid"] == self._model_id:
            raise HTTPError(Messages.CANNOT_MOVE_ITSELF, 400)

        # 移动到顶层目录
        if self._properties["pid"] == 0:
            self._properties["level"] = 0
            return

        # 移动子目录事件
        ids = DashboardGroupDAO.find_children_ids_by_pid(self._model_id)
        # 判断目标分组是否是子目录
        if self._properties["pid"] in ids:
            raise HTTPError(Messages.MOVE_TO_CHILDREN_ERR, 400)

        # 校验目标分组是否存在
        parent_group = DashboardGroupDAO.find_by_id(self._properties["pid"])
        if parent_group is None:
            raise HTTPError(Messages.PARENT_NOT_EXIST, 400)

        self._properties["level"] = parent_group.level + 1
