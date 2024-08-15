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

from flask_appbuilder import has_access, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface

from superset.constants import MenuName
from superset.models.app_attributes import AppAttribute
from superset.superset_typing import FlaskResponse
from superset.sys_manager.menus.dao import SysMenuDAO
from superset.views.base import SupersetModelView, DeleteMixin


class AppAttributeModelView(SupersetModelView, DeleteMixin):
    route_base = "/application/management"
    datamodel = SQLAInterface(AppAttribute)

    @has_access
    @expose("/")
    def list(self) -> FlaskResponse:
        menu = SysMenuDAO.find_by_name(MenuName.DASHBOARD)
        menu.can_access()
        return super().render_app_template()
