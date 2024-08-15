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
from typing import Any, List

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import MenuName, GRANT, AuthSourceType, VIEW, DatabaseAuthType
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.sys_manager.dept.commands.get_data_command import \
    SysDeptDataCommand, DeptAuthDetailCommand
from superset.sys_manager.menus.commands.get_data_command import \
    SysMenuDataCommand, MenuAuthDetailCommand
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.constants import AuthType, DirectionType
from superset.sys_manager.permission.dao import DatabaseAuthDAO
from superset.v2.charts.group.commands.get_data_command import \
    ChartGroupDataCommand, ChartAuthDetailCommand
from superset.v2.dashboards.group.commands.get_data_command import \
    DashboardGroupDataCommand, DashboardAuthDetailCommand
from superset.v2.database_sync.group.commands.get_data_command import DatabaseSyncGroupDataCommand, \
    DatabaseSyncAuthDetailCommand
from superset.v2.databases.dao import DatabaseV2DAO
from superset.v2.datasets.group.commands.get_data_command import \
    DatasetGroupDataCommand, DatasetAuthDetailCommand
from superset.v2.datasources.group.commands.get_data_command import \
    DataSourceGroupDataCommand, DataSourceAuthDetailCommand
from superset.v2.role.commands.get_data_command import RoleV2ListCommand, \
    RoleAuthDetailCommand
from superset.v2.user.commands.get_data_command import UserV2ListCommand, \
    UserAuthDetailCommand

logger = logging.getLogger(__name__)


_source = {
    AuthType.DEPT: SysDeptDataCommand,
    AuthType.ROLE: RoleV2ListCommand,
    AuthType.USER: UserV2ListCommand,
    AuthType.DATASOURCE: DataSourceGroupDataCommand,
    AuthType.DASHBOARD: DashboardGroupDataCommand,
    AuthType.CHART: ChartGroupDataCommand,
    AuthType.DATASET: DatasetGroupDataCommand,
    AuthType.MENU: SysMenuDataCommand,
}


_target = {
    AuthType.DEPT: DeptAuthDetailCommand,
    AuthType.ROLE: RoleAuthDetailCommand,
    AuthType.USER: UserAuthDetailCommand,
    AuthType.DATASOURCE: DataSourceAuthDetailCommand,
    AuthType.DASHBOARD: DashboardAuthDetailCommand,
    AuthType.CHART: ChartAuthDetailCommand,
    AuthType.DATASET: DatasetAuthDetailCommand,
    AuthType.MENU: MenuAuthDetailCommand,
    AuthType.DATABASE_SYNC: DatabaseSyncAuthDetailCommand,
}


class SysAuthDataCommand(BaseCommand):
    def __init__(self, user: User, auth_type: str, **kwargs: Any):
        self._actor = user
        self._auth_type: str = auth_type
        self._properties = kwargs

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        func = _source.get(self._auth_type)
        return func(self._actor, **self._properties).run(perm=GRANT)


class SysAuthDetailDataCommand(BaseCommand):
    def __init__(self, user: User, data: dict):
        self._actor = user
        self._properties = data

    def run(self, **kwargs: Any) -> List[Any]:
        direction = self._properties.pop("direction")
        # 按用户配置权限
        if direction == DirectionType.SOURCE:
            func = _target.get(self._properties["auth_source_type"])
        # 按资源配置权限
        else:
            func = _target.get(self._properties["auth_target_type"])

        return func(self._actor, self._properties).run(**kwargs)

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.PERMISSION_MANAGEMENT)
        menu.can_access()


