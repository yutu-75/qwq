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
import datetime
import logging
from flask_babel import gettext as __

from flask import request, Response
from flask_appbuilder.api import expose, safe
from marshmallow import ValidationError

from superset import conf
from superset.dashboards.dao import DashboardDAO
from superset.dashboards.share.commands.create import CreateDashboardShareCommand
from superset.dashboards.share.commands.update import UpdateDashboardShareCommand
from superset.dashboards.share.dao import DashboardShareDAO
from superset.embedded.dao import EmbeddedDAO
from superset.extensions import event_logger
from flask_appbuilder.security.decorators import protect

from superset.security.api import GuestTokenCreateSchema
from superset.views.base_api import (
    statsd_metrics,
    BaseSupersetApi
)
from superset.dashboards.share.schemas import (
    DashboardsShareGetSchema, DashboardsShareSetPWDSchema,
    DashboardsShareResetPWDSchemaMax20, DashboardsShareResetExpirySchema,
)
from superset.utils.generate import Passwd

logger = logging.getLogger(__name__)

Thedashboarddoesnotexist = "The dashboard does not exist"
Thedashboardsharedoesnotexist = "The dashboard share does not exist"


class DashboardsShareRestApi(BaseSupersetApi):
    class_permission_name = "DashboardsShareRestApi"
    resource_name = "dashboard"
    openapi_spec_tag = "Dashboard Share"
    allow_browser_login = True
    openapi_spec_component_schemas = (

        DashboardsShareGetSchema,
        DashboardsShareSetPWDSchema,
    )

    @expose("/<dashboard_id>/share", methods=["POST"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.share",
        log_to_statsd=False,
    )
    def share_dashboard(self, dashboard_id: int) -> Response:
        """Creates a new Dashboard Share
        ---
        post:
          description: >-
            Creates a new Dashboard Share.
          parameters:
          - in: path
            schema:
              type: integer
            name: dashboard_id
          responses:
            200:
              description: Dashboard share added
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      id:
                        type: number
                      result:
                        $ref: '#/components/schemas/DashboardsShareGetSchema'
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        dashboard = DashboardDAO.get_dashboard_by_id(dashboard_id)
        if dashboard is None:
            return self.response_400(message=Thedashboarddoesnotexist)

        http_origin = request.headers.environ.get("HTTP_ORIGIN") or ""
        assets_prefix = conf['STATIC_ASSETS_PREFIX']
        url = f"{http_origin}{assets_prefix}/superset/share/dashboard/{dashboard_id}/"

        dashboard_share = dashboard.dashboard_share
        if dashboard_share:
            if dashboard_share[0].url != url:
                UpdateDashboardShareCommand(
                    dashboard_share[0], {"url": url}).run()
            return self.response(200, result=dashboard_share[0].to_json())

        pwd = Passwd.create_password()
        dashboard_share = {
            "dashboard_id": dashboard_id,
            "url": url,
            "password": pwd
        }
        new_dashboard_share = CreateDashboardShareCommand(dashboard_share).run()
        dashboard_share["id"] = new_dashboard_share.id
        EmbeddedDAO.upsert(dashboard, [])
        return self.response(200, result=new_dashboard_share.to_json())

    @expose("/<dashboard_id>/login", methods=["POST"])
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.login",
        log_to_statsd=False,
    )
    @statsd_metrics
    def login(self, dashboard_id: int) -> Response:
        """Dashboard Share Login
        ---
        post:
          description: >-
            将返回的token加入headers(headers={Token: XXXXXX})在请求接口,
          parameters:
          - in: path
            schema:
              type: integer
            name: dashboard_id
          requestBody:
            description: Dashboard Share Password
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardsShareResetPWDSchema'
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        type: object
                        properties:
                          embedded_uuid:
                            type: string
                          token:
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
        dashboard_share = DashboardShareDAO.find_by_dashboard_id(dashboard_id)
        if not dashboard_share:
            return self.response_400(message=Thedashboardsharedoesnotexist)

        dashboard = dashboard_share.dashboard
        if not dashboard:
            return self.response_400(message=Thedashboarddoesnotexist)

        try:
            item = DashboardsShareResetPWDSchemaMax20().load(request.json)
        except ValidationError as error:
            return self.response_400(message=error.messages)

        time_delta = dashboard_share.start_time + datetime.timedelta(
            seconds=dashboard_share.expiry)
        is_expiry = datetime.datetime.now() > time_delta

        error_str = __("The sharing link has expired.")

        if not dashboard_share.is_permanent and is_expiry:
            return self.response_400(message=error_str)

        if item["password"] == dashboard_share.password:
            uuid = str(dashboard.embedded[0].uuid)
            param = {
                "user": {
                    "username": "guest_user",
                    "first_name": "guest_user",
                    "last_name": "guest_user",
                    "is_admin": False,
                    "id": 1
                },
                "resources": [
                    {
                        "type": "dashboard",
                        "id": uuid
                    }
                ],
                "rls": []
            }
            try:
                body = GuestTokenCreateSchema().load(param)
            except ValidationError as error:
                return self.response_400(message=error.messages)

            self.appbuilder.sm.validate_guest_token_resources(body["resources"])
            token = self.appbuilder.sm.create_guest_access_token(
                body["user"], body["resources"], body["rls"]
            )
            return self.response(200, result={
                "token": token,
                "embedded_uuid": uuid
            })

        return self.response_400(message="password error.")

    @expose("/<dashboard_id>/share_reset_pwd", methods=["POST"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs:
        f"{self.__class__.__name__}.share_reset_pwd",
        log_to_statsd=False,
    )
    def share_reset_pwd(self, dashboard_id: int) -> Response:
        """Reset Dashboard Share Password
        ---
        post:
          description: >-
            Reset Dashboard Share Password
          parameters:
          - in: path
            schema:
              type: integer
            name: dashboard_id
          requestBody:
            description: Old Dashboard Share Password
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardsShareResetPWDSchema'
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/DashboardsShareResetPWDSchema'
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        dashboard_share = DashboardShareDAO.find_by_dashboard_id(dashboard_id)
        if not dashboard_share:
            return self.response_400(message=Thedashboardsharedoesnotexist)

        dashboard = dashboard_share.dashboard
        if not dashboard:
            return self.response_400(message=Thedashboarddoesnotexist)

        pwd = {
            "password": Passwd.create_password_pwd()
        }
        DashboardShareDAO.update(dashboard_share, pwd)
        return self.response(200, result=pwd)

    @expose("/<dashboard_id>/share_set_pwd", methods=["POST"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.share_set_pwd",
        log_to_statsd=False,
    )
    def share_set_pwd(self, dashboard_id: int) -> Response:
        """Set Dashboard Share Password
        ---
        post:
          description: >-
            Set Dashboard Share Password
          parameters:
          - in: path
            schema:
              type: integer
            name: dashboard_id
          requestBody:
            description: New Dashboard Share Password
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardsShareSetPWDSchema'
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/DashboardsShareSetPWDSchema'
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        try:
            item = DashboardsShareResetPWDSchemaMax20().load(request.json)
        except ValidationError as error:
            return self.response_400(message=error.messages)
        dashboard_share = DashboardShareDAO.find_by_dashboard_id(dashboard_id)
        if not dashboard_share:
            return self.response_400(message=Thedashboardsharedoesnotexist)

        dashboard = dashboard_share.dashboard
        if not dashboard:
            return self.response_400(message=Thedashboarddoesnotexist)

        pwd = {
            "password": item["password"]
        }
        DashboardShareDAO.update(dashboard_share, pwd)
        return self.response(200, result=pwd)

    @expose("/<dashboard_id>/share_set_expiry", methods=["POST"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args,
                      **kwargs: f"{self.__class__.__name__}.share_set_expiry",
        log_to_statsd=False,
    )
    def share_set_expiry(self, dashboard_id: int) -> Response:
        """Set Dashboard Share Expiry
        ---
        post:
          description: >-
            Set Dashboard Share Expiry
          parameters:
          - in: path
            schema:
              type: integer
            name: dashboard_id
          requestBody:
            description: Dashboard Share Expiry
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DashboardsShareResetExpirySchema'
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/DashboardsShareResetExpirySchema'
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        try:
            item = DashboardsShareResetExpirySchema().load(request.json)
        except ValidationError as error:
            return self.response_400(message=error.messages)
        dashboard_share = DashboardShareDAO.find_by_dashboard_id(dashboard_id)
        if not dashboard_share:
            return self.response_400(message=Thedashboardsharedoesnotexist)

        dashboard = dashboard_share.dashboard
        if not dashboard:
            return self.response_400(message=Thedashboarddoesnotexist)

        start_time = datetime.datetime.now()

        update_data = {
            "start_time": start_time,
            "expiry": item["expiry"]
        }
        result_data = DashboardShareDAO.update(dashboard_share, update_data).to_json()

        return self.response(200, result=result_data)

    @expose("/<dashboard_id>/check_expiry", methods=["GET"])
    # @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.check_expiry",
        log_to_statsd=False,
    )
    def check_expiry(self, dashboard_id: int) -> Response:
        """Check Dashboard Share Expiry
        ---
        post:
          description: >-
            Check Dashboard Share Expiry
          parameters:
          - in: path
            schema:
              type: integer
            name: dashboard_id
          responses:
            200:
              content:
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """

        dashboard_share = DashboardShareDAO.find_by_dashboard_id(dashboard_id)
        if dashboard_share is None:
            return self.response_400(message=Thedashboarddoesnotexist)

        time_delta = dashboard_share.start_time + datetime.timedelta(
            seconds=dashboard_share.expiry)
        is_expiry = datetime.datetime.now() > time_delta

        result_data = {
            "is_expiry": is_expiry,
            "start_time": dashboard_share.start_time,
            "expiry": dashboard_share.expiry,
            "dashboard_id": dashboard_id,
            "is_permanent": dashboard_share.is_permanent

        }

        return self.response(200, result=result_data)
