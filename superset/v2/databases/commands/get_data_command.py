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
from typing import Any, List, Dict

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import AuthSourceType, VIEW
from superset.v2.databases.dao import DatabaseV2DAO
from superset.v2.datasources.group.dao import DataSourceGroupDAO

logger = logging.getLogger(__name__)


class DatabaseListDataCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[Dict]:
        name = kwargs.get('name', None)
        if self._actor.is_admin:
            return DatabaseV2DAO.get_admin_databases(name)

        # 数据权限
        data_auth = DataSourceGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASOURCE, self._actor.id, VIEW)
        return DatabaseV2DAO.get_user_databases(name, set(data_auth.keys()))
