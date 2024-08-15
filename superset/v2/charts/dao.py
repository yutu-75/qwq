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
from sqlalchemy import select

from superset.charts.dao import ChartDAO
from superset.extensions import db
from superset.models.core import FavStar, FavStarClassName

logger = logging.getLogger(__name__)


class ChartV2DAO(ChartDAO):
    @classmethod
    def search_charts(
        cls,
        name: str,
        ids: [list, set],
        user_id: int = 0,
        limit: int = 20
    ) -> select:
        where = []
        if name:
            where += [cls.model_cls.slice_name.like(f'''{name}%''')]

        if ids:
            where += [cls.model_cls.id.in_(ids)]

        if user_id > 0:
            where += [cls.model_cls.created_by_fk == user_id]

        query = select(cls.model_cls).where(*where).order_by(
            cls.model_cls.changed_on.desc()
        )
        if int(limit) > 0:
            query = query.limit(limit)

        res = db.session.execute(query).all()
        return res

    @classmethod
    def find_favorite_chart_ids(cls, user_id: int):
        query = db.session.query(FavStar.obj_id).filter(
            FavStar.user_id == user_id,
            FavStar.class_name == FavStarClassName.CHART
        )
        return [item[0] for item in query.all()]

    @classmethod
    def validate_uniqueness(cls, slice_name: str, group_id: int, **kwargs) -> bool:
        dataset_query = db.session.query(cls.model_cls).filter(
            cls.model_cls.slice_name == slice_name,
            cls.model_cls.slice_group_id == group_id
        )
        return not db.session.query(dataset_query.exists()).scalar()

    @classmethod
    def find_by_group_ids(cls, group_ids: list) -> list:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.slice_group_id.in_(group_ids)
        )
        return query.all()
