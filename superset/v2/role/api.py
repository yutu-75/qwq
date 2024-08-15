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
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging

from flask import g, request, Response
from flask_appbuilder.api import expose

from superset.extensions import event_logger
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.role.commands.create import RoleV2CreateCommand, RoleV2AddUserCreateCommand
from superset.v2.role.commands.delete import RoleV2DeleteCommand
from superset.v2.role.commands.get_data_command import (
    RoleV2ListCommand,
    RoleUsersInfoCommand
)
from superset.v2.role.commands.update import RoleV2UpdateCommand, RoleV2RemoveUserCommand
from superset.v2.role.schemas import RoleV2GetResponseSchema, \
    RoleV2PostSchema, RoleV2PutSchema, RoleV2RemoveUserSchema, RoleV2AddUserSchema
from superset.views.base_api import (
    requires_json,
    statsd_metrics, BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class RoleV2RestApi(BaseSupersetBaseApi):
    resource_name = "role"
    openapi_spec_component_schemas = (
        RoleV2PostSchema,
        RoleV2PutSchema,
        RoleV2GetResponseSchema,
        RoleV2RemoveUserSchema,
        RoleV2AddUserSchema,
    )

    @expose("/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """查询角色列表
        ---
        get:
          description: >-
            查询角色列表，需系统管理菜单权限
          parameters:
            - in: query
              schema:
                type: int
              name: page_size
              description: 页大小
            - in: query
              schema:
                type: int
              name: page_index
              description: 页码
            - in: query
              schema:
                type: string
              name: name
              description: 角色名
          responses:
            200:
              description: role
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/RoleV2GetResponseSchema'
        """
        data = RoleV2ListCommand(g.user).run(**request.args)
        return self.format_response(200, data=data)

    @expose("/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_ROLE,
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """新增角色
        ---
        post:
          description: >-
            新增角色,需角色管理菜单权限
          requestBody:
            description: role schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/RoleV2PostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = RoleV2PostSchema().load(request.json)
        RoleV2CreateCommand(g.user, item).run()
        return self.format_response(200)

    @expose("/<pk>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_ROLE,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, pk: int) -> Response:
        """编辑角色
        ---
        put:
          description: >-
            编辑角色, 需角色管理菜单权限
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          requestBody:
            description: role schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/RoleV2PutSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = RoleV2PutSchema().load(request.json)
        RoleV2UpdateCommand(g.user, pk, item).run()
        return self.format_response(200)

    @expose("/<pk>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_ROLE,
        log_to_statsd=False,
    )
    def delete(self, pk: int) -> Response:
        """删除角色, 需角色管理菜单权限
        ---
        delete:
          description: >-
            删除角色
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        RoleV2DeleteCommand(g.user, pk).run()
        return self.format_response(200)

    @expose("/<int:role_id>/users/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_role_users(self, role_id: int) -> Response:
        """查询此角色的所有用户列表, 需角色管理菜单权限
        ---
        get:
          parameters:
            - in: path
              schema:
                type: integer
              name: role_id
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
        data = RoleUsersInfoCommand(g.user, int(role_id)).run(**request.args)
        return self.format_response(200, data=data)

    @expose("/<int:role_id>/users/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_ROLE_USERS,
        log_to_statsd=False,
    )
    @requires_json
    def add_user(self, role_id: int) -> Response:
        """角色添加用户
        ---
        post:
          description: >-
            角色添加用户, 需角色管理菜单权限
          parameters:
            - in: path
              schema:
                type: integer
              name: role_id
          requestBody:
            description: role add user schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/RoleV2AddUserSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = RoleV2AddUserSchema().load(request.json)
        RoleV2AddUserCreateCommand(g.user, role_id, item).run()
        return self.format_response(200)

    @expose("/<int:role_id>/users/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_ROLE_USERS,
        log_to_statsd=False,
    )
    def remove_user(self, role_id: int) -> Response:
        """移除角色下的用户
        ---
        delete:
          description: >-
            移除角色下的用户, 需角色管理菜单权限
          parameters:
            - in: path
              schema:
                type: integer
              name: role_id
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/RoleV2RemoveUserSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = RoleV2RemoveUserSchema().load(request.json)
        RoleV2RemoveUserCommand(g.user, role_id, item).run()
        return self.format_response(200)
