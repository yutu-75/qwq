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
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from datetime import datetime
from io import BytesIO
from typing import Callable

from flask import g, request, Response, current_app, send_file
from flask_appbuilder.api import expose

from superset.constants import MenuName
from superset.exceptions import HTTPError
from superset.extensions import event_logger
from superset.global_messages import Messages
from superset.logs_messages import LogsMessages
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.utils.decorators import authenticated
from superset.v2.user.commands.create import (
    CreateUserV2Command,
    ImportUsersCommand
)
from superset.v2.user.commands.delete import DeleteUserV2Command
from superset.v2.user.commands.get_data_command import (
    UserV2ListCommand,
    UserV2InfoCommand
)
from superset.v2.user.commands.update import (
    UpdateUserV2Command,
    UpdateUserActiveCommand
)
from superset.v2.user.schemas import (
    UserV2GetResponseSchema,
    UserV2PostSchema,
    UserV2PutSchema,
    UserActivePatchSchema, UserSearchSchema
)
from superset.views.base_api import (
    requires_json,
    statsd_metrics,
    BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class UserV2RestApi(BaseSupersetBaseApi):
    resource_name = "user"
    openapi_spec_component_schemas = (
        UserV2PostSchema,
        UserV2PutSchema,
        UserV2GetResponseSchema,
        UserActivePatchSchema,
    )

    @expose("/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """Response
        ---
        get:
          description: 查询用户列表
          parameters:
            - in: query
              schema:
                type: integer
              name: page_size
              description: 页大小
            - in: query
              schema:
                type: integer
              name: page_index
              description: 页码
            - in: query
              schema:
                type: string
              name: username
              description: 用户名
            - in: query
              schema:
                type: integer
              name: role_id
            - in: query
              schema:
                type: integer
              name: dept_id
            - in: query
              schema:
                type: integer
              name: filter_role_id
            - in: query
              schema:
                type: integer
              name: filter_dept_id
          responses:
            200:
              description: User
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/UserV2GetResponseSchema'
        """
        item = UserSearchSchema().load(request.args)
        data = UserV2ListCommand(g.user, **item).run()
        return self.format_response(200, data=data)

    @expose("/<pk>/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_info(self, pk: str) -> Response:
        """Response
        ---
        get:
          description: >-
            查询用户信息, 需要用户管理菜单权限
          parameters:
            - in: path
              schema:
                type: string
              name: pk
          responses:
            200:
              description: User
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/UserV2GetResponseSchema'
        """
        data = UserV2InfoCommand(g.user, pk).run()
        return self.format_response(200, data=data)

    @expose("/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_extra_payload
    @requires_json
    def post(
        self,
        add_extra_log_payload: Callable[..., None] = lambda **kwargs: None
    ) -> Response:
        """
        ---
        post:
          description: >-
            新增用户, 需要用户管理菜单权限
          requestBody:
            description: User schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UserV2PostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """

        item = UserV2PostSchema().load(request.json)
        CreateUserV2Command(g.user, item).run()
        add_extra_log_payload(
            action=LogsMessages.LM_ADD_USER,
            message=LogsMessages.SUCCESS,
            username=item["username"],
            cn_name=item["cn_name"]
        )
        return self.format_response(200)

    @expose("/<pk>/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_extra_payload
    @requires_json
    def put(
        self,
        pk: int,
        add_extra_log_payload: Callable[..., None] = lambda **kwargs: None
    ) -> Response:
        """
        ---
        put:
          description: 编辑用户信息, 需要用户管理菜单权限
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          requestBody:
            description: User schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UserV2PutSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = UserV2PutSchema().load(request.json)
        UpdateUserV2Command(g.user, pk, item).run()
        add_extra_log_payload(
            action=LogsMessages.LM_EDIT_USER,
            message=LogsMessages.SUCCESS,
            username=item["username"],
            cn_name=item["cn_name"]
        )
        return self.format_response(200)

    @expose("/<int:user_id>/active/", methods=("PATCH",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_extra_payload
    @requires_json
    def patch(
        self,
        user_id: int,
        add_extra_log_payload: Callable[..., None] = lambda **kwargs: None
    ) -> Response:
        """
        ---
        patch:
          description: 编辑用户ACTIVE, 需要用户管理菜单权限
          parameters:
          - in: path
            schema:
              type: integer
            name: user_id
          requestBody:
            description: User schema
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UserActivePatchSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = UserActivePatchSchema().load(request.json)
        user = UpdateUserActiveCommand(g.user, user_id, item).run()
        add_extra_log_payload(
            action=LogsMessages.LM_EDIT_USER,
            message='用户激活' if item["active"] else '关闭用户',
            username=user.username,
            cn_name=user.cn_name
        )
        return self.format_response(200)

    @expose("/<pk>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_extra_payload
    def delete(
        self,
        pk: int,
        add_extra_log_payload: Callable[..., None] = lambda **kwargs: None
    ) -> Response:
        """
        ---
        delete:
          description: >-
            删除用户, 需要用户管理菜单权限
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        user = DeleteUserV2Command(g.user, pk).run()
        add_extra_log_payload(
            action=LogsMessages.LM_DEL_USER,
            message=LogsMessages.SUCCESS,
            username=user["username"],
            cn_name=user["cn_name"]
        )
        return self.format_response(200)

    @expose("/import/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_extra_payload
    def import_(self, add_extra_log_payload: Callable[..., None] = lambda **kwargs: None):
        """---
        post:
          description: 导入用户, 需要用户管理菜单权限
          requestBody:
            required: true
            content:
              multipart/form-data:
                schema:
                  type: object
                  properties:
                    formData:
                      description: upload file (xls or xlsx)
                      type: string
                      format: binary
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        upload = request.files.get("formData", False)
        if upload:
            file_type = upload.filename.split(".")[-1]
            if file_type in self.appbuilder.app.config["EXCEL_EXTENSIONS"]:
                ImportUsersCommand(g.user, upload).run()
                add_extra_log_payload(
                    action=LogsMessages.IMPORT_USERS,
                    message=LogsMessages.SUCCESS,
                )
                return self.format_response(200)

        add_extra_log_payload(
            action=LogsMessages.IMPORT_USERS,
            message=LogsMessages.FAIL,
        )
        raise HTTPError(Messages.FILE_TYPE_ERROR)

    @expose("/import/template/", methods=["GET"])
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EXPORT_USER_IMPORT_TEMPLATE,
        log_to_statsd=False,
    )
    def export(self) -> Response:
        """Export charts
        ---
        get:
          description: 下载导入用户模板，需要用户管理菜单权限
          responses:
            200:
              content:
                application/xlsx:
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
        menu = SysMenuDAO.find_by_name(MenuName.USER_MANAGEMENT)
        menu.can_access()
        with open(current_app.config['USER_IMPORT_TEMPLATE'], "br") as fp:
            buf = BytesIO(fp.read())

        timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
        filename = f"user_import_template_{timestamp}.xlsx"
        response = send_file(
            buf,
            mimetype="application/xlsx",
            as_attachment=True,
            download_name=filename,
        )
        return response
