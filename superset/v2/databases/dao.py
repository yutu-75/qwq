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

import logging
from typing import List

from superset.constants import DataSourceType
from superset.databases.dao import DatabaseDAO
from superset.extensions import db
from superset.models.core import Database
from superset.models.datasource import DataSource

logger = logging.getLogger(__name__)


class DatabaseV2DAO(DatabaseDAO):
    @classmethod
    def find_by_name(cls, name: str) -> Database:
        res = db.session.query(cls.model_cls).filter(
            cls.model_cls.database_name == name
        ).first()
        return res

    @classmethod
    def get_all_databases(cls, name) -> List[dict]:
        query = (
            db.session.query(
                Database.id,
                DataSource.id,
                DataSource.name,
            ).join(
                DataSource,
                Database.id == DataSource.database_id
            )
        )
        if name:
            res = query.filter(
                DataSource.name.startswith(name),
                DataSource.d_type == DataSourceType.DATABASE,
            )
        else:
            res = query.filter(DataSource.d_type == DataSourceType.DATABASE)
        return res.all()

    @classmethod
    def get_admin_databases(cls, name: str) -> List[dict]:
        res = cls.get_all_databases(name)
        return [{
            "database_id": item[0],
            "datasource_id": item[1],
            "datasource_name": item[2],
        } for item in res]

    @classmethod
    def get_user_databases(cls, name: str, data_auth: set) -> List[dict]:
        res = cls.get_all_databases(name)
        return [{
            "database_id": item[0],
            "datasource_id": item[1],
            "datasource_name": item[2],
        } for item in res if item[1] in data_auth]
