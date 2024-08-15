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
@Time       : 2023/5/15 17:59
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask import Response, request, g
from flask_appbuilder.api import expose

from superset import event_logger
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.datasets.rls_filter.commands.create import CreateRLSDataCommand
from superset.v2.datasets.rls_filter.commands.delete import \
    DeleteRLSFilterCommand
from superset.v2.datasets.rls_filter.commands.get_data_command import \
    RLSFilterDataCommand, DatasetRLSFilterDataCommand
from superset.v2.datasets.rls_filter.commands.update import \
    UpdateRLSFilterCommand, ChangeRLSFilterStatusCommand
from superset.v2.datasets.rls_filter.schemas import RLSPostDataSchema, \
    RLSPutDataSchema, ChangeRLSStatusSchema
from superset.views.base_api import statsd_metrics, requires_json, \
    BaseSupersetBaseApi


class DatasetRLSFilterApi(BaseSupersetBaseApi):
    resource_name = "dataset/rls"
    openapi_spec_component_schemas = (
        RLSPutDataSchema,
        RLSPostDataSchema,
        ChangeRLSStatusSchema
    )

    @expose(url="/<int:dataset_id>/list/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_list(self, dataset_id: int) -> Response:
        """
        查询数据集行级权限,需拥有此数据集行列权限
        ---
        get:
          parameters:
          - in: path
            schema:
              type: integer
            name: dataset_id
            description: 数据集ID
          - in: query
            schema:
              type: integer
            name: page
            default: 1
            description: 页数
          - in: query
            schema:
              type: integer
            name: limit
            default: 20
            description: 每页条数
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 20))
        comand = DatasetRLSFilterDataCommand(g.user, dataset_id)
        data = comand.run(page=page, limit=limit)
        return self.format_response(200, data=data)

    @expose(url="/<int:rls_id>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_rls(self, rls_id: int) -> Response:
        """
        查询行级权限详细信息,需拥有此数据集行列权限
        ---
        get:
          parameters:
          - in: path
            schema:
              type: integer
            name: rls_id
            description: 行级权限ID
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = RLSFilterDataCommand(g.user, rls_id).run()
        return self.format_response(200, data=data)

    @expose("/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_RLS,
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """
        ---
        post:
          description: 新增数据集行级权限,需拥有此数据集行列权限
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/RLSPostDataSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = RLSPostDataSchema().load(request.json)
        data = CreateRLSDataCommand(g.user, item).run()
        return self.format_response(200, data=data)

    @expose("/<int:rls_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_RLS,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, rls_id: int) -> Response:
        """
        ---
        put:
          description: 编辑数据集行级权限,需拥有此数据集行列权限
          parameters:
          - in: path
            schema:
              type: integer
            name: rls_id
            description: 行级权限ID
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/RLSPutDataSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = RLSPutDataSchema().load(request.json)
        data = UpdateRLSFilterCommand(g.user, rls_id, item).run()
        return self.format_response(200, data=data.to_json())

    @expose("/<int:rls_id>/", methods=("PATCH",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_COLSE_RLS,
        log_to_statsd=False,
    )
    @requires_json
    def patch(self, rls_id: int) -> Response:
        """关闭行级过滤
        ---
        patch:
          description: 关闭行级过滤
          parameters:
          - in: path
            schema:
              type: integer
            name: rls_id
            description: 行级权限ID
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ChangeRLSStatusSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = ChangeRLSStatusSchema().load(request.json)
        data = ChangeRLSFilterStatusCommand(g.user, rls_id, item).run()
        return self.format_response(200, data=data.to_json())

    @expose(url="/<int:rls_id>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_RLS,
        log_to_statsd=False,
    )
    def delete(self, rls_id: int) -> Response:
        """删除行级权限,需拥有此数据集行列权限
        ---
        delete:
          parameters:
          - in: path
            schema:
              type: integer
            name: rls_idrls_id
            description: 行级权限ID
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        DeleteRLSFilterCommand(g.user, rls_id).run()
        return self.format_response(200)
