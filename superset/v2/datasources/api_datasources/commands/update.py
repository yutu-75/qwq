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
@Time       : 2023/7/5 9:31
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
import logging
from typing import Any, Dict, Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import MANAGE, DataSourceType
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.core import Database
from superset.v2.datasources.api_datasources.dao import APITablesDAO
from superset.v2.datasources.dao import DataSourceDAO
from superset.v2.utils.data_save_db import get_save_default_db

logger = logging.getLogger(__name__)


class UpdateApiDataSourceCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[Database] = None

    def run(self) -> Model:
        self.validate()
        old_tables = self._model.api_tables
        len_ = len(old_tables)
        for i, item in enumerate(self._properties["tables"]):
            if i < len_:
                old_tables[i].name = item["name"]
                old_tables[i].datasource_id = self._model_id
                old_tables[i].configuration = json.dumps(item["configuration"])
                old_tables[i].data_path = json.dumps(item["data_path"])
                old_tables[i].status = item.get("status", 1)
                old_tables[i].extra = item["extra"]
                continue

            api_table = APITablesDAO.create(
                {
                    "name": item["name"],
                    "datasource_id": self._model_id,
                    "configuration": json.dumps(item["configuration"]),
                    "data_path": json.dumps(item["data_path"]),
                    "extra": item["extra"],
                    "status": item.get("status", 1)
                },
                commit=False
            )
            old_tables.append(api_table)

        self._model.api_tables = old_tables[:len(self._properties["tables"])]
        datasource = DataSourceDAO.update(
            self._model,
            {
                'name': self._properties["name"],
                'desc': self._properties["desc"],
                "database": self._properties["database"],
                "d_type": self._properties.get("d_type", DataSourceType.API),
            }
        )
        APITablesDAO.delete_by_null()
        return datasource

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
        if self._model.name != self._properties["name"]:
            if not DataSourceDAO.validate_uniqueness(
                self._properties["name"],
                self._properties["group_id"],
            ):
                raise HTTPError(Messages.DUPLICATE_NAME, 400)

        self._properties["database"] = get_save_default_db(self._actor)
        # 校验表名称是否重复
        tables = set()
        for item in self._properties["tables"]:
            if item["name"] in tables:
                raise HTTPError(Messages.API_DATASOURCE_TABLE_NAME_DUPLICATE,
                                400)

            tables.add(item["name"])
