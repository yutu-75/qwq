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
@Time       : 2023/3/17 13:46
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask import Response, g, request
from flask_appbuilder.api import expose

from superset import event_logger
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.datasources.commands.delete import DeleteDataSourceCommand
from superset.v2.datasources.commands.get_data_command import (
    DataSourceTableDataCommand,
    DataSourceTableColumnDataCommand,
    DataSourceDataCommand,
    DataSourceDatasetsListCommand
)
from superset.v2.datasources.commands.move import MoveDataSourceCommand
from superset.v2.datasources.schemas import (
    DataSourcePatchSchema,
    DataSourceResponseDataSchema,
    DataSourceTablesInfoResponseSchema,
    DataSourcePutSchema,
)
from superset.views.base_api import (
    BaseSupersetBaseApi,
    statsd_metrics,
    requires_json
)


class DataSourcesRestApi(BaseSupersetBaseApi):
    resource_name = "datasource"
    openapi_spec_component_schemas = (
        DataSourceResponseDataSchema,
        DataSourcePatchSchema,
        DataSourceTablesInfoResponseSchema,
        DataSourcePutSchema,
    )

    @expose(url="/<int:datasource_id>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_datasource_info(self, datasource_id: int) -> Response:
        """
        ---
        get:
          description: 查询数据源信息，需要此数据源拥有管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: datasource_id
            description: 数据源ID
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/DataSourceResponseDataSchema'
        """
        data = DataSourceDataCommand(g.user, datasource_id).run()
        return self.format_response(200, data=data)

    @expose(url="/<int:datasource_id>/tables/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self, datasource_id: int) -> Response:
        """
        ---
        get:
          description: 查询数据源表信息，需要此数据源拥有查看以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: datasource_id
            description: 数据源ID
          - in: query
            schema:
              type: string
            name: force
            description: 是否强制刷新（填写任意字符都为强制刷新，不传此参数为获取缓存）
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/DataSourceTablesInfoResponseSchema'
        """
        data = DataSourceTableDataCommand(g.user, datasource_id).run(**request.args)
        return self.format_response(200, data=data)

    @expose(url="/<int:datasource_id>/<string:table_name>/columns/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_columns(self, datasource_id: int, table_name: str) -> Response:
        """
        ---
        get:
          description: 查询数据源信息，需要此数据源拥有查看以上权限
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/DataSourceResponseDataSchema'
        """
        command = DataSourceTableColumnDataCommand(g.user, datasource_id, table_name)
        data = command.run()
        return self.format_response(200, data=data)

    @expose(url="/<int:datasource_id>/", methods=("PATCH",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_MOVE_DATA_SOURCE,
        log_to_statsd=False,
    )
    @requires_json
    def patch(self, datasource_id: int) -> Response:
        """
        ---
        patch:
          description: 移动数据源
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DataSourcePatchSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DataSourcePatchSchema().load(request.json)
        datasource = MoveDataSourceCommand(
            g.user, datasource_id, item
        ).run()
        return self.format_response(200, data=datasource.to_json())

    @expose("/<int:datasource_id>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    def delete(self, datasource_id: int) -> Response:
        """
        ---
        delete:
          description: 删除数据源
          parameters:
          - in: path
            schema:
              type: integer
            name: datasource_id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        datasource = DeleteDataSourceCommand(g.user, datasource_id).run()
        event_logger.log_with_context(
            action=LogsMessages.LM_DEL_DATASOURCE,
            name=datasource.name,
        )
        return self.format_response(200)

    @expose("/<int:datasource_id>/datasets/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def pre_delete(self, datasource_id: int) -> Response:
        """
        ---
        get:
          description: 查询数据源关联的所有数据集
          parameters:
          - in: path
            schema:
              type: integer
            name: datasource_id
          responses:
            200:
              description: '[] : 没有关联数据集'
        """
        data = DataSourceDatasetsListCommand(g.user, datasource_id).run()
        return self.format_response(200, data=data)
