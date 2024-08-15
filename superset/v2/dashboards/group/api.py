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
@Time       : 2023/3/29 12:37
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask import Response, g, request
from flask_appbuilder.api import expose
from marshmallow import ValidationError

from superset import event_logger
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.dashboards.group.commands.create import \
    CreateDashboardGroupCommand
from superset.v2.dashboards.group.commands.delete import \
    DeleteDashboardGroupCommand
from superset.v2.dashboards.group.commands.get_data_command import \
    DashboardGroupDataCommand, DashboardGroupTreeCommand
from superset.v2.dashboards.group.commands.update import \
    UpdateDashboardGroupCommand
from superset.v2.dashboards.group.schemas import DashboardGroupPostSchema, \
    DashboardGroupResponseSchema
from superset.views.base_api import (
    BaseSupersetBaseApi,
    statsd_metrics,
    requires_json
)


class DashboardGroupRestApi(BaseSupersetBaseApi):
    resource_name = "dashboard/group"
    openapi_spec_component_schemas = (
        DashboardGroupPostSchema,
        DashboardGroupResponseSchema,
    )

    @expose(url="/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """Response
        Returns all dashboard group info.
        ---
        get:
          description: 查询看板分组列表
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
            name: force
            description: 是否强制刷新
            schema:
              type: string
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/DashboardGroupResponseSchema'
        """
        data = DashboardGroupDataCommand(g.user).run(**request.args)
        return self.format_response(200, data=data)

    @expose(url="/tree/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_tree(self) -> Response:
        """
        ---
        get:
          description: 查询看板分组树
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/DashboardGroupResponseSchema'
        """
        data = DashboardGroupTreeCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DASHBOARD_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """Response
        add dashboard group.
        ---
        post:
          description: 新增看板分组，需校验当前用户是否拥有父级分组的管理以上权限
          requestBody:
            description: dashboard_group schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardGroupPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DashboardGroupPostSchema().load(request.json)
        group = CreateDashboardGroupCommand(g.user, item).run()
        return self.format_response(200, data=group.to_json())

    @expose(url="/<int:group_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_DASHBOARD_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, group_id: int) -> Response:
        """Response
        update dashboard group.
        ---
        put:
          description: 修改看板分组,重命名，需校验当前分组是否拥有管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: group_id
            description: The dashboard group id
          requestBody:
            description: dashboard_group schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardGroupSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DashboardGroupPostSchema().load(request.json)
        group = UpdateDashboardGroupCommand(g.user, group_id, item).run()
        return self.format_response(200, data=group.to_json())

    @expose(url="/<int:group_id>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_DASHBOARD_GROUP,
        log_to_statsd=False,
    )
    def delete(self, group_id: int) -> Response:
        """Response
        delete dashboard group.
        ---
        delete:
          description: 删除看板分组，需校验当前分组是否拥有管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: group_id
            description: The dashboard group id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        DeleteDashboardGroupCommand(g.user, group_id).run()
        return self.format_response(200)
