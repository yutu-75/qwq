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
@Time       : 2023/3/29 14:29
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Optional

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.dashboards.share.dao import DashboardShareDAO
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.dashboard import Dashboard
from superset.constants import AuthSourceType, MANAGE
from superset.v2.dashboards.dao import DashboardV2DAO
from superset.v2.dashboards.group.dao import DashboardGroupDAO


class DashboardV2DeleteCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[Dashboard] = None

    def run(self):
        self.validate()

        # 判断是否关联的分享链接,有则先删除关联的分享链接
        dashboard_share_id = DashboardShareDAO.find_by_dashboard_id(self._model.id)
        if dashboard_share_id:
            DashboardShareDAO.delete(dashboard_share_id)

        DashboardV2DAO.delete(self._model, commit=False)
        DashboardGroupDAO.delete_auth_by_source({
            "auth_source": self._model_id,
            "auth_source_type": AuthSourceType.DASHBOARD,
        })
        self.archiving()
        return self._model

    def validate(self) -> None:
        self._model = DashboardV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        if (
            not self._actor.is_admin and
            self._model.created_by_fk != self._actor.id
        ):
            raise HTTPError(Messages.FORBIDDEN, 403)

        self._model.can_access(MANAGE)

    def archiving(self):
        """将删除的dashboard归档"""
        doc_json = self._model.to_json()
        doc_json["uuid"] = doc_json["uuid"].hex
        DashboardGroupDAO.archiving_docs("dashboard", doc_json)
