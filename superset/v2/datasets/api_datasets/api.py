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
@Time       : 2023/7/12 12:54
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging

from croniter import croniter
from flask import g, request, Response
from flask_appbuilder.api import expose

from superset import event_logger
from superset.exceptions import HTTPError
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.datasets.api_datasets.commands.create import \
    CreateAPIDatasetCommand, CreateAPIDatasetTaskCommand, RunAPIDatasetTaskCommand
from superset.v2.datasets.api_datasets.commands.delete import DeleteDatasetTaskCommand
from superset.v2.datasets.api_datasets.commands.get_data_command import \
    APITableDataCommand, DatasetTaskListCommand, DatasetTaskLogInfoCommand
from superset.v2.datasets.api_datasets.commands.update import UpdateDatasetTaskCommand
from superset.v2.datasets.api_datasets.schemas import APIDatasetPostSchema, \
    APITableTaskPostSchema

from superset.views.base_api import (
    requires_json,
    statsd_metrics,
    BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class APIDatasetRestApi(BaseSupersetBaseApi):
    resource_name = "dataset/api"
    openapi_spec_component_schemas = (
        APIDatasetPostSchema,
        APITableTaskPostSchema,
    )

    @authenticated()
    @statsd_metrics
    @expose("/<int:api_table_id>/preview/", methods=("GET",))
    def get_data(self, api_table_id: int):
        """Response
        ---
        get:
          description: >-
            预览api数据集内容,需当前用户拥有此数据集查看以上权限
          parameters:
            - in: path
              schema:
                type: integer
              name: api_table_id
              description: api数据源表id
            - in: query
              schema:
                type: string
              name: limit
              description: 限制
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = APITableDataCommand(g.user, api_table_id).run(**request.args)
        return self.format_response(200, data=data)

    @expose("/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @requires_json
    def post(self) -> Response:
        """
        ---
        post:
          description: 新增API数据集，须校验当前用户是否拥有此分组的管理以上权限和数据集查看以上权限
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/APIDatasetPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = APIDatasetPostSchema().load(request.json)
        dataset = CreateAPIDatasetCommand(g.user, item).run()
        event_logger.log_with_context(
            action=LogsMessages.LM_ADD_API_DATASET,
            name=dataset.custom_name,
        )
        return self.format_response(200)

    @authenticated()
    @statsd_metrics
    @expose("/task/<int:table_id>/", methods=("GET",))
    def get_task(self, table_id: int):
        """Response
        ---
        get:
          description: 查询数据集任务信息
          parameters:
          - in: path
            schema:
              type: integer
            name: table_id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = DatasetTaskListCommand(g.user, table_id).run(**request.args)
        return self.format_response(200, data=data)

    @expose("/<int:table_id>/task", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_API_DATASET_TASK,
        log_to_statsd=True,
    )
    @requires_json
    def post_task(self, table_id: int) -> Response:
        """
        ---
        post:
          description: 新增API数据集任务，须校验当前用户是否拥有数据集管理以上权限<br>
            update_type(APPEND/REPLACE)<br>
            rate(0(立即执行)/1（cron）/2(简单配置))
          parameters:
          - in: path
            schema:
              type: integer
            name: table_id
            description: 数据集ID
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/APITableTaskPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = APITableTaskPostSchema().load(request.json)
        if item.get('cron', None) and not croniter.is_valid(str(item["cron"])):
            raise HTTPError("请检查cron表达式是否正确", 400)
        model = CreateAPIDatasetTaskCommand(g.user, table_id, item).run()
        return self.format_response(200, data=model.to_json())

    @expose("/task/<int:table_task_id>/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @requires_json
    def run_task(self, table_task_id: int) -> Response:
        """
        ---
        post:
          description: 立即执行
          parameters:
          - in: path
            schema:
              type: integer
            name: table_task_id
            description: 数据集任务ID
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        model = RunAPIDatasetTaskCommand(g.user, table_task_id).run()
        return self.format_response(200, data=model.to_json())

    @expose(url="/task/<int:table_task_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_API_DATASET_TASK,
        log_to_statsd=False,
    )
    @requires_json
    def put_task(self, table_task_id: int) -> Response:
        """Response
        ---
        put:
          description: 修改api dataset任务,需当前用户拥有此数据集管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: table_task_id
          requestBody:
            description: dataset group schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/APITableTaskPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = APITableTaskPostSchema().load(request.json)
        if item.get('cron', None) and not croniter.is_valid(str(item["cron"])):
            raise HTTPError("请检查cron表达式是否正确", 400)
        model = UpdateDatasetTaskCommand(g.user, table_task_id, item).run()
        return self.format_response(200, data=model.to_json())

    @expose(url="/task/<int:table_task_id>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_API_DATASET_TASK,
        log_to_statsd=False,
    )
    def delete_task(self, table_task_id: int) -> Response:
        """Response
        ---
        delete:
          description: 删除 API数据集任务,需当前用户拥有此分组管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: table_task_id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        DeleteDatasetTaskCommand(g.user, table_task_id).run()
        return self.format_response(200)

    @authenticated()
    @statsd_metrics
    @expose("/task/<int:table_task_id>/log/", methods=("GET",))
    def get_task_log(self, table_task_id: int):
        """Response
        ---
        get:
          description: 查询数据集任务日志
          parameters:
          - in: path
            schema:
              type: integer
            name: table_task_id
          - in: query
            schema:
              type: integer
            name: page
          - in: query
            schema:
              type: integer
            name: limit
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = DatasetTaskLogInfoCommand(g.user, table_task_id).run(**request.args)
        return self.format_response(200, data=data)
