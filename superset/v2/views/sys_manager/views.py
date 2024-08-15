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
@Time       : 2023/4/6 12:50
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json

from flask import g, abort
from flask_appbuilder import expose, BaseView

from superset.constants import MenuName
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.utils import core as utils
from superset.utils.decorators import authenticated
from superset.views.base import common_bootstrap_payload
from superset.views.utils import bootstrap_user_data


class SysManagerBaseView(BaseView):
    route_base = "/sys"

    @expose("/manager/", methods=("GET",))
    @authenticated()
    def manager(self):
        menu = SysMenuDAO.find_by_name(MenuName.SYSTEM_MANAGER)
        menu.can_access()
        payload = {
            "user": bootstrap_user_data(g.user, include_perms=False),
            "common": common_bootstrap_payload(g.user),
        }
        return self.render_template(
            "superset/spa.html",
            entry="spa",
            bootstrap_data=json.dumps(
                payload, default=utils.pessimistic_json_iso_dttm_ser
            ),
        )

    @expose("/logs/", methods=("GET",))
    @authenticated()
    def logs(self):
        payload = {
            "user": bootstrap_user_data(g.user, include_perms=False),
            "common": common_bootstrap_payload(g.user),
        }
        return self.render_template(
            "superset/spa.html",
            entry="spa",
            bootstrap_data=json.dumps(
                payload, default=utils.pessimistic_json_iso_dttm_ser
            ),
        )

    @expose("/watermark", methods=("GET",))
    @authenticated()
    def watermark(self):
        if not g.user.is_admin:
            return abort(404)

        payload = {
            "user": bootstrap_user_data(g.user, include_perms=False),
            "common": common_bootstrap_payload(g.user),
        }
        return self.render_template(
            "superset/spa.html",
            entry="spa",
            bootstrap_data=json.dumps(
                payload, default=utils.pessimistic_json_iso_dttm_ser
            ),
        )
