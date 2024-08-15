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
@Time       : 2023/7/4 17:54
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask import Response, g, request
from flask_appbuilder.api import expose

from superset import event_logger
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.datasources.database.commands.create import (
    CreateDatabaseDataSourceCommand,
)
from superset.v2.datasources.database.commands.get_data_command import \
    DatabaseDataSourceListCommand
from superset.v2.datasources.database.schemas import \
    DatabaseDataSourcePostSchema
from superset.views.base_api import (
    BaseSupersetBaseApi,
    statsd_metrics,
    requires_json
)


class DataSourcesDatabaseRestApi(BaseSupersetBaseApi):
    resource_name = "datasource/database"
    openapi_spec_component_schemas = (
        DatabaseDataSourcePostSchema,
    )

    @expose(url="/list/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_list(self) -> Response:
        """
        ---
        get:
          description: 查询数据库数据源列表
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      id:
                        type: integer
                      name:
                        type: string
                      d_type:
                        type: string
                      database_id:
                        type: integer

        """
        data = DatabaseDataSourceListCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @requires_json
    def add_database(self) -> Response:
        """
        ---
        post:
          description: 新增数据库数据源，需要此数据源分组拥有管理以上权限
          requestBody:
            description: d_type = database
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatabaseDataSourcePostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DatabaseDataSourcePostSchema().load(request.json)
        datasource = CreateDatabaseDataSourceCommand(g.user, item).run()
        event_logger.log_with_context(
            action=LogsMessages.LM_ADD_DATABASE_DATA_SOURCE,
            name=datasource.name,
        )
        return self.format_response(200, data=datasource.to_json())
