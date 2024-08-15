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

import logging
from typing import List

from flask_appbuilder import Model
from sqlalchemy import or_

from superset.connectors.sqla.models import SqlaTable
from superset.dao.base import BaseGroupDAO
from superset.exceptions import HTTPError
from superset.extensions import db
from superset.global_messages import Messages
from superset.constants import VIEW
from superset.models.database_sync import DatabaseSyncGroup, DatabaseSync
from superset.models.user import UserV2

logger = logging.getLogger(__name__)


class DatabaseSyncGroupDAO(BaseGroupDAO):
    model_cls = DatabaseSyncGroup

    @classmethod
    def check_group_is_empty(cls, group_id: int):
        """
        先检查分组内是否含有分组，在检查分组内是否有资源
        :param group_id:
        :return:
        """
        super(DatabaseSyncGroupDAO, cls).check_group_is_empty(group_id)
        data = db.session.query(SqlaTable.id).filter_by(table_group_id=group_id).first()
        if data:
            raise HTTPError(Messages.DEL_GROUP_ERROR, 400)

    @classmethod
    def find_tables(
        cls, name: str = None,
        creator: str = None,
        type_: int = None
    ) -> List[Model]:
        query = db.session.query(
            DatabaseSync.id,
            DatabaseSync.group_id,
            DatabaseSync.database_type,
            DatabaseSync.name,
            DatabaseSync.desc,
            DatabaseSync.database_id,
            DatabaseSync.created_by_fk
        )

        if creator:
            query = query.filter(
                DatabaseSync.created_by_fk.in_(
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
        type_: int = None,
        max_data_auth: dict = {},
        max_group_auth: dict = {},
    ) -> List[dict]:
        tables = cls.find_tables(name, creator, type_)

        database_sync = {}
        for table in tables:
            data_perm = perm or data_auth.get(table[5], 0)
            if filter_or_not and data_perm == 0:
                continue
            item = {
                "id": table[0],
                "group_id": table[1],
                "database_type": table[2],
                "name": table[3],
                "desc": table[4],
                "database_id":table[5],
                "created_by_fk":table[6],
                "perm":data_perm,
                "max_perm": max_data_auth.get(table[0], 0)
            }
            if database_sync.get(table[1], False):
                database_sync[table[1]].append(item)

            else:
                database_sync[table[1]] = [item]

        res = cls._find_tree_by_admin(
            perm=perm,
            group_auth=group_auth,
            key='database_sync',
            data=database_sync,
            group_name=group_name,
            filter_empty_group=bool(name or creator) or type_ is not None,
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
        tables = cls.find_tables()
        database_sync = {}
        for table in tables:
            if data_filter is None:
                if data_auth.get(table[0], 0) < VIEW:
                    continue

            else:
                if table[0] not in data_filter:
                    continue

            item = {
                "database_sync_id": table[0],
                "database_sync_name": table[2] or table[3],
                "database_id": table[4],
                "schema": table[5],
                "type_classify": table[6],
                "creator_id": table[7],
                "perm": data_auth.get(table[0], 0),
                "max_perm": max_data_auth.get(table[0], 0)
            }
            if database_sync.get(table[1], False):
                database_sync[table[1]].append(item)

            else:
                database_sync[table[1]] = [item]

        res = cls._find_tree_by_user(
            group_auth=group_auth,
            key='database_sync',
            data=database_sync,
            group_filter=group_filter,
            max_group_auth=max_group_auth,
        )
        return res

    @classmethod
    def find_del_group_ids(cls, model: Model, pid: int, ids: List[int]) -> List:
        """查询出所有的分组，若分组内存在数据则400"""
        res = db.session.query(model.id).filter_by(table_group_id=pid).first()
        if res is None:
            groups = db.session.query(cls.model_cls.id).filter_by(pid=pid).all()
            for item in groups:
                ids.append(item[0])
                cls.find_del_group_ids(model, item[0], ids)

            return ids

        raise HTTPError(Messages.DEL_GROUP_ERROR, 400)
