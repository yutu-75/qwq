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
@Time       : 2023/6/9 15:14
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Callable

import flask
from flask import request, Response
from flask_appbuilder.api import expose
from flask_login import login_user

from superset.cache_key import UserCacheKey
from superset.extensions import cache_manager, event_logger

from superset import conf
from superset.constants import SystemLoginType, LoginMethod, SystemConfigType
from superset.exceptions import HTTPError
from superset.utils.decorators import authenticated
from superset.v2.login.schemas import LoginSchema
from superset.sys_manager.sys_config.dao import SysConfigDAO
from superset.v2.user.dao import UserV2DAO
from superset.v2.utils.params_utils import aes_decryption
from superset.v2.utils.req_utils import get_cas_user_info
from superset.views.base_api import BaseSupersetBaseApi, statsd_metrics

logger = logging.getLogger(__name__)


class LoginRestApi(BaseSupersetBaseApi):
    resource_name = "user"
    openapi_spec_component_schemas = (
        LoginSchema,
    )

    @expose("/<int:user_id>/account/lock", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    def del_account_lock(self, user_id: int):
        """Delete Account Lock
        ---
        delete:
          description: >-
            Delete Account Lock
          parameters:
          - in: path
            schema:
              type: integer
            name: user_id
            description: user id
          responses:
            200:
              description: Item deleted
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
            404:
              $ref: '#/components/responses/404'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        user = UserV2DAO.find_by_id(user_id)
        if user:
            cache_key = UserCacheKey.ACCOUNT_LOCK_KEY % user.username
            cache = cache_manager.cache_read_client
            cache.delete(cache_key)

        return self.format_response(200)

    @expose("/login/", methods=("POST",))
    @statsd_metrics
    @event_logger.log_this_with_extra_payload
    def post(
        self,
        add_extra_log_payload: Callable[..., None] = lambda **kwargs: None
    ) -> Response:
        """Response
        ---
        post:
          description: 用户登录
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/LoginSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        # 登录失败次数限制
        item = LoginSchema().load(request.json)
        cache_key = UserCacheKey.ACCOUNT_LOCK_KEY % item["username"]
        cache = cache_manager.cache_read_client
        times = int(cache.get(cache_key) or 0)
        # 从数据库更新配置项
        system_param = SysConfigDAO.find_by_type(SystemConfigType.SYSTEM_PARAM)
        if system_param:
            conf.update({item.param_key: item.param_value for item in system_param})

        if times >= int(conf["NUM_OF_LOGIN_FAILURES"]):
            ttl = cache.ttl(cache_key)
            add_extra_log_payload(
                action="用户登录",
                message=f"账户已被锁定，请{int(ttl/60)}分钟后在登陆"
            )
            raise HTTPError(f"账户已被锁定，请{int(ttl/60)}分钟后在登陆", 400)

        user = None
        if item["type"] == LoginMethod.DB:
            logger.info(item)
            pwd = aes_decryption(item["password"])
            user = self.appbuilder.sm.auth_user_db(item["username"], pwd)

        elif item["type"] == LoginMethod.LDAP:
            ldap = SysConfigDAO.find_by_type(SystemLoginType.LOGIN_LDAP)
            if ldap:
                conf.update({item.param_key: item.param_value for item in ldap})

            user = self.appbuilder.sm.auth_user_ldap(
                item["username"], item["password"]
            )

        elif item["type"] == LoginMethod.CAS:
            cas = SysConfigDAO.find_by_type(SystemLoginType.LOGIN_CAS)
            if cas:
                conf.update({item.param_key: item.param_value for item in cas})

            pwd = aes_decryption(item["password"])
            user_info = get_cas_user_info(item["username"], pwd)
            user = self.appbuilder.sm.auth_user_remote_user(item["username"]) \
                if user_info else None

        if user:
            login_user(user, remember=False)
            prefix = self.appbuilder.app.config["STATIC_ASSETS_PREFIX"]
            cache.delete(cache_key)  # 重置登陆失败次数
            add_extra_log_payload(
                action="用户登录",
                message=f"{item['type']}登陆成功"
            )
            return self.format_response(
                200,
                data={
                    "uri": prefix + "/superset/welcome/" if prefix else "/superset/welcome/"
                }
            )

        if times > 0:
            times = cache.incr(cache_key, 1)
        else:
            timeout = int(float(conf["LOGIN_FAILURE_TIME"]) * 60 * 60)
            cache.setex(cache_key, timeout, 1)
            times = 1

        message = f"用户名或密码错误。剩余{int(conf['NUM_OF_LOGIN_FAILURES']) - times}次登陆失败将会锁定账号登录"
        add_extra_log_payload(
            action="用户登录",
            message=message
        )
        raise HTTPError(message, 400)

    @expose("/cas/login/", methods=("GET",))
    @statsd_metrics
    @event_logger.log_this_with_extra_payload
    def cas(
        self,
        add_extra_log_payload: Callable[..., None] = lambda **kwargs: None
    ) -> Response:
        """Response
        ---
        get:
          description: 用户登录
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        cas = SysConfigDAO.find_by_type(SystemLoginType.LOGIN_CAS)
        if cas:
            conf.update({item.param_key: item.param_value for item in cas})

        flask.session['CAS_AFTER_LOGIN_SESSION_URL'] = (
            flask.request.script_root +
            conf["CAS_AFTER_LOGIN"]
        )
        add_extra_log_payload(
            action="用户登录",
            message="CAS登录成功"
        )
        return self.format_response(
            200,
            data={"url": flask.url_for('cas.login', _external=True)}
        )
