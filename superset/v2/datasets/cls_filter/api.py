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
from superset.v2.datasets.cls_filter.commands.get_data_command import \
    CLSFilterDataCommand, DatasetCLSFilterDataCommand
from superset.v2.datasets.cls_filter.commands.update import \
    UpdateCLSFilterCommand
from superset.v2.datasets.cls_filter.schemas import CLSPutDataSchema
from superset.views.base_api import statsd_metrics, requires_json, \
    BaseSupersetBaseApi


class DatasetCLSFilterApi(BaseSupersetBaseApi):
    resource_name = "dataset/cls"
    openapi_spec_component_schemas = (
        CLSPutDataSchema,
    )

    @expose(url="/<int:dataset_id>/list/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_list(self, dataset_id: int) -> Response:
        """
        查询数据集所有字段权限,需拥有此数据集行列权限
        ---
        get:
          parameters:
          - in: path
            schema:
              type: integer
            name: dataset_id
            description: 数据集ID
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = DatasetCLSFilterDataCommand(g.user, dataset_id).run()
        return self.format_response(200, data=data)

    @expose(url="/<int:column_id>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_rls(self, column_id: int) -> Response:
        """
        查询列级权限详细信息,需拥有此数据集行列权限
        ---
        get:
          parameters:
          - in: path
            schema:
              type: integer
            name: column_id
            description: 列ID
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = CLSFilterDataCommand(g.user, column_id).run()
        return self.format_response(200, data=data)

    @expose("/<int:column_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_CLS,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, column_id: int) -> Response:
        """
        ---
        put:
          description: 编辑数据集列级权限,需拥有此数据集行列权限
          parameters:
          - in: path
            schema:
              type: integer
            name: column_id
            description: 列级权限ID
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/CLSPutDataSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = CLSPutDataSchema().load(request.json)
        UpdateCLSFilterCommand(g.user, column_id, item).run()
        return self.format_response(200)
