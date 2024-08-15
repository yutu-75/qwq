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
@Time       : 2023/6/9 13:48
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask import g
from flask_appbuilder.menu import Menu

without_prefix_url = [
    "/application/management/",
    "/record/list/",
    "/csstemplatemodelview/list/",
    "/alert/list/",
    "/annotationlayer/list/"
]
# TODO 自动判断是否加前缀


class CustomMenu(Menu):
    def get_data(self, menu=None):
        if not g.user.is_authenticated:
            return []

        from superset import conf
        if menu is None:
            from superset.sys_manager.menus.commands.get_data_command import \
                SysMenuDataCommand
            menu = SysMenuDataCommand(g.user).run()

        res = []
        for item in menu:
            if item["name"] == "System Manager" or item["name"] == "Dataset":
                res.append({
                    "name": item["name"],
                    "icon": item["icon"],
                    "label": item["label"],
                    "url": conf["STATIC_ASSETS_PREFIX"] + item["url"],
                    "children": item["children"]
                })

            elif item["children"]:
                childs = [
                    {
                        "name": _["name"],
                        "icon": _["icon"],
                        "label": _["label"],
                        "url": _["url"] if _["url"] in without_prefix_url else conf["STATIC_ASSETS_PREFIX"] + _["url"]
                        if _["url"] else ""
                    } for _ in item["children"]
                ]

                res.append({
                    "name": item["name"],
                    "icon": item["icon"],
                    "label": item["label"],
                    "childs": childs,
                })

            else:
                res.append({
                    "name": item["name"],
                    "icon": item["icon"],
                    "label": item["label"],
                    "url": conf["STATIC_ASSETS_PREFIX"] + item["url"]
                    if item["url"] else "",
                })

        return res
