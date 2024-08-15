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
from superset.connectors.sqla.models import TableGroup
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import AuthSourceType, MANAGE
from superset.v2.datasets.dao import DatasetV2DAO
from superset.v2.datasets.group.dao import DatasetGroupDAO

logger = logging.getLogger(__name__)


class DeleteDatasetGroupCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[TableGroup] = None

    def run(self) -> Model:
        self.validate()
        group_ids = DatasetGroupDAO.find_children_ids_by_pid(self._model_id)
        group_ids.add(self._model_id)
        dataset = DatasetV2DAO.find_by_group_ids(group_ids)
        if dataset:
            raise HTTPError(Messages.DEL_GROUP_ERROR, 400)
        DatasetGroupDAO.delete_by_ids(group_ids)
        DatasetGroupDAO.delete_auth_by_source_ids(
            auth_source_ids=group_ids,
            auth_source_type=AuthSourceType.DATASET_GROUP,
        )
        self.archiving()
        return self._model

    def validate(self) -> None:
        self._model = DatasetGroupDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        if (
            not self._actor.is_admin and
            self._model.created_by_fk != self._actor.id
        ):
            raise HTTPError(Messages.FORBIDDEN, 403)

        self._model.can_access(MANAGE)
        # DatasetGroupDAO.check_group_is_empty(self._model_id)

    def archiving(self):
        """将删除的dataset group归档"""
        doc_json = self._model.to_json()
        DatasetGroupDAO.archiving_docs("dataset_group", doc_json)
