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
@Time       : 2023/3/16 17:20
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, Dict, Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand, CreateMixin
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.slice import Slice
from superset.constants import MANAGE
from superset.v2.charts.dao import ChartV2DAO
from superset.v2.charts.group.dao import ChartGroupDAO

logger = logging.getLogger(__name__)


class MoveV2ChartCommand(CreateMixin, BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[Slice] = None
        self._properties = data

    def run(self) -> Model:
        self.validate()
        ChartV2DAO.update(
            self._model,
            {
                "slice_group_id": self._properties["target_id"],
                "slice_name": self._properties["new_title"],
            }
        )
        return self._model

    def validate(self) -> None:
        self._model = ChartV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
        # 校验重名
        if not ChartV2DAO.validate_uniqueness(
            self._properties["new_title"],
            self._properties["target_id"]
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

        # 重命名事件
        if self._properties["target_id"] == self._model.slice_group_id:
            return

        # 移动到顶层
        if self._properties["target_id"] == 0:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        # 查询分组是否存在
        group = ChartGroupDAO.find_by_id(self._properties["target_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)
