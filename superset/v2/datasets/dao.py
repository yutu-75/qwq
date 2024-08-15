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
from typing import Any, List

from flask_appbuilder import Model

from superset.datasets.dao import DatasetDAO
from superset.extensions import db

logger = logging.getLogger(__name__)


class DatasetV2DAO(DatasetDAO):
    @classmethod
    def find_datasets(cls, name: str, database_id: int, schema: str) -> List[Any]:
        query = db.session.query(cls.model_cls)
        if name:
            query = query.filter(cls.model_cls.custom_name.contains(name))

        if database_id:
            query = query.filter(cls.model_cls.database_id == database_id)

        if schema:
            query = query.filter(cls.model_cls.schema == schema)

        query.order_by(cls.model_cls.custom_name)
        return query.all()

    @classmethod
    def get_admin_datasets(cls, name: str, database_id: int, schema: str) -> List[Any]:
        res = cls.find_datasets(name, database_id, schema)
        return [{
            "datasource_type": item.datasource_type,
            "id": item.id,
            "custom_name": item.custom_name,
            "table_name": item.custom_name or item.table_name,
            "database_id": item.database_id,
            "kind": item.kind,
            "schema": item.schema,
            "database": {"database_name": item.database_name},
            "owners": [{"first_name": item.changed_by_name, "last_name": ""}]
        } for item in res]

    @classmethod
    def get_user_datasets(
        cls,
        name: str,
        data_auth: set,
        database_id: int,
        schema: str
    ) -> List[Any]:
        res = cls.find_datasets(name, database_id, schema)
        return [{
            "datasource_type": item.datasource_type,
            "id": item.id,
            "custom_name": item.custom_name,
            "table_name": item.custom_name or item.table_name,
            "database_id": item.database_id,
            "kind": item.kind,
            "schema": item.schema,
            "database": {"database_name": item.database_name},
            "owners": [{"first_name": item.changed_by_name, "last_name": ""}]
        } for item in res if item.id in data_auth]

    @classmethod
    def validate_uniqueness(cls, custom_name: str, group_id: int, **kwargs) -> bool:
        dataset_query = db.session.query(cls.model_cls).filter(
            cls.model_cls.custom_name == custom_name,
            cls.model_cls.table_group_id == group_id
        )
        return not db.session.query(dataset_query.exists()).scalar()

    @classmethod
    def find_by_table_name(cls, table_name: str) -> Model:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.table_name == table_name,
        )
        return query.first()

    @classmethod
    def find_by_group_ids(cls, group_ids: list) -> list:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.table_group_id.in_(group_ids),
        )
        return query.all()
