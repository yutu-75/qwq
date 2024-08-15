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
@Time       : 2023/3/16 17:20
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, Dict, Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand, CreateMixin
from superset.databases.dao import DatabaseDAO
from superset.exceptions import HTTPError
from superset.models.core import Database

logger = logging.getLogger(__name__)


class MoveDatabaseCommand(CreateMixin, BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[Database] = None
        self._properties = data

    def run(self) -> Model:
        self.validate()
        DatabaseDAO.update(
            self._model,
            {
                "db_group_id": self._properties["target_id"],
                "database_name": self._properties["new_title"],
            }
        )
        return self._model

    def validate(self) -> None:
        database = DatabaseDAO.find_by_id(self._model_id)
        if database is None:
            raise HTTPError("数据库不存在", 400)

        self._model = database
