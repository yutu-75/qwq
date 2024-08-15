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
@Time       : 2023/3/17 13:46
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask import Response, g, request
from flask_appbuilder.api import expose

from superset import event_logger
from superset.logs_messages import LogsMessages
from superset.sys_manager.dept.commands.create import (
    CreateSysDeptCommand,
    CreateSysDeptUsersCommand
)
from superset.sys_manager.dept.commands.delete import DeleteSysDeptCommand, \
    DeleteSysDeptUsersCommand
from superset.sys_manager.dept.commands.get_data_command import \
    SysDeptDataCommand, SysDeptUsersDataCommand
from superset.sys_manager.dept.commands.update import UpdateSysDeptCommand
from superset.sys_manager.dept.schemas import (
    SysDeptPostSchema,
    SysDeptResponseSchema,
    SysDeptUserPostSchema,
    SysDeptUsersResponseSchema
)
from superset.utils.decorators import authenticated
from superset.views.base_api import (
    BaseSupersetBaseApi,
    statsd_metrics,
    requires_json
)


class SysDeptRestApi(BaseSupersetBaseApi):
    resource_name = "dept"
    openapi_spec_component_schemas = (
        SysDeptPostSchema,
        SysDeptResponseSchema,
        SysDeptUserPostSchema,
        SysDeptUsersResponseSchema,
    )

    @expose(url="/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_list(self) -> Response:
        """
        ---
        get:
          description: 获取组织信息，需组织管理菜单权限
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
                            type: array
                            items:
                                $ref: '#/components/schemas/SysDeptResponseSchema'
        """
        data = SysDeptDataCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DEPT,
        log_to_statsd=False,
    )
    @requires_json
    def add(self) -> Response:
        """
        ---
        post:
          description: 新增组织，需组织管理菜单权限
          requestBody:
            description: pid(父组织ID)
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/SysDeptPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = SysDeptPostSchema().load(request.json)
        dept = CreateSysDeptCommand(g.user, item).run()
        return self.format_response(200, data=dept.to_json())

    @expose(url="/<int:dept_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_DEPT,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, dept_id: int) -> Response:
        """
        ---
        put:
          description: 编辑组织，需组织管理菜单权限
          parameters:
          - in: path
            schema:
              type: integer
            name: dept_id
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/SysDeptPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = SysDeptPostSchema().load(request.json)
        dept = UpdateSysDeptCommand(g.user, dept_id, item).run()
        return self.format_response(200, data=dept.to_json())

    @expose("/<int:dept_id>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_DEPT,
        log_to_statsd=False,
    )
    def delete(self, dept_id: int) -> Response:
        """
        ---
        delete:
          description: 删除组织，需组织管理菜单权限
          parameters:
          - in: path
            schema:
              type: integer
            name: dept_id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        DeleteSysDeptCommand(g.user, dept_id).run()
        return self.format_response(200)

    @expose(url="/<int:dept_id>/users/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_user_list(self, dept_id: int) -> Response:
        """
        ---
        get:
          description: 获取当前组织用户，需组织管理菜单权限
          parameters:
          - in: path
            schema:
              type: integer
            name: dept_id
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
                            type: array
                            items:
                              type: object
                              properties:
                                id:
                                  type: integer
                                username:
                                  type: string
        """
        data = SysDeptUsersDataCommand(g.user, dept_id).run(**request.args)
        return self.format_response(200, data=data)

    @expose(url="/<int:dept_id>/users/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DEPT_USERS,
        log_to_statsd=False,
    )
    @requires_json
    def add_users(self, dept_id: int) -> Response:
        """
        ---
        post:
          description: 添加组织用户，需组织管理菜单权限
          parameters:
          - in: path
            schema:
              type: integer
            name: dept_id
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/SysDeptUserPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = SysDeptUserPostSchema().load(request.json)
        CreateSysDeptUsersCommand(g.user, dept_id, item).run()
        return self.format_response(200)

    @expose(url="/<int:dept_id>/users/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_DEPT_USERS,
        log_to_statsd=False,
    )
    @requires_json
    def delete_users(self, dept_id: int) -> Response:
        """
        ---
        delete:
          description: 删除组织用户，需组织管理菜单权限
          parameters:
          - in: path
            schema:
              type: integer
            name: dept_id
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/SysDeptUserPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = SysDeptUserPostSchema().load(request.json)
        DeleteSysDeptUsersCommand(g.user, dept_id, item).run()
        return self.format_response(200)
