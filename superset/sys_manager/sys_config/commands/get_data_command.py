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
from typing import Any

from flask import g

from superset.commands.base import BaseCommand
from superset.constants import MenuName
from superset.models.user import UserV2
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.sys_manager.sys_config.dao import SysConfigDAO

logger = logging.getLogger(__name__)


class SysConfigInfoCommand(BaseCommand):
    def __init__(self, user: UserV2, _type: str):
        self._type = _type
        self._actor = user

    def run(self, **kwargs: Any) -> dict:
        self.validate()
        res = SysConfigDAO.find_by_type(self._type)
        if res:
            status = res[0].status
            res = {item.param_key: item.param_value for item in res}
            res.update({"status": status})
            # 水印文字使用name和工号
            if self._type == "WATER_MARK":
                res["original_text"] = res["TEXT"]
                res["TEXT"] = res["TEXT"].replace(
                    '${email}', g.user.email).replace(
                    '${username}', g.user.username).replace(
                    '${name}', g.user.cn_name).replace(
                    '/#', "")
            return res

        return {}

    def validate(self) -> None:
        pass
