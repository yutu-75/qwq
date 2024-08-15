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
from superset.v2.charts.commands.copy import CopyChartCommand
from superset.v2.charts.commands.create import CreateChartV2Command
from superset.v2.charts.commands.delete import DeleteV2ChartCommand
from superset.v2.charts.commands.explore import ChartExploreCommand
from superset.v2.charts.commands.get_data_command import (
    ChartListDataCommand,
    ChartDashboardsListCommand
)
from superset.v2.charts.commands.move import MoveV2ChartCommand
from superset.v2.charts.commands.update import UpdateV2ChartCommand
from superset.v2.charts.schemas import (
    ChartV2PostSchema,
    ChartV2PutSchema,
    ChartV2PatchSchema,
    ChartV2ExploreSchema,
    ChartCopySchema,
)
from superset.views.base_api import (
    requires_json,
    BaseSupersetBaseApi
)
from superset.views.base_api import statsd_metrics

logger = logging.getLogger(__name__)


class ChartV2RestApi(BaseSupersetBaseApi):
    resource_name = "chart"
    openapi_spec_component_schemas = (
        ChartV2PostSchema,
        ChartV2PutSchema,
        ChartV2PatchSchema,
        ChartV2ExploreSchema,
        ChartCopySchema,
    )

    @expose(url="/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """
        ---
        get:
          description: 查询授权的图表列表
          parameters:
          - in: query
            schema:
              type: integer
            name: limit
            description: 个数
          - in: query
            schema:
              type: string
            name: title
            description: 图表名称
          - in: query
            schema:
              type: string
            name: force
            description: 是否强制刷新
          - in: query
            schema:
              type: bool
            name: favorite
            description: 收藏（true/false）
          - in: query
            schema:
              type: bool
            name: owner
            description: 我的（true/false）
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = ChartListDataCommand(g.user).run(**request.args)
        return self.format_response(200, data=data)

    @expose("/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_CHART,
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """
        ---
        post:
          description: 新增 chart，需拥有当前分组的管理权限
          requestBody:
            description: chart schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ChartV2PostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = ChartV2PostSchema().load(request.json)
        CreateChartV2Command(g.user, item).run()
        return self.format_response(200)

    @expose("/<int:pk>/", methods=("PATCH",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_MOVE_CHART,
        log_to_statsd=False,
    )
    @requires_json
    def patch(self, pk: int) -> Response:
        """
        ---
        patch:
          description: 将当前图表移动到目标分组内或者重命名，需拥有当前图表的管理权限
          requestBody:
            description: "target_id: 目标ID， new_title: new title"
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ChartV2PatchSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = ChartV2PatchSchema().load(request.json)
        MoveV2ChartCommand(g.user, pk, item).run()
        return self.format_response(200)

    @expose("/<pk>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_CHART,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, pk: int) -> Response:
        """
        ---
        put:
          description: 修改 chart，需拥有当前图表的管理权限
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          requestBody:
            description: chart schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ChartV2PutSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = ChartV2PutSchema().load(request.json)
        UpdateV2ChartCommand(g.user, pk, item).run()
        return self.format_response(200)

    @expose("/<pk>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    def delete(self, pk: int) -> Response:
        """
        ---
        delete:
          description: 删除 chart
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        chart = DeleteV2ChartCommand(g.user, pk).run()
        event_logger.log_with_context(
            action=LogsMessages.LM_DEL_CHART,
            name=chart.slice_name,
        )
        return self.format_response(200)

    @expose("/<int:chart_id>/dashboards/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def pre_delete(self, chart_id: int) -> Response:
        """
        ---
        get:
          description: 查询图表关联的所有看板
          parameters:
          - in: path
            schema:
              type: integer
            name: chart_id
          responses:
            200:
              description: '[] : 没有关联看板'
        """
        data = ChartDashboardsListCommand(g.user, chart_id).run()
        return self.format_response(200, data=data)

    @expose("/explore/<pk>/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.EXPLORE_CHART_EXCEL,
        log_to_statsd=False,
    )
    def data(self, pk: str) -> Response:
        """
        ---
        post:
          description: 图表导出 excel, pdf
          parameters:
          - in: path
            schema:
              type: string
            name: pk
          requestBody:
            description: "image_data: 图片base64格式，data:image/png;base64,开头 <br>
                          explore_format: excel,pdf"
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ChartV2ExploreSchema'
          responses:
            200:
              description: ''
        """
        item = ChartV2ExploreSchema().load(request.json)
        resp = ChartExploreCommand(g.user, pk, item).run()
        return resp

    @expose("/copy/<int:pk>/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_MOVE_CHART,
        log_to_statsd=False,
    )
    @requires_json
    def copy(self, pk: int) -> Response:
        """
        ---
        post:
          description: 复制图标，需拥有当前图表的管理权限
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ChartCopySchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = ChartCopySchema().load(request.json)
        CopyChartCommand(g.user, pk, item).run()
        return self.format_response(200)
