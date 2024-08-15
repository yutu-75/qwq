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
# pylint: disable=isinstance-second-argument-not-valid-type
"""
修改:陈果-2023-05-08
修改内容:增加基类方法
-------------------------------------------

"""
import json
from typing import Any, Dict, List, Optional, Type, Union

from flask import g
from flask_appbuilder.models.filters import BaseFilter
from flask_appbuilder.models.sqla import Model
from flask_appbuilder.models.sqla.interface import SQLAInterface
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.exc import SQLAlchemyError, StatementError
from sqlalchemy.orm import Session

from superset.constants import VIEW, GRANT, MANAGE
from superset.dao.exceptions import (
    DAOConfigError,
    DAOCreateFailedError,
    DAODeleteFailedError,
    DAOUpdateFailedError,
)
from superset.exceptions import HTTPError
from superset.extensions import db
from superset.global_messages import Messages
from superset.models.sys_manager import Archive, SysAuth


class BaseDAO:
    """
    Base DAO, implement base CRUD sqlalchemy operations
    """

    model_cls: Optional[Type[Model]] = None
    """
    Child classes need to state the Model class so they don't need to implement basic
    create, update and delete methods
    """
    base_filter: Optional[BaseFilter] = None
    """
    Child classes can register base filtering to be aplied to all filter methods
    """
    id_column_name = "id"

    @classmethod
    def find_by_id(
        cls,
        model_id: Union[str, int],
        session: Session = None,
        skip_base_filter: bool = False,
    ) -> Optional[Model]:
        """
        Find a model by id, if defined applies `base_filter`
        """
        session = session or db.session
        query = session.query(cls.model_cls)
        if cls.base_filter and not skip_base_filter:
            data_model = SQLAInterface(cls.model_cls, session)
            query = cls.base_filter(  # pylint: disable=not-callable
                cls.id_column_name, data_model
            ).apply(query, None)
        id_column = getattr(cls.model_cls, cls.id_column_name)
        try:
            return query.filter(id_column == model_id).one_or_none()
        except StatementError:
            # can happen if int is passed instead of a string or similar
            return None

    @classmethod
    def find_by_ids(
        cls,
        model_ids: Union[List[str], List[int]],
        session: Session = None,
        skip_base_filter: bool = False,
    ) -> List[Model]:
        """
        Find a List of models by a list of ids, if defined applies `base_filter`
        """
        id_col = getattr(cls.model_cls, cls.id_column_name, None)
        if id_col is None:
            return []
        session = session or db.session
        query = session.query(cls.model_cls).filter(id_col.in_(model_ids))
        if cls.base_filter and not skip_base_filter:
            data_model = SQLAInterface(cls.model_cls, session)
            query = cls.base_filter(  # pylint: disable=not-callable
                cls.id_column_name, data_model
            ).apply(query, None)
        return query.all()

    @classmethod
    def find_all(cls) -> List[Model]:
        """
        Get all that fit the `base_filter`
        """
        query = db.session.query(cls.model_cls)
        if cls.base_filter:
            data_model = SQLAInterface(cls.model_cls, db.session)
            query = cls.base_filter(  # pylint: disable=not-callable
                cls.id_column_name, data_model
            ).apply(query, None)
        return query.all()

    @classmethod
    def find_one_or_none(cls, **filter_by: Any) -> Optional[Model]:
        """
        Get the first that fit the `base_filter`
        """
        query = db.session.query(cls.model_cls)
        if cls.base_filter:
            data_model = SQLAInterface(cls.model_cls, db.session)
            query = cls.base_filter(  # pylint: disable=not-callable
                cls.id_column_name, data_model
            ).apply(query, None)
        return query.filter_by(**filter_by).one_or_none()

    @classmethod
    def create(cls, properties: Dict[str, Any], commit: bool = True) -> Model:
        """
        Generic for creating models
        :raises: DAOCreateFailedError
        """
        if cls.model_cls is None:
            raise DAOConfigError()
        model = cls.model_cls()  # pylint: disable=not-callable
        for key, value in properties.items():
            setattr(model, key, value)
        try:
            db.session.add(model)
            if commit:
                db.session.commit()
        except SQLAlchemyError as ex:  # pragma: no cover
            db.session.rollback()
            raise DAOCreateFailedError(exception=ex) from ex
        return model

    @classmethod
    def save(cls, instance_model: Model, commit: bool = True) -> Model:
        """
        Generic for saving models
        :raises: DAOCreateFailedError
        """
        if cls.model_cls is None:
            raise DAOConfigError()
        if not isinstance(instance_model, cls.model_cls):
            raise DAOCreateFailedError(
                "the instance model is not a type of the model class"
            )
        try:
            db.session.add(instance_model)
            if commit:
                db.session.commit()
        except SQLAlchemyError as ex:  # pragma: no cover
            db.session.rollback()
            raise DAOCreateFailedError(exception=ex) from ex
        return instance_model

    @classmethod
    def update(
        cls, model: Model, properties: Dict[str, Any], commit: bool = True
    ) -> Model:
        """
        Generic update a model
        :raises: DAOCreateFailedError
        """
        for key, value in properties.items():
            setattr(model, key, value)
        try:
            db.session.merge(model)
            if commit:
                db.session.commit()
        except SQLAlchemyError as ex:  # pragma: no cover
            db.session.rollback()
            raise DAOUpdateFailedError(exception=ex) from ex
        return model

    @classmethod
    def delete(cls, model: Model, commit: bool = True) -> Model:
        """
        Generic delete a model
        :raises: DAODeleteFailedError
        """
        try:
            db.session.delete(model)
            if commit:
                db.session.commit()
        except SQLAlchemyError as ex:  # pragma: no cover
            db.session.rollback()
            raise DAODeleteFailedError(exception=ex) from ex
        return model

    @classmethod
    def delete_by_ids(cls, ids: List[int] or set) -> List[int]:
        db.session.query(cls.model_cls).filter(
            cls.model_cls.id.in_(ids)
        ).delete(synchronize_session="fetch")
        return ids

    @classmethod
    def delete_auth_by_source(cls, data: dict):
        db.session.query(SysAuth).filter_by(
            auth_source=data["auth_source"],
            auth_source_type=data["auth_source_type"]
        ).delete()

    @classmethod
    def delete_auth_by_source_ids(
        cls,
        auth_source_ids: List[int] or set,
        auth_source_type: str,
    ):
        db.session.query(SysAuth).filter(
            SysAuth.auth_source.in_(auth_source_ids),
            SysAuth.auth_source_type == auth_source_type
        ).delete(synchronize_session="fetch")

    @classmethod
    def delete_auth_by_target(cls, data: dict, commit: bool = True):
        db.session.query(SysAuth).filter_by(
            auth_target=data["auth_target"],
            auth_target_type=data["auth_target_type"]
        ).delete()
        if commit:
            db.session.commit()

    @classmethod
    def insert_or_update(
        cls,
        properties: Dict[str, Any],
        update_properties: Dict[str, Any],
        commit: bool = True
    ) -> None:
        try:
            model = insert(cls.model_cls).values(
                **properties
            ).on_duplicate_key_update(
                **update_properties
            )
            db.session.execute(model)
            if commit:
                db.session.commit()
        except SQLAlchemyError as ex:
            db.session.rollback()
            raise HTTPError(ex, 500)

    @classmethod
    def archiving_docs(cls, doc_type: str, doc_json: Dict):
        archive = Archive(doc_type=doc_type, doc_json=json.dumps(doc_json))
        db.session.add(archive)
        db.session.commit()

    @staticmethod
    def find_auth_source_perm_by_user(
        auth_source_type: str,
        user_id: int,
        privilege_value: int
    ) -> dict:
        sql = f'''
            SELECT
                auth_source,
                MAX(privilege_value) AS privilege_value
            FROM
                sys_auth
            WHERE
                sys_auth.auth_source_type = :auth_source_type
            AND sys_auth.privilege_value >= :privilege_value
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
            "privilege_value": privilege_value
        }).fetchall()
        return {item[0]: item[1] for item in data}

    @staticmethod
    def validate_auth_source(
        auth_source: int,
        auth_source_type: str,
        privilege_value: int
    ) -> bool:
        if g.user.is_admin:
            return True

        user_id = g.user.id
        sql = f'''
            SELECT
                id
            FROM
                sys_auth
            WHERE
                sys_auth.auth_source = :auth_source
            AND sys_auth.auth_source_type = :auth_source_type
            AND sys_auth.privilege_value >= :privilege_value
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
        '''

        data = db.session.execute(sql, params={
            "auth_source": auth_source,
            "auth_source_type": auth_source_type,
            "privilege_value": privilege_value,
        }).first()
        return False if data is None else True

    @classmethod
    def find_source_perm_by_target(
        cls,
        auth_target: int,
        auth_target_type: str,
        auth_source_type: str,
    ) -> dict:
        data = db.session.query(
            SysAuth.auth_source,
            SysAuth.privilege_value
        ).filter_by(
            auth_target=auth_target,
            auth_target_type=auth_target_type,
            auth_source_type=auth_source_type
        ).all()
        return {item.auth_source: item.privilege_value for item in data}

    @classmethod
    def find_target_perm_by_source(
        cls,
        auth_source: int,
        auth_target_type: str,
        auth_source_type: str
    ) -> dict:
        data = db.session.query(
            SysAuth.auth_target,
            SysAuth.privilege_value
        ).filter_by(
            auth_source=auth_source,
            auth_target_type=auth_target_type,
            auth_source_type=auth_source_type
        ).all()
        return {item.auth_target: item.privilege_value for item in data}

    @classmethod
    def find_user_max_privilege_by_source_type(
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
    def find_perm(
        cls,
        auth_source: int,
        auth_source_type: str,
    ) -> int:
        if g.user.is_admin:
            return GRANT

        user_id = g.user.id
        sql = f'''
            SELECT
                MAX(privilege_value)
            FROM
                sys_auth
            WHERE
                sys_auth.auth_source = :auth_source
            AND sys_auth.auth_source_type = :auth_source_type
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
        '''

        data = db.session.execute(sql, params={
            "auth_source": auth_source,
            "auth_source_type": auth_source_type,
        }).first()
        return data[0] or 0


class BaseGroupDAO(BaseDAO):
    @classmethod
    def check_group_is_empty(cls, group_id: int):
        child_groups = db.session.query(
            cls.model_cls.id
        ).filter_by(
            pid=group_id
        ).first()
        if child_groups:
            raise HTTPError(Messages.DEL_GROUP_ERROR, 400)

    @classmethod
    def validate_uniqueness(cls, pid: int, name: str):
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.pid == pid,
            cls.model_cls.name == name,
        )
        return db.session.query(query.exists()).scalar()

    @classmethod
    def find_group_by_pid_name(cls, pid: int, name: str) -> Model:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.pid == pid,
            cls.model_cls.name == name,
        )
        return query.first()

    @classmethod
    def export_group(cls, pid: int) -> list:
        if pid == 0:
            return []

        group = cls.find_by_id(pid)
        if group is None:
            return []

        if group.pid == 0:
            return [group.name]

        return cls.export_group(group.pid) + [group.name]

    @classmethod
    def import_group(cls, group_path: list) -> Model:
        parent_group = cls.model_cls(id=0, pid=0, level=0)
        if group_path:
            for group_name in group_path:
                group = cls.find_group_by_pid_name(parent_group.id, group_name)
                if group is None:
                    group = cls.create({
                        "name": group_name,
                        "pid": parent_group.id,
                        "level": parent_group.level + 1,
                    })

                return group

        # 旧数据导入默认放入最先创建的分组
        return db.session.query(cls.model_cls).first()

    @classmethod
    def find_by_pid(cls, pid: int = 0) -> List[dict]:
        return db.session.query(cls.model_cls).filter_by(pid=pid).all()

    @classmethod
    def find_del_group_ids(cls, model: Model, pid: int, ids: List[int]) -> List:
        """
        查询出所有的分组，若分组内存在数据则400
        :param model: 分组模型
        :param pid: 父级ID
        :param ids: 所有子分组的ID列表
        :return:
        """
        res = db.session.query(model.id).filter_by(group_id=pid).first()
        if res is None:
            groups = db.session.query(cls.model_cls.id).filter_by(pid=pid).all()
            for item in groups:
                ids.append(item[0])
                cls.find_del_group_ids(model, item[0], ids)

            return ids

        raise HTTPError(Messages.DEL_GROUP_ERROR, 400)

    @classmethod
    def find_groups(cls, group_name: str = None) -> List[Model]:
        """
        查询分组信息
        :param group_name: 查询的分组名称
        :return:
        """
        query = db.session.query(cls.model_cls)
        if group_name:
            query = query.filter(
                cls.model_cls.name.startswith(group_name)
            )

        return query.order_by(cls.model_cls.level.desc()).all()

    @classmethod
    def _empty_group_filter(
        cls,
        groups: list,
        perm: int = None,
        group_auth: dict = dict(),
        key: str = None,
        data: dict = dict(),
        filter_empty_group: bool = False,
        filter_or_not: bool = False,
        max_group_auth: dict = dict(),
    ) -> dict:
        """
        过滤资源或者创建者时filter_empty_group = True, 非过滤状态下False
        :param groups: 所有分组
        :param perm: 默认权限
        :param group_auth: 各分组的权限等级字典
        :param key: 用于区分数据集、数据源、图表、看板
        :param data: 详细数据
        :param filter_empty_group: 是否过滤空分组
        :return:
        """
        res = {}
        for item in groups:
            data_perm = perm or group_auth.get(item.id, 0)
            if filter_or_not and data_perm == 0:
                continue

            group = {
                "group_id": item.id,
                "name": item.name,
                "pid": item.pid,
                "level": item.level,
                "perm": data_perm,
                "children": res.get(item.id, []),
                "max_perm": max_group_auth.get(item.id, 0)
            }

            if key is not None:
                group[key] = data.get(item.id, [])

            # 过滤空分组
            if (
                filter_empty_group
                and (not group["children"] and not group[key])
            ):
                continue

            if res.get(item.pid, False):
                res[item.pid].append(group)

            else:
                res[item.pid] = [group]

        return res

    @classmethod
    def _group_name_filter(
        cls,
        groups: list,
        perm: int = None,
        group_auth: dict = dict(),
        key: str = None,
        data: dict = dict(),
        group_name: str = None,
        filter_or_not: bool = False,
        max_group_auth: dict = dict(),
    ) -> dict:
        """
        分组过滤方法
        :param groups: 所有分组
        :param perm: 默认权限
        :param group_auth: 各分组的权限等级字典
        :param key: 用于区分数据集、数据源、图表、看板
        :param data: 详细数据
        :param group_name: 查询的分组名称
        :return:
        """
        detail_dict = {}
        res = {}
        for item in groups:
            data_perm = perm or group_auth.get(item.id, 0)
            if filter_or_not and data_perm < VIEW:
                continue

            group = {
                "group_id": item.id,
                "name": item.name,
                "pid": item.pid,
                "level": item.level,
                "perm": data_perm,
                "children": detail_dict.get(item.id, []),
                "max_perm": max_group_auth.get(item.id, 0)
            }

            if key is not None:
                group[key] = data.get(item.id, [])

            if detail_dict.get(item.pid, False):
                detail_dict[item.pid].append(group)

            else:
                detail_dict[item.pid] = [group]

            if item.name.find(group_name) > -1:
                group = detail_dict[item.pid][-1]
            elif res.get(item.id, False):  # 有children清空资源
                group = {
                    "group_id": item.id,
                    "name": item.name,
                    "pid": item.pid,
                    "level": item.level,
                    "perm": perm or group_auth.get(item.id, 0),
                    "children": res.get(item.id, []),
                    "max_perm": max_group_auth.get(item.id, 0)
                }
            else:
                # 分组名称不匹配并且自身没有子分组，直接跳过
                continue

            if res.get(item.pid, False):
                res[item.pid].append(group)

            else:
                res[item.pid] = [group]

        return res

    @classmethod
    def _find_tree_by_admin(
        cls,
        perm: int = None,
        group_auth: dict = dict(),
        key: str = None,
        data: dict = dict(),
        group_name: str = None,
        filter_empty_group: bool = False,
        filter_or_not: bool = False,
        max_group_auth: dict = dict(),
    ) -> List[dict]:
        """
        以分组加工数据或获取分组目录树
        :param perm: 默认权限，用于超级管理员查询数据时，直接输出最高权限
        :param group_auth: 用户各分组的权限等级字典
        :param key: 用于区分数据集、数据源、看板、图表
        :param data: 用户各分组内的数据，以分组ID为KEY
        :param group_name: 过滤分组名称
        :param filter_empty_group: 是否过滤空分组的展示
        :param filter_or_not: 是否过滤掉没有查看权限的数据，用于普通用户
        :param max_group_auth: 用户拥有的最高权限
        :return: 分组详情列表
        """
        # TODO 重复代码过多，需优化
        groups = cls.find_groups()
        # 分组查询
        if group_name:
            res = cls._group_name_filter(
                groups, perm, group_auth, key, data,
                group_name, filter_or_not, max_group_auth)

        else:
            res = cls._empty_group_filter(
                groups, perm, group_auth, key, data,
                filter_empty_group, filter_or_not, max_group_auth)

        res = res.get(0, [])
        res.sort(key=lambda k: (k.get('name', '')))
        return res

    @classmethod
    def _find_tree_by_user(
        cls,
        group_auth: dict,
        key: str = None,
        data: dict = dict(),
        group_filter: set = None,
        group_name: str = None,
        max_group_auth: dict = dict(),
    ) -> List[dict]:
        groups = cls.find_groups(group_name)
        res = {}
        for item in groups:
            if group_filter is None:
                if group_auth.get(item.id, 0) < VIEW:
                    continue

            else:
                if item.id not in group_filter:
                    continue

            group = {
                "group_id": item.id,
                "name": item.name,
                "pid": item.pid,
                "level": item.level,
                "perm": group_auth.get(item.id, 0),
                "children": res.get(item.id, []),
                "max_perm": max_group_auth.get(item.id, 0)
            }
            if key is not None:
                group[key] = data.get(item.id, [])

            if res.get(item.pid, False):
                res[item.pid].append(group)

            else:
                res[item.pid] = [group]

        res = res.get(0, [])
        res.sort(key=lambda k: (k.get('name', '')))
        return res

    @classmethod
    def find_tree(cls, user: Model, auth_source_type: str, perm: int):
        if user.is_admin:
            return cls._find_tree_by_admin(perm=perm)

        # 分组权限
        group_auth = cls.find_auth_source_perm_by_user(
            auth_source_type, user.id, MANAGE)
        return cls._find_tree_by_user(group_auth)

    @classmethod
    def find_children_ids_by_pid(cls, pid: int, ids: set = None) -> set:
        """
        获取所有子目录ID
        :param ids:
        :param pid: 父目录ID
        :return:
        """
        if ids is None:
            ids = set()

        query = db.session.query(cls.model_cls.id).filter_by(pid=pid)
        for item in query.all():
            ids.add(item[0])
            cls.find_children_ids_by_pid(item[0], ids)

        return ids

    @classmethod
    def update_children_level(cls, pid: int, level: int, commit: bool = False):
        """父级目录移动后，递归修改子目录level"""
        query = db.session.query(cls.model_cls).filter_by(pid=pid)
        for item in query.all():
            cls.update(item, {"level": level + 1}, commit=commit)
            return cls.update_children_level(item.id, level)
