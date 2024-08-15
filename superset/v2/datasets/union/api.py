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
@Time       : 2023/7/12 15:32
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging

from flask import g, request, Response
from flask_appbuilder.api import expose

from superset import event_logger

from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.datasets.union.commands.create import CreateUnionDatasetCommand
from superset.v2.datasets.union.commands.get_data_command import \
    TestUnionDatasetCommand, UnionDatasetInfoCommand
from superset.v2.datasets.union.commands.update import UpdateUnionDatasetCommand
from superset.v2.datasets.union.schemas import (
    UnionDatasetSchema,
    UnionDatasetPostSchema,
    UnionDatasetPutSchema,
)

from superset.views.base_api import (
    requires_json,
    statsd_metrics, BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class UnionDatasetRestApi(BaseSupersetBaseApi):
    resource_name = "dataset/union"
    openapi_spec_component_schemas = (
        UnionDatasetSchema,
        UnionDatasetPostSchema,
        UnionDatasetPutSchema,
    )

    @expose(url="/<int:dataset_id>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self, dataset_id: int) -> Response:
        """Response
        查询关联数据集
        ---
        get:
          parameters:
            - in: path
              schema:
                type: integer
              name: dataset_id
              description: 数据集id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = UnionDatasetInfoCommand(g.user, dataset_id).run()
        return self.format_response(200, data=data)

    @expose("/test/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @requires_json
    def test(self) -> Response:
        """
        ---
        post:
          description: 预览关联数据集数据
          parameters:
          - in: query
            name: limit
            description: 数据行数， 默认20
            schema:
              type: integer
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UnionDatasetSchema'
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      sql:
                        type: string
                      schema:
                        type: string
                      database_id:
                        type: string
                      label_columns:
                        type: object
                      data:
                       type: array
        """
        item = UnionDatasetSchema().load(request.json)
        data = TestUnionDatasetCommand(g.user, item).run(**request.args)
        return self.format_response(200, data=data)

    @expose("/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @requires_json
    def post(self) -> Response:
        """
        ---
        post:
          description: 新增关联数据集数据
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UnionDatasetPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = UnionDatasetPostSchema().load(request.json)
        union_detail = item.pop('union_detail')
        command = TestUnionDatasetCommand(g.user, union_detail)
        res = command.run(limit=1)
        item['schema'] = res['schema']
        item['sql'] = res['sql']
        item['label_columns'] = res['label_columns']
        item['database_id'] = res['database_id']
        data = CreateUnionDatasetCommand(g.user, item).run()
        event_logger.log_with_context(
            action=LogsMessages.LM_ADD_UNION_DATASET,
            name=data.custom_name,
        )
        return self.format_response(200, data=data.to_json())

    @expose("/<int:dataset_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    def put(self, dataset_id: int) -> Response:
        """
        ---
        put:
          description: 编辑关联数据集
          parameters:
          - in: path
            name: dataset_id
            description: 数据集id
            schema:
              type: integer
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UnionDatasetPutSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = UnionDatasetPutSchema().load(request.json)
        union_detail = item.pop('union_detail')
        command = TestUnionDatasetCommand(g.user, union_detail)
        res = command.run(limit=1)
        item['schema'] = res['schema']
        item['sql'] = res['sql']
        item['label_columns'] = res['label_columns']
        item['database_id'] = res['database_id']
        dataset = UpdateUnionDatasetCommand(g.user, dataset_id, item).run()
        event_logger.log_with_context(
            action=LogsMessages.LM_EDIT_DATASET,
            name=dataset.custom_name,
        )
        return self.format_response(200, data=dataset.to_json())
