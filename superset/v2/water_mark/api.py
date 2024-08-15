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
from superset.v2.water_mark.commands.get_data_command import WaterMarkV2GetCommand
from superset.v2.water_mark.commands.update import UpdateWaterMarkV2Command
from superset.v2.water_mark.schemas import WaterMarkV2GetSchema, WaterMarkV2PutSchema
from superset.views.base_api import (
    requires_json,
    statsd_metrics,
    BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class WaterMarkV2RestApi(BaseSupersetBaseApi):
    resource_name = "water_mark"
    openapi_spec_component_schemas = (
        WaterMarkV2GetSchema,
        WaterMarkV2PutSchema,
    )

    @expose("/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """Response
        ---
        get:
          description: >-
            查询水印配置
          responses:
            200:
              description: 水印配置
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/WaterMarkV2GetSchema'
        """
        data = WaterMarkV2GetCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose("/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_WATER_MARK,
        log_to_statsd=False,
    )
    @requires_json
    def put(self) -> Response:
        """
        ---
        put:
          description: 编辑水印配置
          requestBody:
            description: 水印配置
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/WaterMarkV2PutSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = WaterMarkV2PutSchema().load(request.json)
        UpdateWaterMarkV2Command(g.user, item).run()
        return self.format_response(200)
