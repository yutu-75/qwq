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
@Time       : 2023/7/5 9:05
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from datetime import datetime
from typing import Dict, Any

from flask_appbuilder.security.sqla.models import User
from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import GRANT, MANAGE
from superset.v2.databases.dao import DatabaseV2DAO
from superset.v2.datasources.dao import DataSourceDAO
from superset.v2.datasources.group.dao import DataSourceGroupDAO


class CreateDatabaseDataSourceCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self, **kwargs):
        self.validate()
        group_id = self._properties.pop("group_id")
        d_name = self._properties.pop("database_name")
        ts = int(datetime.now().timestamp() * 1000)
        self._properties["verbose_name"] = d_name
        self._properties["database_name"] = d_name + f"_{ts}"
        self._properties.pop("masked_encrypted_extra", None)
        database = DatabaseV2DAO.create(self._properties)
        database.set_sqlalchemy_uri(database.sqlalchemy_uri)
        datasource = DataSourceDAO.create({
            "name": d_name,
            "group_id": group_id,
            "database_id": database.id
        })
        datasource.add_user_permission(GRANT)  # 写入权限
        database.add_user_db_permission(GRANT)
        return datasource

    def validate(self) -> None:
        group = DataSourceGroupDAO.find_by_id(self._properties["group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        group.can_access(MANAGE)  # 验证当前分组是否有新建权限
        if not DataSourceDAO.validate_uniqueness(
            self._properties["database_name"],
            self._properties["group_id"],
        ):
            raise HTTPError(Messages.DUPLICATE_NAME, 400)

        if not self._properties.get("sqlalchemy_uri", False):
            raise HTTPError(Messages.PARAMETER_ERROR, 400)
