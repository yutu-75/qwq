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
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging

from flask import g, request, Response
from flask_appbuilder.api import expose

from superset.extensions import event_logger
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.sys_manager.sys_config.commands.get_data_command import SysConfigInfoCommand
from superset.sys_manager.sys_config.commands.update import SysConfigUpdateCommand
from superset.sys_manager.sys_config.schemas import (
    SysConfigPutSchema,
    SysConfigGetSchema
)
from superset.views.base_api import (
    requires_json,
    statsd_metrics,
    BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class SysConfigRestApi(BaseSupersetBaseApi):
    resource_name = "sys/config"
    openapi_spec_component_schemas = (
        SysConfigGetSchema,
        SysConfigPutSchema,
    )

    @expose("/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get(self) -> Response:
        """Response
        ---
        get:
          description: 查询系统配置信息
          parameters:
            - in: query
              description: 参数类型（WATER_MARK：水印）
              schema:
                type: string
              name: type
              default: WATER_MARK
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      meta:
                        type: object
                        properties:
                          code:
                            type: integer
                          message:
                            type: string
                          data:
                            type: object
                            properties:
                              TEXT:
                                type: string
                              SIZE:
                                type: string
                              COLOR:
                                type: string
                              SPACE:
                                type: string
                                description: 水印文字间隔
                              ANGLE:
                                type: string
                                description: 水印文字旋转角度
        """
        _type = request.args.get("type", None)
        data = SysConfigInfoCommand(g.user, _type).run()
        return self.format_response(200, data=data)

    @expose("/", methods=("PUT",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_EDIT_SYS_CONFIG,
        log_to_statsd=False,
    )
    @requires_json
    def put(self) -> Response:
        """
        ---
        put:
          description: 编辑或新增系统配置
          requestBody:
            description:
              "<br>
              1. LOGIN_LDAP: {<br>
                    'AUTH_LDAP_SERVER': '',<br>
                    AUTH_LDAP_SEARCH = 'dc=example,dc=org',<br>
                    AUTH_LDAP_UID_FIELD = 'cn',<br>
                    AUTH_LDAP_USERNAME_FORMAT = 'cn=%s',<br>
                    AUTH_LDAP_BIND_USER = 'cn=watcher,dc=example,dc=org',<br>
                    AUTH_LDAP_BIND_PASSWORD = '' ,<br>
                } <br>
              2. LOGIN_CAS: {<br>
                   'CAS_SERVER': 'http://caddmuat.changan.com.cn',<br>
                   'CAS_LOGIN_ROUTE': '/cas/login',<br>
                   'CAS_AFTER_LOGIN' 'http://devlocal.changan.com.cn:30010/login/',<br>
                   'CAS_LOGOUT_ROUTE': '/cas/logout',<br>
                   'CAS_AFTER_LOGOUT': 'http://devlocal.changan.com.cn:30010/login/',<br>
                }<br>
              3. WATER_MARK: {<br>
                TEXT = 长安水印logo<br>
                COLOR = '#8B8B1B'<br>
                SIZE = 30<br>
                OPACITY = 0.5<br>
                SPACE = 400<br>
                ANGLE = 50<br>
                PDF_WIDTH = 1200<br>
                PDF_HIGH = 2000<br>
                }<br>
              "
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/SysConfigPutSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = SysConfigPutSchema().load(request.json)
        SysConfigUpdateCommand(g.user, item).run()
        return self.format_response(200)
