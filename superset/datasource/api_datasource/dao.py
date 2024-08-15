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
@Time       : 2023/7/18 14:50
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from sqlalchemy import null

from superset import db
from superset.dao.base import BaseDAO
from superset.models.datasource import DataSource, APITables


class DataSourceDAO(BaseDAO):
    model_cls = DataSource

    @classmethod
    def validate_uniqueness(cls, name: str):
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.name == name
        )
        return db.session.query(query.exists()).scalar()

    @classmethod
    def find_by_type(cls, d_type: str = 'api'):
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.d_type == d_type
        )
        return query.all()


class APITablesDAO(BaseDAO):
    model_cls = APITables

    @classmethod
    def delete_by_null(cls) -> None:
        db.session.query(
            cls.model_cls
        ).filter(
            cls.model_cls.datasource_id == null()
        ).delete()
