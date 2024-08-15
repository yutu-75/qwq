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

from superset import event_logger
from superset.utils.decorators import authenticated
from superset.v2.log.commands.get_data_command import LogV2ListCommand, LogV2InfoCommand
from superset.v2.log.schemas import LogV2GetResponseSchema, LogV2SearchSchema, \
    LogPostSchema
from superset.views.base_api import (
    statsd_metrics,
    BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class LogV2RestApi(BaseSupersetBaseApi):
    resource_name = "log"
    openapi_spec_component_schemas = (
        LogV2GetResponseSchema,
        LogPostSchema
    )

    @expose("/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """Response
        ---
        get:
          description: >-
            查询日志列表
          parameters:
            - in: query
              schema:
                type: string
              name: page_size
              description: 页大小
            - in: query
              schema:
                type: string
              name: page_index
              description: 页码
            - in: query
              schema:
                type: string
              name: user_id
              description: 用户id
            - in: query
              schema:
                type: string
              name: action
              description: 操作名
            - in: query
              schema:
                type: string
              name: dttm_start
              description: 开始时间
            - in: query
              schema:
                type: string
              name: dttm_end
              description: 结束时间
          responses:
            200:
              description: Log
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/LogV2GetResponseSchema'
        """
        item = LogV2SearchSchema().load(request.args)
        data = LogV2ListCommand(g.user, item).run()
        return self.format_response(200, data=data)

    @expose("/<pk>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_info(self, pk: str) -> Response:
        """Response
        ---
        get:
          description: >-
            查询日志详细信息
          parameters:
            - in: path
              schema:
                type: string
              name: pk
          responses:
            200:
              description: User
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/LogV2GetResponseSchema'
        """
        data = LogV2InfoCommand(g.user, pk).run()
        return self.format_response(200, data=data)

    @expose("/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    def post(self) -> Response:
        """Response
        ---
        post:
          description: 记录日志
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/LogPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = LogPostSchema().load(request.args)
        event_logger.log_with_context(
            action=item["action"],
            **item["extra"]
        )
        return self.format_response(200)
