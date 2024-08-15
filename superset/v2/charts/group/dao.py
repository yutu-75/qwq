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

from superset import conf
from superset.constants import VIEW
from superset.dao.base import BaseGroupDAO
from superset.exceptions import HTTPError
from superset.extensions import db
from superset.global_messages import Messages
from superset.models.slice import SliceGroup, Slice
from superset.models.user import UserV2
from superset.v2.user.dao import UserV2DAO

logger = logging.getLogger(__name__)


class ChartGroupDAO(BaseGroupDAO):
    model_cls = SliceGroup

    @classmethod
    def check_group_is_empty(cls, group_id: int):
        """
        先检查分组内是否含有分组，在检查分组内是否有资源
        :param group_id:
        :return:
        """
        super(ChartGroupDAO, cls).check_group_is_empty(group_id)
        data = db.session.query(Slice.id).filter_by(
            slice_group_id=group_id).first()
        if data:
            raise HTTPError(Messages.DEL_GROUP_ERROR, 400)

    @classmethod
    def find_del_group_ids(cls, model: Model, pid: int, ids: List[int]) -> List:
        """查询出所有的分组，若分组内存在数据则400"""
        res = db.session.query(model.id).filter_by(
            slice_group_id=pid).first()
        if res is None:
            groups = db.session.query(cls.model_cls.id).filter_by(pid=pid).all()
            for item in groups:
                ids.append(item[0])
                cls.find_del_group_ids(model, item[0], ids)

            return ids

        raise HTTPError(Messages.DEL_GROUP_ERROR, 400)

    @classmethod
    def find_charts(
        cls, name:
        str = None,
        creator: str = None,
        viz_type: str = None,
    ) -> List[Model]:
        query = db.session.query(
            Slice.id,
            Slice.slice_name,
            Slice.datasource_id,
            Slice.datasource_type,
            Slice.query_context,
            Slice.slice_group_id,
            Slice.created_by_fk,
            Slice.created_on,
            Slice.changed_on,
            Slice.changed_by_fk,
        )
        if name:
            query = query.filter(
                Slice.slice_name.contains(name)
            )

        if viz_type:
            query = query.filter(
                Slice.viz_type == viz_type
            )

        if creator:
            query = query.filter(
                Slice.created_by_fk.in_(
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
        viz_type: str = None,
        max_data_auth: dict = {},
        max_group_auth: dict = {},
    ) -> List[dict]:
        slices = cls.find_charts(name, creator, viz_type)
        charts = {}
        users = UserV2DAO.find_users_cn_name()
        for slice in slices:
            data_perm = perm or data_auth.get(slice[0], 0)
            if filter_or_not and data_perm == 0:
                continue

            item = {
                "slice_id": slice[0],
                "slice_name": slice[1],
                "url": f"{conf['STATIC_ASSETS_PREFIX']}/explore/?slice_id={slice[0]}",
                "datasource_type": slice[3],
                "query_context": slice[4],
                "created_by_fk": users.get(slice[6]),
                "created_on": str(slice[7]),
                "changed_on": str(slice[8]),
                "changed_by_fk": users.get(slice[9]),
                "perm": data_perm,
                "max_perm": max_data_auth.get(slice[0], 0)
            }
            if charts.get(slice[5], False):
                charts[slice[5]].append(item)

            else:
                charts[slice[5]] = [item]

        res = cls._find_tree_by_admin(
            perm=perm,
            group_auth=group_auth,
            key='slices',
            data=charts,
            group_name=group_name,
            filter_empty_group=bool(name or creator or viz_type),
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
        slices = cls.find_charts()
        charts = {}
        for slice in slices:
            if data_filter is None:
                if data_auth.get(slice[0], 0) < VIEW:
                    continue

            else:
                if slice[0] not in data_filter:
                    continue

            item = {
                "slice_id": slice[0],
                "slice_name": slice[1],
                "url": f"{conf['STATIC_ASSETS_PREFIX']}/explore/?slice_id={slice[0]}",
                "datasource_id": slice[2],
                "datasource_type": slice[3],
                "query_context": slice[4],
                "perm": data_auth.get(slice[0], 0),
                "max_perm": max_data_auth.get(slice[0], 0)
            }
            if charts.get(slice[5], False):
                charts[slice[5]].append(item)

            else:
                charts[slice[5]] = [item]

        res = cls._find_tree_by_user(
            group_auth=group_auth,
            key='slices',
            data=charts,
            group_filter=group_filter,
            max_group_auth=max_group_auth,
        )
        return res
