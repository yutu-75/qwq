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
@Time       : 2023/5/16 9:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Optional

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.dashboards.group.dao import DashboardGroupDAO
from superset.v2.datasets.rls_filter.dao import RLSFilterDAO


class DeleteRLSFilterCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[Model] = None

    def run(self) -> Model:
        self.validate()
        RLSFilterDAO.delete(self._model, commit=False)
        return self._model

    def validate(self) -> None:
        self._model = RLSFilterDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access()

    def archiving(self):
        """将删除的dashboard group归档"""
        doc_json = self._model.to_json()
        DashboardGroupDAO.archiving_docs("rls_filter", doc_json)
