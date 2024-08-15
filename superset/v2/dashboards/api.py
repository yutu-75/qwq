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
@Time       : 2023/3/29 13:39
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask import Response, g, request
from flask_appbuilder.api import expose

from superset import event_logger
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.dashboards.commands.copy import DashboardCopyCommand
from superset.v2.dashboards.commands.create import DashboardV2CreateCommand
from superset.v2.dashboards.commands.delete import DashboardV2DeleteCommand
from superset.v2.dashboards.commands.explore import DashboardExploreCommand
from superset.v2.dashboards.commands.get_data_command import \
    DashboardListCommand
from superset.v2.dashboards.commands.move import DashboardV2MoveCommand
from superset.v2.dashboards.schemas import DashboardResponseSchema
from superset.v2.dashboards.schemas import DashboardV2PostSchema, DashboardV2ExploreSchema
from superset.views.base_api import (
    BaseSupersetBaseApi,
    statsd_metrics,
    requires_json
)


class DashboardV2RestApi(BaseSupersetBaseApi):
    resource_name = "dashboard"
    openapi_spec_component_schemas = (
        DashboardV2PostSchema,
        DashboardV2ExploreSchema,
        DashboardResponseSchema
    )

    @expose(url="/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """
        ---
        get:
          description: 查询看板
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
            description: 看板名称
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
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/DashboardResponseSchema'
        """
        data = DashboardListCommand(g.user).run(**request.args)
        return self.format_response(200, data=data)

    @expose("/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DASHBOARD,
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """Creates a new Dashboard
        ---
        post:
          description: 新增 a new Dashboard，需校验当前分组是否拥有管理以上权限
          requestBody:
            description: Dashboard schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardV2PostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DashboardV2PostSchema().load(request.json)
        dashboard = DashboardV2CreateCommand(g.user, item).run()
        return self.format_response(200, data=dashboard.to_json())

    @expose("/copy/<int:dashboard_id>/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_COPY_DASHBOARD,
        log_to_statsd=False,
    )
    @requires_json
    def copy(self, dashboard_id: int) -> Response:
        """复制 Dashboard
        ---
        post:
          description: 复制 Dashboard，须校验当前用户对此看板是否拥有管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: dashboard_id
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardV2PostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DashboardV2PostSchema().load(request.json)
        dashboard = DashboardCopyCommand(g.user, dashboard_id, item).run()
        return self.format_response(200, data=dashboard.to_json())

    @expose("/<int:dashboard_id>/", methods=("PATCH",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_MOVE_DASHBOARD,
        log_to_statsd=False,
    )
    @requires_json
    def patch(self, dashboard_id: int) -> Response:
        """移动或重命名 Dashboard
        ---
        patch:
          description: 移动或重命名 Dashboard，须校验当前用户对此看板是否拥有管理以上权限
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardV2PostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DashboardV2PostSchema().load(request.json)
        dashboard = DashboardV2MoveCommand(g.user, dashboard_id, item).run()
        return self.format_response(200, data=dashboard.to_json())

    @expose(url="/<int:pk>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_DASHBOARD,
        log_to_statsd=False,
    )
    def delete(self, pk: int) -> Response:
        """Response
        delete dashboard.
        ---
        delete:
          description: >-
            删除 Dashboard，须校验当前用户对此看板是否拥有管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
            description: The dashboard id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        dash = DashboardV2DeleteCommand(g.user, pk).run()
        event_logger.log_with_context(
            action=LogsMessages.LM_DEL_DASHBOARD,
            dashboard_title=dash.dashboard_title,
        )
        return self.format_response(200)

    @expose("/explore/<pk>/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.EXPLORE_DASHBOARD_EXCEL,
        log_to_statsd=False,
    )
    def data(self, pk: str) -> Response:
        """导出pdf，excel
        ---
        post:
          description: 看板导出 excel, pdf
          parameters:
          - in: path
            schema:
              type: string
            name: pk
          requestBody:
            description: "image_data: 图片base64格式，data:image/*;base64,开头 <br>
                          explore_format: excel,pdf"
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardV2ExploreSchema'
          responses:
            200:
              description: ''
        """
        item = DashboardV2ExploreSchema().load(request.json)
        resp = DashboardExploreCommand(g.user, pk, item).run()
        return resp

    # @expose("/explore/img/<pk>/", methods=("GET",))
    # @authenticated()
    # @statsd_metrics
    # @event_logger.log_this_with_context(
    #     action=LogsMessages.LM_EXPLORE_DASHBOARD_IMG,
    #     log_to_statsd=False,
    # )
    # @requires_json
    # def explore_img(self, pk: str) -> Response:
    #     """看板导出图片
    #     ---
    #     post:
    #       description: 看板导出图片
    #       parameters:
    #       - in: path
    #         schema:
    #           type: string
    #         name: pk
    #       requestBody:
    #         description: "image_data: 图片base64格式，data:image/*;base64,开头"
    #         required: true
    #         content:
    #           application/json:
    #             schema:
    #               $ref: '#/components/schemas/DashboardV2ExploreSchema'
    #       responses:
    #         200:
    #           $ref: '#/components/responses/200'
    #     """
    #     item = DashboardV2ExploreSchema().load(request.json)
    #     data = DashboardExploreImgCommand(g.user, pk, item).run()
    #     return self.format_response(200, data=data)
