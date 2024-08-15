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
@Time       : 2023/3/29 12:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
from typing import List

from flask_appbuilder import Model
from sqlalchemy import or_

from superset import db
from superset.constants import (
    GRANT,
    VIEW,
    AuthSourceType,
    ALL_VIEW,
    ALL_EXPORT,
    ALL_MANAGE,
    ALL_ROW_COL_SECURITY,
    ALL_GRANT
)
from superset.dao.base import BaseGroupDAO
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.dashboard import DashboardGroup, Dashboard
from superset.models.user import UserV2
from superset.v2.user.dao import UserV2DAO


class DashboardGroupDAO(BaseGroupDAO):
    model_cls = DashboardGroup

    @classmethod
    def find_groups_perm(cls, user_id, perm=VIEW):
        """
        子分组继承父分组权限
        """
        groups_perm = DashboardGroupDAO.find_auth_source_perm_by_user(
            AuthSourceType.DASHBOARD_GROUP, user_id, perm)
        groups = db.session.query(
            DashboardGroup.id,
            DashboardGroup.pid
        )
        for group in groups:
            pid_perm = groups_perm.get(group[1], 0)
            group_perm = groups_perm.get(group[0], 0)
            if pid_perm > group_perm:
                if pid_perm in {ALL_VIEW, ALL_EXPORT, ALL_MANAGE, ALL_ROW_COL_SECURITY, ALL_GRANT}:
                    groups_perm[group.id] = pid_perm

        return groups_perm

    @classmethod
    def find_data_perm(cls, user_id, group_auth, perm=VIEW):
        """
        资源继承分组权限
        """
        dashs_perm = cls.find_auth_source_perm_by_user(
            AuthSourceType.DASHBOARD, user_id, perm)
        dashs = db.session.query(
            Dashboard.id,
            Dashboard.dashboard_group_id
        )
        for dash in dashs:
            group_perm = group_auth.get(dash[1], 0)
            dash_perm = dashs_perm.get(dash[0], 0)
            if group_perm > dash_perm:
                if group_perm in {ALL_VIEW, ALL_EXPORT, ALL_MANAGE, ALL_ROW_COL_SECURITY, ALL_GRANT}:
                    dashs_perm[dash[0]] = group_perm

        return dashs_perm

    @classmethod
    def find_creator(cls):
        subquery1 = db.session.query(cls.model_cls.created_by_fk).subquery()
        subquery2 = db.session.query(cls.model_cls.changed_by_fk).subquery()
        query = db.session.query(
            UserV2.id,
            UserV2.cn_name,
        ).filter(or_(
            UserV2.id.in_(subquery1),
            UserV2.id.in_(subquery2)
        ))
        return {
            item[0]: {"id": item[0], "cn_name": item[1]}
            for item in query.all()
        }

    @classmethod
    def find_dashs_group(
        cls,
        dashs: list,
        data_auth: dict,
        group_auth: dict,
        is_admin: bool = False
    ) -> dict:
        dashboards = {}
        users = cls.find_creator()
        for dashboard in dashs:
            data_perm = data_auth.get(dashboard[0], 0)
            dash_group_auth = group_auth.get(dashboard[1], 0)
            if dash_group_auth > data_perm:
                data_perm = GRANT

            dash = {
                "dashboard_id": dashboard[0],
                "dashboard_title": dashboard[2],
                "created_by_fk": users.get(dashboard[3]),
                "created_on": str(dashboard[4]),
                "changed_on": str(dashboard[5]),
                "changed_by_fk": users.get(dashboard[6]),
                "adaptation_equipment": dashboard[7],
                "perm": data_perm,
                "max_perm": data_perm,
                "layout_mode": ""
            }
            # TODO 长度超过65535报错
            if dashboard[-1]:
                try:
                    dash['layout_mode'] = json.loads(dashboard[-1]).get("layout_mode",
                                                                        "")
                except Exception as e:
                    pass

            if dashboards.get(dashboard[1], False):
                dashboards[dashboard[1]].append(dash)

            else:
                dashboards[dashboard[1]] = [dash]
        return dashboards

    @classmethod
    def find_groups_dashs_by_user(cls, **kwargs):
        """
        看板继承分组权限
        """
        name = kwargs.pop('name', None)
        creator = kwargs.pop('creator', None)
        data_auth = kwargs.get('data_auth', dict())
        group_auth = kwargs.get('group_auth', dict())
        group_name = kwargs.get('group_name', None)
        filter_or_not = kwargs.get('filter_or_not', False)
        dashs = cls.find_dashboards(name, creator)
        dashboards = cls.find_dashs_group(dashs, data_auth, group_auth)

        res = cls._find_tree_by_admin(
            perm=kwargs.get('perm', None),
            group_auth=group_auth,
            key='dashboards',
            data=dashboards,
            group_name=group_name,
            filter_empty_group=bool(name or creator),
            filter_or_not=filter_or_not,
        )
        return res

    @classmethod
    def check_group_is_empty(cls, group_id: int):
        """
        先检查分组内是否含有分组，在检查分组内是否有资源
        :param group_id:
        :return:
        """
        super(DashboardGroupDAO, cls).check_group_is_empty(group_id)
        data = db.session.query(Dashboard.id).filter_by(dashboard_group_id=group_id).first()
        if data:
            raise HTTPError(Messages.DEL_GROUP_ERROR, 400)

    @classmethod
    def find_dashboards(cls, name: str = None, creator: str = None) -> List[Model]:
        query = db.session.query(
            Dashboard.id,
            Dashboard.dashboard_group_id,
            Dashboard.dashboard_title,
            Dashboard.created_by_fk,
            Dashboard.created_on,
            Dashboard.changed_on,
            Dashboard.changed_by_fk,
            Dashboard.adaptation_equipment,
            Dashboard.json_metadata
        )
        if name:
            query = query.filter(
                Dashboard.dashboard_title.contains(name)
            )

        if creator:
            query = query.filter(
                Dashboard.created_by_fk.in_(
                    db.session.query(UserV2.id).filter(
                        or_(
                            UserV2.username.contains(creator),
                            UserV2.cn_name.contains(creator),
                        )
                    ).subquery()
                )
            )

        return query.all()

    @classmethod
    def find_all_by_admin(
        cls,
        perm: int = None,
        group_auth: dict = dict(),
        data_auth: dict = dict(),
        filter_or_not: bool = False,
        group_name: str = None,
        name: str = None,
        creator: str = None,
        max_data_auth: dict = {},
        max_group_auth: dict = {},
    ) -> List[dict]:
        """

        :param perm: 默认权限
        :param group_auth:
        :param data_auth:
        :param filter_or_not: 是否过滤没有查看权限的数据
        :param group_name:
        :param name:
        :param creator:
        :param max_data_auth:
        :param max_group_auth:
        :return:
        """
        dashs = cls.find_dashboards(name, creator)
        dashboards = {}
        users = UserV2DAO.find_users_cn_name()
        for dashboard in dashs:
            data_perm = perm or data_auth.get(dashboard[0], 0)
            if filter_or_not and data_perm == 0:
                continue

            dash = {
                "dashboard_id": dashboard[0],
                "dashboard_title": dashboard[2],
                "created_by_fk": users.get(dashboard[3]),
                "created_on": str(dashboard[4]),
                "changed_on": str(dashboard[5]),
                "changed_by_fk": users.get(dashboard[6]),
                "adaptation_equipment": dashboard[7],
                "perm": data_perm,
                "max_perm": max_data_auth.get(dashboard[0], 0),
                "layout_mode": ""
            }
            # TODO 长度超过65535报错
            if dashboard[-1]:
                try:
                    dash['layout_mode'] = json.loads(dashboard[-1]).get("layout_mode", "")
                except Exception as e:
                    pass

            if dashboards.get(dashboard[1], False):
                dashboards[dashboard[1]].append(dash)

            else:
                dashboards[dashboard[1]] = [dash]

        res = cls._find_tree_by_admin(
            perm=perm,
            group_auth=group_auth,
            key='dashboards',
            data=dashboards,
            group_name=group_name,
            filter_empty_group=bool(name or creator),
            filter_or_not=filter_or_not,
            max_group_auth=max_group_auth,
        )
        return res

    @classmethod
    def find_all_by_user(
        cls,
        group_auth: dict,
        data_auth: dict,
        group_filter: set = None,
        data_filter: set = None,
        group_name: str = None,
        name: str = None,
        creator: str = None,
        max_data_auth: dict = {},
        max_group_auth: dict = {},
    ) -> List[dict]:
        dashs = cls.find_dashboards(name, creator)
        dashboards = {}
        for dashboard in dashs:
            if data_filter is None:
                if data_auth.get(dashboard[0], 0) < VIEW:
                    continue

            else:
                if dashboard[0] not in data_filter:
                    continue

            dash = {
                "dashboard_id": dashboard[0],
                "dashboard_title": dashboard[2],
                "creator_id": dashboard[3],
                "created_on": str(dashboard[4]),
                "changed_on": str(dashboard[5]),
                "changed_by_fk": dashboard[6],
                "adaptation_equipment": dashboard[7],
                "perm": data_auth.get(dashboard[0], 0),
                "max_perm": max_data_auth.get(dashboard[0], 0),
                "layout_mode": json.loads(dashboard[-1]).get("layout_mode", "") if
                dashboard[-1] else ""
            }
            if dashboards.get(dashboard[1], False):
                dashboards[dashboard[1]].append(dash)

            else:
                dashboards[dashboard[1]] = [dash]

        res = cls._find_tree_by_user(
            group_auth=group_auth,
            key='dashboards',
            data=dashboards,
            group_filter=group_filter,
            group_name=group_name,
            max_group_auth=max_group_auth,
        )
        return res

    @classmethod
    def find_del_group_ids(cls, model: Model, pid: int, ids: List[int]) -> List:
        """查询出所有的分组，若分组内存在数据则400"""
        res = db.session.query(model.id).filter_by(dashboard_group_id=pid).first()
        if res is None:
            groups = db.session.query(cls.model_cls.id).filter_by(pid=pid).all()
            for item in groups:
                ids.append(item[0])
                cls.find_del_group_ids(model, item[0], ids)

            return ids

        raise HTTPError(Messages.DEL_GROUP_ERROR, 400)

    @classmethod
    def find_admin_result(cls, pid: int = 0):
        group = cls.find_by_pid(pid)
        return [
            {
                "group_id": item.id,
                "name": item.name,
                "pid": item.pid,
                "level": item.level,
                "perm": 4,
                "dashboards": [
                    {
                        "dashboard_id": dashboard.id,
                        "dashboard_title": dashboard.dashboard_title,
                        "perm": 4,
                    } for dashboard in item.dashboards
                ],
                "children": cls.find_admin_result(item.id)
            } for item in group
        ]

    @classmethod
    def find_auth_detail_by_admin(
        cls,
        pid: int,
        group_auth: dict,
        data_auth: dict
    ) -> List[dict]:
        res = cls.find_by_pid(pid)
        return [
            {
                "group_id": item.id,
                "name": item.name,
                "pid": item.pid,
                "perm": group_auth.get(item.id, 0),
                "dashboards": [
                    {
                        "dashboard_id": dashboard.id,
                        "dashboard_title": dashboard.dashboard_title,
                        "perm": data_auth.get(dashboard.id, 0),
                    } for dashboard in item.dashboards
                ],
                "children": cls.find_auth_detail_by_admin(
                    item.id, group_auth, data_auth)
            } for item in res
        ]

    @classmethod
    def find_auth_detail_by_user(
        cls,
        pid: int,
        group_auth: dict,
        data_auth: dict
    ) -> List[dict]:
        res = cls.find_by_pid(pid)
        return [
            {
                "group_id": item.id,
                "name": item.name,
                "pid": item.pid,
                "perm": group_auth.get(item.id, 0),
                "dashboards": [
                    {
                        "dashboard_id": dashboard.id,
                        "dashboard_title": dashboard.dashboard_title,
                        "perm": data_auth.get(dashboard.id, 0),
                    } for dashboard in item.dashboards if
                    data_auth.get(dashboard.id, 0)
                ],
                "children": cls.find_auth_detail_by_user(
                    item.id, group_auth, data_auth)
            } for item in res if group_auth.get(item.id, 0)
        ]
