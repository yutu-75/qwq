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
from typing import Any, List, Optional

from flask_appbuilder.security.sqla.models import User

from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import AuthSourceType, MANAGE, GRANT, VIEW, AuthType, \
    AuthTargetType
from superset.utils.cache import memoized_func

from superset.commands.base import BaseCommand
from superset.sys_manager.menus.dao import SysMenuDAO

logger = logging.getLogger(__name__)


class SysMenuSysManagerCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user
        self._model = None

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        if self._actor.is_admin:
            data = SysMenuDAO.find_menus_by_pid(self._model.id)
            return data

        data_auth = SysMenuDAO.find_auth_source_perm_by_user(
            AuthSourceType.MENU, self._actor.id, MANAGE)
        return SysMenuDAO.find_auth_detail_by_user(self._model.id, data_auth)

    def validate(self) -> None:
        self._model = SysMenuDAO.find_by_name("System Manager")
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)


class SysMenuDatasetCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user
        self._model = None

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        if self._actor.is_admin:
            data = SysMenuDAO.find_menus_by_pid(self._model.id)
            return data

        data_auth = SysMenuDAO.find_auth_source_perm_by_user(
            AuthSourceType.MENU, self._actor.id, MANAGE)
        return SysMenuDAO.find_auth_detail_by_user(self._model.id, data_auth)

    def validate(self) -> None:
        self._model = SysMenuDAO.find_by_name("Dataset")
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)


class SysMenuDataCommand(BaseCommand):
    def __init__(self, user: User, **kwargs):
        self._actor = user

    def run(self, **kwargs: Any) -> List[dict]:
        perm = kwargs.get("perm", VIEW)
        if self._actor.is_admin:
            return SysMenuDAO.find_all_by_pid(self._actor)

        data_auth = SysMenuDAO.find_auth_source_perm_by_user(
            AuthSourceType.MENU, self._actor.id, perm)
        return SysMenuDAO.find_auth_detail_by_user(0, data_auth)


class MenuAuthDetailCommand(BaseCommand):
    def __init__(self, user: User, data: dict):
        self._actor = user
        self._properties = data

    def run(self, **kwargs: Any) -> List[dict]:
        force = kwargs.get("force", True)
        if self._actor.is_admin:
            return self.cache_admin_result(cache_timeout=30 * 60, force=force)

        return self.cache_user_result(
            user_id=self._actor.id, cache_timeout=30 * 60, force=force)

    def get_max_data_auth(self):
        max_data_auth = {}
        if self._properties["auth_target_type"] == AuthTargetType.USER:
            max_data_auth = SysMenuDAO.find_user_max_privilege_by_source_type(
                self._properties["auth_target"],
                self._properties["auth_source_type"]
            )

        return max_data_auth

    @memoized_func(
        key='menu:auth:detail:admin'
    )
    def cache_admin_result(
        self,
        pid: int = 0,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        # 获取数据权限
        data_auth = SysMenuDAO.find_source_perm_by_target(**self._properties)
        max_data_auth = self.get_max_data_auth()
        return SysMenuDAO.find_auth_detail_by_admin(pid, data_auth, max_data_auth)

    def cache_user_result(
        self,
        user_id: int,
        pid: int = 0,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        # 用户可授权数据
        user_data = SysMenuDAO.find_auth_source_perm_by_user(
            AuthSourceType.MENU, user_id, GRANT)
        data_filter = set(user_data.keys())
        # 获取数据权限
        data_auth = SysMenuDAO.find_source_perm_by_target(**self._properties)
        max_data_auth = self.get_max_data_auth()
        return SysMenuDAO.find_all_by_user(data_auth, data_filter, max_data_auth)


class SysMenuPermCommand(BaseCommand):
    def __init__(self, user: User, menu_name: str):
        self._actor = user
        self._menu_name = menu_name

    def run(self, **kwargs: Any) -> int:
        self.validate()
        menu = SysMenuDAO.find_by_name(self._menu_name)
        if menu:
            return SysMenuDAO.find_perm(menu.id, AuthType.MENU)

        return 0
