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
from superset.models.core import Log

logger = logging.getLogger(__name__)


class LogV2DAO(BaseDAO):
    model_cls = Log

    @classmethod
    def get_all(cls, params: dict):
        conditions = []
        if params.get('user_id', ''):
            conditions.append(Log.user_id == params['user_id'])
        if params.get('action', ''):
            conditions.append(Log.action.startswith(params['action']))
        if params.get('dttm_start', ''):
            conditions.append(Log.dttm >= params['dttm_start'])
        if params.get('dttm_end', ''):
            conditions.append(Log.dttm <= params['dttm_end'])

        # 总数
        count = db.session.query(Log).filter(*conditions).count()

        if count == 0:
            return {
                "count": 0,
                "list": [],
            }
        else:
            obj_list = db.session.query(
                Log
            ).filter(*conditions).order_by(
                Log.dttm.desc()
            ).limit(
                params.get("page_size", 100)
            ).offset(
                (params.get("page_index", 1) - 1) * params.get("page_size", 100)
            )

        return {
            "count": count,
            "list": [
                {
                    "id": item.id,
                    "user_id": item.user_id,
                    "dashboard_id": item.dashboard_id,
                    "slice_id": item.slice_id,
                    "duration_ms": item.duration_ms,
                    "action": item.action,
                    "referrer": item.referrer,
                    "json": item.json,
                    "dttm": item.dttm,
                    "user":
                        {
                            "id": item.user.id,
                            "username": item.user.username,
                            'cn_name': item.user.cn_name,
                            'first_name': item.user.first_name,
                            'last_name': item.user.last_name,
                        } if item.user is not None else {}
                } for item in obj_list
            ]
        }

    @classmethod
    def get_users(cls):
        res = cls.find_all()
        return [
            {
                "id": item.id,
                "first_name": item.first_name,
                "last_name": item.last_name,
                "username": item.username,
                "cn_name": item.cn_name,
                "email": item.email,
                "active": item.active,
            } for item in res
        ]
