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
from typing import Any, Dict, List, Optional

from flask_appbuilder.security.sqla.models import User

from superset.constants import AuthSourceType, GRANT, VIEW, AuthTargetType
from superset.utils.cache import memoized_func

from superset.commands.base import BaseCommand
from superset.v2.datasources.group.dao import DataSourceGroupDAO

logger = logging.getLogger(__name__)


class DataSourceGroupDataCommand(BaseCommand):
    def __init__(self, user: User, **kwargs):
        self._actor = user

    def run(self, **kwargs: Any) -> List[Dict]:
        # force = kwargs.pop("force", True)
        perm = kwargs.pop("perm", VIEW)
        if self._actor.is_admin:
            return DataSourceGroupDAO.find_all_by_admin(perm=GRANT, **kwargs)

        # 分组权限
        group_auth = DataSourceGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASOURCE_GROUP, self._actor.id, perm)
        # 数据权限
        data_auth = DataSourceGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASOURCE, self._actor.id, perm)
        return DataSourceGroupDAO.find_all_by_admin(
            group_auth=group_auth, data_auth=data_auth, filter_or_not=True, **kwargs)


class DataSourceAuthDetailCommand(BaseCommand):
    def __init__(self, user: User, data: dict):
        self._actor = user
        self._properties = data

    def run(self, **kwargs: Any) -> List[Dict]:
        force = kwargs.get("force", True)
        if self._actor.is_admin:
            return self.cache_admin_result(cache_timeout=30 * 60, force=force)

        return self.cache_user_result(
            user_id=self._actor.id, cache_timeout=30 * 60, force=force)

    def get_max_data_auth(self):
        max_data_auth = {}
        if self._properties["auth_target_type"] == AuthTargetType.USER:
            max_data_auth = DataSourceGroupDAO.find_user_max_privilege_by_source_type(
                self._properties["auth_target"],
                self._properties["auth_source_type"]
            )

        return max_data_auth

    def get_max_group_auth(self):
        max_group_auth = {}
        if self._properties["auth_target_type"] == AuthTargetType.USER:
            max_group_auth = DataSourceGroupDAO.find_user_max_privilege_by_source_type(
                self._properties["auth_target"],
                self._properties["auth_source_type"]
            )

        return max_group_auth

    @memoized_func(
        key='datasource:auth:detail:admin:result'
    )
    def cache_admin_result(
        self,
        pid: int = 0,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        # 获取数据权限
        data_auth = DataSourceGroupDAO.find_source_perm_by_target(**self._properties)
        max_data_auth = self.get_max_data_auth()
        # 分组权限
        self._properties["auth_source_type"] = AuthSourceType.DATASOURCE_GROUP
        group_auth = DataSourceGroupDAO.find_source_perm_by_target(**self._properties)
        max_group_auth = self.get_max_group_auth()
        return DataSourceGroupDAO.find_all_by_admin(
            group_auth=group_auth,
            data_auth=data_auth,
            max_data_auth=max_data_auth,
            max_group_auth=max_group_auth,
        )

    # @memoized_func(
    #     key='{self._actor.username}:{self._actor.id}:datasource:auth:detail:result'
    # )
    def cache_user_result(
        self,
        user_id: int,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        # 用户可授权分组
        user_group = DataSourceGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASOURCE_GROUP, user_id, GRANT)
        group_filter = set(user_group.keys())
        # 用户分组拥有的最高权限
        max_data_auth = self.get_max_data_auth()
        # 用户可授权数据
        user_data = DataSourceGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASOURCE, user_id, GRANT)
        data_filter = set(user_data.keys())
        # 获取数据权限
        data_auth = DataSourceGroupDAO.find_source_perm_by_target(
            **self._properties)
        # 分组权限
        self._properties["auth_source_type"] = AuthSourceType.DATASOURCE_GROUP
        group_auth = DataSourceGroupDAO.find_source_perm_by_target(
            **self._properties)
        max_group_auth = self.get_max_group_auth()
        return DataSourceGroupDAO.find_all_by_user(
            group_auth=group_auth,
            data_auth=data_auth,
            group_filter=group_filter,
            data_filter=data_filter,
            max_data_auth=max_data_auth,
            max_group_auth=max_group_auth,
        )


class DataSourceGroupTreeCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[Dict]:
        return DataSourceGroupDAO.find_tree(
            self._actor,
            AuthSourceType.DATASOURCE_GROUP,
            GRANT
        )
