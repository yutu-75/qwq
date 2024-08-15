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
@Time       : 2023/3/17 13:46
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask import Response, g
from flask_appbuilder.api import expose

from superset.sys_manager.menus.commands.get_data_command import \
    SysMenuSysManagerCommand, SysMenuDatasetCommand, SysMenuPermCommand
from superset.utils.decorators import authenticated
from superset.views.base_api import BaseSupersetBaseApi, statsd_metrics


class SysMenuRestApi(BaseSupersetBaseApi):
    resource_name = "menu"

    @expose(url="/sys/manager/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_manager(self) -> Response:
        """
        ---
        get:
          description: 获取Sys Manage子菜单
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
                            default: 200
                          message:
                            type: string
                            default: 'success'
                          data:
                            type: array
                            items:
                              type: object
                              properties:
                                id:
                                  type: integer
                                pid:
                                  type: integer
                                name:
                                  type: string
                                icon:
                                  type: string
                                label:
                                  type: string
        """
        data = SysMenuSysManagerCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/dataset/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_dataset(self) -> Response:
        """
        ---
        get:
          description: 获取数据集子菜单
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
                            default: 200
                          message:
                            type: string
                            default: 'success'
                          data:
                            type: array
                            items:
                              type: object
                              properties:
                                id:
                                  type: integer
                                pid:
                                  type: integer
                                name:
                                  type: string
                                icon:
                                  type: string
                                label:
                                  type: string
        """
        data = SysMenuDatasetCommand(g.user).run()
        return self.format_response(200, data=data)

    @expose(url="/<string:menu_name>/perm", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def get_menu_perm(self, menu_name: str) -> Response:
        """
        ---
        get:
          description: 获取菜单权限
          parameters:
          - in: path
            schema:
              type: string
            name: menu_name
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
                            default: 200
                          message:
                            type: string
                            default: 'success'
                          data:
                            type: object
                            properties:
                                perm:
                                  type: integer
        """
        data = SysMenuPermCommand(g.user, menu_name).run()
        return self.format_response(200, data={"perm": data})
