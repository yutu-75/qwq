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
import logging
from typing import Any, Dict, Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import MenuName, DataSourceType
from superset.global_messages import Messages
from superset.models.sys_manager import SysDept
from superset.sys_manager.dept.dao import SysDeptDAO
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.v2.datasources.dao import DataSourceDAO
from superset.exceptions import HTTPError
from superset.models.core import Database

logger = logging.getLogger(__name__)


class UpdateSysDeptCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[SysDept] = None

    def run(self) -> SysDept:
        self.validate()
        dept = SysDeptDAO.update(self._model, self._properties)
        return dept

    def validate(self) -> None:
        """校验当前组织是否存在"""
        menu = SysMenuDAO.find_by_name(MenuName.DEPT_MANAGEMENT)
        menu.can_access()
        self._model = SysDeptDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.DEPT_EXIST, 400)

        # 不能是自身
        if self._model.id == self._properties["pid"]:
            raise HTTPError(Messages.DEPT_EXIST, 400)

        if self._properties["pid"] == 0:
            self._properties["level"] = 0

        else:
            parent_dept = SysDeptDAO.find_by_id(self._properties["pid"])
            if parent_dept is None:
                raise HTTPError(Messages.PARENT_DEPT_NOT_EXIST, 400)

            self._properties["level"] = parent_dept.level + 1
            self._properties["top_id"] = parent_dept.top_id


class UpdateApiDataSourceCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[Database] = None

    def run(self) -> Model:
        self.validate()
        datasource = DataSourceDAO.update(self._model, self._properties)
        return datasource

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError('数据源不存在', 400)

        if self._model.d_type != DataSourceType.API:
            raise HTTPError('数据源类型错误', 400)
