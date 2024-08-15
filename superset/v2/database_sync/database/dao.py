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




from typing import List

from superset import db
from superset.connectors.sqla.models import SqlaTable
from superset.dao.base import BaseDAO
from superset.models.core import Database
from superset.models.database_sync import DatabaseSyncTask, DatabaseSync

from superset.constants import DataSourceType


class DatabaseSyncDAO(BaseDAO):
    model_cls = DatabaseSync

    @staticmethod
    def find_by_uuid(uuid: str) -> DatabaseSync:
        database_sync = db.session.query(DatabaseSync).filter_by(
            uuid=uuid
        ).one_or_none()
        return database_sync

    @staticmethod
    def find_by_database_id(database_id: int) -> DatabaseSync:
        database_sync = db.session.query(DatabaseSync).filter_by(
            database_id=database_id
        ).first()
        return database_sync

    @classmethod
    def validate_uniqueness(cls, name: str, group_id: int) -> bool:
        database_sync_query = db.session.query(DatabaseSync).filter(
            cls.model_cls.name == name,
            cls.model_cls.group_id == group_id
        )
        return not db.session.query(database_sync_query.exists()).scalar()

    @staticmethod
    def find_id_by_name(name: str) -> int:
        datasource = db.session.query(DatabaseSync.id).filter(
            DatabaseSync.name == name
        ).one_or_none()
        return 0 if datasource is None else datasource[0]

    @classmethod
    def find_by_type(cls, d_type: str) -> List[DatabaseSync]:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.d_type == d_type,
            cls.model_cls.group_id > 0,
        ).order_by(cls.model_cls.name)
        return query.all()

    # @classmethod
    # def find_by_api_tables_by_type(cls, d_type: str) -> List:
    #     subquery = (
    #         db.session.query(cls.model_cls.id)
    #         .filter(cls.model_cls.d_type == d_type)
    #         .subquery()
    #     )
    #     query = db.session.query(
    #         APITables.id,
    #         APITables.datasource_id,
    #         APITables.name,
    #     ).filter(APITables.datasource_id.in_(subquery))
    #     return query.all()

    @classmethod
    def find_databases(cls) -> List[DatabaseSync]:
        query = db.session.query(cls.model_cls, Database).filter(
            cls.model_cls.d_type == DataSourceType.DATABASE,
            cls.model_cls.group_id > 0
        ).join(Database, Database.id == cls.model_cls.database_id).order_by(
            cls.model_cls.changed_on.desc()).group_by(
            cls.model_cls.database_id)
        return query.all()

    # @classmethod
    # def find_datasets(cls, datasource_id: int) -> List[SqlaTable]:
    #     api_tables_query = (
    #         db.session.query(APITables.id)
    #         .filter(APITables.datasource_id == datasource_id)
    #         .subquery()
    #     )
    #     query = db.session.query(SqlaTable).filter(
    #         SqlaTable.api_table_id.in_(api_tables_query)
    #     )
    #     return query.all()
class DataBaseSyncDAO(BaseDAO):
    model_cls = DatabaseSync

    @staticmethod
    def find_by_uuid(uuid: str) -> DatabaseSync:
        datasource = db.session.query(DatabaseSync).filter_by(
            uuid=uuid
        ).one_or_none()
        return datasource

    @staticmethod
    def find_by_database_id(database_id: int) -> DatabaseSync:
        datasource = db.session.query(DatabaseSync).filter_by(
            database_id=database_id
        ).first()
        return datasource

    @classmethod
    def validate_uniqueness(cls, name: str, group_id: int) -> bool:
        datasource_query = db.session.query(DatabaseSync).filter(
            cls.model_cls.name == name,
            cls.model_cls.group_id == group_id
        )
        return not db.session.query(datasource_query.exists()).scalar()

    @staticmethod
    def find_id_by_name(name: str) -> int:
        datasource = db.session.query(DatabaseSync.id).filter(
            DatabaseSync.name == name
        ).one_or_none()
        return 0 if datasource is None else datasource[0]

    @classmethod
    def find_by_type(cls, d_type: str) -> List[DatabaseSync]:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.d_type == d_type,
            cls.model_cls.group_id > 0,
        ).order_by(cls.model_cls.name)
        return query.all()

    # @classmethod
    # def find_by_api_tables_by_type(cls, d_type: str) -> List:
    #     subquery = (
    #         db.session.query(cls.model_cls.id)
    #         .filter(cls.model_cls.d_type == d_type)
    #         .subquery()
    #     )
    #     query = db.session.query(
    #         APITables.id,
    #         APITables.datasource_id,
    #         APITables.name,
    #     ).filter(APITables.datasource_id.in_(subquery))
    #     return query.all()

    @classmethod
    def find_databases(cls) -> List[DatabaseSync]:
        query = db.session.query(cls.model_cls, Database).filter(
            cls.model_cls.d_type == DataSourceType.DATABASE,
            cls.model_cls.group_id > 0
        ).join(Database, Database.id == cls.model_cls.database_id).order_by(
            cls.model_cls.changed_on.desc()).group_by(
            cls.model_cls.database_id)
        return query.all()

    # @classmethod
    # def find_datasets(cls, datasource_id: int) -> List[SqlaTable]:
    #     api_tables_query = (
    #         db.session.query(APITables.id)
    #         .filter(APITables.datasource_id == datasource_id)
    #         .subquery()
    #     )
    #     query = db.session.query(SqlaTable).filter(
    #         SqlaTable.api_table_id.in_(api_tables_query)
    #     )
    #     return query.all()
