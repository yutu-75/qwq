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

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import VIEW, MANAGE, DataSourceType, DatabaseAuthType
from superset.models.datasource import DataSource
from superset.sys_manager.permission.dao import DatabaseAuthDAO
from superset.utils.cache import memoized_func
from superset.v2.datasources.dao import DataSourceDAO

logger = logging.getLogger(__name__)


class DataSourceDataCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._model_id = model_id
        self._actor = user
        self._model = None

    def run(self, **kwargs: Any) -> Dict[str, Any]:
        self.validate()
        if self._model.d_type == DataSourceType.DATABASE:
            return self._model.database.to_json()

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if self._model_id is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)


class DataSourceTableDataCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._model_id = model_id
        self._actor = user
        self._model = None

    def run(self, **kwargs: Any) -> List[Any]:
        self.validate()
        force = kwargs.get("force", False)
        if self._model.d_type == DataSourceType.DATABASE:
            return self.cache_tables_info(cache_timeout=24 * 60 * 60, force=force)

        # API数据源直接展示名称
        return [{
            "table_name": item.name,
            "comment": ""
        } for item in self._model.api_tables]

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(VIEW)

    def cache_tables_info(
        self,
        cache: bool = False,
        cache_timeout: Optional[int] = None,
        force: bool = False
    ) -> List[Any]:
        database = self._model.database
        schema = self._model.get_default_schema()
        tables_name = database.get_all_tables_name(schema)
        views = database.get_all_view_names_in_schema(schema)
        tables_name = tables_name.union({item[0] for item in views})
        all_tables_perm = DatabaseAuthDAO.check_all_tables_perm(
            self._actor.id, database.id, schema)
        if self._actor.is_admin or all_tables_perm:
            return [
                {
                    "table_name": table_name,
                    # "comment": self.database.get_table_comment(table_name, schema),
                    "comment": "",
                    "schema": schema,
                } for table_name in tables_name
            ]

        data_auth = DatabaseAuthDAO.find_perm_by_user_id(
            self._actor.id, database.id, DatabaseAuthType.DB_SCHEMA_TABLE, schema)
        return [
            {
                "table_name": table_name,
                # "comment": self.database.get_table_comment(table_name, schema),
                "comment": "",
                "schema": schema,
            } for table_name in tables_name
            if data_auth.get(f"{database.id}_{schema}_{table_name}", 0) > 0
        ]


class DataSourceTableColumnDataCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, table_name: str):
        self._model_id = model_id
        self._actor = user
        self._model = None
        self._table_name = table_name

    def run(self, **kwargs: Any) -> Dict[str, Any]:
        self.validate()
        columns = self._model.get_columns(self._table_name)
        return columns

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if self._model_id is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(VIEW)


class DataSourceDatasetsListCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[DataSource] = None

    def run(self) -> List[dict]:
        self.validate()
        if self._model.d_type == DataSourceType.DATABASE:
            res = self._model.database.tables
        elif self._model.d_type == DataSourceType.API:
            res = DataSourceDAO.find_datasets(self._model_id)

        return [{
            "id": item.id,
            "title": item.custom_name or item.table_name
        } for item in res]

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
