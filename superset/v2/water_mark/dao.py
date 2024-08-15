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

from superset.dao.base import BaseDAO
from superset.extensions import db
from superset.models.sys_config import SysConfig
from superset.sys_manager.sys_config.dao import SysConfigDAO

logger = logging.getLogger(__name__)


class WaterMarkDAO(BaseDAO):

    @classmethod
    def get_all_water_mark_config(cls):

        res = SysConfigDAO.find_by_type('WATER_MARK')
        if res:
            res = {item.param_key: item.param_value for item in res}
        else:
            res = {}

        return {
            "TEXT": res.get('TEXT', '长安水印logo'),
            "COLOR": res.get('COLOR', '#8B8B1B'),
            "SIZE": int(res.get('SIZE', '30')),
            "OPACITY": float(res.get('OPACITY', '0.5')),
            "SPACE": int(res.get('SPACE', '400')),
            "ANGLE": int(res.get('ANGLE', '50')),
            "PDF_WIDTH": int(res.get('PDF_WIDTH', '1200')),
            "PDF_HIGH": int(res.get('PDF_HIGH', '2000')),
        }

    @classmethod
    def edit_water_mark_config(cls, params: dict):
        for key, value in params.items():
            obj = db.session.query(SysConfig).filter(
                SysConfig.config_type == 'WATER_MARK',
                SysConfig.param_key == key
            ).first()
            if obj:
                obj.param_value = value

        db.session.commit()
