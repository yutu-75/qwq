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
@Time       : 2023/3/17 16:25
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging

from flask import Response, g, request
from flask_appbuilder.api import expose

from superset import event_logger
from superset.logs_messages import LogsMessages
from superset.sys_manager.permission.commands.create import (
    CreateSysAuthCommand,
    CreateDatabaseAuthCommand,
)
from superset.sys_manager.permission.commands.get_data_command import \
    SysAuthDataCommand, SysAuthDetailDataCommand, DatabaseSchemaDetailCommand, \
    DatabaseSchemaTablesDetailCommand
from superset.sys_manager.permission.schemas import (
    SysAuthPostSchema,
    SysAuthDetailPostSchema,
    SysAuthTypeSchema,
    SysAuthDetailGetSchema,
    BatchChangeAuthSchema,
    DatabaseAuthPostSchema,
    DatabaseSchemaAuthSchema
)
from superset.utils.decorators import authenticated
from superset.views.base_api import BaseSupersetBaseApi, statsd_metrics, \
    requires_json

logger = logging.getLogger(__name__)


class SysAuthRestApi(BaseSupersetBaseApi):
    resource_name = "auth"
    openapi_spec_component_schemas = (
        SysAuthPostSchema,
        SysAuthDetailPostSchema,
        SysAuthDetailGetSchema,
        BatchChangeAuthSchema,
        DatabaseAuthPostSchema,
        DatabaseSchemaAuthSchema
    )

    @expose(url="/<string:auth_type>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_by_auth_type(self, auth_type: str) -> Response:
        """
        ---
        get:
          description: 获取各模块信息，需权限管理菜单拥有管理权限
          parameters:
          - in: path
            name: auth_type
            description: dept/role/user/datasource/dataset/dashboard/chart/menu
            schema:
              type: string
          - in: query
            schema:
              type: integer
            name: page_size
            description: 页大小
          - in: query
            schema:
              type: integer
            name: page_index
            description: 页码
          - in: query
            schema:
              type: string
            name: username
            description: 用户名
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        SysAuthTypeSchema().load({"auth_type": auth_type})
        data = SysAuthDataCommand(g.user, auth_type, **request.args).run()
        return self.format_response(200, data=data)

    @expose(url="/change/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_AUTH,
        log_to_statsd=False,
    )
    @requires_json
    def add(self) -> Response:
        """
        ---
        post:
          description: 权限设置， 需权限管理菜单拥有授权权限
          requestBody:
            description: >-
              auth_source_type -> 数据源类别(dashboard/dashboard_group/chart/
                chart_group/datasource/datasource_group/dataset/dataset_group/menu)<br>
              auth_source -> 数据源ID(dashboard_id/chart_id...) <br>
              auth_target_type -> 授权目标类别(dept/role/user) <br>
              auth_target_type -> 授权目标ID(dept_id/role_id/user_id) <br>
              privilege_value -> 1(查看)/2(导入)/4(管理)/8(授权)
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/SysAuthPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = SysAuthPostSchema().load(request.json)
        CreateSysAuthCommand(g.user, item).run()
        return self.format_response(200)

    @expose(url="/change/database/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_AUTH,
        log_to_statsd=False,
    )
    @requires_json
    def change_database(self) -> Response:
        """
        ---
        post:
          description: 权限设置， 需权限管理菜单拥有授权权限
          requestBody:
            description: >-
              auth_source_type -> 数据源类别(db_schema/db_schema_table)<br>
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatabaseAuthPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DatabaseAuthPostSchema().load(request.json)
        data = CreateDatabaseAuthCommand(g.user, item).run()
        return self.format_response(200, data=data)

    @expose(url="/detail/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    def get_auth_detail(self) -> Response:
        """
        ---
        post:
          description: 获取授权详情, 需权限管理菜单拥有管理权限
          parameters:
          - in: query
            schema:
              type: integer
            name: page_size
            description: 页大小
          - in: query
            schema:
              type: integer
            name: page_index
            description: 页码
          - in: query
            schema:
              type: string
            name: username
            description: 用户名
          requestBody:
            description: >-
              direction -> source/target<br>
              auth_source_type -> 数据源类别(dashboard/chart/datasource/dataset/menu)<br>
              auth_source -> 数据源ID(dashboard_id/chart_id...)<br>
              auth_target_type -> 授权目标类别(dept/role/user) <br>
              auth_target -> 授权目标ID<br>
              注意：当direction=source请务必不传auth_source，direction=target不传auth_target
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/SysAuthDetailGetSchema'
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      meta:
                        type: object
                        properties:
                          code:
                            type: integer
                            default: 200
                          message:
                            type: string
                            default: 'success'
                          data:
                            type: object
        """
        item = SysAuthDetailGetSchema().load(request.json)
        data = SysAuthDetailDataCommand(g.user, item).run(**request.args)
        return self.format_response(200, data=data)

    @expose(url="/database/<int:database_id>/schema/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    def get_schema(self, database_id: int) -> Response:
        """
        ---
        post:
          description: 获取授权详情, 需权限管理菜单拥有管理权限
          parameters:
          - in: path
            schema:
              type: integer
            name: database_id
            description: db ID
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatabaseSchemaAuthSchema'
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      meta:
                        type: object
                        properties:
                          code:
                            type: integer
                            default: 200
                          message:
                            type: string
                            default: 'success'
                          data:
                            type: object
        """
        item = DatabaseSchemaAuthSchema().load(request.json)
        data = DatabaseSchemaDetailCommand(g.user, item, database_id).run()
        return self.format_response(200, data=data)

    @expose(url="/database/<int:database_id>/schema/<string:schema_name>/tables", methods=("POST",))
    @authenticated()
    @statsd_metrics
    def get_schema_tables(self, database_id: int, schema_name: str) -> Response:
        """
        ---
        post:
          description: 获取授权详情, 需权限管理菜单拥有管理权限
          parameters:
          - in: path
            schema:
              type: integer
            name: database_id
            description: db ID
          - in: path
            schema:
              type: string
            name: schema_name
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatabaseSchemaAuthSchema'
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      meta:
                        type: object
                        properties:
                          code:
                            type: integer
                            default: 200
                          message:
                            type: string
                            default: 'success'
                          data:
                            type: object
        """
        item = DatabaseSchemaAuthSchema().load(request.json)
        data = DatabaseSchemaTablesDetailCommand(g.user, item, database_id, schema_name).run()
        return self.format_response(200, data=data)
