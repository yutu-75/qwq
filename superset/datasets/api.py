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
import json
import logging
from datetime import datetime
from io import BytesIO
from typing import Any
from zipfile import is_zipfile, ZipFile

import pandas as pd
import yaml
from flask import request, Response, send_file, g, flash
from flask_appbuilder.api import expose, protect, rison, safe
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import ngettext
from marshmallow import ValidationError
from flask_appbuilder.const import API_SELECT_COLUMNS_RIS_KEY, API_RESULT_RES_KEY
from sqlalchemy import create_engine

from superset import event_logger, is_feature_enabled, db, app
from superset.commands.importers.exceptions import NoValidFilesFoundError
from superset.commands.importers.v1.utils import get_contents_from_bundle
from superset import conf
from superset.connectors.sqla.models import SqlaTable, TableColumn, DatasetCategory
from superset.constants import MODEL_API_RW_METHOD_PERMISSION_MAP, RouteMethod
from superset.dao.exceptions import DatasourceTypeNotSupportedError, DatasourceNotFound
from superset.databases.filters import DatabaseFilter
from superset.datasets.commands.bulk_delete import BulkDeleteDatasetCommand
from superset.datasets.commands.create import CreateDatasetCommand
from superset.datasets.commands.delete import DeleteDatasetCommand
from superset.datasets.commands.duplicate import DuplicateDatasetCommand
from superset.datasets.commands.exceptions import (
    DatasetBulkDeleteFailedError,
    DatasetCreateFailedError,
    DatasetDeleteFailedError,
    DatasetForbiddenError,
    DatasetInvalidError,
    DatasetNotFoundError,
    DatasetRefreshFailedError,
    DatasetUpdateFailedError,
)
from superset.datasets.commands.export import ExportDatasetsCommand
from superset.datasets.commands.importers.dispatcher import ImportDatasetsCommand
from superset.datasets.commands.refresh import RefreshDatasetCommand
from superset.datasets.commands.update import UpdateDatasetCommand
from superset.datasets.dao import DatasetDAO
from superset.datasets.filters import DatasetCertifiedFilter, DatasetIsNullOrEmptyFilter
from superset.datasets.schemas import (
    DatasetDuplicateSchema,
    DatasetPostSchema,
    DatasetPutSchema,
    DatasetRelatedObjectsResponse,
    get_delete_ids_schema,
    get_export_ids_schema,
    GetOrCreateDatasetSchema,
)
from superset.datasource.api import DatasourceRestApi
from superset.datasource.dao import DatasourceDAO
from superset.exceptions import SupersetSecurityException
from superset.models.core import Database
from superset.utils.core import parse_boolean_string, DatasourceType, \
    apply_max_row_limit
from superset.v2.datasets.commands.get_data_command import DatasetDataCommand
from superset.views.base import DatasourceFilter, generate_download_headers
from superset.views.base_api import (
    BaseSupersetModelRestApi,
    RelatedFieldFilter,
    requires_form_data,
    requires_json,
    statsd_metrics,
)
from superset.views.filters import BaseFilterRelatedUsers, FilterRelatedOwners

logger = logging.getLogger(__name__)

database_database_name = "database.database_name"
changed_by_first_name = "changed_by.first_name"
Error_creating = "Error creating model %s: %s"


