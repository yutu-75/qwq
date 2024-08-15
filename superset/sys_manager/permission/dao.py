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
@Time       : 2023/3/14 14:10
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import List

from superset import db
from superset.dao.base import BaseDAO
from superset.models.sys_manager import SysAuth, DatabaseAuth
from superset.constants import AuthSourceType, AuthTargetType, DatabaseAuthType, VIEW
from superset.v2.datasources.dao import DataSourceDAO

_result = {
    AuthSourceType.DATASOURCE: DataSourceDAO,
    AuthSourceType.DATASET: DataSourceDAO,
    AuthSourceType.DASHBOARD: DataSourceDAO,
    AuthSourceType.CHART: DataSourceDAO,
}


class SysAuthDAO(BaseDAO):
    model_cls = SysAuth

    @classmethod
    def save_auth(cls, data: List[dict]):
        for item in data:
            cls.insert_or_update(
                item, {"privilege_value": item["privilege_value"]}, commit=False
            )

        db.session.commit()

    @classmethod
    def batch_auth(cls, data: dict):
        group = data.get("group", False)
        if group:
            db.session.query(cls.model_cls).filter(
                cls.model_cls.auth_source.in_(group["auth_sources"]),
                cls.model_cls.auth_source_type == group["auth_source_type"],
                cls.model_cls.auth_target == group["auth_target"],
                cls.model_cls.auth_target_type == group["auth_target_type"],
            ).update({
                cls.model_cls.privilege_value: group["privilege_value"]
            }, synchronize_session=False)

        data = data.get("data", False)
        if data:
            db.session.query(cls.model_cls).filter(
                cls.model_cls.auth_source.in_(data["auth_sources"]),
                cls.model_cls.auth_source_type == data["auth_source_type"],
                cls.model_cls.auth_target == data["auth_target"],
                cls.model_cls.auth_target_type == data["auth_target_type"],
            ).update({
                cls.model_cls.privilege_value: data["privilege_value"]
            }, synchronize_session=False)

        db.session.commit()

    @classmethod
    def del_user_auth(cls, user_id: int):
        db.session.query(cls.model_cls).filter(
            cls.model_cls.auth_target_type == AuthTargetType.USER,
            cls.model_cls.auth_target == user_id
        ).delete()


class DatabaseAuthDAO(BaseDAO):
    model_cls = DatabaseAuth

    @classmethod
    def find_perm_by_target(
        cls,
        auth_target: int,
        auth_target_type: str,
        auth_source_type: str,
        database_id: int,
        schema: str = None,
        privilege_value: int = 1
    ) -> dict:
        query = db.session.query(
            cls.model_cls.database_id,
            cls.model_cls.schema,
            cls.model_cls.table_name,
            cls.model_cls.privilege_value
        ).filter(
            cls.model_cls.auth_target == auth_target,
            cls.model_cls.auth_target_type == auth_target_type,
            cls.model_cls.auth_source_type == auth_source_type,
            cls.model_cls.privilege_value >= privilege_value
        )

        if database_id > 0:
            query = query.filter(cls.model_cls.database_id == database_id)

        if schema:
            query = query.filter(cls.model_cls.schema == schema)

        return {f"{item[0]}_{item[1]}_{item[2]}": item[3] for item in query.all()}

    @classmethod
    def find_perm_by_user_id(
        cls,
        user_id: int,
        database_id: int,
        auth_source_type: str = None,
        schema: str = None,
        privilege_value: int = 1,
    ):
        params = {
            "database_id": database_id,
        }
        filter_auth_source = ''
        if schema:
            filter_auth_source = f"`schema` = :schema AND "
            params["schema"] = schema

        if auth_source_type:
            auth_source_type = 'auth_source_type = :auth_source_type AND '
            params["auth_source_type"] = auth_source_type

        sql = f'''
            SELECT
                database_id,
                `schema`,
                `table_name`,
                MAX(privilege_value)
            FROM
                db_auth
            WHERE
                database_id = :database_id AND 
                {filter_auth_source}
                privilege_value >= {privilege_value}
            AND (
                (
                    auth_target_type = 'dept'
                    AND auth_target IN (
                        SELECT
                            dept_id
                        FROM
                            sys_dept_users
                        WHERE
                            user_id = {user_id}
                    )
                )
                OR (
                    auth_target_type = 'user'
                    AND auth_target = {user_id}
                )
                OR (
                    auth_target_type = 'role'
                    AND auth_target IN (
                        SELECT
                            role_id
                        FROM
                            ab_user_role
                        WHERE
                            user_id = {user_id}
                    )
                )
            )
            GROUP BY `database_id`, `schema`, `table_name`
        '''

        data = db.session.execute(sql, params).all()
        return {f"{item[0]}_{item[1]}_{item[2]}": item[3] for item in data}

    @classmethod
    def find_user_max_privilege(
        cls,
        user_id: int,
        auth_source_type: str,
        auth_source: int = 0,
    ) -> dict:
        filter_auth_source = ''
        if auth_source > 0:
            filter_auth_source = f'sys_auth.auth_source = {auth_source} AND '

        sql = f'''
                SELECT
                    auth_source,
                    MAX(privilege_value)
                FROM
                    sys_auth
                WHERE
                    {filter_auth_source}
                    sys_auth.auth_source_type = :auth_source_type
                AND (
                    (
                        sys_auth.auth_target_type = 'dept'
                        AND sys_auth.auth_target IN (
                            SELECT
                                dept_id
                            FROM
                                sys_dept_users
                            WHERE
                                user_id = {user_id}
                        )
                    )
                    OR (
                        sys_auth.auth_target_type = 'user'
                        AND sys_auth.auth_target = {user_id}
                    )
                    OR (
                        sys_auth.auth_target_type = 'role'
                        AND sys_auth.auth_target IN (
                            SELECT
                                role_id
                            FROM
                                ab_user_role
                            WHERE
                                user_id = {user_id}
                        )
                    )
                )
                GROUP BY auth_source
            '''

        data = db.session.execute(sql, params={
            "auth_source_type": auth_source_type,
        }).all()
        return {item[0]: item[1] for item in data}

    @classmethod
    def save_auth(cls, data: List[dict]):
        for item in data:
            cls.insert_or_update(
                item, {"privilege_value": item["privilege_value"]}, commit=False
            )

        db.session.commit()

    @classmethod
    def check_all_tables_perm(cls, user_id, database_id, schema: str, auth: int = VIEW):
        """
        数据库有查询以上权限，可查看所有表
        :param user_id:
        :param database_id:
        :param schema:
        :return:
        """
        schema_perm = cls.find_perm_by_user_id(
            user_id, database_id, DatabaseAuthType.DB_SCHEMA, schema)
        key_ = f'''{database_id}_{schema}_'''
        if schema_perm.get(key_, 0) >= auth:
            return True

        return False
