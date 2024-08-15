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

# -*- coding: utf-8 -*-

"""
@Time       : 2023/7/18 14:50
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask import Response, g, request
from flask_babel import gettext as _
from flask_appbuilder.api import expose
from flask_appbuilder.security.decorators import protect, permission_name
from marshmallow import ValidationError

from superset import event_logger
from superset.datasource.api_datasource.commands.create import \
    CreateApiDataSourceCommand
from superset.datasource.api_datasource.commands.get_data_command import \
    APIDataSourceInfoCommand, APIDataSourceListCommand, APIDataSourceTableListCommand
from superset.datasource.api_datasource.commands.update import \
    UpdateApiDataSourceCommand
from superset.datasource.api_datasource.schemas import ApiDataSourceTestSchema, \
    ApiDataSourcePostSchema, ApiDataSourcePutSchema, APIDataSourceTableSchema, \
    ApiTablePostSchema, APIDataSourceListResponseSchema
from superset.utils.pd import api_data_to_df
from superset.utils.requests import req

from superset.views.base_api import (
    statsd_metrics,
    requires_json,
    BaseSupersetApi
)


class APIDataSourcesRestApi(BaseSupersetApi):
    resource_name = "datasource/api"
    allow_browser_login = True
    class_permission_name = "Dashboard"
    openapi_spec_component_schemas = (
        ApiDataSourceTestSchema,
        ApiDataSourcePostSchema,
        ApiDataSourcePutSchema,
        APIDataSourceTableSchema,
        ApiTablePostSchema,
        APIDataSourceListResponseSchema,
    )

    @expose(url="/<int:datasource_id>/", methods=["GET"])
    @protect()
    @statsd_metrics
    @permission_name('read')
    def get(self, datasource_id: int) -> Response:
        """
        ---
        get:
          description: 查询API数据源信息
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
                      $ref: '#/components/schemas/ApiDataSourcePostSchema'
        """
        data = APIDataSourceInfoCommand(g.user, datasource_id).run()
        return self.response(200, result=data)

    @expose(url="/test/", methods=["POST"])
    @protect()
    @statsd_metrics
    @requires_json
    @permission_name('read')
    def test(self) -> Response:
        """
        ---
        post:
          description: 测试api是否能正常请求
          requestBody:
            description:
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
        data = req(item)
        if data is None:
            raise self.response_400(_('Request failed or no permission'))

        return self.response(200, result=data)

    @expose(url="/preview/", methods=["POST"])
    @protect()
    @statsd_metrics
    @requires_json
    @permission_name('read')
    def preview(self) -> Response:
        """预览将保存的API数据
        ---
        post:
          description:
            columns: {field_name: rename}
            record_path: str 或者 list of str, 默认 None，每个对象中指向记录列表的路径，
              如果未传递，则假定数据是一个记录数组<br>
            meta: list of paths (str or list of str), 默认 None，
              要用作结果表中每个记录的元数据的字段
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
        try:
            item = ApiTablePostSchema().load(request.json)
        except ValidationError as error:
            return self.response_400(message=error.messages)

        try:
            df = api_data_to_df(item["configuration"], item["data_path"])
        except Exception as ex:
            return self.response_400(_('Data parsing error.'))

        if df is None:
            return self.response_400(_('Request failed or no permission'))

        limit = request.args.get('limit', 10)
        df = df.head(limit)
        return self.response(200, result=df.to_dict(orient="records"))

    @expose(url="/", methods=["POST"])
    @protect()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.post",
        log_to_statsd=False,
    )
    @requires_json
    @permission_name('read')
    def post(self) -> Response:
        """新增api数据源
        ---
        post:
          description:
          requestBody:
            description: d_type = api
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ApiDataSourcePostSchema'

          responses:
            200:
              $ref: '#/components/responses/200'
        """
        try:
            item = ApiDataSourcePostSchema().load(request.json)
        except ValidationError as error:
            return self.response_400(message=error.messages)

        datasource = CreateApiDataSourceCommand(g.user, item).run()
        return self.response(200, result=datasource.to_json())

    @expose(url="/<int:datasource_id>/", methods=("PUT",))
    @protect()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.put",
        log_to_statsd=False,
    )
    @requires_json
    @permission_name('read')
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
        try:
            item = ApiDataSourcePutSchema().load(request.json)
        except ValidationError as error:
            return self.response_400(message=error.messages)

        datasource = UpdateApiDataSourceCommand(
            g.user, datasource_id, item
        ).run()
        return self.response(200, result=datasource.to_json())

    @expose(url="/", methods=["GET"])
    @protect()
    @statsd_metrics
    @permission_name('read')
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
        return self.response(200, result=data)

    @expose(url="/<int:datasource_id>/tables/", methods=["GET"])
    @protect()
    @statsd_metrics
    @permission_name('read')
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
        return self.response(200, result=data)
