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
@Time       : 2023/3/24 13:35
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import List

from flask_appbuilder import Model
from sqlalchemy import or_

from superset import db
from superset.connectors.sqla.models import SqlaTable
from superset.dao.base import BaseGroupDAO
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.datasource import DataSourceGroup, DataSource
from superset.constants import GRANT, VIEW
from superset.models.user import UserV2
from superset.v2.user.dao import UserV2DAO


class DataSourceGroupDAO(BaseGroupDAO):
    model_cls = DataSourceGroup

    @classmethod
    def check_group_is_empty(cls, group_id: int):
        """
        先检查分组内是否含有分组，在检查分组内是否有资源
        :param group_id:
        :return:
        """
        super(DataSourceGroupDAO, cls).check_group_is_empty(group_id)
        data = db.session.query(DataSource.id).filter_by(group_id=group_id).first()
        if data:
            raise HTTPError(Messages.DEL_GROUP_ERROR, 400)

    @classmethod
    def find_datasources(cls, name: str = None, creator: str = None) -> List[Model]:
        query = db.session.query(DataSource)
        if name:
            query = query.filter(
                DataSource.name.contains(name)
            )

        if creator:
            query = query.filter(
                DataSource.created_by_fk.in_(
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
        group_auth: dict = {},
        data_auth: dict = {},
        filter_or_not: bool = False,
        group_name: str = None,
        name: str = None,
        creator: str = None,
        max_data_auth: dict = {},
        max_group_auth: dict = {},
    ) -> List[dict]:
        datasources = cls.find_datasources(name, creator)
        data = {}
        users = UserV2DAO.find_users_cn_name()
        for datasource in datasources:
            data_perm = perm or data_auth.get(datasource.id, 0)
            if filter_or_not and data_perm == 0:
                continue

            item = {
                "datasource_id": datasource.id,
                "database_id": datasource.database_id,
                "name": datasource.name,
                "d_type": datasource.d_type,
                "created_by_fk": users.get(datasource.created_by_fk),
                "created_on": str(datasource.created_on),
                "changed_on": str(datasource.changed_on),
                "changed_by_fk": users.get(datasource.changed_by_fk),
                "perm": data_perm,
                "max_perm": max_data_auth.get(datasource.id, 0),
                "backend": datasource.database.backend
            }
            if data.get(datasource.group_id, False):
                data[datasource.group_id].append(item)

            else:
                data[datasource.group_id] = [item]

        res = cls._find_tree_by_admin(
            perm=perm,
            group_auth=group_auth,
            key='datasources',
            data=data,
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
        max_data_auth: dict = {},
        max_group_auth: dict = {},
    ) -> List[dict]:
        datasources = cls.find_datasources()
        data = {}
        for datasource in datasources:
            if data_filter is None:
                if data_auth.get(datasource.id, 0) < VIEW:
                    continue

            else:
                if datasource.id not in data_filter:
                    continue

            item = {
                "datasource_id": datasource.id,
                "database_id": datasource.database_id,
                "name": datasource.name,
                "d_type": datasource.d_type,
                "perm": data_auth.get(datasource.id, 0),
                "max_perm": max_data_auth.get(datasource.id, 0)
            }
            if data.get(datasource.group_id, False):
                data[datasource.group_id].append(item)

            else:
                data[datasource.group_id] = [item]

        res = cls._find_tree_by_user(
            group_auth=group_auth,
            key='datasources',
            data=data,
            group_filter=group_filter,
            max_group_auth=max_group_auth,
        )
        return res

    @classmethod
    def get_auth_detail_by_user(
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
                "level": item.level,
                "perm": group_auth.get(item.id, 0),
                "datasources": [
                    {
                        "datasource_id": datasource.id,
                        "database_id": datasource.database_id,
                        "name": datasource.name,
                        "d_type": datasource.d_type,
                        "perm": data_auth.get(datasource.id, 0),
                    } for datasource in item.datasources if
                    data_auth.get(datasource.id, 0)
                ],
                "children": cls.get_auth_detail_by_user(
                    item.id, group_auth, data_auth)
            } for item in res if group_auth.get(item.id, 0)
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
                "level": item.level,
                "perm": group_auth.get(item.id, 0),
                "datasources": [
                    {
                        "datasource_id": datasource.id,
                        "database_id": datasource.database_id,
                        "name": datasource.name,
                        "d_type": datasource.d_type,
                        "perm": data_auth.get(datasource.id, 0),
                    } for datasource in item.datasources
                ],
                "children": cls.find_auth_detail_by_admin(
                    item.id, group_auth, data_auth)
            } for item in res
        ]

    @classmethod
    def get_admin_datasources(cls, pid: int = 0) -> List[dict]:
        datasource_group_list = cls.find_by_pid(pid)
        return [
            {
                "group_id": item.id,
                "name": item.name,
                "pid": item.pid,
                "level": item.level,
                "perm": GRANT,
                "datasources": [
                    {
                        "datasource_id": datasource.id,
                        "database_id": datasource.database_id,
                        "name": datasource.name,
                        "d_type": datasource.d_type,
                        "perm": GRANT,
                    } for datasource in item.datasources
                ],
                "children": cls.get_admin_datasources(item.id)
            } for item in datasource_group_list
        ]
