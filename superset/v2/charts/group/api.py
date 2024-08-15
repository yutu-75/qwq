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

from flask import g, request, Response
from flask_appbuilder.api import expose

from superset.extensions import event_logger
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.charts.group.commands.create import CreateChartGroupCommand
from superset.v2.charts.group.commands.delete import DeleteChartGroupCommand
from superset.v2.charts.group.commands.get_data_command import \
    ChartGroupDataCommand, ChartGroupTreeCommand
from superset.v2.charts.group.commands.update import UpdateChartGroupCommand
from superset.v2.charts.group.schemas import ChartGroupPostSchema, ChartGroupSchema, \
    ChartGroupSearchSchema
from superset.views.base_api import (
    requires_json,
    statsd_metrics, BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class ChartGroupRestApi(BaseSupersetBaseApi):
    resource_name = "chart/group"
    add_model_schema = ChartGroupPostSchema()
    openapi_spec_component_schemas = (
        ChartGroupSchema,
    )

    @expose(url="/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """
        ---
        get:
          description: 查询chart group 列表
          parameters:
          - in: query
            name: group_name
            description: 分组名称
            schema:
              type: string
          - in: query
            name: name
            description: 资源名称
            schema:
              type: string
          - in: query
            name: creator
            description: 创建者
            schema:
              type: string
          - in: query
            name: viz_type
            description: 图表类型
            schema:
              type: string
          - in: query
            name: force
            description: 是否强制刷新
            schema:
              type: string
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/ChartGroupSchema'
        """
        item = ChartGroupSearchSchema().load(request.args)
        data = ChartGroupDataCommand(g.user).run(**item)
        return self.format_response(200, data=data)

    @expose(url="/tree/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_tree(self) -> Response:
        """
        ---
        get:
          description: 查询图表分组树
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/ChartGroupSchema'
        """
        data = ChartGroupTreeCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_CHART_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """
        ---
        post:
          description: 新增 chart group, 需校验父级分组是否拥有管理权限
          requestBody:
            description: chart_group schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ChartGroupSchema'

          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = self.add_model_schema.load(request.json)
        CreateChartGroupCommand(g.user, item).run()
        return self.format_response(200)

    @expose(url="/<int:group_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_CHART_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, group_id: int) -> Response:
        """
        ---
        put:
          description: 修改 chart group, 需校验当前分组是否拥有管理权限
          parameters:
          - in: path
            schema:
              type: integer
            name: group_id
            description: chart group id
          requestBody:
            description: chart_group schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ChartGroupSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = self.add_model_schema.load(request.json)
        UpdateChartGroupCommand(g.user, group_id, item).run()
        return self.format_response(200)

    @expose(url="/<int:group_id>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_CHART_GROUP,
        log_to_statsd=False,
    )
    def delete(self, group_id: int) -> Response:
        """
        ---
        delete:
          description: 删除 chart group, 需校验当前分组是否拥有管理权限
          parameters:
          - in: path
            schema:
              type: integer
            name: group_id
            description: chart group id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        DeleteChartGroupCommand(g.user, group_id).run()
        return self.format_response(200)
