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
@Time       : 2023/5/15 18:00
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, List

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import ROW_COL_SECURITY
from superset.v2.datasets.dao import DatasetV2DAO
from superset.v2.datasets.data_masking.dao import DataMaskingDAO

logger = logging.getLogger(__name__)


class MaskingRuleCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> List[Any]:
        self.validate()
        return self._model.data_masking

    def validate(self) -> None:
        self._model = DataMaskingDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(ROW_COL_SECURITY)


class DatasetMaskingRuleListCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> List[Any]:
        self.validate()
        return [item.data_masking for item in self._model.columns]

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(ROW_COL_SECURITY)
