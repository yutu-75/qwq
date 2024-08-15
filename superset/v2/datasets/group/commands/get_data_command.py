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
@Time       : 2023/3/15 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, List, Optional

from flask_appbuilder.security.sqla.models import User

from superset.constants import AuthSourceType, VIEW, ROW_COL_SECURITY, GRANT, \
    AuthTargetType
from superset.utils.cache import memoized_func

from superset.commands.base import BaseCommand
from superset.v2.datasets.group.dao import DatasetGroupDAO

logger = logging.getLogger(__name__)


class DatasetGroupDataCommand(BaseCommand):
    def __init__(self, user: User, **kwargs):
        self._actor = user

    def run(self, **kwargs: Any) -> List[Any]:
        force = kwargs.get("force", True)
        perm = kwargs.pop("perm", VIEW)
        if self._actor.is_admin:
            return DatasetGroupDAO.find_all_by_admin(perm=ROW_COL_SECURITY, **kwargs)

        return self.cache_user_result(
            user_id=self._actor.id,
            cache_timeout=30 * 60,
            force=force,
            perm=perm,
            **kwargs
        )

    @memoized_func(
        key='dataset:group:admin:result'
    )
    def cache_admin_result(
        self,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        return DatasetGroupDAO.find_all_by_admin(perm=ROW_COL_SECURITY)

    @memoized_func(
        key='{self._actor.username}:{self._actor.id}:dataset:auth:detail'
    )
    def cache_user_result(
        self,
        user_id: int,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False,
        perm: int = VIEW,
        **kwargs
    ) -> List[Any]:
        # 分组权限
        group_auth = DatasetGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASET_GROUP, user_id, perm)
        # 数据权限
        data_auth = DatasetGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASET, user_id, perm)
        return DatasetGroupDAO.find_all_by_admin(
            group_auth=group_auth, data_auth=data_auth, filter_or_not=True, **kwargs)


class DatasetAuthDetailCommand(DatasetGroupDataCommand):
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
            max_data_auth = DatasetGroupDAO.find_user_max_privilege_by_source_type(
                self._properties["auth_target"],
                self._properties["auth_source_type"]
            )

        return max_data_auth

    def get_max_group_auth(self):
        max_group_auth = {}
        if self._properties["auth_target_type"] == AuthTargetType.USER:
            max_group_auth = DatasetGroupDAO.find_user_max_privilege_by_source_type(
                self._properties["auth_target"],
                self._properties["auth_source_type"]
            )

        return max_group_auth

    @memoized_func(
        key='dataset:auth:detail:admin'
    )
    def cache_admin_result(
        self,
        pid: int = 0,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        # 获取数据权限
        data_auth = DatasetGroupDAO.find_source_perm_by_target(**self._properties)
        max_data_auth = self.get_max_data_auth()
        # 分组权限
        self._properties["auth_source_type"] = AuthSourceType.DATASET_GROUP
        group_auth = DatasetGroupDAO.find_source_perm_by_target(**self._properties)
        max_group_auth = self.get_max_group_auth()
        return DatasetGroupDAO.find_all_by_admin(
            group_auth=group_auth,
            data_auth=data_auth,
            max_data_auth=max_data_auth,
            max_group_auth=max_group_auth,
        )

    def cache_user_result(
        self,
        user_id: int,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        # 用户可授权分组
        user_group = DatasetGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASET_GROUP, user_id, GRANT)
        group_filter = set(user_group.keys())
        max_data_auth = self.get_max_data_auth()
        # 用户可授权数据
        user_data = DatasetGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASET, user_id, GRANT)
        data_filter = set(user_data.keys())
        # 获取数据权限
        data_auth = DatasetGroupDAO.find_source_perm_by_target(
            **self._properties)
        # 分组权限
        self._properties["auth_source_type"] = AuthSourceType.DATASET_GROUP
        group_auth = DatasetGroupDAO.find_source_perm_by_target(
            **self._properties)
        max_group_auth = self.get_max_group_auth()
        return DatasetGroupDAO.find_all_by_user(
            group_auth=group_auth,
            data_auth=data_auth,
            group_filter=group_filter,
            data_filter=data_filter,
            max_data_auth=max_data_auth,
            max_group_auth=max_group_auth,
        )


class DatasetGroupTreeCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[Any]:
        return DatasetGroupDAO.find_tree(
            self._actor,
            AuthSourceType.DATASET_GROUP,
            ROW_COL_SECURITY,
        )
