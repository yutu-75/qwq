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
@Time       : 2023/6/14 16:28
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, List

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import AuthSourceType, GRANT, VIEW
from superset.v2.dashboards.dao import DashboardV2DAO

logger = logging.getLogger(__name__)


class DashboardListCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[Any]:
        self.validate()
        title = kwargs.get("title", False)
        favorite = kwargs.get("favorite", 'false').lower() == 'true'
        owner = kwargs.get("owner", 'false').lower() == 'true'
        limit = kwargs.get("limit", 20)
        ids = list()
        if favorite:
            ids = DashboardV2DAO.find_favorite_dash_ids(self._actor.id, limit)
            if len(ids) == 0:
                return []

        user_id = self._actor.id if owner else 0
        if self._actor.is_admin:
            res = DashboardV2DAO.search_dashboards(title, ids, user_id, limit)
            return [{
                'perm': GRANT,
                'url': item[0].url,
                **item[0].info
            } for item in res]

        data_auth = DashboardV2DAO.find_auth_source_perm_by_user(
            AuthSourceType.DASHBOARD, self._actor.id, VIEW)
        auth_ids = set(data_auth.keys())
        ids = (set(ids) & auth_ids) if len(ids) > 0 else auth_ids
        if len(ids) == 0:
            return []

        res = DashboardV2DAO.search_dashboards(title, ids, user_id, limit)
        return [{
            'perm': data_auth.get(item[0].id, 0),
            'url': item[0].url,
            **item[0].info
        } for item in res]
