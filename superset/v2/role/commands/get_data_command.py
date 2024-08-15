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
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, List, Optional

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User

from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import AuthSourceType, MenuName, VIEW
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.utils.cache import memoized_func

from superset.commands.base import BaseCommand
from superset.models.user import UserV2
from superset.v2.role.dao import RoleV2DAO

logger = logging.getLogger(__name__)


class RoleV2ListCommand(BaseCommand):
    def __init__(self, user: UserV2, **kwargs):
        self._actor = user

    def run(self, **kwargs: Any) -> dict:
        if self._actor.is_admin:
            return RoleV2DAO.find_roles(**kwargs)

        kwargs["user_id"] = self._actor.id
        data = RoleV2DAO.find_roles(**kwargs)
        return data

    def validate(self) -> None:
        pass
        # menu = SysMenuDAO.find_by_name(MenuName.SYSTEM_MANAGER)
        # menu.can_access()


class RoleUsersInfoCommand(BaseCommand):
    def __init__(self, user: UserV2, model_id: int):
        self._model_id = model_id
        self._actor = user
        self._model = None

    def run(self, **kwargs: Any):
        self.validate()
        data = RoleV2DAO.get_users_by_role_id(self._model_id, **kwargs)
        return data

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.ROLE_MANAGEMENT)
        menu.can_access()

        self._model = RoleV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)


class RoleAuthDetailCommand(BaseCommand):
    def __init__(self, user: User, data: dict, **kwargs):
        self._actor = user
        self._properties = data

    def run(self, **kwargs: Any) -> List[dict]:
        force = kwargs.get("force", True)
        return self.cache_admin_result(cache_timeout=30 * 60, force=force)
        # if self._actor.is_admin:
        #     return self.cache_admin_result(cache_timeout=30 * 60, force=force)
        #
        # return self.cache_user_result(
        #     user_id=self._actor.id, cache_timeout=30 * 60, force=force)

    def validate(self) -> None:
        pass

    @memoized_func(
        key='role:auth:detail:admin'
    )
    def cache_admin_result(
        self,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        # 获取数据权限
        data_auth = RoleV2DAO.find_target_perm_by_source(**self._properties)
        return RoleV2DAO.find_auth_detail_by_admin(data_auth)

    @memoized_func(
        key='{self._actor.username}:{self._actor.id}:role:auth:detail'
    )
    def cache_user_result(
        self,
        user_id: int,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        # 数据权限
        data_auth = RoleV2DAO.find_role_perm_by_source_user(
            user_id=user_id, privilege_value=VIEW, **self._properties)
        return RoleV2DAO.find_auth_detail_by_user(self._actor.roles, data_auth)
