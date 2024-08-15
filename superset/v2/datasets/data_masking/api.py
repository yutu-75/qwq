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
import simplejson
from flask import Response, request, g
from flask_appbuilder.api import expose
from simplejson import JSONDecodeError

from superset import event_logger
from superset.exceptions import HTTPError
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.datasets.data_masking.commands.get_data_command import \
    DatasetMaskingRuleListCommand, MaskingRuleCommand
from superset.v2.datasets.data_masking.commands.update import \
    UpdateMaskingRuleCommand
from superset.v2.datasets.data_masking.schemas import DataMaskingPutDataSchema
from superset.views.base_api import statsd_metrics, BaseSupersetBaseApi


class DataMaskingApi(BaseSupersetBaseApi):
    resource_name = "data/masking"
    openapi_spec_component_schemas = (
        DataMaskingPutDataSchema,
    )

    @expose(url="/reg/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_reg(self) -> Response:
        """
        获取所有定义的脱敏规则
        ---
        get:
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = [
            {
                "id": 1,
                "name": '电话号码脱敏',
                "pattern": r'^(\d{3})\d{4}(\d{4})$',
                "repl": r'\1****\2'
            },
            {
                "id": 2,
                "name": '身份证号码脱敏',
                "pattern": r'^(.{6})(?:\d+)(.{4})$',
                "repl": r'\1******\2'
            }
        ]
        return self.format_response(200, data=data)

    @expose(url="/dataset/<int:dataset_id>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_list(self, dataset_id: int) -> Response:
        """
        查询数据集所有字段,需拥有此数据集行列权限
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
        data = DatasetMaskingRuleListCommand(g.user, dataset_id).run()
        return self.format_response(200, data=data)

    @expose(url="/<int:column_id>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_rls(self, column_id: int) -> Response:
        """
        查询详细脱敏规则,需拥有此数据集行列权限
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
        data = MaskingRuleCommand(g.user, column_id).run()
        return self.format_response(200, data=data)

    @expose("/<int:column_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_MASKING_RULE,
        log_to_statsd=False,
    )
    def put(self, column_id: int) -> Response:
        """
        ---
        put:
          description: 编辑数据集脱敏规则,需拥有此数据集行列权限
          parameters:
          - in: path
            schema:
              type: integer
            name: column_id
            description: 字段ID
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DataMaskingPutDataSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        try:
            data = request.get_data().decode().strip()
            data.replace("\\", '\\\\')
            data = simplejson.loads(data)
        except JSONDecodeError:
            raise HTTPError(r"使用反斜杠时，请使用双反斜杠替换", 400)

        item = DataMaskingPutDataSchema().load(data)
        model = UpdateMaskingRuleCommand(g.user, column_id, item).run()
        return self.format_response(200, data=model.to_json())
