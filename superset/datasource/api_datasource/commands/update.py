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
@Time       : 2023/7/5 9:31
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
from typing import Any, Dict, Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.datasource.api_datasource.dao import APITablesDAO, DataSourceDAO
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.core import Database
from superset.v2.utils.data_save_db import get_save_default_db


class UpdateApiDataSourceCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[Database] = None

    def run(self) -> Model:
        self.validate()
        tables = self._properties.pop("tables")
        self._model.api_tables = []
        for item in tables:
            model = APITablesDAO.create(
                {
                    "name": item["name"],
                    "datasource_id": self._model_id,
                    "configuration": json.dumps(item["configuration"]),
                    "data_path": json.dumps(item["data_path"]),
                },
                commit=False
            )
            self._model.api_tables.append(model)

        datasource = DataSourceDAO.update(
            self._model,
            {
                'name': self._properties["name"],
                "database": self._properties["database"],
            }
        )
        APITablesDAO.delete_by_null()
        return datasource

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError('Dataset does not exist', 400)

        if self._model.name != self._properties["name"]:
            if DataSourceDAO.validate_uniqueness(self._properties["name"]):
                raise HTTPError(Messages.DUPLICATE_NAME, 400)

        self._properties["database"] = get_save_default_db(self._actor)

        tables = set()
        for item in self._properties["tables"]:
            if item["name"] in tables:
                raise HTTPError('Duplicate data table name', 400)

            tables.add(item["name"])
