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

from superset import event_logger
from superset.datasets_mask.utils import fix_sample_data, get_mask_status
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.datasets.commands.create import (
    CreateDatasetV2Command,
    CreateSQLDatasetCommand,
    CreateFileDatasetCommand,
)
from superset.v2.datasets.commands.delete import DeleteDatasetV2Command
from superset.v2.datasets.commands.get_data_command import (
    DatasetListDataCommand,
    DatasetDataCommand,
    DatasetChartsListCommand,
    FileDataCommand,
    DatasetInfoCommand,
    DatasetTableColumnsDataCommand
)
from superset.v2.datasets.commands.move import MoveDatasetV2Command
from superset.v2.datasets.commands.update import UpdateFileDatasetCommand
from superset.v2.datasets.schemas import (
    DatasetV2PostSchema,
    DatasetV2PutSchema,
    DatasetV2PatchSchema,
    DatasetV2TableColumsPutSchema,
    RelatedDatasetV2PostSchema,
    RelatedDatasetV2PutSchema,
    RelatedDatasetV2PatchSchema,
    SqlLabVizSchema,
    FileDatasetPutSchema,
)
from superset.views.base_api import (
    requires_json,
    statsd_metrics, BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class DatasetV2RestApi(BaseSupersetBaseApi):
    resource_name = "dataset"
    openapi_spec_component_schemas = (
        DatasetV2PostSchema,
        DatasetV2PutSchema,
        DatasetV2PatchSchema,
        DatasetV2TableColumsPutSchema,
        RelatedDatasetV2PostSchema,
        RelatedDatasetV2PutSchema,
        RelatedDatasetV2PatchSchema,
        SqlLabVizSchema,
        FileDatasetPutSchema,
    )

    @expose(url="/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def datasets(self) -> Response:
        """Response
        查询用户有权查看的数据集
        ---
        get:
          description: 查询数据集内容,需当前用户拥有此数据集查看以上权限
          parameters:
            - in: query
              schema:
                type: integer
              name: limit
              description: 行数
            - in: query
              schema:
                type: string
              name: name
              description: 数据集名称
            - in: query
              schema:
                type: integer
              name: database_id
              description: 数据库id
            - in: query
              schema:
                type: string
              name: 'schema'
              description: 数据库名
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = DatasetListDataCommand(g.user).run(**request.args)
        data = fix_sample_data(data, g.user.id)
        return self.format_response(200, data=data)

    @authenticated()
    @statsd_metrics
    @event_logger.log_this
    @expose("/<int:pk>/", methods=("GET",))
    def get_data(self, pk: int):
        """Response
        ---
        get:
          description: >-
            查询数据集内容,需当前用户拥有此数据集查看以上权限
          parameters:
            - in: path
              schema:
                type: integer
              name: pk
              description: 数据集id
            - in: query
              schema:
                type: string
              name: limit
              description: 限制
            - in: query
              schema:
                type: string
              name: force_cached
              description: 是否强制刷新（填写任意字符都为强制刷新，不传此参数为获取缓存）
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = DatasetDataCommand(g.user, pk).run(**request.args)
        data.update({'mark_id': get_mask_status(pk, g.user.id)})
        return self.format_response(200, data=data)

    @authenticated()
    @statsd_metrics
    @event_logger.log_this
    @expose("/<int:pk>/info/", methods=("GET",))
    def get_info(self, pk: int):
        """Response
        ---
        get:
          description: 查询数据集信息,需当前用户拥有此数据集查看以上权限
          parameters:
            - in: path
              schema:
                type: integer
              name: pk
              description: 数据集id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = DatasetInfoCommand(g.user, pk).run()
        return self.format_response(200, data=data)

    @authenticated()
    @statsd_metrics
    @event_logger.log_this
    @expose("/columns/<int:pk>/", methods=("GET",))
    def get_table_columns(self, pk: int):
        """Response
        ---
        get:
          description: >-
            查询数据集,字段信息，需当前用户拥有此数据集查看以上权限
          parameters:
            - in: path
              schema:
                type: string
              name: pk
              description: 数据集id
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = DatasetTableColumnsDataCommand(g.user, pk).run()
        return self.format_response(200, data=data)

    @expose("/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DATASET,
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """
        ---
        post:
          description: 新增数据库数据集
          requestBody:
            description: "type_classify <br>
                          0: 数据库数据集<br>
                          1: SQL数据集<br>
                          2: Excel数据集<br>
                          3: 关联数据集<br>
                          4: API数据集<br>
                          "
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatasetV2PostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DatasetV2PostSchema().load(request.json)
        CreateDatasetV2Command(g.user, item).run()
        return self.format_response(200)

    @expose("/<int:pk>/", methods=("PATCH",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_MOVE_DATASET,
        log_to_statsd=True,
    )
    @requires_json
    def patch(self, pk: int) -> Response:
        """
        ---
        patch:
          description: >-
            将当前数据集移动到目标分组内或者重命名,需当前用户拥有此数据集管理以上权限
          requestBody:
            description: "target_id: 目标ID， new_title: new title"
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatasetV2PatchSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = DatasetV2PatchSchema().load(request.json)
        MoveDatasetV2Command(g.user, pk, item).run()
        return self.format_response(200)

    @expose("/<pk>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    def delete(self, pk: int) -> Response:
        """
        ---
        delete:
          description: >-
            删除 a dataset,需当前用户拥有此数据集管理以上权限
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        dataset = DeleteDatasetV2Command(g.user, pk).run()
        event_logger.log_with_context(
            action=LogsMessages.LM_DEL_DATASET,
            name=dataset.custom_name,
        )
        return self.format_response(200)

    @expose("/<int:dataset_id>/charts/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def pre_delete(self, dataset_id: int) -> Response:
        """
        ---
        get:
          description: 查询数据集关联的所有图表
          parameters:
          - in: path
            schema:
              type: integer
            name: dataset_id
          responses:
            200:
              description: '[] : 没有关联图表'
        """
        data = DatasetChartsListCommand(g.user, dataset_id).run()
        return self.format_response(200, data=data)

    @expose("/sqllab_viz/", methods=["POST"])
    @event_logger.log_this
    @authenticated()
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_SQL_DATASET,
        log_to_statsd=False,
    )
    def sqllab_viz(self) -> Response:
        """Response
        ---
        post:
          description: 保存为SQL数据集
          requestBody:
            description: SqlLabVizSchema schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/SqlLabVizSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = SqlLabVizSchema().load(request.json)
        data = CreateSQLDatasetCommand(g.user, item).run()
        return self.format_response(200, data=data.to_json())

    @expose("/file/data/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    def get_file_data(self) -> Response:
        """
        ---
        post:
          description: 获取文件数据
          requestBody:
            description: 上传EXCEL/CSV/JSON
            required: true
            content:
              multipart/form-data:
                schema:
                  type: object
                  properties:
                    formData:
                      description: formData对象
                      type: string
                      format: binary
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        upload = request.files.get("formData", None)
        data = FileDataCommand(g.user, upload).run()
        return self.format_response(200, data=data)

    @expose("/file/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_FILE_DATASET,
        log_to_statsd=False,
    )
    def add_file_dataset(self) -> Response:
        """
        ---
        post:
          description: 新增文件数据集
          parameters:
          - in: query
            name: dataset_name
            schema:
              type: string
          - in: query
            name: group_id
            schema:
              type: integer
          requestBody:
            description: 上传EXCEL/CSV/JSON
            required: true
            content:
              multipart/form-data:
                schema:
                  type: object
                  properties:
                    formData:
                      description: formData对象
                      type: string
                      format: binary
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        upload = request.files.get("formData", None)
        dataset_name = request.args.get('dataset_name', None)
        group_id = request.args.get('group_id', None)
        sheet_name = request.args.get("sheet_name", None)
        table_name = request.args.get('table_name', dataset_name)
        command = CreateFileDatasetCommand(
            g.user,
            upload,
            {
                "custom_name": dataset_name,
                "table_name": table_name,
                "table_group_id": group_id,
            }
        )
        dataset = command.run(sheet_name=sheet_name)
        return self.format_response(200, data=dataset.to_json())

    @expose("/file/<int:dataset_id>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_DATASET,
        log_to_statsd=False,
    )
    def edit_file_dataset(self, dataset_id: int) -> Response:
        """
        ---
        put:
          description: 编辑文件数据集
          parameters:
          - in: path
            name: dataset_id
            description: 数据集id
            schema:
              type: integer
          - in: query
            name: if_exists
            description: 替换方式(FAIL/REPLACE/APPEND)
            default: REPLACE
            schema:
              type: string
          requestBody:
            description:
            required: true
            content:
              multipart/form-data:
                schema:
                  type: object
                  properties:
                    formData:
                      description: formData对象
                      type: string
                      format: binary
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = FileDatasetPutSchema().load({
            "upload": request.files.get("formData", None),
            "if_exists": request.args.get("if_exists", 'REPLACE')
        })
        sheet_name = request.args.get("sheet_name", None)
        dataset = UpdateFileDatasetCommand(
            g.user, dataset_id, **item
        ).run(sheet_name=sheet_name)
        return self.format_response(200, data=dataset.to_json())
