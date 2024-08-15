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
@Time       : 2023/3/29 13:38
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Union, List, Any

from sqlalchemy import select

from superset import db
from superset.dao.base import BaseDAO
from superset.models.core import FavStar, FavStarClassName
from superset.models.dashboard import Dashboard, dashboard_slices
from superset.models.slice import Slice


class DashboardV2DAO(BaseDAO):
    model_cls = Dashboard

    @classmethod
    def find_charts_by_dashboard_id(cls, model_id: Union[str, int]) -> List[Any]:
        """
            通过看板id，查找看板关联的所有图表
        """
        # 查找看板 关联的所有图表
        chart_ids = db.session.query(dashboard_slices.c.slice_id).filter(
            dashboard_slices.c.dashboard_id == model_id).all()
        charts = db.session.query(Slice).filter(Slice.id.in_(chart_ids)).all()
        return charts

    @classmethod
    def search_dashboards(
        cls,
        name: str,
        ids: [list, set],
        user_id: int = 0,
        limit: int = 20
    ) -> select:
        where = []
        if name:
            where += [cls.model_cls.dashboard_title.like(f'''{name}%''')]

        if ids:
            where += [cls.model_cls.id.in_(ids)]

        if user_id > 0:
            where += [cls.model_cls.created_by_fk == user_id]

        query = select(cls.model_cls).where(*where).order_by(
            cls.model_cls.changed_on.desc()
        )
        res = db.session.execute(query.limit(limit)).all()
        return res

    @classmethod
    def find_favorite_dash_ids(cls, user_id: int, limit: int):
        query = db.session.query(FavStar.obj_id).filter(
            FavStar.user_id == user_id,
            FavStar.class_name == FavStarClassName.DASHBOARD
        )
        return [item[0] for item in query.limit(limit).all()]

    @classmethod
    def validate_uniqueness(cls, name: str, group_id: int) -> bool:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.dashboard_title == name,
            cls.model_cls.dashboard_group_id == group_id
        )
        return not db.session.query(query.exists()).scalar()

    @classmethod
    def find_by_group_ids(cls, group_ids: list) -> list:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.dashboard_group_id.in_(group_ids)
        )
        return query.all()
