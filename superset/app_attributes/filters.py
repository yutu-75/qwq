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
import json
from typing import Any
from flask_appbuilder.models.filters import BaseFilter
from sqlalchemy import or_
from sqlalchemy.orm import Query
from superset import security_manager
from superset.utils.filters import get_dataset_access_filters


class AppAttributeFilter(BaseFilter):

    def apply(self, query: Query, value: Any) -> Query:
        """
        过滤已经被逻辑删除的数据
        :param query:
        :param value:
        :return:
        """
        if security_manager.can_access_all_datasources():
            query = query.filter(self.model.is_delete == False)
            return query

        return query.filter(get_dataset_access_filters(self.model))


class SearchTextFilter(BaseFilter):

    # TODO 待封装成公用组件

    arg_name = "search"

    def apply(self, query: Query, value: Any) -> Query:
        if not value:
            return query
        ilike_value = f"%{value}%"
        return query.filter(
            or_(
                self.model.name.ilike(ilike_value),
                self.model.code.ilike(ilike_value),
            )
        )


class SearchSyncTextFilter(BaseFilter):
    arg_name = "sync_search"

    def apply(self, query: Query, value: Any) -> Query:
        if not value:
            return query
        ilike_value = f"%{value}%"
        return query.filter(
            or_(
                self.model.id.ilike(ilike_value),
                self.model.name.ilike(ilike_value),
                self.model.database_id.ilike(ilike_value),
                self.model.database_type.ilike(ilike_value),
                self.model.desc.ilike(ilike_value),
                self.model.group_id.ilike(ilike_value),
            )
        )


class SearchTaskTextFilter(BaseFilter):

    arg_name = "task_search"

    def apply(self, query: Query, value: Any) -> Query:
        print(value)
        if not value:
            return query

        if isinstance(value, str):
            value = json.loads(value)

        value_str = value.get("value")
        database_sync_id = value.get("database_sync_id")
        ilike_value = f"%{value_str}%"
        return query.filter(
            or_(
                self.model.task_id.ilike(ilike_value),
                self.model.task_name.ilike(ilike_value),
                self.model.task_code.ilike(ilike_value),
                self.model.execute_type.ilike(ilike_value),
                self.model.execute_status.ilike(ilike_value),
                self.model.target_database_type.ilike(ilike_value),
                self.model.target_database_name.ilike(ilike_value),
                self.model.target_database_table_name.ilike(ilike_value),
                self.model.source_dbs_id.ilike(ilike_value),
                self.model.update_type.ilike(ilike_value),
                self.model.is_active.ilike(ilike_value),
                self.model.source_name.ilike(ilike_value),
                self.model.source_database_type.ilike(ilike_value),
                self.model.source_database_name.ilike(ilike_value),
                self.model.source_database_table_name.ilike(ilike_value),
                self.model.column_range_data.ilike(ilike_value),
                self.model.row_range_data.ilike(ilike_value),

            ),
            self.model.database_sync_id == database_sync_id
        )
