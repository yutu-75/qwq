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
import math
from typing import Any, List

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import ROW_COL_SECURITY
from superset.v2.datasets.dao import DatasetV2DAO
from superset.v2.datasets.rls_filter.dao import RLSFilterDAO

logger = logging.getLogger(__name__)


class RLSFilterDataCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> List[Any]:
        self.validate()
        return self._model.data

    def validate(self) -> None:
        self._model = RLSFilterDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access()


class DatasetRLSFilterDataCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> dict:
        self.validate()
        page = kwargs.get("page", 1)
        limit = kwargs.get("limit", 20)
        res = self._model.row_level_security_filters
        count_ = len(res)
        total_page = math.ceil(count_ / 20)
        if page > total_page:
            return {"result": [], "total_page": total_page}

        return {
            "result": [item.data for item in res[(page-1)*limit: page*limit]],
            "total_page": total_page
        }

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(ROW_COL_SECURITY)
