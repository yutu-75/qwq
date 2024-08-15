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
@Time       : 2023/7/28 14:29
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import List, Any

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import AuthSourceType, VIEW
from superset.v2.datasources.dao import DataSourceDAO


class DatabaseDataSourceListCommand(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        res = DataSourceDAO.find_databases()
        if self._actor.is_admin:
            return [
                {
                    "id": item[0].database_id,
                    "datasource_id": item[0].id,
                    "database_name": item[0].name,
                    "d_type": item[0].d_type,
                    "backend": item[1].backend,
                } for item in res
            ]

        data_auth = DataSourceDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASOURCE, self._actor.id, VIEW)
        return [
            {
                "id": item[0].database_id,
                "datasource_id": item[0].id,
                "database_name": item[0].name,
                "d_type": item[0].d_type,
                "backend": item[1].backend,
            } for item in res if data_auth.get(item[0].id, 0) > 0
        ]
