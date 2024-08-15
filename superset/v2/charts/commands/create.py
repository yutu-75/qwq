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

from flask_sqlalchemy import Model

from superset.charts.commands.create import CreateChartCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.constants import MANAGE, GRANT
from superset.v2.charts.dao import ChartV2DAO
from superset.v2.charts.group.dao import ChartGroupDAO

logger = logging.getLogger(__name__)


class CreateChartV2Command(CreateChartCommand):
    def run(self) -> Model:
        chart = super(CreateChartV2Command, self).run()
        chart.add_user_permission(GRANT)  # 写入权限
        return chart

    def validate(self) -> None:
        group = ChartGroupDAO.find_by_id(self._properties["slice_group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

        group.can_access(MANAGE)

        if not ChartV2DAO.validate_uniqueness(
            self._properties['slice_name'],
            self._properties['slice_group_id']
        ):
            raise HTTPError(Messages.DUPLICATE_NAME, 400)

        super(CreateChartV2Command, self).validate()
