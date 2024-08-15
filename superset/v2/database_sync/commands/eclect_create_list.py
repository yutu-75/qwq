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


from typing import List, Any

from flask_appbuilder.security.sqla.models import User

from superset import db, conf
from superset.commands.base import BaseCommand
from superset.constants import AuthSourceType, VIEW
from superset.models.core import Database
from superset.v2.datasources.dao import DataSourceDAO


class GetDatabase(BaseCommand):
    def __init__(self, user: User):
        self._actor = user

    def run(self, **kwargs: Any) -> List[dict]:
        self.validate()
        res = DataSourceDAO.find_databases()
        databases = self.get_database_names()  # 调用get_database_names方法获取数据库信息
        if self._actor.is_admin:
            result = []
            for item in res:
                verbose_name = databases.get(item[0].name, "")
                if verbose_name:
                    id = item[0].database_id
                    db_type = databases.get(item[0].database_id, "")
                    result.append({
                        "id": id,
                        "verbose_name": verbose_name,
                        "type": db_type,
                    })
            return result

        data_auth = DataSourceDAO.find_auth_source_perm_by_user(
            AuthSourceType.DATASOURCE, self._actor.id, VIEW)
        return [
            {
                "id": item[0].database_id,
                "verbose_name": item[0].name,
                "type": databases.get(item[0].database_id, ""),
            } for item in res if data_auth.get(item[0].id, 0) > 0
        ]

    @staticmethod
    def get_database_names() -> dict:
        databases = db.session.query(Database).all()
        result = {}
        for database in databases:
            if "hive" in database.sqlalchemy_uri or "mysql" in database.sqlalchemy_uri:
                if conf.get("UPLOAD_SCHEMA") in database.sqlalchemy_uri:
                    continue
                verbose_name = database.verbose_name
                db_id = database.id
                db_type = ""
                if "hive" in database.sqlalchemy_uri:
                    db_type = "hive"
                elif "mysql" in database.sqlalchemy_uri:
                    db_type = "mysql"
                result[db_id] = db_type  # 使用数据库id作为键，类型作为值存储在字典中
                result[verbose_name] = verbose_name

        return result

    @staticmethod
    def get_database_data(dbs_id):
        dbs_models = db.session.query(Database).filter(Database.id == dbs_id).first()

        source_database_name = dbs_models.sqlalchemy_uri.split("/")[-1].split("?")[0]
        source_database_type = dbs_models.get_dialect().name
        source_database_table_name_list = list(dbs_models.get_all_tables_name())
        if dbs_models.get_dialect().name == "hive":
            source_database_table_name_list += [
                i[0] for i in dbs_models.get_all_view_names_in_schema(
                    source_database_name
                )
            ]

        result_data = dict(
            source_name=dbs_models.name,
            source_database_type=source_database_type,
            source_database_name=source_database_name,
            source_database_table_name_list=source_database_table_name_list,
        )

        return result_data

    @staticmethod
    def get_database_table_fields(item):
        dbs_models = db.session.query(Database).filter(
            Database.id == item.get("dbs_id")
        ).first()
        if not dbs_models:
            raise Exception("Unable to find dbs_id.")
        result_data = dict(
            table_name_list=[
                i.get("name") for i in dbs_models.get_columns(item.get('table_name'))
            ]
        )
        return result_data

    @staticmethod
    def get_field_value_data(item):
        dbs_models = db.session.query(Database).filter(
            Database.id == item.get("dbs_id")
        ).first()
        if not dbs_models:
            raise Exception("Unable to find dbs_id.")
        return [i[0] for i in dbs_models.get_field_value_group(item.get('table_name'),
                                                               group_by_field=item.get(
                                                                   'field_name'))]
