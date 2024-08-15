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
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, Dict

from superset.commands.base import BaseCommand, UpdateMixin
from superset.constants import MenuName
from superset.models.user import UserV2
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.v2.water_mark.dao import WaterMarkDAO

logger = logging.getLogger(__name__)


class UpdateWaterMarkV2Command(UpdateMixin, BaseCommand):
    def __init__(self, user: UserV2, data: Dict[str, Any]):
        self._actor = user
        self._properties = data.copy()

    def run(self):
        # self.validate()
        WaterMarkDAO.edit_water_mark_config(self._properties)

    def validate(self):
        menu = SysMenuDAO.find_by_name(MenuName.USER_MANAGEMENT)
        menu.can_access()
