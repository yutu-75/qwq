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
from superset.utils.decorators import authenticated
from superset.v2.datasources.group.commands.create import CreateDataSourceGroupCommand
from superset.v2.datasources.group.commands.delete import \
    DeleteDataSourceGroupCommand
from superset.v2.datasources.group.commands.get_data_command import \
    DataSourceGroupDataCommand, DataSourceGroupTreeCommand
from superset.v2.datasources.group.commands.update import \
    UpdateDataSourceGroupCommand
from superset.v2.datasources.group.schemas import (
    DataSourceGroupPostSchema,
    DataSourceGroupResponseSchema
)
from superset.views.base_api import (
    BaseSupersetBaseApi,
    statsd_metrics,
    requires_json
)


class DataSourcesGroupRestApi(BaseSupersetBaseApi):
    resource_name = "datasource/group"
    openapi_spec_component_schemas = (
        DataSourceGroupPostSchema,
    )

    @expose(url="/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_list(self) -> Response:
        """Response
        Returns all datasource info.
        ---
        get:
          description: 获取数据源分组列表
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
                            $ref: '#/components/schemas/SysDeptResponseSchema'
        """
        data = DataSourceGroupDataCommand(g.user).run(**request.args)
        return self.format_response(200, data=data)

    @expose(url="/tree/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_tree(self) -> Response:
        """
        ---
        get:
          description: 获取数据源分组树
          parameter:
          - in:
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
                            $ref: '#/components/schemas/SysDeptResponseSchema'
        """
        data = DataSourceGroupTreeCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DATA_SOURCE_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def add(self) -> Response:
        """
        ---
        post:
          description: >-
             新增数据源,需要用户拥有当前分组管理以上权限
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DataSourceGroupPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DataSourceGroupPostSchema().load(request.json)
        group = CreateDataSourceGroupCommand(g.user, item).run()
        return self.format_response(201, data=group.to_json())

    @expose(url="/<int:group_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_DATA_SOURCE_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, group_id: int) -> Response:
        """
        ---
        post:
          description: 修改数据源分组信息,需要用户拥有此数据源管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: group_id
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DataSourcePostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DataSourceGroupResponseSchema().load(request.json)
        group = UpdateDataSourceGroupCommand(g.user, group_id, item).run()
        return self.format_response(200, data=group.to_json())

    @expose("/<int:group_id>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_DATABASE,
        log_to_statsd=False,
    )
    def delete(self, group_id: int) -> Response:
        """Delete a datasource group
        ---
        delete:
          description: 删除 a datasource group,需要用户拥有此数据源管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: group_id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        DeleteDataSourceGroupCommand(g.user, group_id).run()
        return self.format_response(200)
