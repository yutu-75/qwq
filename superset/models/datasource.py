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

# -*- coding: utf-8 -*-

"""
@Time       : 2023/3/21 9:38
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
from typing import Dict, Any, Optional, List

from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint,
    DateTime,
    Text,
    BigInteger,
    SmallInteger,
)
from sqlalchemy.orm import relationship, backref

from superset import conf
from superset.constants import AuthSourceType, DataSourceType
from superset.databases.utils import make_url_safe
from superset.models.core import Database
from superset.models.helpers import AuditMixinNullable, ImportExportMixin


class DataSource(Model, AuditMixinNullable, ImportExportMixin):
    __tablename__ = "datasource"
    __table_args__ = (UniqueConstraint("name", "group_id"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, comment='名称')
    database_id = Column(Integer, ForeignKey("dbs.id"))
    database = relationship(Database, backref="datasource")
    d_type = Column(String(20), nullable=False, default="database", comment='类型')
    desc = Column(String(1000), nullable=True, comment='描述')
    group_id = Column(Integer, ForeignKey("datasource_group.id"))
    api_tables = relationship(
        "APITables",
        backref="datasource",
        cascade="all, delete-orphan",
    )

    export_fields = [
        'name',
        'd_type',
        'desc',
        'configuration',
        'data_path',
    ]

    @property
    def api_datasource_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "d_type": self.d_type,
            "desc": self.desc,
            "group_id": self.group_id,
            "tables": [item.to_json() for item in self.api_tables],
        }

    def get_kylin_first_schame(self):
        schemas = self.database.get_all_schema_names()
        if schemas:
            return schemas[-1]
        return None

    def get_presto_starrocks_schema(self):
        """
        用presto 连 starrocks数据库，starrocks不支持 SHOW TABLES FROM database 语法，
        因为连接的时候没有指定database，而是指定了Catalog，导致出现 SHOW TABLES FROM Catalog,
        语法错误，

        此方式 默认取出 指定 schemas名字
        :return:
        """
        conf.get("PRESTO_STARROCKS_SCHEMA", "ods_user_research")
        schemas = self.database.get_all_schema_names()
        if schemas:
            if conf.get("PRESTO_STARROCKS_SCHEMA", "ods_user_research") in schemas:
                return conf.get("PRESTO_STARROCKS_SCHEMA", "ods_user_research")
            else:
                return schemas[-1]
        return None

    def get_default_schema(self):
        url = make_url_safe(self.database.sqlalchemy_uri)

        if url.drivername == "kylin":
            return self.get_kylin_first_schame()

        if url.drivername == "presto" and "starrocks" in url.database:
            return self.get_presto_starrocks_schema()

        return url.database

    def get_tables_info(self) -> List[dict]:
        if self.d_type == DataSourceType.DATABASE:
            schema = self.get_default_schema()
            tables_name = self.database.get_all_tables_name(schema)
            views = self.database.get_all_view_names_in_schema(schema)
            return [
                {
                    "table_name": table_name,
                    # "comment": self.database.get_table_comment(table_name, schema),
                    "comment": "",
                    "schema": schema,
                } for table_name in tables_name
            ] + [
                {
                    "table_name": table_name[0],
                    "comment": "",
                    "schema": schema,
                } for table_name in views
            ]

        return []

    def get_columns(
        self, table_name: str, schema: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        if self.d_type == DataSourceType.API:
            # API数据源字段信息从参数解析
            for item in self.api_tables:
                if item.name == table_name:
                    data_path = json.loads(item.data_path)
                    return [{
                        "autoincrement": "",
                        "comment": "",
                        "default": "",
                        "name": col,
                        "nullable": "",
                        "type": ""
                    }for col in data_path.get("columns", {}).values()]

        if schema is None:
            schema = self.get_default_schema()

        cols = self.database.get_columns(table_name, schema)
        for col in cols:
            col["type"] = col["type"].compile().lower()
        return cols

    def add_user_permission(self, privilege_value: int = 1):
        """新增用户权限，在新增数据时调用"""
        self._add_user_permission(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATASOURCE,
            privilege_value=privilege_value,
        )

    def can_access(self, privilege_value: int = 1):
        """验证当前用户是否有权限"""
        self._can_access(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATASOURCE,
            privilege_value=privilege_value,
        )


class DataSourceGroup(Model, AuditMixinNullable):
    __tablename__ = "datasource_group"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    pid = Column(Integer, nullable=False, default=0, index=True, comment='parent id')
    level = Column(Integer, nullable=False, default=0, comment='级别')
    datasource = relationship(
        DataSource,
        backref="datasource_group",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<DataSourceGroup id={self.id} name={self.name}"

    def add_user_permission(self, privilege_value: int = 1):
        self._add_user_permission(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATASOURCE_GROUP,
            privilege_value=privilege_value,
        )

    def can_access(self, privilege_value: int = 1):
        """验证当前用户是否有权限"""
        self._can_access(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATASOURCE_GROUP,
            privilege_value=privilege_value,
        )


class APITables(Model, AuditMixinNullable, ImportExportMixin):
    __tablename__ = "api_tables"
    # __table_args__ = (UniqueConstraint("name", "datasource_id"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    status = Column(Integer)
    configuration = Column(String(5000), nullable=True)
    data_path = Column(String(5000), nullable=True)
    datasource_id = Column(Integer, ForeignKey("datasource.id"), index=True)
    extra = Column(String(1000), comment='额外信息')
    table_task = relationship("TablesTask",
                              backref="api_table",
                              cascade="all, delete-orphan",)

    @property
    def table_name(self):
        return self.uuid.hex


class TablesTask(Model, AuditMixinNullable):
    __tablename__ = "tables_task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    table = relationship(
        "SqlaTable",
        backref=backref("table_tasks", cascade="all, delete-orphan"),
    )
    api_table_id = Column(Integer, ForeignKey("api_tables.id"))
    name = Column(String(50), nullable=False)
    update_type = Column(String(50), nullable=False)
    start_time = Column(BigInteger)
    rate = Column(Integer, nullable=False)
    cron = Column(String(255))
    end = Column(String(50))
    end_time = Column(BigInteger)
    last_exec_time = Column(DateTime)
    last_exec_status = Column(String(50))
    extra_data = Column(Text)
    status = Column(Integer)
    table_task_logs = relationship(
        "TablesTaskLog",
        backref="table_task",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return self.name


class TablesTaskLog(Model):
    __tablename__ = "tables_task_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_task_id = Column(Integer, ForeignKey("tables_task.id"))
    task_id = Column(String(50))
    start_time = Column(BigInteger)
    end_time = Column(BigInteger)
    status = Column(SmallInteger)
    info = Column(Text)
