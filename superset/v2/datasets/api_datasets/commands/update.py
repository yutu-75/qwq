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
@Time       : 2023/8/8 14:48
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, Dict

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import UpdateMixin
from superset.constants import MANAGE
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.datasets.api_datasets.commands.create import \
    CreateAPIDatasetTaskCommand
from superset.v2.datasets.api_datasets.dao import TableTaskDAO

logger = logging.getLogger(__name__)


class UpdateDatasetTaskCommand(UpdateMixin, CreateAPIDatasetTaskCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._model = None
        self._table = None
        self._properties = data

    def run(self):
        self.validate()
        if self._properties["rate"] == 1:
            self.update_api_dataset(self._table, self._model.api_table)

        task = TableTaskDAO.update(self._model, self._properties)
        return task

    def validate(self):
        self._model = TableTaskDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._table = self._model.table
        self._table.can_access(MANAGE)
        if TableTaskDAO.validate_uniqueness(
            self._properties["name"],
            self._table.id,
            self._model_id
        ):
            raise HTTPError(Messages.IS_EXIST, 400)
