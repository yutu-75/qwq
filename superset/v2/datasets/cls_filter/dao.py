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
@Time       : 2023/5/15 17:59
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from superset.connectors.sqla.models import TableColumn
from superset.dao.base import BaseDAO
from superset.sys_manager.dept.dao import SysDeptDAO
from superset.v2.role.dao import RoleV2DAO
from superset.v2.user.dao import UserV2DAO


class CLSFilterDAO(BaseDAO):
    model_cls = TableColumn

    @staticmethod
    def get_cls_properties(data: dict) -> dict:
        res = {
            "users": [],
            "roles": [],
            "depts": [],
            "white_list": [],
            "cls_status": data.get("cls_status", 1)
        }
        if data["user_ids"]:
            res["users"] = UserV2DAO.find_by_ids(data["user_ids"])
        if data["role_ids"]:
            res["roles"] = RoleV2DAO.find_by_ids(data["role_ids"])
        if data["dept_ids"]:
            res["depts"] = SysDeptDAO.find_by_ids(data["dept_ids"])
        if data["white_list"]:
            res["white_list"] = UserV2DAO.find_by_ids(data["white_list"])

        return res
