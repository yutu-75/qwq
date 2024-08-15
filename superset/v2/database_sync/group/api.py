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

from superset import event_logger, app
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.database_sync.group.commands.create import \
    CreateDatabaseSyncGroupCommand
from superset.v2.database_sync.group.commands.delete import \
    DeleteDatabaseSyncGroupCommand
from superset.v2.database_sync.group.commands.get_data_command import \
    DatabaseSyncGroupDataCommand, DatabaseSyncGroupTreeCommand
from superset.v2.database_sync.group.commands.update import \
    UpdateDatabaseSyncGroupCommand
from superset.v2.database_sync.group.schemas import DatabaseSyncGroupSearchSchema, \
    DatabaseSyncGroupPutSchema, DatabaseSyncGroupSchema, DatabaseSyncGroupPostSchema

from superset.views.base_api import (
    requires_json,
    statsd_metrics, BaseSupersetBaseApi
)

config = app.config
logger = logging.getLogger(__name__)


class DatabaseSyncGroupRestApi(BaseSupersetBaseApi):
    resource_name = "database_sync/group"
    openapi_spec_component_schemas = (
        DatabaseSyncGroupSchema,
    )

    @expose(url="/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """Response
        ---
        get:
          description: 查询 database_sync group 列表
          parameters:
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
            name: type_
            description: 类型
            schema:
              type: int
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
                    $ref: '#/components/schemas/DatabaseSyncGroupSchema'
        """
        item = DatabaseSyncGroupSearchSchema().load(request.args)
        data = DatabaseSyncGroupDataCommand(g.user).run(**item)
        return self.format_response(200, data=data)

    @expose(url="/tree/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_tree(self) -> Response:
        """Response
        ---
        get:
          description: 查询分组树
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/DatabaseSyncGroupSchema'
        """
        data = DatabaseSyncGroupTreeCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DATABASE_SYNC_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """Response
        ---
        post:
          description: 新增 database_sync group,需当前用户拥有父级分组管理以上权限
          requestBody:
            description: database_sync_group schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatabaseSyncGroupSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DatabaseSyncGroupPostSchema().load(request.json)
        CreateDatabaseSyncGroupCommand(g.user, item).run()
        return self.format_response(200)

    @expose(url="/<int:group_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_DATABASE_SYNC_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, group_id: int) -> Response:
        """Response
        ---
        put:
          description: 修改 database_sync group,需当前用户拥有此分组管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: group_id
            description: The database_sync group id
          requestBody:
            description: database_sync group schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatabaseSyncGroupSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DatabaseSyncGroupPutSchema().load(request.json)
        UpdateDatabaseSyncGroupCommand(g.user, group_id, item).run()
        return self.format_response(200)

    @expose(url="/<int:group_id>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_DATABASE_SYNC_GROUP,
        log_to_statsd=False,
    )
    def delete(self, group_id: int) -> Response:
        """Response
        ---
        delete:
          description: 删除 database_sync group,需当前用户拥有此分组管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: group_id
            description: The database_sync group id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        DeleteDatabaseSyncGroupCommand(g.user, group_id).run()
        return self.format_response(200)







