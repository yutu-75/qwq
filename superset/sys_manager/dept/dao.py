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
from sqlalchemy import and_

from superset import db
from superset.dao.base import BaseDAO
from superset.models.sys_manager import SysDept, SysDeptUsers, SysAuth
from superset.constants import AuthTargetType
from superset.models.user import UserV2
from superset.v2.user.dao import UserV2DAO


class SysDeptDAO(BaseDAO):
    model_cls = SysDept

    @classmethod
    def find_users_by_dept_id(cls, dept_id: int, **kwargs):
        count, users = UserV2DAO.filter_users(dept_id=dept_id, **kwargs)
        return [{
            "count": count,
            "id": item.id,
            "cn_name": item.cn_name,
            "username": item.username
        } for item in users]

    @classmethod
    def find_depts_by_ids(cls, ids: list = None) -> List[Model]:
        query = db.session.query(cls.model_cls)
        if ids:
            query = query.filter(cls.model_cls.id.in_(ids))

        query = query.order_by(cls.model_cls.level.desc())
        return query.all()

    @staticmethod
    def find_by_pid(pid: int = 0):
        return db.session.query(SysDept).filter_by(pid=pid).all()

    @staticmethod
    def get_by_pid_title(pid: int, title: str) -> SysDept:
        query = db.session.query(SysDept.id).filter_by(pid=pid, title=title)
        return query.one_or_none()

    @classmethod
    def find_top_dept_by_id(cls, dept_id: int) -> Model:
        dept = db.session.query(cls.model_cls).filter_by(id=dept_id).first()
        if dept and dept.pid > 0:
            return cls.find_top_dept_by_id(dept.pid)

        return dept

    @classmethod
    def find_by_user(cls, user: UserV2) -> list:
        """
        查询用户有权查看的所有组织
        :param user:
        :return:
        """
        ids = []
        res = []
        for item in user.depts:
            if item.id in set(ids):
                continue

            # TODO
            # 用户可加入任意组织，逻辑混乱,需过滤掉加入的下级组织
            ids.append(item.id)
            cls.find_depts_id_by_pid(item.id, ids)
            data = {
                "dept_id": item.id,
                "title": item.title,
                "pid": item.pid,
                "level": item.level,
                "created_on": item.created_on,
                "perm": 0,
                "children": cls.find_dept_by_pid(item.id)
            }
            res.append(data)

        return res

    @classmethod
    def find_depts_id_by_pid(cls, pid: int, ids: list) -> list:
        dept = db.session.query(cls.model_cls.id).filter_by(pid=pid).all()
        for item in dept:
            ids.append(item[0])
            cls.find_depts_id_by_pid(item[0], ids)

    @classmethod
    def find_depts_id_by_user(cls, user: UserV2) -> List:
        ids = []
        for dept in user.depts:
            ids.append(dept.id)
            cls.find_depts_id_by_pid(dept.id, ids)

        return ids

    @classmethod
    def delete_dept(cls, model: SysDept, commit: bool = True) -> None:
        cls.delete(model, commit=False)
        # db.session.query(SysDeptUsers).filter_by(dept_id=model.id).delete()
        cls.delete_auth_by_target({
            "auth_target": model.id,
            "auth_target_type": AuthTargetType.DEPT,
        }, commit=False)
        models = db.session.query(SysDept).filter_by(pid=model.id).all()
        for model in models:
            return cls.delete_dept(model, commit)

    @classmethod
    def find_dept_by_pid(
        cls,
        pid: int = 0,
        data_auth: dict = {}
    ) -> List[dict]:
        res = cls.find_by_pid(pid)
        return [
            {
                "dept_id": item.id,
                "title": item.title,
                "pid": item.pid,
                "level": item.level,
                "created_on": item.created_on,
                "perm": data_auth.get(item.id, 0),
                "children": cls.find_dept_by_pid(item.id, data_auth)
            } for item in res
        ]

    @staticmethod
    def find_dept_perm(
        auth_source: int,
        auth_source_type: str,
        auth_target_type: str = AuthTargetType.DEPT,
        depts_id: list = None,
    ) -> dict:
        """查询各组织（用户所在组织）的权限"""
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
            query = query.filter(SysAuth.auth_target.in_(depts_id))

        return {item[0]: item[1] for item in query.all()}

    @classmethod
    def find_auth_detail_by_user(
        cls,
        user: UserV2,
        data_auth: dict = dict(),
    ) -> List[dict]:
        ids = []
        res = []
        for item in user.depts:
            if item.id in set(ids):
                continue

            # TODO
            # 用户可加入任意组织，逻辑混乱,需过滤掉加入的下级组织
            ids.append(item.id)
            cls.find_depts_id_by_pid(item.id, ids)
            dept = {
                "dept_id": item.id,
                "title": item.title,
                "pid": 0,  # 必须传0，否则前端报错
                "level": item.level,
                "created_on": item.created_on,
                "perm": data_auth.get(item.id, 0),
                "children": cls.find_dept_by_pid(item.id, data_auth)
            }
            res.append(dept)

        res.sort(key=lambda k: (k.get('created_on', '')))
        return res

    @classmethod
    def find_auth_detail(
        cls,
        perm: int = None,
        data_auth: dict = dict(),
        depts_id: list = None,
    ) -> List[dict]:
        depts = cls.find_depts_by_ids(depts_id)
        res = {}
        for item in depts:
            dept = {
                "dept_id": item.id,
                "title": item.title,
                "pid": item.pid,
                "level": item.level,
                "created_on": item.created_on,
                "perm": perm or data_auth.get(item.id, 0),
                "children": res.get(item.id, [])
            }

            if res.get(item.pid, False):
                res[item.pid].append(dept)

            else:
                res[item.pid] = [dept]

        res = res.get(0, [])
        res.sort(key=lambda k: (k.get('created_on', '')))
        return res


class SysDeptUsersDAO(BaseDAO):
    model_cls = SysDeptUsers

    @staticmethod
    def get_users_by_dept_id(dept_id: int) -> List[dict]:
        query = (
            db.session.query(SysDeptUsers.user_id)
            .filter(SysDeptUsers.dept_id == dept_id)
            .subquery()
        )

        users = db.session.query(
            UserV2.id,
            UserV2.cn_name,
            UserV2.username,
            UserV2.email,
        ).filter(UserV2.id.in_(query)).all()
        return [{
            "id": user[0],
            "cn_name": user[1],
            "email": user[2],
            "username": user[3],
        } for user in users]

    @staticmethod
    def bulk_save_dept_users(dept: SysDept, user_ids: List) -> None:
        dept.users += UserV2DAO.find_by_ids(user_ids)
        db.session.add(dept)
        db.session.commit()

    @staticmethod
    def delete_dept_users(dept: SysDept, user_ids: List) -> None:
        users = UserV2DAO.find_by_ids(user_ids)
        for user in users:
            dept.users.remove(user)

        db.session.commit()
