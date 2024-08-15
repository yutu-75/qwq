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
@Time       : 2023/3/17 13:53
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, List

from flask_appbuilder.security.sqla.models import User

from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.user import UserV2
from superset.sys_manager.menus.dao import SysMenuDAO

from superset.commands.base import BaseCommand
from superset.sys_manager.dept.dao import SysDeptDAO
from superset.constants import MenuName, ROW_COL_SECURITY, VIEW

logger = logging.getLogger(__name__)


class SysDeptDataCommand(BaseCommand):
    def __init__(self, user: UserV2, **kwargs):
        self._actor = user

    def run(self, **kwargs: Any) -> List[dict]:
        if self._actor.is_admin:
            return SysDeptDAO.find_auth_detail(perm=ROW_COL_SECURITY)

        return SysDeptDAO.find_by_user(self._actor)


class SysDeptUsersDataCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        return SysDeptDAO.find_users_by_dept_id(self._model_id, **kwargs)

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.DEPT_MANAGEMENT)
        menu.can_access()

        self._model = SysDeptDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)


class DeptAuthDetailCommand(BaseCommand):
    def __init__(self, user: UserV2, data: dict):
        self._actor = user
        self._properties = data

    def run(self, **kwargs: Any) -> List[dict]:
        if self._actor.is_admin:
            data_auth = SysDeptDAO.find_target_perm_by_source(**self._properties)
            return SysDeptDAO.find_auth_detail(data_auth=data_auth)

        # 获取用户所在组织的所有组织的ID
        depts_id = SysDeptDAO.find_depts_id_by_user(self._actor)
        data_auth = SysDeptDAO.find_dept_perm(depts_id=depts_id, **self._properties)
        return SysDeptDAO.find_auth_detail_by_user(self._actor, data_auth)
