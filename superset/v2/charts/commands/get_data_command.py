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
@Time       : 2023/5/10 9:12
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, List, Optional

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import AuthSourceType, MANAGE, VIEW, GRANT
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.slice import Slice
from superset.utils.cache import memoized_func
from superset.v2.charts.dao import ChartV2DAO

logger = logging.getLogger(__name__)


class ChartListDataCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[Any]:
        self.validate()
        force = kwargs.get("force", True)
        limit = kwargs.get("limit", 0)
        title = kwargs.get("title", False)
        favorite = kwargs.get("favorite", 'false').lower() == 'true'
        owner = kwargs.get("owner", 'false').lower() == 'true'
        ids = list()
        if favorite:
            ids = ChartV2DAO.find_favorite_chart_ids(self._actor.id)
            if len(ids) == 0:
                return []

        user_id = self._actor.id if owner else 0
        if self._actor.is_admin:
            return self.cache_admin_result(
                ids=ids,
                user_id=user_id,
                title=title,
                limit=limit,
                cache_timeout=30 * 60,
                force=force,
            )

        return self.cache_user_result(
            ids=ids,
            owner_id=user_id,
            user_id=self._actor.id,
            title=title,
            limit=limit,
            cache_timeout=30 * 60,
            force=force
        )

    @memoized_func(
        key='chart:list:admin:result'
    )
    def cache_admin_result(
        self,
        ids: list,
        user_id: int,
        title: str,
        limit: int = 200,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False,
    ) -> List[Any]:
        res = ChartV2DAO.search_charts(title, ids, user_id, limit)
        return [{
            "perm": GRANT,
            'url': item[0].url,
            **item[0].info
        } for item in res]

    @memoized_func(
        key='chart:list:{self._actor.username}:{self._actor.id}:result'
    )
    def cache_user_result(
        self,
        ids: list,
        owner_id: int,
        user_id: int,
        title: str,
        limit: int = 200,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        # 数据权限
        data_auth = ChartV2DAO.find_auth_source_perm_by_user(
            AuthSourceType.CHART, user_id, VIEW)
        auth_ids = set(data_auth.keys())
        ids = (set(ids) & auth_ids) if len(ids) > 0 else auth_ids
        if len(ids) == 0:
            return []

        res = ChartV2DAO.search_charts(title, ids, owner_id, limit)
        return [
            {
                "perm": data_auth.get(item[0].id, 0),
                'url': item[0].url,
                **item[0].info
            } for item in res if data_auth.get(item[0].id, 0) > 0
        ]


class ChartDashboardsListCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[Slice] = None

    def run(self) -> List[dict]:
        self.validate()
        return [{
            "id": item.id,
            "title": item.dashboard_title,
        } for item in self._model.dashboards]

    def validate(self) -> None:
        self._model = ChartV2DAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
