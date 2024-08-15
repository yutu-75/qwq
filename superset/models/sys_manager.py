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
@Time       : 2023/3/14 11:26
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from superset.models.helpers import AuditMixinNullable, PermissionMixin
from superset.constants import AuthSourceType, VIEW
from superset.models.user import UserV2


class SysAuth(Model, AuditMixinNullable):
    __tablename__ = "sys_auth"
    __table_args__ = (UniqueConstraint(
        "auth_target", "auth_target_type", "auth_source", "auth_source_type"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    auth_source_type = Column(String(100), nullable=False, comment="授权数据源类型")
    auth_source = Column(Integer, index=True, nullable=False, comment="授权数据源ID")
    auth_target_type = Column(String(100), nullable=False, comment="搜授权目标类型")
    auth_target = Column(Integer, nullable=False, comment="授权目标ID")
    privilege_value = Column(Integer, nullable=False, default=0, comment="授权级别")


class DatabaseAuth(Model, AuditMixinNullable):
    __tablename__ = "db_auth"
    __table_args__ = (UniqueConstraint(
        "database_id", "schema", "table_name", "auth_target", "auth_target_type"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    auth_source_type = Column(String(100), nullable=False, comment="授权数据源类型")
    datasource_id = Column(Integer, index=True, nullable=False, comment="数据源ID")
    database_id = Column(Integer, index=True, nullable=False, comment="数据库ID")
    schema = Column(String(100), nullable=False, comment="模式")
    table_name = Column(String(100), nullable=False, comment="表名称")
    auth_target_type = Column(String(100), nullable=False, comment="搜授权目标类型")
    auth_target = Column(Integer, nullable=False, comment="授权目标ID")
    privilege_value = Column(Integer, nullable=False, default=0, comment="授权级别")


SysDeptUsers = Table(
    "sys_dept_users",
    Model.metadata,
    Column("id", Integer, primary_key=True),
    Column("dept_id", Integer, ForeignKey("sys_dept.id", ondelete="CASCADE")),
    Column("user_id", Integer, ForeignKey("ab_user.id", ondelete="CASCADE")),
)


class SysDept(Model, AuditMixinNullable):
    __tablename__ = "sys_dept"
    __table_args__ = (UniqueConstraint("pid", "title"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(128), nullable=False, comment="组织名称")
    pid = Column(Integer, nullable=False, default=0, comment="父组织ID")
    top_id = Column(Integer, nullable=False, default=0, comment="顶层组织ID")
    level = Column(Integer, nullable=False, default=0, comment="等级")
    users = relationship(
        UserV2,
        secondary=SysDeptUsers,
        backref="depts",
        passive_deletes=True
    )


class Archive(Model, AuditMixinNullable):
    __tablename__ = "archive"

    id = Column(Integer, primary_key=True, autoincrement=True)
    doc_type = Column(String(50), nullable=False, comment='类型')
    doc_json = Column(Text, comment='json 元数据')


class SysMenu(Model, PermissionMixin):
    __tablename__ = "sys_menu"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pid = Column(Integer, nullable=False, default=0, comment="父菜单ID")
    name = Column(String(50), nullable=False, comment="菜单名称")
    icon = Column(String(50), nullable=True, default='', comment="菜单图标")
    label = Column(String(50), nullable=True, default='', comment="菜单标签")
    url = Column(String(255), nullable=True, default='', comment="菜单链接")

    def can_access(self, privilege_value: int = VIEW):
        """验证当前用户是否有权限"""
        self._can_access(
            auth_source=self.id,
            auth_source_type=AuthSourceType.MENU,
            privilege_value=privilege_value,
        )
