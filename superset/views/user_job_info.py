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
修改：李洪浩2022-12-20
修改内容：新增UserJobInfoFiltersModelView模型视图，方便前端进行增删改查
"""

from flask import current_app
from flask_appbuilder import BaseView, Model, ModelView
from flask_appbuilder.actions import action
from flask_appbuilder.models.sqla.filters import BaseFilter
from flask_appbuilder.security.sqla.models import User
from flask_babel import lazy_gettext as _, gettext as __
from superset.models.user_job_info_model import UserJobInfo
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqual, FilterNotEqual
from superset.views.base import DeleteMixin, SupersetModelView
from superset.views.base import DeleteMixin, SupersetListWidget
from typing import Any, cast


class UserJobInfoListWidget(
    SupersetListWidget
):  # pylint: disable=too-few-public-methods
    template = "superset/models/rls/list.html"

    def __init__(self, **kwargs: Any):
        kwargs["appbuilder"] = current_app.appbuilder
        super().__init__(**kwargs)


class UserJobInfoFiltersModelView(SupersetModelView, DeleteMixin):
    # route_base = "/userjobinfofilters"
    datamodel = SQLAInterface(UserJobInfo)

    list_widget = cast(SupersetListWidget, UserJobInfoListWidget)

    list_title = _("User job info filter")
    show_title = _("Show User job info filter")
    add_title = _("Add User job info filter")
    edit_title = _("Edit User job info filter")

    # 定义前端model list页面显示的列, my_name为自定义样式的一列
    # list_columns = ["user_account", "user_name", "user_type", "position_name",
    #                 "organization_code", "organization_name",
    #                 "invest_code", "invest_name",
    #                 "parent_dept_code", "dept_code", "dept_name", "dept_level",
    #                 "active", "remarks", "creator", "modified"]

    list_columns = ["user_account", "user_name", "user_type",
                    "organization_code", "invest_code",
                    "dept_code", "dept_name",
                    "active", "creator", "modified"]

    edit_columns = ["user_account", "user_name", "user_type", "position_name",
                    "organization_code", "organization_name",
                    "invest_code", "invest_name",
                    "parent_dept_code", "dept_code", "dept_name", "dept_level",
                    "active", "remarks"]

    show_columns = edit_columns
    add_columns = edit_columns
    # # 定义在前端显示时，model的列，显示成一个新别名, my_name为模型中自定义显示的内容
    # label_columns = {"user_account": "用户账号", "user_name": "姓名", "user_type": "用户类型",
    #                  "organization_code": "组织编码", "organization_name": "组织名称",
    #                  "invest_code": "经销商集团编码", "invest_name": "经销商集团名称",
    #                  "parent_dept_code": "父部门编码", "dept_code": "部门编码",
    #                  "dept_name": "部门名称", "dept_level": "部门级别编码",
    #                  "position_name": "职务名称",
    #                  "active": "是否激活",
    #                  "created_on": "创建时间", "changed_on": "修改时间",
    #                  "remarks": "备注信息"}

    # 定义表中字段翻译时名称
    label_columns = {
        "user_account": _("user account"),
        "user_name": _("user name"),
        "user_type": _("user type"),
        "organization_code": _("organization code"),
        "organization_name": _("organization name"),
        "invest_code": _("investment code"),
        "invest_name": _("investment name"),
        "parent_dept_code": _("parent department code"),
        "dept_code": _("department code"),
        "dept_name": _("department name"),
        "dept_level": _("department level"),
        "position_name": _("position name"),
        "active": _("active status"),
        "created_on": _("created time"),
        "remarks": _("remarks"),
        "creator": _("Creator"),
        "modified": _("Modify time"),
    }

    description_columns = {
        "user_account": _("Used to associate the account number in the user table"),
        "user_name": _("Full name of the user"),
        "user_type": _("Determine whether the user is internal or external, an administrator or a regular employee"),
        "position_name": _("User's job title"),
        "organization_code": _("Division or company code of the user"),
        "organization_name": _("Name of the division or company the user belongs to"),
        "invest_code": _("The code of the dealer group to which the user belongs"),
        "invest_name": _("The name of the dealer group to which the user belongs"),
        "parent_dept_code": _("Parent department code of the user's department"),
        "dept_code": _("User's department code or dealer code"),
        "dept_name": _("User's department name or dealer name"),
        "dept_level": _("User's department level"),
        "active": _("It's not a good policy to remove a user, just make it inactive"),
        "remarks": _("The user extra information"),
    }

    base_filters = [["user_account", FilterNotEqual, ''], ]  # 过滤掉空账号
    order_columns = ["user_type", "organization_code", "invest_code", "dept_level", "modified"]
    base_order = ('id', 'desc')

    search_exclude_columns = ["created_on", "changed_on", "remarks"]

