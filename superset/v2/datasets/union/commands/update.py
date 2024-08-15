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
@Time       : 2023/7/18 14:21
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Dict, Any

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User
from superset.commands.base import BaseCommand
from superset.constants import DatasetType
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.datasets.dao import DatasetV2DAO


class UpdateUnionDatasetCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._properties = data
        self._model = None

    def run(self, **kwargs) -> Model:
        self.validate()
        dataset = DatasetV2DAO.update(self._model, self._properties)
        return dataset

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        if self._model.type_classify != DatasetType.UNION:
            raise HTTPError(Messages.NOT_EXIST, 400)
