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
@Time       : 2023/7/12 15:45
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Dict, Any

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import MANAGE, DatasetType, GRANT
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.databases.dao import DatabaseV2DAO
from superset.v2.datasets.dao import DatasetV2DAO
from superset.v2.datasets.group.dao import DatasetGroupDAO

logger = logging.getLogger(__name__)


class CreateUnionDatasetCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self) -> Model:
        self.validate()
        # Creates SqlaTable (Dataset)
        dataset = DatasetV2DAO.create(self._properties, commit=False)
        # Updates columns and metrics from the dataset
        dataset.fetch_metadata(label_columns=self._properties['label_columns'])
        dataset.add_user_permission(GRANT)
        return dataset

    def validate(self) -> None:
        group = DatasetGroupDAO.find_by_id(self._properties["table_group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        group.can_access(MANAGE)
        if not DatasetV2DAO.validate_uniqueness(
            self._properties["custom_name"],
            self._properties["table_group_id"]
        ):
            raise HTTPError(Messages.DUPLICATE_NAME, 400)

        self._properties["database"] = DatabaseV2DAO.find_by_id(
            self._properties["database_id"])
        if self._properties["database"] is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._properties["type_classify"] = DatasetType.UNION
        self._properties["table_name"] = self._properties["custom_name"]
