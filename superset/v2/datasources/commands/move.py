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
@Time       : 2023/3/28 18:00
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from datetime import datetime
from typing import Any, Dict, Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import MANAGE
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.datasources.dao import DataSourceDAO
from superset.v2.datasources.group.dao import DataSourceGroupDAO

logger = logging.getLogger(__name__)


class MoveDataSourceCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[Model] = None

    def run(self) -> Model:
        self.validate()
        datasource = DataSourceDAO.update(
            self._model, self._properties, commit=False)
        return datasource

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
        # 重命名事件
        if self._properties["group_id"] == self._model.group_id:
            # 校验重名
            if not DataSourceDAO.validate_uniqueness(
                self._properties["name"],
                self._properties["group_id"],
            ):
                raise HTTPError(Messages.IS_EXIST, 400)

            ts = int(datetime.now().timestamp() * 1000)
            DataSourceDAO.update(self._model.database, {
                "verbose_name": self._properties["name"],
                "database_name": self._properties["name"] + f"_{ts}"
            }, commit=False)
            return

        # 移动到顶层
        if self._properties["group_id"] == 0:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        # 查询分组是否存在
        group = DataSourceGroupDAO.find_by_id(self._properties["group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)