class DatabaseSchemaDetailCommand(BaseCommand):
    def __init__(self, user: User, data: dict, model_id: int):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> List[Any]:
        # direction = self._properties.pop("direction")
        self.validate()
        schemas = self._model.get_all_schema_names()
        max_auth = None
        if self._properties["auth_target_type"] == 'user':
            max_auth = DatabaseAuthDAO.find_perm_by_user_id(
                self._properties["auth_target"],
                self._model_id,
                DatabaseAuthType.DB_SCHEMA
            )

        data_auth = DatabaseAuthDAO.find_perm_by_target(
            auth_target=self._properties["auth_target"],
            auth_target_type=self._properties["auth_target_type"].value,
            auth_source_type=DatabaseAuthType.DB_SCHEMA.value,
            database_id=self._model_id,
        )
        if self._actor.is_admin:
            if max_auth is None:
                return [
                    {
                        "database_id": self._model_id,
                        "schema": schema,
                        "perm": data_auth.get(f"{self._model_id}_{schema}_", 0),
                        "max_perm": 0,
                        "current_user_perm": GRANT,
                    } for schema in schemas
                ]

            return [
                {
                    "database_id": self._model_id,
                    "schema": schema,
                    "perm": data_auth.get(f"{self._model_id}_{schema}_", 0),
                    "max_perm": max_auth.get(f"{self._model_id}_{schema}_", 0),
                    "current_user_perm": GRANT,
                } for schema in schemas
            ]

        # 当前登录用户可授权数据
        current_user_auth = DatabaseAuthDAO.find_perm_by_user_id(
            self._actor.id,
            self._model_id,
            DatabaseAuthType.DB_SCHEMA,
            privilege_value=VIEW
        )
        if max_auth is None:
            return [
                {
                    "database_id": self._model_id,
                    "schema": schema,
                    "perm": data_auth.get(f"{self._model_id}_{schema}_", 0),
                    "max_perm": 0,
                    "current_user_perm": current_user_auth.get(
                        f"{self._model_id}_{schema}_", 0),
                } for schema in schemas if
                current_user_auth.get(f"{self._model_id}_{schema}_", 0) >= VIEW
            ]

        return [
            {
                "database_id": self._model_id,
                "schema": schema,
                "perm": data_auth.get(f"{self._model_id}_{schema}_", 0),
                "max_perm": max_auth.get(f"{self._model_id}_{schema}_", 0),
                "current_user_perm": current_user_auth.get(f"{self._model_id}_{schema}_", 0),
            } for schema in schemas if
            current_user_auth.get(f"{self._model_id}_{schema}_", 0) >= VIEW
        ]

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.PERMISSION_MANAGEMENT)
        menu.can_access()

        self._model = DatabaseV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)


class DatabaseSchemaTablesDetailCommand(BaseCommand):
    def __init__(self, user: User, data: dict, model_id: int, schema: str):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._schema = schema
        self._model = None

    def run(self, **kwargs: Any) -> List[Any]:
        # direction = self._properties.pop("direction")
        self.validate()
        tables = self._model.get_all_tables_name(self._schema)
        tables = list(tables)
        tables.sort(key=lambda k: k)
        data_auth = DatabaseAuthDAO.find_perm_by_target(
            auth_target=self._properties["auth_target"],
            auth_target_type=self._properties["auth_target_type"],
            auth_source_type=DatabaseAuthType.DB_SCHEMA_TABLE,
            database_id=self._model_id,
            schema=self._schema,
        )
        max_auth = None
        if self._properties["auth_target_type"] == 'user':
            max_auth = DatabaseAuthDAO.find_perm_by_user_id(
                self._properties["auth_target"],
                self._model_id,
                DatabaseAuthType.DB_SCHEMA_TABLE,
                self._schema,
            )
        all_tables_perm = DatabaseAuthDAO.check_all_tables_perm(
            self._actor.id, self._model_id, self._schema, GRANT)
        if self._actor.is_admin or all_tables_perm:
            if max_auth is None:
                return [
                    {
                        "database_id": self._model_id,
                        "schema": self._schema,
                        "table_name": table,
                        "perm": data_auth.get(
                            f"{self._model_id}_{self._schema}_{table}", 0),
                        "max_perm": 0
                    } for table in tables
                ]

            return [
                {
                    "database_id": self._model_id,
                    "schema": self._schema,
                    "table_name": table,
                    "perm": data_auth.get(f"{self._model_id}_{self._schema}_{table}", 0),
                    "max_perm": max_auth.get(f"{self._model_id}_{self._schema}_{table}", 0)
                } for table in tables
            ]

        all_tables_perm = DatabaseAuthDAO.check_all_tables_perm(
            self._actor.id, self._model_id, self._schema, 6)
        if not all_tables_perm:
            return []

        current_user_auth = DatabaseAuthDAO.find_perm_by_user_id(
            self._actor.id,
            self._model_id,
            DatabaseAuthType.DB_SCHEMA_TABLE,
            self._schema,
            privilege_value=GRANT
        )
        if max_auth is None:
            return [
                {
                    "database_id": self._model_id,
                    "schema": self._schema,
                    "table_name": table,
                    "perm": data_auth.get(f"{self._model_id}_{self._schema}_{table}", 0),
                    "max_perm": 0
                } for table in tables if
                current_user_auth.get(f"{self._model_id}_{self._schema}_{table}", 0) > 0
            ]

        return [
            {
                "database_id": self._model_id,
                "schema": self._schema,
                "table_name": table,
                "perm": data_auth.get(f"{self._model_id}_{self._schema}_{table}", 0),
                "max_perm": max_auth.get(f"{self._model_id}_{self._schema}_{table}", 0)
            } for table in tables if
            current_user_auth.get(f"{self._model_id}_{self._schema}_{table}", 0) > 0
        ]

    def validate(self) -> None:
        menu = SysMenuDAO.find_by_name(MenuName.PERMISSION_MANAGEMENT)
        menu.can_access()

        self._model = DatabaseV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)
