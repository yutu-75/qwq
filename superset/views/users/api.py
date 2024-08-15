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
修改：陈果-2023-03-10
修改内容：修复使用过程中token过期问题
修改：陈果-2023-03-23
修改内容：还原session登录
"""
from flask import g, Response, request
from flask_appbuilder.api import BaseApi
from flask_appbuilder.api import expose, safe
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_jwt_extended.exceptions import NoAuthorizationError
from superset.views.base_api import BaseSupersetApi
from superset.views.utils import bootstrap_user_data
from .schemas import UserResponseSchema
from superset import appbuilder, db
from superset.models.user import UserV2
from superset.tripartite_attribute.tripartite_certification import \
    tripartite_certification

from superset.tripartite_attribute.tripartite_api_log import record_tripartite_api_log

user_response_schema = UserResponseSchema()


class CurrentUserRestApi(BaseSupersetApi):
    """An api to get information about the current user"""

    resource_name = "me"
    openapi_spec_tag = "Current User"
    openapi_spec_component_schemas = (UserResponseSchema,)

    @expose("/", methods=["GET"])
    @safe
    def get_me(self) -> Response:
        """Get the user object corresponding to the agent making the request
        ---
        get:
          description: >-
            Returns the user object corresponding to the agent making the request,
            or returns a 401 error if the user is unauthenticated.
          responses:
            200:
              description: The current user
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/UserResponseSchema'
            401:
              $ref: '#/components/responses/401'
        """
        try:
            if g.user is None or g.user.is_anonymous:
                return self.response_401()
        except NoAuthorizationError:
            return self.response_401()

        return self.response(200, result=user_response_schema.dump(g.user))

    @expose("/roles/", methods=["GET"])
    @safe
    def get_my_roles(self) -> Response:
        """Get the user roles corresponding to the agent making the request
        ---
        get:
          description: >-
            Returns the user roles corresponding to the agent making the request,
            or returns a 401 error if the user is unauthenticated.
          responses:
            200:
              description: The current user
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/UserResponseSchema'
            401:
              $ref: '#/components/responses/401'
        """
        try:
            if g.user is None or g.user.is_anonymous:
                return self.response_401()
        except NoAuthorizationError:
            return self.response_401()
        user = bootstrap_user_data(g.user, include_perms=True)
        return self.response(200, result=user)


class UserRestApi(BaseApi):
    """
    继承Flask-appbuilder原生用户视图类, 扩展用户操作的接口类
    """
    route_base = "/api/v1/users"
    datamodel = SQLAInterface(UserV2)
    include_route_methods = {
        "check_and_add",
        "check_and_del",
        "get_zzfx_user"
    }

    def response_401(self) -> Response:
        return self.response(401, result={
            "status": "Failed",
            "message": "Authentication failed",
        })

    @record_tripartite_api_log
    @expose("/check_and_add", methods=["POST"])
    @tripartite_certification
    @safe
    def check_and_add(self, **kwargs):
        """自助分析平台用户同步模块 判断用户是否创建, 没有则新增用户并给admin权限,密码默认为123456.
        :param kwargs:   tripartite为True 则为通过验证
        :return:
        ---
        post:
          description: >-
            自助分析平台用户同步模块 判断用户是否创建, 没有则新增用户并给admin权限,密码默认为123456.
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
          requestBody:
            description: 请求参数
            required: true
            content:
              application/json:
                schema:
                    type: object
                    properties:
                      users:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                            loginid:
                              type: string
          responses:
            200:
              description: 反回参数
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                          type: object
                          properties:
                            failed_list:
                              type: array
                              items:
                                type: string
                            message:
                              type: string
                            status:
                              type: string
                            success_list:
                              type: array
                              items:
                                type: string
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
        """
        tripartite = kwargs.pop('tripartite')
        if tripartite:
            data = request.get_json()
            users_list = data.get("users")
            failed_user_list = []
            success_user_list = []
            for user in users_list:
                loginid = user.get("loginid")
                user_models = UserV2.get_model_by_username(loginid)

                # 没有则新建用户
                if loginid and not user_models:
                    result = appbuilder.sm.add_user(
                        loginid,
                        user.get("name"),
                        user.get("name"),
                        f"{loginid}@{loginid}.com",
                        kwargs.get("role_id"),
                        is_admin=True,
                        cn_name=f"zzfx-{loginid}-{user.get('name')}",
                        password="t1)*>(T0mAjz",
                    )
                    if result:
                        success_user_list.append(loginid)
                    else:
                        failed_user_list.append(loginid)

                # 有用户没激活则激活用户
                elif not user_models.active and kwargs.get("role_id") == \
                    user_models.roles[0].id:
                    user_models.active = True
                    db.session.commit()
                    success_user_list.append(loginid)
                else:
                    failed_user_list.append(loginid)
            return self.response(200, result={
                "status": "Success",
                "message": "ok",
                "success_list": success_user_list,
                "failed_list": failed_user_list

            })
        else:
            return self.response_401()

    @record_tripartite_api_log
    @expose("/check_and_del", methods=["DELETE"])
    @tripartite_certification
    @safe
    def check_and_del(self, **kwargs):
        """自助分析平台用户同步模块,判断用户是否删除, 没有则逻辑删除(修改用户状态为未激活).
        :param kwargs:   tripartite为True 则为通过验证
        :return:
        ---
        delete:
          description: >-
            自助分析平台用户同步模块,判断用户是否删除, 没有则逻辑删除(修改用户状态为未激活).
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
          requestBody:
            description: 请求参数
            required: true
            content:
              application/json:
                schema:
                    type: object
                    properties:
                      users:
                        type: array
                        items:
                          type: string

          responses:
            200:
              description: 反回参数
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                          type: object
                          properties:
                            failed_list:
                              type: array
                              items:
                                type: string
                            message:
                              type: string
                            status:
                              type: string
                            success_list:
                              type: array
                              items:
                                type: string
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
        """

        tripartite = kwargs.pop('tripartite')
        if tripartite:
            data = request.get_json()
            users_list = data.get("users")
            failed_user_list = []
            success_user_list = []
            for loginid in users_list:
                user_models = UserV2.get_model_by_username(loginid)

                # 判断当前用户的角色和appKey是否一致并且是激活状态,是则修改用户状态
                if user_models and (
                    kwargs.get("role_id") == user_models.roles[0].id
                ) and user_models.active == True:
                    user_models.active = False
                    db.session.commit()
                    success_user_list.append(loginid)
                else:
                    failed_user_list.append(loginid)
            return self.response(200, result={
                "status": "Success",
                "message": "ok",
                "success_list": success_user_list,
                "failed_list": failed_user_list

            })
        else:
            return self.response_401()

    @record_tripartite_api_log
    @expose("/get_zzfx_user", methods=["GET"])
    @tripartite_certification
    @safe
    def get_zzfx_user(self, **kwargs):
        """自助分析平台 获取自助分析平台所有的用户.
        :param kwargs:   tripartite为True 则为通过验证
        :return:
        ---
        get:
          description: >-
            自助分析平台 获取自助分析平台所有的用户.
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
          responses:
            200:
              description: 反回参数
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                          type: object
                          properties:
                            message:
                              type: string
                            status:
                              type: string
                            user_data:
                              type: object
                              properties:
                                loginid:
                                  type: string
                                name:
                                  type: string
                                active:
                                  type: string
                                created_on:
                                  type: string
                                login_count:
                                  type: string
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
        """
        tripartite = kwargs.pop('tripartite')
        if tripartite:
            user_data = UserV2.get_zzfx_user()
            user_dicts = [
                {
                    "loginid": user.username, "name": user.first_name,
                    "active": user.active, "created_on": user.created_on,
                    "login_count": user.login_count
                } for user
                in user_data
            ]
            return self.response(200, result={
                "status": "Success",
                "message": "ok",
                "user_data": user_dicts,
            })
        else:
            return self.response_401()
