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
from typing import Optional, Any

from flask import request, g, redirect, session, make_response, get_flashed_messages
from flask_appbuilder import Model
from flask_appbuilder.const import LOGMSG_WAR_SEC_LOGIN_FAILED
from flask_appbuilder.security.views import expose, AuthView
from flask_login import login_user, current_user
from pymysql import IntegrityError
from sqlalchemy import and_
from werkzeug.security import generate_password_hash

from superset.security import SupersetSecurityManager
from superset import db
from .constants import SystemLoginType, GET_DASHBOARD_VIEW_URL_FORMAT
from .ichangan_util import IChangAnUtil
from .models.user import UserV2
from .utils.request_api import get_caps_user_info, get_cds_user_info, get_upm_user_name, \
    get_token, get_cmp_user_by_token
from .utils.user_management.public_user_registration import (
    register_user_publicly,
    add_user_permissions
)

logger = logging.getLogger(__name__)


class LoginView(AuthView):
    login_template = "superset/spa.html"

    @expose("/login/", methods=["GET"])
    def login(self):
        if g.user is not None and g.user.is_authenticated:
            return redirect(self.appbuilder.get_url_for_index)

        username = session.get('CAS_USERNAME')
        if username:
            user: Optional[Any] = self.appbuilder.sm.auth_user_remote_user(username)
            if user:
                login_user(user, remember=False)

                if 'next' in request.args.keys():
                    return redirect(request.args['next'])
                else:
                    return redirect(self.appbuilder.get_url_for_index)

        next_ = request.args.get("next", False)
        token = (
            request.args.get("token", False) or
            request.headers.get("Token", "") or
            request.cookies.get("TOKEN", "")
        )
        system_type = request.args.get("system_type", "")
        logger.info(f"NEXT: {next_}")
        logger.info(f"TOKEN: {token}")
        logger.info(f"SYSTEM_TYPE: {system_type}")
        if token:
            if isinstance(token, list):
                token = token[0]

            if "Bearer" not in token:
                # 智积工具门户集成
                if "iic" in system_type:
                    data = get_cmp_user_by_token(token)
                    if data is not None and isinstance(data, dict):
                        user_enabled = data.get("enabled", False)
                        if user_enabled:
                            return self.url_redict(data)
                        else:
                            logger.warning(f"Current User Unactivated!")
                            return make_response("User Unactivated!", 401)

                    else:
                        logger.warning(f"Current User Unauthorized By CMP!")
                        return make_response("User Unauthorized By CMP!", 401)

                # 渝北工厂统一门户用户登录集成
                else:
                    data = get_caps_user_info(token)
                    if data is not None and isinstance(data, dict):
                        return self.url_redict(data)
                    else:
                        logger.warning(f"Current User Unauthorized By Yb!")
                        return make_response("User Unauthorized By Yb!", 401)

            # CDS盖亚门户集成自助BI平台主页
            else:
                _token = token.split("Bearer ")[-1]
                data = get_cds_user_info(token)
                if data is not None and isinstance(data, dict):
                    return self.url_redict(data)
                else:
                    logger.warning(f"Current User Unauthorized By GAIA!")
                    return make_response("User Unauthorized By GAIA", 401)

        elif isinstance(next_, str) and "token" in next_ and "rzxx" not in next_: # CDS盖亚门户集成自助BI
            token = get_token(next_)
            if token is not "":
                data = get_cds_user_info(token)
                if data is not None and isinstance(data, dict):
                    return self.url_redict(data)
                else:
                    logger.warning(f"Current User Unauthorized By GAIA!")
                    return make_response("User Unauthorized By GAIA", 401)
            else:
                logger.warning(f"Get User Token Fail!")
                return make_response("Get User Token Fail!", 401)

        # 集成CADDM看板挂载
        elif isinstance(next_, str) and "IdentityToken" in next_ and "rzxx" not in next_:
            parse_util = IChangAnUtil(next_)
            cmp_user = parse_util.get_cmp_user_by_token()
            if cmp_user:
                user = self.appbuilder.sm.auth_user_remote_user(cmp_user)
                if user:
                    login_res = login_user(
                        user,
                        remember=True,
                        duration=self.appbuilder.app.config.get("REMEMBER_TIMEOUT")
                    )
                    if login_res:
                        get_flashed_messages()
                        _url = (f"{self.appbuilder.app.config.get('STATIC_ASSETS_PREFIX', '')}"
                                + f"{GET_DASHBOARD_VIEW_URL_FORMAT.format(parse_util.get_dashboard_id)}")
                        get_flashed_messages()
                        return redirect(_url)

                    else:
                        logger.warning(
                            f"username: {cmp_user} Unactivated!")
                        return make_response("User Unactivated", 401)
                else:
                    return make_response("User does not exist", 401)
            else:
                return make_response("Illegal request", 401)

        elif next_ and request.cookies.get("X-Token", None):
            # upm登录
            x_token = request.cookies.get("X-Token", None)
            usid = request.cookies.get("usid", None)
            if x_token and usid:
                username = get_upm_user_name(
                    self.appbuilder.app.config["UMP_USER_INFO_URL"],
                    x_token,
                    usid
                )
                if username:
                    user = self.appbuilder.sm.auth_user_remote_user(username, is_admin=True)

                    # TODO 自主分析平台的权限需要细分,需要指定角色
                    if user:
                        login_user(user, remember=False)

                        if "next" in request.args.keys():
                            redirect_url = request.args["next"]
                            logger.info(f"redirect_url>>>>>{redirect_url}")
                            return redirect(redirect_url)
                        else:
                            logger.info(
                                f"redirect_url_for_index>>>>>{self.appbuilder.get_url_for_index}")
                            return redirect(self.appbuilder.get_url_for_index)

        elif isinstance(next_, str) and (
            "superset/dashboard/p/" in next_ or "superset/explore/p/" in next_):

            user = UserV2().get_user_by_cn_name("public_share")
            if not user:
                user = register_user_publicly()

            if "superset/dashboard/p/" in next_:
                add_user_permissions(user.id, next_, "dashboard")
            else:
                add_user_permissions(user.id, next_, "chart")
            login_user(user, remember=False)
            if "next" in request.args.keys():
                # 刷新“访问被拒绝”闪现消息
                get_flashed_messages()
                return redirect(request.args['next'])
            else:
                return redirect(self.appbuilder.get_url_for_index)

        elif next_ and "rzxx" in next_:
            parse_util = IChangAnUtil(next_)
            if parse_util.check_user_by_login_id:
                user = self.appbuilder.sm.find_user(username=parse_util.get_employee_number)
                if user:
                    login_res = login_user(
                        user, remember=True,
                        duration=self.appbuilder.app.config.get("REMEMBER_TIMEOUT")
                    )
                    if login_res:
                        get_flashed_messages()
                        return redirect(
                            f"{self.appbuilder.app.config.get('STATIC_ASSETS_PREFIX', '')}"
                            f"{GET_DASHBOARD_VIEW_URL_FORMAT.format(parse_util.get_dashboard_id)}"
                        )
                    else:
                        logger.warning(
                            f"username: {parse_util.get_employee_number} unactivated!")
                        return make_response("User unactivated", 401)
                else:
                    return make_response("User does not exist", 401)
            else:
                return make_response("Illegal request", 401)

        from .views.base import common_bootstrap_payload
        payload = {
            "common": common_bootstrap_payload(g.user),
            "login_methods": self.appbuilder.sm.get_login_methods(),
        }
        logger.debug(payload["login_methods"])
        return self.render_template(
            self.login_template,
            entry="spa",
            bootstrap_data=json.dumps(payload)
        )

    @expose("/logout/")
    def logout(self):
        session.clear()
        response = redirect(
            self.appbuilder.app.config.get(
                "LOGOUT_REDIRECT_URL", self.appbuilder.get_url_for_index
            )
        )
        response.set_cookie("TOKEN", "")
        return response

    def url_redict(self, _data):
        user_account = _data.get("loginID", False)
        if not user_account:
            user_account = _data.get("loginId", False)
        user = self.appbuilder.sm.auth_user_remote_user(user_account)
        if user:
            login_res = login_user(user, remember=True, duration=self.appbuilder.app.config.get('REMEMBER_TIMEOUT'))

            if login_res and 'next' in request.args.keys():
                get_flashed_messages()
                response = make_response(redirect(request.args['next']))
                response.set_cookie(
                    '_user_source',
                    self.appbuilder.app.config.get("CAPS"),
                    secure=True,
                    samesite='None')
                return response
            else:
                return redirect(self.appbuilder.get_url_for_index)
        else:
            logger.warning(f"Can't Find Current User In Certification Center!")
            return make_response("Can't Find Current User In Certification Center!", 401)


