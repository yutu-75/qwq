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
@Time       : 2023/5/15 18:15
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, Dict

from superset.commands.base import BaseCommand
from superset.datasets.dao import DatasetDAO
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.user import UserV2
from superset.constants import ROW_COL_SECURITY
from superset.v2.datasets.rls_filter.dao import RLSFilterDAO

logger = logging.getLogger(__name__)


class CreateRLSDataCommand(BaseCommand):
    def __init__(self, user: UserV2, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._dataset = None

    def run(self) -> dict:
        self.validate()
        rls = RLSFilterDAO.add_rls_filter(self._dataset, self._properties)
        return rls.to_json()

    def validate(self) -> None:
        self._dataset = DatasetDAO.find_by_id(self._properties["dataset_id"])
        if self._dataset is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._dataset.can_access(ROW_COL_SECURITY)
