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

from flask import request, Response
from flask_appbuilder.api import expose, safe, rison, get_list_schema
from sqlalchemy.ext.declarative import declarative_base

from superset.dashboards.api import DashboardRestApi

from superset.dashboards.dao import DashboardDAO
from superset.dashboards.schemas import DashboardsUserAccessLevelResponseSchema
from superset.extensions import event_logger, db
from superset.models.user import UserV2

from superset.superset_typing import FlaskResponse
from superset.tripartite_attribute.tripartite_api_log import record_tripartite_api_log
from superset.tripartite_attribute.tripartite_certification import \
    tripartite_certification
from superset.v2.models.user_role import UserRole

from superset.views.base_api import (
    statsd_metrics,
    BaseSupersetApi
)

logger = logging.getLogger(__name__)

# 创建映射类
Base = declarative_base()


class DashboardsUserAccessLevelRestApi(DashboardRestApi):
    openapi_spec_tag = "Dashboard UserAccessLeve"
    dashboard_get_response_schema = DashboardsUserAccessLevelResponseSchema()
    include_route_methods = {
        "get_role_dashboards",
        "set_permissions",
        "del_dashboard",
        "copy_dashboard"
    }

    list_columns = DashboardRestApi.list_columns + [
        'created_on',
        'changed_on',
        'created_by.username'
    ]

    def response_401(self) -> Response:
        return self.response(401, result={
            "message": "Sign authentication failed, please calibrate the sign",
            "status": "Failed"
        })

    max_page_size = 10000 * 100

    @record_tripartite_api_log
    @expose("/simple", methods=["GET"])
    @tripartite_certification
    # @protect()
    @rison(get_list_schema)
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs:
        f"{self.__class__.__name__}.simple",
        log_to_statsd=False,
    )
    def get_role_dashboards(self, **kwargs) -> Response:
        """Get list of items from Model
        ---
        get:
          description: >-
            Get a list of models
          parameters:
          - name: appKey
            in: header
            description: 系统为应用分配自动分配密钥
            required: true
            schema:
              type: string
          - name: sign
            in: header
            description: 按照规则加密的签名
            required: true
            schema:
              type: string
          - name: timestamp
            in: header
            description: 时间戳，到毫秒
            required: true
            schema:
              type: string
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
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
        """
        tripartite = kwargs.pop('tripartite')
        role_id = kwargs.pop('role_id') if kwargs.get('role_id') else None

        if tripartite:
            if not role_id:
                return self.response_403()

            if not kwargs.get("rison"):
                kwargs["rison"] = {}
            kwargs["rison"]["page_size"] = self.max_page_size

            return super().get_list_headless(**kwargs)

            # 旧版代码备份
            # dashboard_ids = DashboardDAO.get_dashboard_ids()
            # result = [
            #     self.dashboard_get_response_schema.dump(
            #         i
            #     ) for i in dashboard_ids
            # ]
            # return self.response(200, result=result)
        else:
            return self.response_401()

    @record_tripartite_api_log
    @expose("/<dashboard_id>/permissions", methods=["POST"])
    @tripartite_certification
    # @protect()
    @safe
    def set_permissions(self, dashboard_id, **kwargs) -> Response:
        """
        设置一个或者多个人共享，也可设置当前角色共享，此接口为新增api
        @return:
        """
        tripartite = kwargs.pop('tripartite')
        role_id = kwargs.pop('role_id') if kwargs.get('role_id') else None

        if tripartite:
            if not role_id:
                return self.response_403()
            data = request.get_json()
            users_list = data.get('users')
            current_role = data.get('current_role')

            if "users" not in data.keys() or "current_role" not in data.keys():
                return self.response(400, result={
                    "status": "Failed",
                    "message": "The 'users' and' current_role 'parameters are incorrect"
                })

            users_models = db.session.query(UserV2).where(UserV2.username.in_(users_list)).all()
            result_users_list = []
            for i in users_models:
                result_users_list.append(
                    {
                        "id": i.id,
                        "username": i.username,
                        "first_name": i.first_name,
                        "last_name": i.last_name,
                    }
                )
            result = DashboardDAO.set_permissions(result_users_list, current_role, dashboard_id)
            if result == "ok":
                return self.response(200, result={"status": "Success",
                                                  "message": "ok",
                                                  "users": result_users_list
                                                  })
            else:
                return self.response(400, result={"status": "Failed",
                                                  "message": str(result)})

        else:
            return self.response_401()

    @record_tripartite_api_log
    @expose("/del/<pk>", methods=["DELETE"])
    @tripartite_certification
    # @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.delete",
        log_to_statsd=False,
    )
    def del_dashboard(self, pk: int, **kwargs) -> Response:
        """
        根据看板id删除对应数据
        @param pk: 看板id
        @return:
        """
        tripartite = kwargs.pop('tripartite')
        role_id = kwargs.pop('role_id') if kwargs.get('role_id') else None

        if tripartite:
            if not role_id:
                return self.response_403()
            result = DashboardDAO.delete_data(pk)
            if result == "ok":
                return self.response(200, result={"status": "Success",
                                                  "message": "ok"})
            else:
                return self.response(400, result={"status": "Failed",
                                                  "message": str(result)})
        else:
            return self.response_401()

    @record_tripartite_api_log
    @expose("/copy_dash/copy/<int:dashboard_id>", methods=["POST"])
    @tripartite_certification
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.delete",
        log_to_statsd=False,
    )
    def copy_dashboard(  # pylint: disable=no-self-use
        self, dashboard_id: int,
        **kwargs
    ) -> FlaskResponse:
        """
        根据看板id复制对应数据
        @param dashboard_id:
        @return:
        """
        tripartite = kwargs.pop('tripartite')
        role_id = kwargs.pop('role_id') if kwargs.get('role_id') else None

        if tripartite:
            if not role_id:
                return self.response_403()
            data = request.get_json()
            user = data.get('user')
            users_models = db.session.query(UserV2).where(
                UserV2.username == user).first()

            if not users_models or not is_user_in_role(users_models.id):
                return self.response(400, result={"status": "Failed",
                                                  "message": "The [user] parameter is incorrect"})
            result = DashboardDAO.copy_data(dashboard_id, users_models)
            if result == "ok":
                return self.response(200, result={"status": "Success",
                                                  "message": "ok"})
            else:
                return self.response(400, result={"status": "Failed",
                                                  "message": str(result)})
        else:
            return self.response_401()


def is_user_in_role(user_id):

    dashboard_user_access_levels_models = DashboardDAO.get_app_attribute_models()
    users = db.session.query(UserRole.user_id).filter(
        UserRole.user_id == user_id,
        UserRole.role_id == dashboard_user_access_levels_models.role_id,
    ).all()

    return bool(users)

