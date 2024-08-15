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

import logging
from typing import Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import AuthSourceType, MANAGE, DataBaseType
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.datasource import DataSource
from superset.v2.database_sync.database.dao import DatabaseSyncDAO

logger = logging.getLogger(__name__)


class DeleteDatabaseSyncCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[DataSource] = None

    def run(self) -> Model:
        self.validate()
        try:

            DatabaseSyncDAO.delete(self._model, commit=False)
            DatabaseSyncDAO.delete_auth_by_source({
                "auth_source": self._model_id,
                "auth_source_type": AuthSourceType.DATABASE_SYNC,
            })
        except Exception as e:
            raise HTTPError(Messages.DEL_SYNC_TASK_ERR, 400)

        return self._model

    def validate(self) -> None:

        self._model = DatabaseSyncDAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError(Messages.NOT_EXIST, 400)

        if (
            not self._actor.is_admin and
            self._model.created_by_fk != self._actor.id
        ):
            raise HTTPError(Messages.FORBIDDEN, 403)

        self._model.can_access(MANAGE)
