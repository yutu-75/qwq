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
@Time       : 2023/7/4 17:20
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
from json.decoder import JSONDecodeError

from flask import Response, g, request
from flask_appbuilder.api import expose

from superset import event_logger
from superset.exceptions import HTTPError
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.datasources.api_datasources.commands.get_data_command import (
    APIDataSourceListCommand,
    APIDataSourceTableListCommand,
    APIDataSourceCommand,
    TokenAPIListCommand,
)
from superset.v2.datasources.api_datasources.commands.create import (
    CreateApiDataSourceCommand,
)
from superset.v2.datasources.api_datasources.commands.update import (
    UpdateApiDataSourceCommand
)
from superset.v2.datasources.api_datasources.schemas import (
    ApiDataSourcePostSchema,
    ApiDataSourceTestSchema,
    ApiDataSourcePutSchema,
    APIDataSourceListResponseSchema,
    APIDataSourceTableSchema,
    ApiTablePostSchema,
    TokenAPIListResponseSchema,
)
from superset.v2.utils.data_save_db import api_data_to_df, get_dynamic_token
from superset.v2.utils.req_utils import req
from superset.views.base_api import (
    BaseSupersetBaseApi,
    statsd_metrics,
    requires_json
)


class APIDataSourcesRestApi(BaseSupersetBaseApi):
    resource_name = "datasource/api"
    openapi_spec_component_schemas = (
        APIDataSourceListResponseSchema,
        ApiDataSourceTestSchema,
        ApiDataSourcePostSchema,
        ApiDataSourcePutSchema,
        APIDataSourceTableSchema,
        ApiTablePostSchema,
        TokenAPIListResponseSchema,
    )

    @expose(url="/<int:datasource_id>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_info(self, datasource_id: int) -> Response:
        """
        ---
        get:
          description: 查询API数据源信息，需要此数据源拥有查询以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: datasource_id
            description: 数据源ID
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/ApiDataSourcePostSchema'
        """
        data = APIDataSourceCommand(g.user, datasource_id).run()
        return self.format_response(200, data=data)

    @expose(url="/list/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_list(self) -> Response:
        """
        ---
        get:
          description: 查询API数据源列表
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/APIDataSourceListResponseSchema'
        """
        data = APIDataSourceListCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/token_tables/list/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def toekn_api_list(self) -> Response:
        """
        ---
        get:
          description: 查询TOKEN API数据源列表
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/TokenAPIListResponseSchema'
        """
        data = TokenAPIListCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/<int:datasource_id>/tables/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def table_list(self, datasource_id: int) -> Response:
        """
        ---
        get:
          description: 查询当前API数据源包含的tables
          parameters:
          - in: path
            schema:
              type: integer
            name: datasource_id
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: array
                    items:
                      $ref: '#/components/schemas/APIDataSourceTableSchema'
        """
        data = APIDataSourceTableListCommand(g.user, datasource_id).run()
        return self.format_response(200, data=data)

    @expose(url="/test/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @requires_json
    def test(self) -> Response:
        """
        ---
        post:
          description: 测试api是否能正常请求
          requestBody:
            description:
              "
                'url: url'<br>
                'method: get/post'<br>
                'headers: headers'<br>
                'params: query参数'<br>
                'data: body参数'<br>
                'token_api: {key: str, value: {api_table_id: 1, name: str}}'<br>
              "
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ApiDataSourceTestSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = ApiDataSourceTestSchema().load(request.json)
        item = get_dynamic_token(item)
        data, headers = req(item, response_headers=True)
        return self.format_response(200, data={
            "headers": headers,
            "result": data,
        })

    @expose(url="/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_API_DATA_SOURCE,
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """
        ---
        post:
          description: 新增api数据源，需要此数据源分组拥有管理以上权限
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ApiDataSourcePostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = ApiDataSourcePostSchema().load(request.json)
        datasource = CreateApiDataSourceCommand(g.user, item).run()
        return self.format_response(200, data=datasource.to_json())

    @expose(url="/<int:datasource_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_API_DATA_SOURCE,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, datasource_id: int) -> Response:
        """编辑api数据源
        ---
        put:
          description: 编辑api数据源
          parameters:
          - in: path
            schema:
              type: integer
            name: datasource_id
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ApiDataSourcePutSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = ApiDataSourcePutSchema().load(request.json)
        datasource = UpdateApiDataSourceCommand(
            g.user, datasource_id, item
        ).run()
        return self.format_response(200, data=datasource.to_json())

    @expose(url="/preview/", methods=["POST"])
    @authenticated()
    @statsd_metrics
    @requires_json
    def preview(self) -> Response:
        """预览将保存的API数据
        ---
        post:
          description:
            "
            'columns': {field_name: rename}, 选择的字段<br>
            'record_path': str 或者 list of str, 默认 None，每个对象中指向记录列表的路径，
              如果未传递，则假定数据是一个记录数组<br>
            'meta': list of paths (str or list of str), 默认 None，
              要用作结果表中每个记录的元数据的字段
            "
          parameters:
            - in: query
              name: limit
              description: 数据条数
              schema:
                type: integer
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ApiTablePostSchema'

          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = ApiTablePostSchema().load(request.json)
        df = api_data_to_df(item["configuration"], item["data_path"])
        if df is None:
            raise HTTPError('Request failed or no permission', 400)

        limit = request.args.get('limit', 10)
        df = df.head(int(limit))
        return self.format_response(200, data=df.to_dict(orient="records"))
