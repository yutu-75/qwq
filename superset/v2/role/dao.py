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

from typing import List

from flask_appbuilder.security.sqla.models import Role

from superset.dao.base import BaseDAO
from superset.exceptions import HTTPError
from superset.extensions import db
from superset.constants import AuthTargetType
from superset.v2.models.user_role import UserRole, RoleV2
from superset.v2.user.dao import UserV2DAO

logger = logging.getLogger(__name__)


class UserRoleDAO(BaseDAO):
    model_cls = UserRole

    @classmethod
    def delete_by_role_id(cls, role_id: int, commit: bool = False):
        db.session.query(cls.model_cls).filter(
            cls.model_cls.role_id == role_id
        ).delete()
        if commit:
            db.session.commit()


class RoleDAO(BaseDAO):
    model_cls = Role


class RoleV2DAO(BaseDAO):
    model_cls = RoleV2

    @classmethod
    def find_roles(cls, **kwargs):
        name = kwargs.get("name", False)
        page = int(kwargs.get("page_index", 0))
        page_size = int(kwargs.get("page_size", 0))
        # role_ids = kwargs.get("role_ids", False)
        user_id = kwargs.get("user_id", False)
        query = db.session.query(cls.model_cls)
        if user_id:
            query = query.filter(cls.model_cls.creator_id==user_id)

        if name:
            query = query.filter(cls.model_cls.name.contains(name))

        # 总数
        count = query.count()
        if page > 0 and page_size > 0:
            query = query.order_by(
                cls.model_cls.name
            ).limit(page_size).offset((page - 1) * page_size)

        return {
            "count": count,
            "list": [
                {
                    "id": item.id,
                    "name": item.name,
                } for item in query.all()
            ]
        }

    @staticmethod
    def get_users_by_role_id(role_id: int, **kwargs) -> List[dict]:
        """查询角色详细信息"""
        count, users = UserV2DAO.filter_users(role_id=role_id, **kwargs)
        return [{
            "count": count,
            "id": item.id,
            "cn_name": item.cn_name,
            "username": item.username
        } for item in users]

    @staticmethod
    def add_role(role: Role):
        """新增角色"""
        db.session.add(role)
        db.session.commit()

    @staticmethod
    def delete_role(id: int) -> None:
        """删除角色"""
        db.session.query(Role).filter(Role.id == id).delete()
        db.session.commit()

    @staticmethod
    def role_add_user(user_role: UserRole):
        """角色新增用户"""
        db.session.add(user_role)
        db.session.commit()

    @classmethod
    def get_roles(cls):
        res = cls.find_all()
        return [
            {
                "id": item.id,
                "name": item.name,
            } for item in res
        ]

    @staticmethod
    def find_role_perm_by_source_user(
        auth_source: int,
        auth_source_type: str,
        user_id: int,
        privilege_value: int,
        auth_target_type: str = AuthTargetType.ROLE,
    ) -> dict:
        """查询数据源各角色（用户角色）的权限"""
        sql = f'''
            SELECT
                auth_target,
                privilege_value
            FROM
                sys_auth
            WHERE
                sys_auth.auth_source = :auth_source
            AND sys_auth.auth_source_type = :auth_source_type
            AND sys_auth.auth_target_type = :auth_target_type
            AND sys_auth.auth_target IN (
                SELECT
                    role_id
                FROM
                    ab_user_role
                WHERE
                    user_id = {user_id}
            )
            AND sys_auth.privilege_value >= :privilege_value
        '''

        data = db.session.execute(sql, params={
            "auth_source": auth_source,
            "auth_source_type": auth_source_type,
            "auth_target_type": auth_target_type,
            "privilege_value": privilege_value
        }).fetchall()
        return {item[0]: item[1] for item in data}

    @classmethod
    def find_auth_detail_by_admin(
        cls,
        data_auth: dict
    ) -> List[dict]:
        res = cls.find_all()
        return [
            {
                "id": item.id,
                "name": item.name,
                "perm": data_auth.get(item.id, 0),
            } for item in res
        ]

    @classmethod
    def find_auth_detail_by_user(
        cls,
        roles: list,
        data_auth: dict
    ) -> List[dict]:
        return [
            {
                "id": item.id,
                "name": item.name,
                "perm": data_auth.get(item.id, 0),
            } for item in roles
        ]

    @classmethod
    def validate_name_exist(cls, name: str) -> bool:
        res = db.session.query(cls.model_cls.id).filter_by(name=name).first()
        return False if res is None else True

    @staticmethod
    def delete_role_users(role: Role, user_ids: List) -> None:
        users = UserV2DAO.find_by_ids(user_ids)
        for user in users:
            if len(user.roles) < 2:
                raise HTTPError("用户只有此角色，不可删除", 400)

        db.session.query(UserRole).filter(
            UserRole.role_id == role.id,
            UserRole.user_id.in_(user_ids)
        ).delete()
        db.session.commit()