class CustomSsoSecurityManager(SupersetSecurityManager):
    logger.info("using customize my security manager")
    authdbview = LoginView
    user_model = UserV2
    from .v2.models.user_role import RoleV2
    role_model = RoleV2
    from .models.sys_config import SysConfig
    sys_config = SysConfig

    def has_access(self, permission_name: str = "", view_name: str = "") -> bool:
        """
        Check if current user or public has access to view or menu
        """
        if current_user.is_authenticated:
            return True

        return False

    def can_access(self, permission_name: str, view_name: str) -> bool:
        return True

    def can_access_all_queries(self) -> bool:
        return True

    def can_access_all_datasources(self) -> bool:
        return True

    def can_access_database(self, database: "Database") -> bool:
        return True

    def can_access_schema(self, datasource: "BaseDatasource") -> bool:
        return True

    def can_access_datasource(self, datasource: "BaseDatasource") -> bool:
        return True

    def can_access_table(self, database: "Database", table: "Table") -> bool:
        return True

    def raise_for_access(
        self,
        database: Optional["Database"] = None,
        datasource: Optional["BaseDatasource"] = None,
        query: Optional["Query"] = None,
        query_context: Optional["QueryContext"] = None,
        table: Optional["Table"] = None,
        viz: Optional["BaseViz"] = None,
    ) -> None:
        pass

    def raise_for_dashboard_access(self, dashboard: "Dashboard") -> None:
        dashboard.can_access()

    @staticmethod
    def can_access_based_on_dashboard(datasource: "BaseDatasource") -> bool:
        return True

    def raise_for_ownership(self, resource: Model) -> None:
        return True

    def get_login_methods(self):
        res = self.get_session.query(self.sys_config.config_type).filter(
            and_(
                self.sys_config.config_type.in_(SystemLoginType),
                self.sys_config.status == 1,
            )
        ).distinct()
        login_methods_contain_db = self.appbuilder.app.config.get("LOGIN_METHODS_CONTAIN_DB")
        ret = [item[0] for item in res.all()]
        if len(ret) == 0:
            ret = ["DB"]
        else:
            ret if not login_methods_contain_db else ret.append("DB")
        return ret

    def is_admin(self) -> bool:
        return g.user.is_admin

    def add_user(
        self,
        username,
        first_name,
        last_name,
        email,
        role,
        password="",
        hashed_password="",
        is_admin=False,
        cn_name="",
    ):
        """
            Generic function to create user
        """
        try:
            user = self.user_model()
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.active = True
            user.is_admin = is_admin
            user.cn_name = cn_name
            user.roles = role if isinstance(role, list) else [role]
            if hashed_password:
                user.password = hashed_password
            else:
                user.password = generate_password_hash(password)
            self.get_session.add(user)
            self.get_session.commit()
            return user
        except IntegrityError as ex:
            logger.error(ex)
            self.get_session.rollback()
            return None

    def find_user_by_id(self, user_id: int):
        return (
            self.get_session.query(self.user_model)
            .filter(self.user_model.id == user_id)
            .one_or_none()
        )

    def auth_user_remote_user(self, username, is_admin=False):
        """
                REMOTE_USER user Authentication

                :param is_admin:
                :param username: user's username for remote auth
                :type self: User model
                """
        user = self.find_user(username=username)

        # User does not exist, create one if auto user registration.
        if user is None and self.auth_user_registration:
            user = self.add_user(
                # All we have is REMOTE_USER, so we set
                # the other fields to blank.
                username=username,
                first_name=username,
                last_name="",
                email=str(username) + "@any3.com",
                role=self.find_role(self.auth_user_registration_role),
                cn_name=username,
                password=f"ichangan@ps_{str(username)[0]}",
                is_admin=is_admin
            )

        # If user does not exist on the DB and not auto user registration,
        # or user is inactive, go away.
        elif user is None or (not user.is_active):
            logger.info(LOGMSG_WAR_SEC_LOGIN_FAILED.format(username))
            return None

        self.update_user_auth_stat(user)
        return user
