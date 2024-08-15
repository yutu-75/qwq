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

# -*- coding: utf-8 -*-

"""
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging

from typing import List, Any
import pandas as pd
from flask import current_app
from flask_appbuilder.security.sqla.models import Role, assoc_user_role
from sqlalchemy import or_, and_, not_
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from superset import conf
from superset.cache_key import UserCacheKey
from superset.constants import AuthTargetType
from superset.dao.base import BaseDAO
from superset.exceptions import HTTPError
from superset.extensions import db, cache_manager
from superset.global_messages import Messages
from superset.models.sys_manager import SysDeptUsers, SysAuth
from superset.models.user import UserV2
from superset.v2.models.user_role import UserRole
from superset.v2.utils.password_strength import PasswordStrength

logger = logging.getLogger(__name__)


class UserV2DAO(BaseDAO):
    model_cls = UserV2

    @classmethod
    def find_users_cn_name(cls):
        query = db.session.query(
            cls.model_cls.id,
            cls.model_cls.cn_name,
        )
        return {
            item[0]: {"id": item[0], "cn_name": item[1]}
            for item in query.all()
        }

    @staticmethod
    def find_roles(roles: list):
        query = db.session.query(Role).filter(
            Role.name.in_(roles)
        )
        return query.all()

    @classmethod
    def filter_users(cls, **kwargs: Any):
        username = kwargs.get("username", False)
        dept_id = kwargs.get("dept_id", False)
        role_id = kwargs.get("role_id", False)
        page = int(kwargs.get("page_index", 1))
        page_size = int(kwargs.get("page_size", 100))
        query = db.session.query(cls.model_cls)
        if role_id:
            qry = (
                db.session.query(assoc_user_role.c.user_id)
                .filter(assoc_user_role.c.role_id == role_id)
                .subquery()
            )
            query = query.filter(cls.model_cls.id.in_(qry))

        if dept_id:
            qry = (
                db.session.query(SysDeptUsers.c.user_id)
                .filter(SysDeptUsers.c.dept_id == dept_id)
                .subquery()
            )
            query = query.filter(cls.model_cls.id.in_(qry))

        if username:
            query = query.filter(
                or_(
                    UserV2.username.contains(username),
                    UserV2.cn_name.contains(username)
                )
            )
        # 总数
        count = query.count()
        if count == 0:
            return 0, []
        else:
            query = query.order_by(
                UserV2.changed_on.desc()
            ).limit(
                page_size
            ).offset(
                (page - 1) * page_size
            )

        return count, query.all()

    @classmethod
    def find_users(cls, **kwargs: Any):
        username = kwargs.get("username", False)
        depts_id = kwargs.get("depts_id", False)
        dept_id = kwargs.get("dept_id", False)
        role_id = kwargs.get("role_id", False)
        filter_role_id = kwargs.get("filter_role_id", False)
        filter_dept_id = kwargs.get("filter_dept_id", False)
        page = int(kwargs.get("page_index", 1))
        page_size = int(kwargs.get("page_size", 100))
        query = db.session.query(cls.model_cls)
        # 未加入当前组织的用户
        if filter_dept_id:
            qry = (
                db.session.query(SysDeptUsers.c.user_id)
                .filter(SysDeptUsers.c.dept_id == filter_dept_id)
                .subquery()
            )
            query = query.filter(cls.model_cls.id.notin_(qry))
        # 当前角色以外的用户
        if filter_role_id:
            qry = (
                db.session.query(assoc_user_role.c.user_id)
                .filter(assoc_user_role.c.role_id == filter_role_id)
                .subquery()
            )
            query = query.filter(cls.model_cls.id.notin_(qry))

        if dept_id:
            qry = (
                db.session.query(SysDeptUsers.c.user_id)
                .filter(SysDeptUsers.c.dept_id == dept_id)
                .subquery()
            )
            query = query.filter(cls.model_cls.id.in_(qry))

        if role_id:
            qry = (
                db.session.query(assoc_user_role.c.user_id)
                .filter(assoc_user_role.c.role_id == role_id)
                .subquery()
            )
            query = query.filter(cls.model_cls.id.in_(qry))

        if depts_id:
            qry = (
                db.session.query(SysDeptUsers.c.user_id)
                .filter(SysDeptUsers.c.dept_id.in_(depts_id))
                .subquery()
            )
            query = query.filter(cls.model_cls.id.in_(qry))

        if username:
            query = query.filter(
                or_(
                    UserV2.username.contains(username),
                    UserV2.cn_name.contains(username)
                )
            )
        # 总数
        count = query.count()
        if page > 0 and page_size > 0:
            query = query.order_by(
                UserV2.changed_on.desc()
            ).limit(
                page_size
            ).offset(
                (page - 1) * page_size
            )
        return count, query.all()

    @staticmethod
    def generate_password_hash(pwd: str) -> str:
        return generate_password_hash(pwd)

    @classmethod
    def get_all_user(cls, params: dict):
        count, user_list = cls.find_users(**params)
        data = []
        cache = cache_manager.cache_read_client
        for item in user_list:
            res = {
                "id": item.id,
                "first_name": item.first_name,
                "last_name": item.last_name,
                "username": item.username,
                "cn_name": item.cn_name,
                "email": item.email,
                "active": item.active or False,
                "is_admin": item.is_admin,
                "created_on": item.created_on,
                "changed_on": item.changed_on,
                "last_login": item.last_login,
                "login_count": item.login_count,
                "fail_login_count": item.fail_login_count,
                "roles": [
                    {
                        "id": role.id,
                        "name": role.name,
                    } for role in item.roles
                ],
                "depts": [
                    {
                        "id": dept.id,
                        "title": dept.title,
                    } for dept in item.depts
                ],
                "account_lock": {
                    "status": 0,
                    "ttl": 0
                }
            }

            cache_key = UserCacheKey.ACCOUNT_LOCK_KEY % item.username
            times = int(cache.get(cache_key) or 0)
            if times >= int(conf["NUM_OF_LOGIN_FAILURES"]):
                res["account_lock"] = {
                    "status": 1,
                    "ttl": cache.ttl(cache_key)
                }

            data.append(res)

        return {
            "count": count,
            "list": data
        }

    @classmethod
    def add_user(cls, data: dict):
        """新增 user"""
        user = cls.create_user_obj(data)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def delete_user(id_: int, commit: bool = True) -> None:
        """删除 user"""
        db.session.query(UserRole).filter(UserRole.user_id == id_).delete()
        db.session.query(UserV2).filter(UserV2.id == id_).delete()
        if commit:
            db.session.commit()

    @classmethod
    def find_users_perm(
        cls,
        auth_source: int,
        auth_source_type: str,
        auth_target_type: str = AuthTargetType.USER,
        depts_id: list = None,
    ) -> dict:
        query = (
            db.session.query(
                SysAuth.auth_target,
                SysAuth.privilege_value
            )
            .filter(
                and_(
                    SysAuth.auth_source == auth_source,
                    SysAuth.auth_source_type == auth_source_type,
                    SysAuth.auth_target_type == auth_target_type,
                )
            )
        )
        if depts_id:
            qry = (
                db.session.query(SysDeptUsers.c.user_id)
                .filter(SysDeptUsers.c.dept_id.in_(depts_id))
                .subquery()
            )
            query = query.filter(SysAuth.auth_target.in_(qry))

        return {item[0]: item[1] for item in query.all()}

    @classmethod
    def find_auth_detail(
        cls,
        perm: int = None,
        data_auth: dict = dict(),
        auth_source=None,
        auth_source_type=None,
        **kwargs: Any,
    ) -> List[dict]:
        count, users = cls.find_users(**kwargs)
        if auth_source and auth_source_type:
            return [
                {
                    "id": item.id,
                    "first_name": item.first_name,
                    "last_name": item.last_name,
                    "username": item.username,
                    "cn_name": item.cn_name,
                    "perm": perm or data_auth.get(item.id, 0),
                    "max_perm": cls.find_user_max_privilege_by_source_type(
                        item.id, auth_source_type, auth_source
                    ).get(auth_source, 0),
                    "count": count,
                } for item in users
            ]

        return [
            {
                "id": item.id,
                "first_name": item.first_name,
                "last_name": item.last_name,
                "username": item.username,
                "cn_name": item.cn_name,
                "perm": perm or data_auth.get(item.id, 0),
                "max_perm": 0,
                "count": count,
            } for item in users
        ]

    @staticmethod
    def create_user_obj(data: dict) -> UserV2:
        model = UserV2()
        roles = []
        for key, value in data.items():
            if key != "roles":
                setattr(model, key, value)
            else:
                for role_id in data[key]:
                    role = (
                        db.session.query(Role).filter(
                            Role.id == role_id).one_or_none()
                    )
                    if role:
                        role.user_id = model.id
                        role.role_id = role_id
                        roles.append(role)

        if "roles" in data.keys():
            model.roles = roles

        if "active" not in data.keys():
            model.active = 0

        model.password = generate_password_hash(data["password"])
        return model

    @classmethod
    def create_import_user_objs(cls, df, user: UserV2) -> None:
        df = df.fillna("")
        df = df.astype(str)
        depts = []
        if user.depts:
            depts = user.depts[:1]

        for _, item in df.iterrows():
            name = item.get("姓名", "").strip()
            email = item.get("邮箱", "").strip()
            username = item.get("用户名", "")
            roles = cls.find_roles(item.get("角色", "").split("、"))
            pwd = item.get("密码", "")
            active = item.get("账号状态", "")
            if not name:
                raise HTTPError(Messages.NAME_ERROR, 400, (_ + 2,))

            if str(email).find("@") < 1:
                raise HTTPError(Messages.MAIL_ERROR, 400, (_ + 2,))

            if not username:
                raise HTTPError(Messages.USERNAME_ERROR, 400, (_ + 2,))

            if not PasswordStrength(pwd).check_pwd_strength:
                raise HTTPError(Messages.PWD_STRENGTH_ERROR, 400)

            if active not in {"0", "1"}:
                raise HTTPError(Messages.STATUS_ERROR, 400)

            db.session.add(
                UserV2(
                    first_name=str(name)[1:] or "",
                    last_name=str(name)[0:1],
                    roles=roles,
                    cn_name=name,
                    email=email,
                    username=username,
                    active=int(active),
                    is_admin=0,
                    password=generate_password_hash(pwd),
                    depts=depts,
                )
            )

        db.session.commit()

    # @staticmethod
    # def create_import_user_objs(df, user: UserV2) -> None:
    #     df = df.fillna("")
    #     # default_role_name = current_app.config["AUTH_USER_REGISTRATION_ROLE"]
    #     # roles = db.session.query(Role).filter_by(name=default_role_name).all()
    #     # depts = []
    #     if user.depts:
    #         depts = user.depts[:1]
    #     #
    #     # if {"姓名", "邮箱", "用户名"} != set(df.columns):
    #     #     raise HTTPError(Messages.EXCEL_TEMPLATE_ERROR, 400)
    #
    #     for _, item in df.iterrows():
    #
    #         name = item.get("姓名", "")
    #         email = item.get("邮箱", "")
    #         username = item.get("用户名", "")
    #         roles = item.get("角色", "")
    #         pwd = item.get("密码", "")
    #         status = item.get("账号状态", "")
    #         is_admin = item.get("是否超级管理员", "")
    #         if pd.isna(name):
    #             raise HTTPError(Messages.NAME_ERROR, 400, (_+2,))
    #
    #         if pd.isna(email) or str(email).find("@") < 1:
    #             raise HTTPError(Messages.MAIL_ERROR, 400, (_+2,))
    #
    #         if pd.isna(username) or len(str(username)) < 6:
    #             raise HTTPError(Messages.USERNAME_ERROR, 400, (_+2,))
    #
    #         db.session.add(
    #             UserV2(
    #                 first_name=str(name)[1:] or name,
    #                 last_name=str(name)[0:1],
    #                 roles=roles,
    #                 cn_name=name,
    #                 email=email,
    #                 username=username,
    #                 active=1,
    #                 is_admin=0,
    #                 password=generate_password_hash(str(username)),
    #                 depts=depts,
    #             )
    #         )
    #     db.session.commit()

    @classmethod
    def mulk_insert_users(cls, df, user: UserV2):
        try:
            cls.create_import_user_objs(df, user)
        except IntegrityError as e:
            db.session.rollback()
            username = e.params[2]  # 重复的用户名
            email = e.params[5]
            raise HTTPError(Messages.DUPLICATE_USERNAME, 400, (username, email))

    @classmethod
    def validate_uniqueness(cls, username: str, email: str, id_: int = 0):
        query = db.session.query(cls.model_cls)
        if id_ > 0:
            query = query.filter(cls.model_cls.id != id_)

        query = query.filter(
            or_(
                cls.model_cls.username == username,
                cls.model_cls.email == email,
            )
        )
        return db.session.query(query.exists()).scalar()
