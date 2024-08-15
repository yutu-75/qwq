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
@Time       : 2023/7/5 9:32
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
from typing import Dict, Any

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User

from superset import db
from superset.commands.base import BaseCommand, CreateMixin
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import GRANT, MANAGE
from superset.v2.datasources.api_datasources.dao import APITablesDAO
from superset.v2.datasources.dao import DataSourceDAO
from superset.v2.datasources.group.dao import DataSourceGroupDAO
from superset.v2.utils.data_save_db import get_save_default_db


class CreateApiDataSourceCommand(CreateMixin, BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self) -> Model:
        self.validate()
        datasource = DataSourceDAO.create({
            'name': self._properties["name"],
            'desc': self._properties["desc"],
            "database": self._properties["database"],
            "d_type": self._properties["d_type"],
            "group_id": self._properties["group_id"],
        }, commit=False)
        db.session.flush()
        for item in self._properties["tables"]:
            APITablesDAO.create(
                {
                    "name": item["name"],
                    "datasource_id": datasource.id,
                    "configuration": json.dumps(item["configuration"]),
                    "data_path": json.dumps(item["data_path"]),
                    "extra": item["extra"],
                    "status": item.get("status", 1)
                },
                commit=False
            )

        datasource.add_user_permission(GRANT)
        return datasource

    def validate(self) -> None:
        group = DataSourceGroupDAO.find_by_id(self._properties["group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        group.can_access(MANAGE)  # 验证当前分组是否有新建权限

        if not DataSourceDAO.validate_uniqueness(
            self._properties["name"],
            self._properties["group_id"]
        ):
            raise HTTPError(Messages.DUPLICATE_NAME, 400)

        self._properties["database"] = get_save_default_db(self._actor)
        tables = set()
        for item in self._properties["tables"]:
            if item["name"] in tables:
                raise HTTPError(Messages.API_DATASOURCE_TABLE_NAME_DUPLICATE, 400)

            tables.add(item["name"])