class DatasetRestApi(BaseSupersetModelRestApi):
    datamodel = SQLAInterface(SqlaTable)
    base_filters = [["id", DatasourceFilter, lambda: []]]
    resource_name = "dataset"
    allow_browser_login = True
    class_permission_name = "Dataset"
    method_permission_name = MODEL_API_RW_METHOD_PERMISSION_MAP
    include_route_methods = RouteMethod.REST_MODEL_VIEW_CRUD_SET | {
        RouteMethod.EXPORT,
        RouteMethod.IMPORT,
        RouteMethod.RELATED,
        RouteMethod.DISTINCT,
        "bulk_delete",
        "refresh",
        "related_objects",
        "duplicate",
        "get_or_create_dataset",
        "get_column_data",
        "save_column",
        "edit_column"
    }
    list_columns = [
        "id",
        "database.id",
        database_database_name,
        "changed_by_name",
        "changed_by_url",
        changed_by_first_name,
        "changed_by.username",
        "changed_on_utc",
        "changed_on_delta_humanized",
        "default_endpoint",
        "description",
        "datasource_type",
        "explore_url",
        "extra",
        "kind",
        "owners.id",
        "owners.username",
        "owners.first_name",
        "owners.last_name",
        "schema",
        "sql",
        "table_name",
    ]
    list_select_columns = list_columns + ["changed_on", "changed_by_fk"]
    order_columns = [
        "table_name",
        "schema",
        changed_by_first_name,
        "changed_on_delta_humanized",
        database_database_name,
    ]
    show_select_columns = [
        "id",
        database_database_name,
        "database.verbose_name",
        "database.id",
        "table_name",
        "sql",
        "filter_select_enabled",
        "fetch_values_predicate",
        "schema",
        "description",
        "main_dttm_col",
        "offset",
        "default_endpoint",
        "cache_timeout",
        "is_sqllab_view",
        "template_params",
        "select_star",
        "owners.id",
        "owners.username",
        "owners.first_name",
        "owners.last_name",
        "columns.advanced_data_type",
        "columns.changed_on",
        "columns.column_name",
        "columns.created_on",
        "columns.description",
        "columns.expression",
        "columns.filterable",
        "columns.groupby",
        "columns.id",
        "columns.is_active",
        "columns.extra",
        "columns.is_dttm",
        "columns.python_date_format",
        "columns.type",
        "columns.uuid",
        "columns.verbose_name",
        "columns.is_cross_field",
        "metrics",  # TODO(john-bodley): Deprecate in 3.0.
        "metrics.changed_on",
        "metrics.created_on",
        "metrics.d3format",
        "metrics.description",
        "metrics.expression",
        "metrics.extra",
        "metrics.id",
        "metrics.metric_name",
        "metrics.metric_type",
        "metrics.verbose_name",
        "metrics.warning_text",
        "datasource_type",
        "url",
        "extra",
        "kind",
        "custom_name",  # 增加的属性用于编辑时数据集同步
        "type_classify",
        "table_group_id",
        "created_on",
        "created_on_humanized",
        "created_by.first_name",
        "created_by.last_name",
        "changed_on",
        "changed_on_humanized",
        changed_by_first_name,
        "changed_by.last_name",
        "categories.id",
        "categories.table_name",
        "categories.first_cate_field",
        "categories.second_cate_field",
        "categories.field_name",
        "categories.field_code",
        "categories.is_cross_field",
        "categories.database_name",
        "categories.database_id",
        "categories.category_type",
        "categories.is_fast_filter",
    ]
    show_columns = show_select_columns + [
        "columns.type_generic",
        "database.backend",
        "columns.advanced_data_type",
        "is_managed_externally",
    ]
    add_model_schema = DatasetPostSchema()
    edit_model_schema = DatasetPutSchema()
    duplicate_model_schema = DatasetDuplicateSchema()
    add_columns = ["database", "schema", "table_name", "sql", "owners"]
    edit_columns = [
        "table_name",
        "sql",
        "filter_select_enabled",
        "fetch_values_predicate",
        "schema",
        "description",
        "main_dttm_col",
        "offset",
        "default_endpoint",
        "cache_timeout",
        "is_sqllab_view",
        "template_params",
        "owners",
        "columns",
        "metrics",
        "extra",
    ]
    openapi_spec_tag = "Datasets"

    base_related_field_filters = {
        "owners": [["id", BaseFilterRelatedUsers, lambda: []]],
        "database": [["id", DatabaseFilter, lambda: []]],
    }
    related_field_filters = {
        "owners": RelatedFieldFilter("first_name", FilterRelatedOwners),
        "database": "database_name",
    }
    search_filters = {
        "sql": [DatasetIsNullOrEmptyFilter],
        "id": [DatasetCertifiedFilter],
    }
    search_columns = ["id", "database", "owners", "schema", "sql", "table_name"]
    allowed_rel_fields = {"database", "owners"}
    allowed_distinct_fields = {"schema"}

    apispec_parameter_schemas = {
        "get_export_ids_schema": get_export_ids_schema,
    }
    openapi_spec_component_schemas = (
        DatasetRelatedObjectsResponse,
        DatasetDuplicateSchema,
        GetOrCreateDatasetSchema,
    )

    list_outer_default_load = True
    show_outer_default_load = True

    @expose("/", methods=["POST"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.post",
        log_to_statsd=False,
    )
    @requires_json
    def post(self) -> Response:
        """Creates a new Dataset
        ---
        post:
          description: >-
            Create a new Dataset
          requestBody:
            description: Dataset schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/{{self.__class__.__name__}}.post'
          responses:
            201:
              description: Dataset added
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      id:
                        type: number
                      result:
                        $ref: '#/components/schemas/{{self.__class__.__name__}}.post'
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        try:
            item = self.add_model_schema.load(request.json)
        # This validates custom Schema with custom validations
        except ValidationError as error:
            return self.response_400(message=error.messages)

        try:
            new_model = CreateDatasetCommand(item).run()
            return self.response(201, id=new_model.id, result=item)
        except DatasetInvalidError as ex:
            return self.response_422(message=ex.normalized_messages())
        except DatasetCreateFailedError as ex:
            logger.error(
                Error_creating,
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            return self.response_422(message=str(ex))

    @expose("/<pk>", methods=["GET"])
    @protect()
    def get(self, pk, **kwargs):
        """Get list of items from Model
        ---
        get:
          description: >-
            Get a list of models
          parameters:
          - in: query
            name: q
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/get_list_schema'
          responses:
            200:
              description: Items from Model
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      label_columns:
                        type: object
                        properties:
                          column_name:
                            description: >-
                              The label for the column name.
                              Will be translated by babel
                            example: A Nice label for the column
                            type: string
                      list_columns:
                        description: >-
                          A list of columns
                        type: array
                        items:
                          type: string
                      description_columns:
                        type: object
                        properties:
                          column_name:
                            description: >-
                              The description for the column name.
                              Will be translated by babel
                            example: A Nice description for the column
                            type: string
                      list_title:
                        description: >-
                          A title to render.
                          Will be translated by babel
                        example: List Items
                        type: string
                      ids:
                        description: >-
                          A list of item ids, useful when you don't know the column id
                        type: array
                        items:
                          type: string
                      count:
                        description: >-
                          The total record count on the backend
                        type: number
                      order_columns:
                        description: >-
                          A list of allowed columns to sort
                        type: array
                        items:
                          type: string
                      result:
                        description: >-
                          The result from the get list query
                        type: array
                        items:
                          $ref: '#/components/schemas/{{self.__class__.__name__}}.get_list'  # noqa
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        item = self.datamodel.get(
            pk,
            select_columns=self.show_select_columns,
            outer_default_load=self.show_outer_default_load,
        )
        if not item:
            return self.response_404()

        datasource_name = item.database_datasource_name

        response = {}

        args = kwargs.get("rison", {})
        select_cols = args.get(API_SELECT_COLUMNS_RIS_KEY, [])
        pruned_select_cols = [col for col in select_cols if col in self.show_columns]
        self.set_response_key_mappings(
            response, self.get, args, **{API_SELECT_COLUMNS_RIS_KEY: pruned_select_cols}
        )
        if pruned_select_cols:
            show_model_schema = self.model2schemaconverter.convert(pruned_select_cols)
        else:
            show_model_schema = self.show_model_schema

        response["id"] = pk
        response[API_RESULT_RES_KEY] = show_model_schema.dump(item, many=False)
        # 显示datasource name
        response["result"]["database"]["datasource_name"] = datasource_name
        self.pre_get(response)
        return self.response(200, **response)

    @expose("/<pk>", methods=["PUT"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.put",
        log_to_statsd=False,
    )
    @requires_json
    def put(self, pk: int) -> Response:
        """Changes a Dataset
        ---
        put:
          description: >-
            Changes a Dataset
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          - in: query
            schema:
              type: boolean
            name: override_columns
          requestBody:
            description: Dataset schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/{{self.__class__.__name__}}.put'
          responses:
            200:
              description: Dataset changed
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      id:
                        type: number
                      result:
                        $ref: '#/components/schemas/{{self.__class__.__name__}}.put'
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            403:
              $ref: '#/components/responses/403'
            404:
              $ref: '#/components/responses/404'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        override_columns = (
            parse_boolean_string(request.args["override_columns"])
            if "override_columns" in request.args
            else False
        )
        try:
            item = self.edit_model_schema.load(request.json)
        # This validates custom Schema with custom validations
        except ValidationError as error:
            return self.response_400(message=error.messages)
        try:
            changed_model = UpdateDatasetCommand(pk, item, override_columns).run()
            if override_columns:
                RefreshDatasetCommand(pk).run()
            response = self.response(200, id=changed_model.id, result=item)
        except DatasetNotFoundError:
            response = self.response_404()
        except DatasetForbiddenError:
            response = self.response_403()
        except DatasetInvalidError as ex:
            response = self.response_422(message=ex.normalized_messages())
        except DatasetUpdateFailedError as ex:
            logger.error(
                "Error updating model %s: %s",
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            response = self.response_422(message=str(ex))
        return response

    @expose("/<pk>", methods=["DELETE"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.delete",
        log_to_statsd=False,
    )
    def delete(self, pk: int) -> Response:
        """Deletes a Dataset
        ---
        delete:
          description: >-
            Deletes a Dataset
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          responses:
            200:
              description: Dataset delete
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
            401:
              $ref: '#/components/responses/401'
            403:
              $ref: '#/components/responses/403'
            404:
              $ref: '#/components/responses/404'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        try:
            DeleteDatasetCommand(pk).run()
            return self.response(200, message="OK")
        except DatasetNotFoundError:
            return self.response_404()
        except DatasetForbiddenError:
            return self.response_403()
        except DatasetDeleteFailedError as ex:
            logger.error(
                "Error deleting model %s: %s",
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            return self.response_422(message=str(ex))

    @expose("/export/", methods=["GET"])
    @protect()
    @safe
    @statsd_metrics
    @rison(get_export_ids_schema)
    def export(self, **kwargs: Any) -> Response:
        """Export datasets
        ---
        get:
          description: >-
            Exports multiple datasets and downloads them as YAML files
          parameters:
          - in: query
            name: q
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/get_export_ids_schema'
          responses:
            200:
              description: Dataset export
              content:
                text/plain:
                  schema:
                    type: string
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        requested_ids = kwargs["rison"]

        if is_feature_enabled("VERSIONED_EXPORT"):
            token = request.args.get("token")
            timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
            root = f"dataset_export_{timestamp}"
            filename = f"{root}.zip"

            buf = BytesIO()
            with ZipFile(buf, "w") as bundle:
                try:
                    for file_name, file_content in ExportDatasetsCommand(
                        requested_ids
                    ).run():
                        with bundle.open(f"{root}/{file_name}", "w") as fp:
                            fp.write(file_content.encode())
                except DatasetNotFoundError:
                    return self.response_404()
            buf.seek(0)

            response = send_file(
                buf,
                mimetype="application/zip",
                as_attachment=True,
                download_name=filename,
            )
            if token:
                response.set_cookie(token, "done", max_age=600)
            return response

        query = self.datamodel.session.query(SqlaTable).filter(
            SqlaTable.id.in_(requested_ids)
        )
        query = self._base_filters.apply_all(query)
        items = query.all()
        ids = [item.id for item in items]
        if len(ids) != len(requested_ids):
            return self.response_404()

        data = [t.export_to_dict() for t in items]
        return Response(
            yaml.safe_dump(data),
            headers=generate_download_headers("yaml"),
            mimetype="application/text",
        )

    @expose("/duplicate", methods=["POST"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}" f".duplicate",
        log_to_statsd=False,
    )
    @requires_json
    def duplicate(self) -> Response:
        """Duplicates a Dataset
        ---
        post:
          description: >-
            Duplicates a Dataset
          requestBody:
            description: Dataset schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatasetDuplicateSchema'
          responses:
            201:
              description: Dataset duplicated
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      id:
                        type: number
                      result:
                        $ref: '#/components/schemas/DatasetDuplicateSchema'
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            403:
              $ref: '#/components/responses/403'
            404:
              $ref: '#/components/responses/404'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        try:
            item = self.duplicate_model_schema.load(request.json)
        # This validates custom Schema with custom validations
        except ValidationError as error:
            return self.response_400(message=error.messages)

        try:
            new_model = DuplicateDatasetCommand(item).run()
            return self.response(201, id=new_model.id, result=item)
        except DatasetInvalidError as ex:
            return self.response_422(
                message=ex.normalized_messages()
                if isinstance(ex, ValidationError)
                else str(ex)
            )
        except DatasetCreateFailedError as ex:
            logger.error(
                Error_creating,
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            return self.response_422(message=str(ex))

    @expose("/<pk>/refresh", methods=["PUT"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}" f".refresh",
        log_to_statsd=False,
    )
    def refresh(self, pk: int) -> Response:
        """Refresh a Dataset
        ---
        put:
          description: >-
            Refreshes and updates columns of a dataset
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          responses:
            200:
              description: Dataset delete
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
            401:
              $ref: '#/components/responses/401'
            403:
              $ref: '#/components/responses/403'
            404:
              $ref: '#/components/responses/404'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        try:
            RefreshDatasetCommand(pk).run()
            return self.response(200, message="OK")
        except DatasetNotFoundError:
            return self.response_404()
        except DatasetForbiddenError:
            return self.response_403()
        except DatasetRefreshFailedError as ex:
            logger.error(
                "Error refreshing dataset %s: %s",
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            return self.response_422(message=str(ex))

    @expose("/<pk>/related_objects", methods=["GET"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}"
                                             f".related_objects",
        log_to_statsd=False,
    )
    def related_objects(self, pk: int) -> Response:
        """Get charts and dashboards count associated to a dataset
        ---
        get:
          description:
            Get charts and dashboards count associated to a dataset
          parameters:
          - in: path
            name: pk
            schema:
              type: integer
          responses:
            200:
            200:
              description: Query result
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/DatasetRelatedObjectsResponse"
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        dataset = DatasetDAO.find_by_id(pk)
        if not dataset:
            return self.response_404()
        data = DatasetDAO.get_related_objects(pk)
        charts = [
            {
                "id": chart.id,
                "slice_name": chart.slice_name,
                "viz_type": chart.viz_type,
            }
            for chart in data["charts"]
        ]
        dashboards = [
            {
                "id": dashboard.id,
                "json_metadata": dashboard.json_metadata,
                "slug": dashboard.slug,
                "title": dashboard.dashboard_title,
            }
            for dashboard in data["dashboards"]
        ]
        return self.response(
            200,
            charts={"count": len(charts), "result": charts},
            dashboards={"count": len(dashboards), "result": dashboards},
        )

    @expose("/", methods=["DELETE"])
    @protect()
    @safe
    @statsd_metrics
    @rison(get_delete_ids_schema)
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.bulk_delete",
        log_to_statsd=False,
    )
    def bulk_delete(self, **kwargs: Any) -> Response:
        """Delete bulk Datasets
        ---
        delete:
          description: >-
            Deletes multiple Datasets in a bulk operation.
          parameters:
          - in: query
            name: q
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/get_delete_ids_schema'
          responses:
            200:
              description: Dataset bulk delete
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            403:
              $ref: '#/components/responses/403'
            404:
              $ref: '#/components/responses/404'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        item_ids = kwargs["rison"]
        try:
            BulkDeleteDatasetCommand(item_ids).run()
            return self.response(
                200,
                message=ngettext(
                    "Deleted %(num)d dataset",
                    "Deleted %(num)d datasets",
                    num=len(item_ids),
                ),
            )
        except DatasetNotFoundError:
            return self.response_404()
        except DatasetForbiddenError:
            return self.response_403()
        except DatasetBulkDeleteFailedError as ex:
            return self.response_422(message=str(ex))

    @expose("/import/", methods=["POST"])
    @protect()
    @statsd_metrics
    @requires_form_data
    def import_(self) -> Response:
        """Import dataset(s) with associated databases
        ---
        post:
          parameters:
          - in: query
            schema:
              type: integer
            name: datasource_group_id
          - in: query
            schema:
              type: integer
            name: dataset_group_id
          requestBody:
            required: true
            content:
              multipart/form-data:
                schema:
                  type: object
                  properties:
                    formData:
                      description: upload file (ZIP or YAML)
                      type: string
                      format: binary
                    passwords:
                      description: >-
                        JSON map of passwords for each featured database in the
                        ZIP file. If the ZIP includes a database config in the path
                        `databases/MyDatabase.yaml`, the password should be provided
                        in the following format:
                        `{"databases/MyDatabase.yaml": "my_password"}`.
                      type: string
                    overwrite:
                      description: overwrite existing datasets?
                      type: boolean
                    sync_columns:
                      description: sync columns?
                      type: boolean
                    sync_metrics:
                      description: sync metrics?
                      type: boolean
          responses:
            200:
              description: Dataset import result
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        upload = request.files.get("formData")
        if not upload:
            return self.response_400()
        if is_zipfile(upload):
            with ZipFile(upload) as bundle:
                contents = get_contents_from_bundle(bundle)
        else:
            upload.seek(0)
            contents = {upload.filename: upload.read()}

        if not contents:
            raise NoValidFilesFoundError()

        passwords = (
            json.loads(request.form["passwords"])
            if "passwords" in request.form
            else None
        )
        overwrite = (
            request.form.get("overwrite") == "true" or
            request.form.get("overwrite") == "覆盖"
        )
        sync_columns = request.form.get("sync_columns") == "true"
        sync_metrics = request.form.get("sync_metrics") == "true"
        datasource_group_id = int(request.form.get("datasource_group_id", 0)),
        dataset_group_id = int(request.form.get("dataset_group_id", 0))

        command = ImportDatasetsCommand(
            contents,
            passwords=passwords,
            overwrite=overwrite,
            sync_columns=sync_columns,
            sync_metrics=sync_metrics,
            datasource_group_id=datasource_group_id,
            dataset_group_id=dataset_group_id
        )
        command.run()
        return self.response(200, message="OK")

    @expose("/get_or_create/", methods=["POST"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}"
                                             f".get_or_create_dataset",
        log_to_statsd=False,
    )
    def get_or_create_dataset(self) -> Response:
        """Retrieve a dataset by name, or create it if it does not exist
        ---
        post:
          summary: Retrieve a table by name, or create it if it does not exist
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/GetOrCreateDatasetSchema'
          responses:
            200:
              description: The ID of the table
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        type: object
                        properties:
                          table_id:
                            type: integer
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        try:
            body = GetOrCreateDatasetSchema().load(request.json)
        except ValidationError as ex:
            return self.response(400, message=ex.messages)
        table_name = body["table_name"]
        database_id = body["database_id"]
        table = DatasetDAO.get_table_by_name(database_id, table_name)
        if table:
            return self.response(200, result={"table_id": table.id})

        body["database"] = database_id
        try:
            tbl = CreateDatasetCommand(body).run()
            return self.response(200, result={"table_id": tbl.id})
        except DatasetInvalidError as ex:
            return self.response_422(message=ex.normalized_messages())
        except DatasetCreateFailedError as ex:
            logger.error(
                Error_creating,
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            return self.response_422(message=ex.message)

    @expose("/<pk>/get_column_data/", methods=['POST'])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.post",
        log_to_statsd=False,
    )
    def get_column_data(self, pk: int):
        """Select the label field in the data source to which you access, and assign
        a new data label by grouping"""
        try:
            base_column = request.json.get('base_column')  # 选择的列名
            result = distinct_data_get(self, pk, base_column)
            is_all_text = all(isinstance(item, str) for item in result)
            is_all_num = all(isinstance(item, (int, float)) for item in result)
            if is_all_text:
                return self.response(200, result={
                    "type": 0,
                    "distinct_values": result,
                })
            elif is_all_num:
                max_value = max(result)
                min_value = min(result)
                return self.response(200, result={
                    "type": 1,
                    "range_values": f"{min_value}～{max_value}",
                })
            else:
                return self.response(200, result={
                    "type": 2,
                    "values": "列类型无效",
                })
        except ValueError as e:
            response_dict = {
                "message": str(e)
            }
            return self.response(400, result=response_dict)

    @expose("/<pk>/save_column/", methods=['POST'])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.post",
        log_to_statsd=False,
    )
    def save_column(self, pk: int):
        '''
        {
          "column_name": "测试赋值列",
          "base_column": "a1",
          "data":{
            "type":"text",
            "data": [
              {
                "name":"分组名1"
                "value":["个体工商户", "事业单位"]
              }
              {
                "name":"分组名2"
                "value":["国家党政机关", "社会团体"]
              }
            ]
          }
            ]
          }
        }
        '''
        try:
            column_id = request.json.get('code_id')
            column_name = request.json.get('column_name')  # 赋值列名
            base_column = request.json.get('base_column')  # 选择的列名
            dataset_query = DatasetDAO.find_dataset_column_by_name(pk, base_column)
            column_type_1 = dataset_query.type.upper()  # 获取该列数据类型
            column_type = request.json.get('types')  # 获取该列数据类型
            echo_data = request.get_json()  # 编辑时的回显数据
            group_data = request.json.get('exitData')  # 列表数据
            range_values = request.json.get('range_values')
            '''
            模拟保存数据格式
            {
                "column_name": "测试赋值列_399",
                "base_column": "gender",
                "data":{
                    "type":"VARCHAR(16)",
                    "data_wei":["test"],
                    "data": [
                        {
                            "name":"分组名1",
                            "value":["girl"]
                        },
                        {
                            "name":"分组名2",
                            "value":["boy"]
                        }
                    ]
                }
            }
            '''
            sql_data = []
            name_list = []
            if column_type == '文本':
                for group in group_data:
                    group_name = group.get('name')
                    if group_name in name_list:
                        raise ValueError("无效的分组：分组名重复")
                    else:
                        name_list.append(group_name)
                        data = "(" + ",".join(
                            [f"\'{item}\'" for item in group.get('value')]) + ")"
                        sql_data.append(
                            f'WHEN `{base_column}` in {data} then "{group_name}"')
                sql_data.append(f'ELSE "" END')
                sql = 'case ' + ' '.join(sql_data)  # 生成sql，存入数据库

            elif column_type == '数字':
                # 输入值范围判断
                min_range_value = float(range_values.split("～")[0])
                max_range_value = float(range_values.split("～")[1])
                # 给定的区间范围
                range_value = [int(min_range_value), int(max_range_value)]

                for group in group_data:
                    group_name = group.get('name1')
                    value_1 = group.get('value_1')
                    option_1 = group.get('option_1')
                    value_2 = group.get('value_2')
                    option_2 = group.get('option_2')
                    if group_name in name_list:
                        raise ValueError("无效的分组：分组名重复")
                    else:
                        name_list.append(group_name)
                        # 排除数值和符号为空
                        if (value_1, value_2, option_2, option_1) is not None:
                            # 排除区间范围为无穷区间：2<x>10
                            if option_1[0] == option_2[0]:
                                # 排除区间范围前后矛盾：1>x>10
                                if value_1 > value_2 and option_1[0] == '>':
                                    m = [value_2, value_1]
                                # 排除区间范围前后矛盾：10<x<1
                                elif value_1 < value_2 and option_1[0] == '<':
                                    m = [value_1, value_2]
                                else:
                                    raise ValueError(
                                        f"无效的分组：分组值范围选择错误,{str(value_1) + option_1}值{option_2 + str(value_2)} 不可取")

                                # 排除掉单个分组区间完全包含给定区间range_value
                                if len(range_value) == 0:
                                    raise ValueError(
                                        f"无效的分组：已存在分组完全包含{str(int(min_range_value)) +'～'+ str(int(max_range_value))}")
                                # 当给定的范围区间range_value与输入的区间m相交时，减掉对应的交集
                                elif type(range_value[0]) is int:
                                    range_value = get_difference(self, range_value, m)

                                # 当给定区间range_value中间断层时,将输入的区间m遍历所有区间进行划分，并减掉对应的交集
                                else:
                                    iterations = len(range_value)  # 控制迭代次数
                                    for _ in range(iterations):
                                        # 每次遍历删掉第一个区间range_value[0]
                                        first_element = range_value.pop(0)
                                        result = get_difference(self, first_element, m)

                                        # 当result为空时，说明当前区间first_element被包含于m
                                        if len(result) == 0:
                                            m[0] = first_element[1]     # 此时，更改m区间值
                                        # 当result为非断层区间[1,2]，说明当前区间first_element与m不相交
                                        elif type(result[0]) is int:
                                            range_value.append(result)
                                        # 当result为断层区间[[1,2],[4,5]]，说明当前区间first_element与m相交，则减掉了相应的交集
                                        else:
                                            for i in result:
                                                range_value.append(i)
                                # 将区间范围值转为SQL语句
                                data1 = str(value_1) + ' ' + option_1
                                data2 = option_2 + ' ' + str(value_2)
                                sql_data.append(
                                    f'WHEN  {data1} `{base_column}` and `{base_column}` {data2} then "{group_name}"')
                            else:
                                raise ValueError("无效的分组：分组值范围选择错误,不可包含无穷区间")
                        # elif value_1 and option_1 and not value_2 and not option_2:
                        #     if min_range_values >= value_1 <= max_range_value:
                        #         data1 = str(value_1) + ' ' + option_1
                        #         sql_data.append(
                        #             f'WHEN {data1} `{base_column}` then "{group_name}"')
                        #     else:
                        #         raise ValueError("无效的分组：分组值选择错误")
                        # elif value_2 and option_2 and not value_1 and not option_1:
                        #     if min_range_values >= value_2 <= max_range_value:
                        #         data2 = option_2 + ' ' + str(value_2)
                        #         sql_data.append(
                        #             f'WHEN `{base_column}` {data2} then "{group_name}"')
                        #     else:
                        #         raise ValueError("无效的分组：分组值选择错误")
                        else:
                            raise ValueError("无效的分组：缺失数据值或范围符号")
                if len(range_value) == 0:
                    sql_data.append(f'ELSE "" END')
                    sql = 'case ' + ' '.join(sql_data)  # 生成sql，存入数据库
                else:
                    raise ValueError("无效的分组：分组数据未全包含给定范围")
            else:
                raise ValueError("无效的列：该列类型错误")

            new_data = {
                "column_name": column_name,  # 赋值列名称
                "table_id": pk,  # 数据集id
                "computed_type": 1,  # 赋值列注释
                "ref_column": base_column,  # 选择的列
                "expr": json.dumps(echo_data),  # 回显数据内容
                "expression": sql,  # sql
                "type": column_type_1,  # 数据列类型
            }

            # 查找已经存在的赋值列
            if column_id:
                exist_column = (db.session.query(TableColumn).filter(
                    TableColumn.id == column_id).one_or_none())
                DatasetDAO.update_column(exist_column, new_data)
                response_dict = {
                    "message": '赋值列已成功修改',
                    "column": new_data
                }
                return self.response(200, result=response_dict)
            else:
                try:
                    DatasetDAO.create_column(new_data)
                    response_dict = {
                        "message": '赋值列已成功新建',
                        "column": new_data
                    }
                except Exception as e:
                    # 处理新建失败的异常
                    error_message = str(e)
                    return self.response(400, error=error_message)
            return self.response(200, result=response_dict)

        except ValueError as e:
            # 处理列类型无效的异常
            error_message = str(e)
            return self.response(201, error=error_message)

    @expose("/<pk>/edit_column/", methods=['POST'])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.post",
        log_to_statsd=False,
    )
    def edit_column(self, pk: int):
        try:
            exist_column = (db.session.query(TableColumn).filter(
                TableColumn.id == pk).one_or_none())
            exist_column_dict = {
                "column_name": exist_column.column_name,
                "base_column": exist_column.ref_column,
                "data": json.loads(exist_column.expr),
                "type": exist_column.type
            }
            return self.response(200, result=exist_column_dict)
        except ValueError as e:
            # 处理列类型无效的异常
            error_message = str(e)
            return self.response(400, error=error_message)


# 数据集单列去重
def distinct_data_get(self, pk: int, base_column: str):
    """
    Gets detailed datasets information and returns.
    """
    datasource_type = "table"
    try:
        datasource = DatasourceDAO.get_datasource(
            db.session, DatasourceType(datasource_type), pk
        )
        datasource.raise_for_access()
    except ValueError:
        return self.response(
            400, message=f"Invalid datasource type: {datasource_type}"
        )
    except DatasourceTypeNotSupportedError as ex:
        return self.response(400, message=ex.message)
    except DatasourceNotFound as ex:
        return self.response(404, message=ex.message)
    except SupersetSecurityException as ex:
        return self.response(403, message=ex.message)

    row_limit = apply_max_row_limit(app.config["FILTER_SELECT_ROW_LIMIT"])
    try:
        payload = datasource.values_for_column(
            column_name=base_column, limit=row_limit
        )
        return payload
    except NotImplementedError:
        return self.response(
            400,
            message=(
                "Unable to get column values for "
                f"datasource type: {datasource_type}"
            ),
        )


# 区间相交判断，合集删除
def get_difference(self, x: list, m: list):
    result = []
    try:
        if x[1] < m[0] or m[1] < x[0]:  # 两个区间不相交
            return x
        else:  # 两个区间相交，计算差集
            # 计算相交部分之外的部分
            if x[0] < m[0]:
                result.append([x[0], min(m[0], x[1])])
            if x[1] > m[1]:
                result.append([max(m[1], x[0]), x[1]])
            return result
    except ValueError as e:
        # 处理列类型无效的异常
        error_message = str(e)
        return self.response(201, error=error_message)
