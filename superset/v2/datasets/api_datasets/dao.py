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
@Time       : 2023/8/8 13:38
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Optional, List

from sqlalchemy.orm import Session

from superset import db
from superset.dao.base import BaseDAO
from superset.models.datasource import TablesTask, TablesTaskLog

logger = logging.getLogger(__name__)


class TableTaskDAO(BaseDAO):
    model_cls = TablesTask

    @classmethod
    def validate_uniqueness(cls, name: str, table_id: int, filter_id: int = None) -> bool:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.name == name,
            cls.model_cls.table_id == table_id,
        )
        if filter_id is not None:
            query = query.filter(cls.model_cls.id != filter_id)

        return db.session.query(query.exists()).scalar()

    @classmethod
    def find_active(cls, session: Optional[Session] = None) -> List[TablesTask]:
        session = session or db.session
        return (
            session.query(cls.model_cls).filter(cls.model_cls.status == 1).all()
        )


class TableTaskLogDAO(BaseDAO):
    model_cls = TablesTaskLog

    @classmethod
    def search(cls, log_id: int, name: str, page: int = 1, limit: int = 20):
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.table_task_id == log_id
        )
        count = query.count()
        query = query.order_by(
            cls.model_cls.start_time.desc()
        ).limit(limit).offset(limit * (page - 1))
        return {
            "count": count,
            "page": page,
            "limit": limit,
            "result": [
                {
                    "task_name": name,
                    **item.to_json()
                } for item in query.all()
            ]
        }
