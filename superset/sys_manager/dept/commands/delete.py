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
from typing import Optional, Dict, Any

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.global_messages import Messages
from superset.models.sys_manager import SysDept
from superset.sys_manager.dept.dao import SysDeptDAO, SysDeptUsersDAO
from superset.exceptions import HTTPError
from superset.constants import (
    AuthSourceType, MenuName
)
from superset.sys_manager.menus.dao import SysMenuDAO

logger = logging.getLogger(__name__)


class DeleteSysDeptCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[SysDept] = None

    def run(self) -> None:
        self.validate()
        SysDeptDAO.delete_dept(self._model, commit=False)
        self.archiving()

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.DEPT_MANAGEMENT)
        menu.can_access()
        self._model = SysDeptDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.DEPT_NOT_EXIST, 400)

    def archiving(self):
        """归档"""
        doc_json = self._model.to_json()
        SysDeptDAO.archiving_docs("sys_dept", doc_json)


class DeleteSysDeptUsersCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._model = None
        self._properties = data

    def run(self) -> None:
        self.validate()
        SysDeptUsersDAO.delete_dept_users(self._model, self._properties["user_ids"])

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.DEPT_MANAGEMENT)
        menu.can_access()

        self._model = SysDeptDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)
