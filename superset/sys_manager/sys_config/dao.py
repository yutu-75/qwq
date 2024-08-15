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
import json
import logging
from typing import List

from superset import db
from superset.dao.base import BaseDAO
from superset.models.sys_config import SysConfig

logger = logging.getLogger(__name__)


class SysConfigDAO(BaseDAO):
    model_cls = SysConfig

    @classmethod
    def find_by_type(cls, _type: str) -> List:
        res = db.session.query(cls.model_cls).filter(
            cls.model_cls.config_type == _type
        ).all()
        return res
