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
@Time       : 2023/3/29 13:15
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
from superset.models.dashboard import DashboardGroup
from superset.constants import AuthSourceType, MANAGE
from superset.v2.dashboards.dao import DashboardV2DAO
from superset.v2.dashboards.group.dao import DashboardGroupDAO


class DeleteDashboardGroupCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[DashboardGroup] = None

    def run(self) -> Model:
        self.validate()
        group_ids = DashboardGroupDAO.find_children_ids_by_pid(self._model_id)
        group_ids.add(self._model_id)
        dashboards = DashboardV2DAO.find_by_group_ids(group_ids)
        if dashboards:
            raise HTTPError(Messages.DEL_GROUP_ERROR, 400)

        DashboardGroupDAO.delete_by_ids(group_ids)
        DashboardGroupDAO.delete_auth_by_source_ids(
            auth_source_ids=group_ids,
            auth_source_type=AuthSourceType.DASHBOARD_GROUP,
        )
        self.archiving()
        return self._model

    def validate(self) -> None:
        self._model = DashboardGroupDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        if (
            not self._actor.is_admin and
            self._model.created_by_fk != self._actor.id
        ):
            raise HTTPError(Messages.FORBIDDEN, 403)

        self._model.can_access(MANAGE)
        # DashboardGroupDAO.check_group_is_empty(self._model_id)

    def archiving(self):
        """将删除的dashboard group归档"""
        doc_json = self._model.to_json()
        dashboard_ids = [dashboard.id for dashboard in self._model.dashboards]
        doc_json.update({"dashboard_ids": dashboard_ids})
        DashboardGroupDAO.archiving_docs("dashboard_group", doc_json)
