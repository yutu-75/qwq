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
import logging

from flask_appbuilder import Model

from superset import db
from superset.connectors.sqla.models import RowLevelSecurityFilter
from superset.dao.base import BaseDAO
from superset.datasets.models import Dataset
from superset.sys_manager.dept.dao import SysDeptDAO
from superset.v2.role.dao import RoleV2DAO
from superset.v2.user.dao import UserV2DAO

logger = logging.getLogger(__name__)


class RLSFilterDAO(BaseDAO):
    model_cls = RowLevelSecurityFilter

    @staticmethod
    def update_rls_properties(rls: Model, data: dict) -> Model:
        if data["user_ids"]:
            rls.users = UserV2DAO.find_by_ids(data["user_ids"])
        else:
            rls.users = []
        if data["role_ids"]:
            rls.roles = RoleV2DAO.find_by_ids(data["role_ids"])
        else:
            rls.roles = []
        if data["dept_ids"]:
            rls.depts = SysDeptDAO.find_by_ids(data["dept_ids"])
        else:
            rls.depts = []
        if data["white_list"]:
            rls.white_list = UserV2DAO.find_by_ids(data["white_list"])
        else:
            rls.white_list = []

        return rls

    @classmethod
    def add_rls_filter(cls, dataset: Dataset, data: dict) -> Model:
        rls = RLSFilterDAO.create({
            "filter_type": "Regular",
            "clause": data["clause"],
            "status": data.get("status", 0)
        }, commit=False)
        rls.tables = [dataset]
        rls = cls.update_rls_properties(rls, data)
        db.session.commit()
        return rls

    @classmethod
    def update_rls_filter(cls, rls: Model, data: dict) -> Model:
        rls = RLSFilterDAO.update(rls, {
            "clause": data["clause"],
            "status": data.get("status", 0)
        }, commit=False)
        rls = cls.update_rls_properties(rls, data)
        db.session.commit()
        return rls
