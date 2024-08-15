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
from typing import Any, cast, Optional, Dict
from zipfile import is_zipfile, ZipFile

from flask import redirect, request, Response, send_file, url_for, g
from flask_appbuilder.api import expose, protect, rison, safe, get_list_schema
from flask_appbuilder.const import API_RESULT_RES_KEY
from flask_appbuilder.hooks import before_request
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import ngettext
from marshmallow import ValidationError
from werkzeug.wrappers import Response as WerkzeugResponse
from werkzeug.wsgi import FileWrapper

from superset import app, is_feature_enabled, thumbnail_cache
from superset.charts.commands.bulk_delete import BulkDeleteChartCommand
from superset.charts.commands.create import CreateChartCommand
from superset.charts.commands.delete import DeleteChartCommand
from superset.charts.commands.exceptions import (
    ChartBulkDeleteFailedError,
    ChartCreateFailedError,
    ChartDeleteFailedError,
    ChartForbiddenError,
    ChartInvalidError,
    ChartNotFoundError,
    ChartUpdateFailedError,
)
from superset.charts.commands.export import ExportChartsCommand
from superset.charts.commands.importers.dispatcher import ImportChartsCommand
from superset.charts.commands.update import UpdateChartCommand
from superset.charts.dao import ChartDAO
from superset.charts.filters import (
    ChartAllTextFilter,
    ChartCertifiedFilter,
    ChartCreatedByMeFilter,
    ChartFavoriteFilter,
    ChartFilter,
    ChartHasCreatedByFilter,
)
from superset.charts.schemas import (
    CHART_SCHEMAS,
    ChartPostSchema,
    ChartPutSchema,
    get_delete_ids_schema,
    get_export_ids_schema,
    get_fav_star_ids_schema,
    openapi_spec_methods_override,
    screenshot_query_schema,
    thumbnail_query_schema,
)
from superset.commands.importers.exceptions import (
    IncorrectFormatError,
    NoValidFilesFoundError,
)
from superset.commands.importers.v1.utils import get_contents_from_bundle
from superset.constants import MODEL_API_RW_METHOD_PERMISSION_MAP, RouteMethod, \
    AuthSourceType, VIEW
from superset.dashboards.api_decorator import api_validate_decorator
from superset.dashboards.schemas import UserSchema, RolesSchema
from superset.exceptions import HTTPError
from superset.extensions import event_logger
from superset.logs_messages import LogsMessages
from superset.models.slice import Slice
from superset.tasks.thumbnails import cache_chart_thumbnail
from superset.tasks.utils import get_current_user
from superset.tripartite_attribute.tripartite_api_log import record_tripartite_api_log
from superset.tripartite_attribute.tripartite_certification import \
    tripartite_certification, verify_slice_role
from superset.utils.screenshots import ChartScreenshot
from superset.utils.urls import get_url_path
from superset.v2.charts.dao import ChartV2DAO
from superset.views.base_api import (
    BaseSupersetModelRestApi,
    RelatedFieldFilter,
    requires_form_data,
    requires_json,
    statsd_metrics,
)
from superset.views.filters import BaseFilterRelatedUsers, FilterRelatedOwners

logger = logging.getLogger(__name__)
config = app.config

dashboard_title = "dashboards.dashboard_title"
dashboards_id = "dashboards.id"


