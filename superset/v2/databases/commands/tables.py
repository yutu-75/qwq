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
from typing import Any, cast, Dict, List, Optional

import simplejson
from flask import g
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.connectors.sqla.models import SqlaTable
from superset.constants import AuthSourceType, MANAGE, VIEW, DatabaseAuthType
from superset.databases.commands.exceptions import (
    DatabaseNotFoundError,
    DatabaseTablesUnexpectedError,
)
from superset.extensions import db, security_manager
from superset.models.core import Database
from superset.sys_manager.permission.dao import DatabaseAuthDAO
from superset.utils.core import DatasourceName

from superset.v2.databases.dao import DatabaseV2DAO
from superset.v2.datasets.dao import DatasetV2DAO
from superset.v2.datasources.dao import DataSourceDAO

logger = logging.getLogger(__name__)


class TablesDatabaseCommand(BaseCommand):
    _model: Database

    def __init__(self, user, db_id: int, schema_name: str, force: bool):
        self._actor = user
        self._db_id = db_id
        self._schema_name = schema_name
        self._force = force

    def run(self, **kwargs: Any) -> Dict[str, Any]:
        self.validate()
        name = kwargs.get("name", False)
        data_auth = DatabaseAuthDAO.find_perm_by_user_id(
            self._actor.id, self._db_id, DatabaseAuthType.DB_SCHEMA_TABLE,
            self._schema_name
        )
        tables = self._model.get_all_tables_name(self._schema_name)
        views = self._model.get_all_view_names_in_schema(self._schema_name)
        tables = tables.union({item[0] for item in views})
        tables = list(tables)
        tables.sort(key=lambda k: k)
        extra_dict_by_name = {
            table.name: table.extra_dict
            for table in (
                db.session.query(SqlaTable).filter(
                    SqlaTable.database_id == self._model.id,
                    SqlaTable.schema == self._schema_name,
                )
            ).all()
        }

        all_tables_perm = DatabaseAuthDAO.check_all_tables_perm(
            self._actor.id, self._db_id, self._schema_name)
        if self._actor.is_admin or all_tables_perm:
            options = sorted(
                [
                    {
                        "value": table,
                        "type": "table",
                        "extra": extra_dict_by_name.get(table, None),
                    }
                    for table in tables
                ],
                key=lambda item: item["value"],
            )
        else:
            options = sorted(
                [
                    {
                        "value": table,
                        "type": "table",
                        "extra": extra_dict_by_name.get(table, None),
                    }
                    for table in tables
                    if data_auth.get(f"{self._db_id}_{self._schema_name}_{table}", 0) > 0
                ],
                key=lambda item: item["value"],
            )

        payload = {"count": len(options), "result": options}
        return payload

        # is_datasource_manager = False
        # names = {}
        # 看当前用户是否有当前数据库对应的数据源的管理权限
        # datasource = DataSourceDAO.find_by_database_id(self._db_id)
        # datasource_auth = DataSourceDAO.find_auth_source_perm_by_user(
        #     AuthSourceType.DATASOURCE, g.user.id, MANAGE)
        # datasource_auth = set(datasource_auth.keys())
        # if datasource.id in datasource_auth:
        #     is_datasource_manager = True

        # 如果不是超级管理员，也没有数据源管理权限，则只能看到数据集中分配到权限的那些表
        # 只有创建了数据库数据集的表才能明确的分配权限
        # if (not g.user.is_admin) and (not is_datasource_manager):
        #     data_auth = DatasetV2DAO.find_auth_source_perm_by_user(
        #         AuthSourceType.DATASET, g.user.id, VIEW)
        #     data_auth = set(data_auth.keys())
        #     user_datasources = DatasetV2DAO.get_user_datasets(name, data_auth, self._db_id, self._schema_name)
        #     names = {d.get('table_name') for d in user_datasources if d.get('schema') == self._schema_name}

        # tables = sorted(
        #     DatasourceName(*datasource_name)
        #     for datasource_name in self._model.get_all_table_names_in_schema(
        #         schema=self._schema_name,
        #         force=self._force,
        #         cache=self._model.table_cache_enabled,
        #         cache_timeout=self._model.table_cache_timeout,
        #     )
        #     if g.user.is_admin or is_datasource_manager or (datasource_name[0] in names)
        # )

        # views = sorted(
        #     DatasourceName(*datasource_name)
        #     for datasource_name in self._model.get_all_view_names_in_schema(
        #         schema=self._schema_name,
        #         force=self._force,
        #         cache=self._model.table_cache_enabled,
        #         cache_timeout=self._model.table_cache_timeout,
        #     )
        #     if g.user.is_admin or is_datasource_manager or (datasource_name[0] in names)
        # )

        # extra_dict_by_name = {
        #     table.name: table.extra_dict
        #     for table in (
        #         db.session.query(SqlaTable).filter(
        #             SqlaTable.database_id == self._model.id,
        #             SqlaTable.schema == self._schema_name,
        #         )
        #     ).all()
        # }
        #
        # options = sorted(
        #     [
        #         {
        #             "value": table.table,
        #             "type": "table",
        #             "extra": extra_dict_by_name.get(table.table, None),
        #         }
        #         for table in tables
        #     ]
        #     + [
        #         {
        #             "value": view.table,
        #             "type": "view",
        #         }
        #         for view in views
        #     ],
        #     key=lambda item: item["value"],
        # )
        #
        # payload = {"count": len(tables) + len(views), "result": options}
        # return payload

    def validate(self) -> None:
        self._model = cast(Database, DatabaseV2DAO.find_by_id(self._db_id))
        if not self._model:
            raise DatabaseNotFoundError()
