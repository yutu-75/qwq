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
@Time       : 2023/3/17 12:18
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import List

from flask_appbuilder import Model
from flask_babel import _

from superset import db
from superset.constants import VIEW, GRANT
from superset.dao.base import BaseDAO
from superset.models.sys_manager import SysMenu


class SysMenuDAO(BaseDAO):
    model_cls = SysMenu

    @classmethod
    def find_by_name(cls, name: str):
        return db.session.query(SysMenu).filter_by(name=name).first()

    @classmethod
    def find_by_pid(cls, pid: int) -> List[dict]:
        return db.session.query(cls.model_cls).filter_by(pid=pid).all()

    @classmethod
    def find_menus_by_pid(cls, pid: int) -> List[dict]:
        res = cls.find_by_pid(pid)
        return [
            {
                "id": item.id,
                "pid": item.pid,
                "name": item.name,
                "icon": item.icon,
                "label": _(item.label),
                "children": cls.find_menus_by_pid(item.id)
            } for item in res
        ]

    @classmethod
    def find_all_by_pid(cls, user: Model, pid: int = 0) -> List[dict]:
        res = cls.find_by_pid(pid)
        result = []
        for item in res:
            menus = {
                "id": item.id,
                "pid": item.pid,
                "name": item.name,
                "icon": item.icon,
                "label": _(item.label),
                "url": item.url,
                "perm": GRANT,
                "children": cls.find_all_by_pid(user, item.id)
            }
            if user.is_admin and pid == 0 and item.name == "Security":
                menus["children"] += [{
                    "id": 0,
                    "pid": item.id,
                    "name": 'Watermark Settings',
                    "icon": item.icon,
                    "label": _('Watermark Settings'),
                    "url": '/sys/watermark',
                    "perm": GRANT,
                    "children": []
                }]

            result.append(menus)

        return result

    @classmethod
    def find_auth_detail_by_admin(
        cls,
        pid: int,
        data_auth: dict,
        max_data_auth: dict = {},
    ) -> List[dict]:
        res = cls.find_by_pid(pid)
        return [
            {
                "id": item.id,
                "pid": item.pid,
                "name": item.name,
                "icon": item.icon,
                "label": _(item.label),
                "perm": data_auth.get(item.id, 0),
                "max_perm": max_data_auth.get(item.id, 0),
                "children": cls.find_auth_detail_by_admin(item.id, data_auth, max_data_auth)
            } for item in res
        ]

    @classmethod
    def find_auth_detail_by_user(
        cls,
        pid: int,
        data_auth: dict
    ) -> List[dict]:
        res = cls.find_by_pid(pid)
        return [
            {
                "id": item.id,
                "pid": item.pid,
                "name": item.name,
                "icon": item.icon,
                "label": _(item.label),
                "url": item.url,
                "perm": data_auth.get(item.id, 0),
                "children": cls.find_auth_detail_by_user(item.id, data_auth)
            } for item in res if data_auth.get(item.id, False)
        ]

    @classmethod
    def find_menus(cls) -> List[Model]:
        query = db.session.query(cls.model_cls).order_by(
            cls.model_cls.pid.desc())
        return query.all()

    @classmethod
    def find_all_by_user(
        cls,
        data_auth: dict,
        data_filter: set = None,
        max_data_auth: dict = {},
    ) -> List[dict]:
        menus = cls.find_menus()
        res = {}
        for item in menus:
            if data_filter is None:
                if data_auth.get(item.id, 0) < VIEW:
                    continue

            else:
                if item.id not in data_filter:
                    continue

            group = {
                "id": item.id,
                "pid": item.pid,
                "name": item.name,
                "icon": item.icon,
                "label": _(item.label),
                "url": item.url,
                "perm": data_auth.get(item.id, 0),
                "children": res.get(item.id, []),
                "max_perm": max_data_auth.get(item.id, 0)
            }

            if res.get(item.pid, False):
                res[item.pid].append(group)

            else:
                res[item.pid] = [group]

        return res.get(0, [])