class ChartRestApi(BaseSupersetModelRestApi):
    datamodel = SQLAInterface(Slice)

    resource_name = "chart"
    allow_browser_login = True

    @before_request(only=["thumbnail", "screenshot", "cache_screenshot"])
    def ensure_thumbnails_enabled(self) -> Optional[Response]:
        if not is_feature_enabled("THUMBNAILS"):
            return self.response_404()
        return None

    def pre_get_list(self, data: Dict[str, Any]) -> None:
        if g.user.is_admin:
            return

        data_auth = ChartV2DAO.find_auth_source_perm_by_user(
            AuthSourceType.CHART, g.user.id, VIEW)
        ids = []
        result = []
        for item in data["result"]:
            if data_auth.get(item["id"], False):
                result.append(item)
                ids.append(item["id"])

        data["ids"] = ids
        data["result"] = result

    include_route_methods = RouteMethod.REST_MODEL_VIEW_CRUD_SET | {
        RouteMethod.EXPORT,
        RouteMethod.IMPORT,
        RouteMethod.RELATED,
        "bulk_delete",  # not using RouteMethod since locally defined
        "viz_types",
        "favorite_status",
        "thumbnail",
        "screenshot",
        "cache_screenshot",
        "simple",
        "chart_del"
    }
    class_permission_name = "Chart"
    method_permission_name = MODEL_API_RW_METHOD_PERMISSION_MAP
    show_columns = [
        "cache_timeout",
        "certified_by",
        "certification_details",
        "changed_on_delta_humanized",
        dashboard_title,
        dashboards_id,
        "dashboards.json_metadata",
        "description",
        "id",
        "owners.first_name",
        "owners.id",
        "owners.last_name",
        "owners.username",
        dashboards_id,
        dashboard_title,
        "params",
        "slice_name",
        "thumbnail_url",
        "url",
        "viz_type",
        "query_context",
        "is_managed_externally",
    ]
    show_select_columns = show_columns + ["table.id"]
    list_columns = [
        "is_managed_externally",
        "certified_by",
        "certification_details",
        "cache_timeout",
        "changed_by.first_name",
        "changed_by.last_name",
        "changed_by_name",
        "changed_by_url",
        "changed_on_delta_humanized",
        "changed_on_utc",
        "created_by.first_name",
        "created_by.id",
        "created_by.last_name",
        "created_on_delta_humanized",
        "datasource_id",
        "datasource_name_text",
        "datasource_type",
        "datasource_url",
        "description",
        "description_markeddown",
        "edit_url",
        "id",
        "last_saved_at",
        "last_saved_by.id",
        "last_saved_by.first_name",
        "last_saved_by.last_name",
        "owners.first_name",
        "owners.id",
        "owners.last_name",
        "owners.username",
        dashboards_id,
        dashboard_title,
        "params",
        "slice_name",
        "table.default_endpoint",
        "table.table_name",
        "thumbnail_url",
        "url",
        "viz_type",
    ]
    list_select_columns = list_columns + ["changed_by_fk", "changed_on"]
    order_columns = [
        "changed_by.first_name",
        "changed_on_delta_humanized",
        "datasource_id",
        "datasource_name",
        "last_saved_at",
        "last_saved_by.id",
        "last_saved_by.first_name",
        "last_saved_by.last_name",
        "slice_name",
        "viz_type",
    ]
    search_columns = [
        "created_by",
        "changed_by",
        "last_saved_at",
        "last_saved_by",
        "datasource_id",
        "datasource_name",
        "datasource_type",
        "description",
        "id",
        "owners",
        "dashboards",
        "slice_name",
        "viz_type",
    ]
    base_order = ("changed_on", "desc")
    base_filters = [["id", ChartFilter, lambda: []]]
    search_filters = {
        "id": [ChartFavoriteFilter, ChartCertifiedFilter],
        "slice_name": [ChartAllTextFilter],
        "created_by": [ChartHasCreatedByFilter, ChartCreatedByMeFilter],
    }

    # Will just affect _info endpoint
    edit_columns = ["slice_name"]
    add_columns = edit_columns

    add_model_schema = ChartPostSchema()
    edit_model_schema = ChartPutSchema()

    openapi_spec_tag = "Charts"
    """ Override the name set for this collection of endpoints """
    openapi_spec_component_schemas = CHART_SCHEMAS

    apispec_parameter_schemas = {
        "screenshot_query_schema": screenshot_query_schema,
        "get_delete_ids_schema": get_delete_ids_schema,
        "get_export_ids_schema": get_export_ids_schema,
        "get_fav_star_ids_schema": get_fav_star_ids_schema,
    }
    """ Add extra schemas to the OpenAPI components schema section """
    openapi_spec_methods = openapi_spec_methods_override
    """ Overrides GET methods OpenApi descriptions """

    order_rel_fields = {
        "slices": ("slice_name", "asc"),
        "owners": ("first_name", "asc"),
    }
    base_related_field_filters = {
        "owners": [["id", BaseFilterRelatedUsers, lambda: []]],
        "created_by": [["id", BaseFilterRelatedUsers, lambda: []]],
    }
    related_field_filters = {
        "owners": RelatedFieldFilter("first_name", FilterRelatedOwners),
        "created_by": RelatedFieldFilter("first_name", FilterRelatedOwners),
    }

    allowed_rel_fields = {"owners", "created_by"}

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
        """Creates a new Chart
        ---
        post:
          description: >-
            Create a new Chart.
          requestBody:
            description: Chart schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/{{self.__class__.__name__}}.post'
          responses:
            201:
              description: Chart added
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
            new_model = CreateChartCommand(item).run()
            return self.response(201, id=new_model.id, result=item)
        except HTTPError as ex:
            return self.response_422(message=ex.message)
        except ChartInvalidError as ex:
            return self.response_422(message=ex.normalized_messages())
        except ChartCreateFailedError as ex:
            logger.error(
                "Error creating model %s: %s",
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            return self.response_422(message=str(ex))

    @expose("/<pk>", methods=["PUT"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_CHART,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, pk: int) -> Response:
        """Changes a Chart
        ---
        put:
          description: >-
            Changes a Chart.
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          requestBody:
            description: Chart schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/{{self.__class__.__name__}}.put'
          responses:
            200:
              description: Chart changed
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
        try:
            item = self.edit_model_schema.load(request.json)
        # This validates custom Schema with custom validations
        except ValidationError as error:
            return self.response_400(message=error.messages)
        try:
            changed_model = UpdateChartCommand(pk, item).run()
            response = self.response(200, id=changed_model.id, result=item)
        except ChartNotFoundError:
            response = self.response_404()
        except (ChartForbiddenError, HTTPError):
            response = self.response_403()
        except ChartInvalidError as ex:
            response = self.response_422(message=ex.normalized_messages())
        except ChartUpdateFailedError as ex:
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
        """Deletes a Chart
        ---
        delete:
          description: >-
            Deletes a Chart.
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          responses:
            200:
              description: Chart delete
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
            DeleteChartCommand(pk).run()
            return self.response(200, message="OK")
        except ChartNotFoundError:
            return self.response_404()
        except ChartForbiddenError:
            return self.response_403()
        except ChartDeleteFailedError as ex:
            logger.error(
                "Error deleting model %s: %s",
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            return self.response_422(message=str(ex))

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
        """Delete bulk Charts
        ---
        delete:
          description: >-
            Deletes multiple Charts in a bulk operation.
          parameters:
          - in: query
            name: q
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/get_delete_ids_schema'
          responses:
            200:
              description: Charts bulk delete
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
        item_ids = kwargs["rison"]
        try:
            BulkDeleteChartCommand(item_ids).run()
            return self.response(
                200,
                message=ngettext(
                    "Deleted %(num)d chart", "Deleted %(num)d charts", num=len(item_ids)
                ),
            )
        except ChartNotFoundError:
            return self.response_404()
        except ChartForbiddenError:
            return self.response_403()
        except ChartBulkDeleteFailedError as ex:
            return self.response_422(message=str(ex))

    @expose("/<pk>/cache_screenshot/", methods=["GET"])
    @protect()
    @rison(screenshot_query_schema)
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}"
                                             f".cache_screenshot",
        log_to_statsd=False,
    )
    def cache_screenshot(self, pk: int, **kwargs: Any) -> WerkzeugResponse:
        """
        ---
        get:
          description: Compute and cache a screenshot.
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          - in: query
            name: q
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/screenshot_query_schema'
          responses:
            202:
              description: Chart async result
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/ChartCacheScreenshotResponseSchema"
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        rison_dict = kwargs["rison"]
        window_size = rison_dict.get("window_size") or (800, 600)

        # Don't shrink the image if thumb_size is not specified
        thumb_size = rison_dict.get("thumb_size") or window_size

        chart = cast(Slice, self.datamodel.get(pk, self._base_filters))
        if not chart:
            return self.response_404()

        chart_url = get_url_path("Superset.slice", slice_id=chart.id)
        screenshot_obj = ChartScreenshot(chart_url, chart.digest)
        cache_key = screenshot_obj.cache_key(window_size, thumb_size)
        image_url = get_url_path(
            "ChartRestApi.screenshot", pk=chart.id, digest=cache_key
        )

        def trigger_celery() -> WerkzeugResponse:
            logger.info("Triggering screenshot ASYNC")
            cache_chart_thumbnail.delay(
                current_user=get_current_user(),
                chart_id=chart.id,
                force=True,
                window_size=window_size,
                thumb_size=thumb_size,
            )
            return self.response(
                202, cache_key=cache_key, chart_url=chart_url, image_url=image_url
            )

        return trigger_celery()

    @expose("/<pk>/screenshot/<digest>/", methods=["GET"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.screenshot",
        log_to_statsd=False,
    )
    def screenshot(self, pk: int, digest: str) -> WerkzeugResponse:
        """Get Chart screenshot
        ---
        get:
          description: Get a computed screenshot from cache.
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          - in: path
            schema:
              type: string
            name: digest
          responses:
            200:
              description: Chart thumbnail image
              content:
               image/*:
                 schema:
                   type: string
                   format: binary
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        chart = self.datamodel.get(pk, self._base_filters)

        # Making sure the chart still exists
        if not chart:
            return self.response_404()

        # fetch the chart screenshot using the current user and cache if set
        img = ChartScreenshot.get_from_cache_key(thumbnail_cache, digest)
        if img:
            return Response(
                FileWrapper(img), mimetype="image/png", direct_passthrough=True
            )
        # TODO: return an empty image
        return self.response_404()

    @expose("/<pk>/thumbnail/<digest>/", methods=["GET"])
    @protect()
    @rison(thumbnail_query_schema)
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.thumbnail",
        log_to_statsd=False,
    )
    def thumbnail(self, pk: int, digest: str, **kwargs: Any) -> WerkzeugResponse:
        """Get Chart thumbnail
        ---
        get:
          description: Compute or get already computed chart thumbnail from cache.
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          - in: path
            schema:
              type: string
            name: digest
          responses:
            200:
              description: Chart thumbnail image
              content:
               image/*:
                 schema:
                   type: string
                   format: binary
            302:
              description: Redirects to the current digest
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        chart = cast(Slice, self.datamodel.get(pk, self._base_filters))
        if not chart:
            return self.response_404()

        current_user = get_current_user()
        url = get_url_path("Superset.slice", slice_id=chart.id)
        if kwargs["rison"].get("force", False):
            logger.info(
                "Triggering thumbnail compute (chart id: %s) ASYNC", str(chart.id)
            )
            cache_chart_thumbnail.delay(
                current_user=current_user,
                chart_id=chart.id,
                force=True,
            )
            return self.response(202, message="OK Async")
        # fetch the chart screenshot using the current user and cache if set
        screenshot = ChartScreenshot(url, chart.digest).get_from_cache(
            cache=thumbnail_cache
        )
        # If not screenshot then send request to compute thumb to celery
        if not screenshot:
            self.incr_stats("async", self.thumbnail.__name__)
            logger.info(
                "Triggering thumbnail compute (chart id: %s) ASYNC", str(chart.id)
            )
            cache_chart_thumbnail.delay(
                current_user=current_user,
                chart_id=chart.id,
                force=True,
            )
            return self.response(202, message="OK Async")
        # If digests
        if chart.digest != digest:
            self.incr_stats("redirect", self.thumbnail.__name__)
            return redirect(
                url_for(
                    f"{self.__class__.__name__}.thumbnail", pk=pk, digest=chart.digest
                )
            )
        self.incr_stats("from_cache", self.thumbnail.__name__)
        return Response(
            FileWrapper(screenshot), mimetype="image/png", direct_passthrough=True
        )

    @expose("/export/", methods=["GET"])
    @protect()
    @safe
    @statsd_metrics
    @rison(get_export_ids_schema)
    def export(self, **kwargs: Any) -> Response:
        """Export charts
        ---
        get:
          description: >-
            Exports multiple charts and downloads them as YAML files
          parameters:
          - in: query
            name: q
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/get_export_ids_schema'
          responses:
            200:
              description: A zip file with chart(s), dataset(s) and database(s) as YAML
              content:
                application/zip:
                  schema:
                    type: string
                    format: binary
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        token = request.args.get("token")
        requested_ids = kwargs["rison"]
        timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
        root = f"chart_export_{timestamp}"
        filename = f"{root}.zip"

        buf = BytesIO()
        with ZipFile(buf, "w") as bundle:
            try:
                for file_name, file_content in ExportChartsCommand(requested_ids).run():
                    with bundle.open(f"{root}/{file_name}", "w") as fp:
                        fp.write(file_content.encode())
            except ChartNotFoundError:
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

    @expose("/favorite_status/", methods=["GET"])
    @protect()
    @safe
    @rison(get_fav_star_ids_schema)
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}"
                                             f".favorite_status",
        log_to_statsd=False,
    )
    def favorite_status(self, **kwargs: Any) -> Response:
        """Favorite stars for Charts
        ---
        get:
          description: >-
            Check favorited dashboards for current user
          parameters:
          - in: query
            name: q
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/get_fav_star_ids_schema'
          responses:
            200:
              description:
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/GetFavStarIdsSchema"
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
        charts = ChartDAO.find_by_ids(requested_ids)
        if not charts:
            return self.response_404()
        favorited_chart_ids = ChartDAO.favorited_ids(charts)
        res = [
            {"id": request_id, "value": request_id in favorited_chart_ids}
            for request_id in requested_ids
        ]
        return self.response(200, result=res)

    @expose("/import/", methods=["POST"])
    @protect()
    @statsd_metrics
    @requires_form_data
    def import_(self) -> Response:
        """Import chart(s) with associated datasets and databases
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
          - in: query
            schema:
              type: integer
            name: slice_group_id
          requestBody:
            required: true
            content:
              multipart/form-data:
                schema:
                  type: object
                  properties:
                    formData:
                      description: upload file (ZIP)
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
                      description: overwrite existing charts?
                      type: boolean
          responses:
            200:
              description: Chart import result
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
        if not is_zipfile(upload):
            raise IncorrectFormatError("Not a ZIP file")
        with ZipFile(upload) as bundle:
            contents = get_contents_from_bundle(bundle)

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
        datasource_group_id = int(request.form.get("datasource_group_id", 0)),
        dataset_group_id = int(request.form.get("dataset_group_id", 0))
        slice_group_id = int(request.form.get("slice_group_id", 0))

        command = ImportChartsCommand(
            contents,
            passwords=passwords,
            overwrite=overwrite,
            datasource_group_id=datasource_group_id,
            dataset_group_id=dataset_group_id,
            slice_group_id=slice_group_id,
        )
        command.run()
        return self.response(200, message="OK")

    @record_tripartite_api_log
    @expose("/simple", methods=["GET"])
    @tripartite_certification
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs:
        f"{self.__class__.__name__}.simple",
        log_to_statsd=False,
    )
    def simple(self, **kwargs) -> Response:
        """
        获取当前应用对应的角色所有看板列表
        @return:
        """
        try:
            tripartite = kwargs.pop('tripartite')
            role_id = kwargs.pop('role_id') if kwargs.get('role_id') else None
            if tripartite:
                if not role_id:
                    return self.response_403()
                from superset.extensions import db
                from superset.models.app_attributes import AppAttribute
                from sqlalchemy import select
                from sqlalchemy.ext.declarative import declarative_base
                from sqlalchemy import create_engine, Column, Integer, String, select, \
                    Table, \
                    ForeignKey, Text, func
                from marshmallow import fields, post_load, Schema
                from flask_appbuilder import Model
                Base = declarative_base()

                class UserRole(Base):
                    __tablename__ = 'ab_user_role'

                    id = Column(Integer, primary_key=True)
                    user_id = Column(Integer)
                    role_id = Column(String)

                class UserAccessLevelResponseSchema(Schema):

                    id = fields.Int()
                    changed_by = fields.Nested(UserSchema)
                    created_by = fields.Nested(UserSchema)

                    datasource_id = fields.Int()
                    datasource_type = fields.String()
                    datasource_name = fields.String()
                    viz_type = fields.String()
                    params = fields.String()
                    query_context = fields.String()
                    description = fields.String()
                    cache_timeout = fields.Int()
                    perm = fields.String()
                    schema_perm = fields.String()

                    last_saved_at = fields.DateTime()
                    last_saved_by_fk = fields.Nested(UserSchema)
                    certified_by = fields.String()
                    certification_details = fields.String()
                    is_managed_externally = fields.Boolean()
                    external_url = fields.String()

                    changed_on = fields.DateTime()
                    created_on = fields.DateTime()
                    slice_name = fields.String()
                    owners = fields.List(fields.Nested(UserSchema))
                    roles = fields.List(fields.Nested(RolesSchema))

                user_schema = UserAccessLevelResponseSchema()
                app_key = request.headers.get("appKey")
                query = db.session.query(AppAttribute).filter(
                    AppAttribute.app_key == app_key,
                ).first()
                page = int(request.args.get("page", "1"))
                page_size = int(request.args.get("page_size", "20"))
                created_on = request.args.get("created_on")
                created_by = request.args.get("created_by")
                viz_type = request.args.get("viz_type")
                slice_name = request.args.get("slice_name")
                # print(page,page_size,created_on)
                if query:
                    # 存在数据，取出某个字段的值
                    role_id = query.role_id

                    users = db.session.query(UserRole.user_id).filter(
                        UserRole.role_id == role_id).all()
                    # 提取用户ID列表
                    user_ids = [user[0] for user in users]

                    # 创建映射类
                    Base = declarative_base()

                    class Users(Base):
                        __tablename__ = 'ab_user'

                        id = Column(Integer, primary_key=True)
                        username = Column(String)
                        first_name = Column(String)
                        last_name = Column(String)

                    user_id = db.session.query(Users.id).where(
                        Users.username == created_by).first()[0]

                    where_data = [
                        Slice.created_by_fk.in_(user_ids)
                    ]

                    if created_on:
                        where_data.append(
                            func.date(Slice.created_on) == datetime.strptime(created_on,
                                                                             '%Y-%m-%d').date()
                        )

                    if created_by:
                        where_data.append(
                            Slice.created_by_fk == user_id
                        )
                    if viz_type:
                        where_data.append(
                            Slice.viz_type == viz_type
                        )
                    if slice_name:
                        where_data.append(
                            Slice.slice_name == slice_name
                        )

                    query = db.session.query(Slice).filter(
                        *where_data
                    )
                    pagination = query.paginate(page=page, per_page=page_size)

                    result = {
                        "data": [user_schema.dump(i) for i in pagination.items],
                        "total": pagination.total
                    }

                    return self.response(200, result=result)
                else:
                    return self.response(400, result={"status": "Failed",
                                                      "message": "The appKey is incorrect"})

            else:
                return self.response(401, result={
                    "message": "Sign authentication failed, please calibrate the sign",
                    "status": "Failed"
                })

        except Exception as e:
            return self.response(400, result={"status": "Failed",
                                              "message": str(e)})

    @record_tripartite_api_log
    @expose("/del/<pk>", methods=["DELETE"])
    @tripartite_certification
    def chart_del(self, pk, **kwargs) -> Response:

        tripartite = kwargs.pop('tripartite')
        role_id = kwargs.pop('role_id') if kwargs.get('role_id') else None
        if tripartite:
            if not role_id:
                return self.response_403()
            from superset.extensions import db
            from superset.models.app_attributes import AppAttribute

            app_key = request.headers.get("appKey")
            query = db.session.query(AppAttribute).filter(
                AppAttribute.app_key == app_key,
            ).first()
            if query:
                try:
                    data = db.session.query(Slice).filter_by(id=pk).first()
                    if data:
                        db.session.delete(data)
                        db.session.commit()
                        return self.response(200, result={"status": "Success",
                                                          "message": "ok"})
                    else:
                        return self.response(400, result={"status": "Failed",
                                                          "message": "No matching data found"})
                except Exception as e:
                    return self.response(400, result={"status": "Failed",
                                                      "message": str(e)})
            else:
                return self.response(400, result={"status": "Failed",
                                                  "message": "The appKey is incorrect"})
        else:
            return self.response(401, result={
                "message": "Sign authentication failed, please calibrate the sign",
                "status": "Failed"
            })

    @record_tripartite_api_log
    @expose("/", methods=["GET"])
    # @protect()
    @rison(get_list_schema)
    @tripartite_certification
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.get_list",
        log_to_statsd=False,
    )
    def get_list(self, **kwargs: Any) -> Response:

        tripartite = kwargs.pop('tripartite')
        role_id = kwargs.pop('role_id') if kwargs.get('role_id') else None
        if tripartite:
            if not role_id:
                return self.response_403()
            else:
                if kwargs.get('rison') and kwargs['rison'].get('columns'):
                    kwargs['rison']['columns'].append('id')
                response = super().get_list_headless(**kwargs)
                if response.status_code == 200:
                    res = dict()
                    result = verify_slice_role(
                        json.loads(response.data).get(API_RESULT_RES_KEY) or [],
                        role_id)
                    res[API_RESULT_RES_KEY] = result
                    res['count'] = len(result)
                    res['ids'] = [i.get('id') for i in result]
                    return self.response(200, **res)
                else:
                    return response
        else:
            return super().get_list(**kwargs)

    @expose("/<pk>", methods=["DELETE"])
    # @protect()
    @tripartite_certification
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.delete",
        log_to_statsd=False,
    )
    def delete(self, pk: int, **kwargs: {dict}) -> Response:
        """Deletes a Chart
        ---
        delete:
          description: >-
            Deletes a Chart.
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          responses:
            200:
              description: Chart delete
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
        tripartite = kwargs.pop('tripartite')
        api_func = kwargs.pop('api_func')

        if tripartite:
            role_id = kwargs.pop('role_id')
            verify_slice_role(int(pk), role_id)
            return super().delete_headless(pk)
        else:
            try:
                protect()(api_func)(self, pk, **kwargs)
                DeleteChartCommand(pk).run()
                return self.response(200, message="OK")
            except ChartNotFoundError:
                return self.response_404()
            except ChartForbiddenError:
                return self.response_403()
            except ChartDeleteFailedError as ex:
                logger.error(
                    "Error deleting model %s: %s",
                    self.__class__.__name__,
                    str(ex),
                    exc_info=True,
                )
                return self.response_422(message=str(ex))
