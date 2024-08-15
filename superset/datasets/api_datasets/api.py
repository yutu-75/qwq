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

# -*- coding: utf-8 -*-

"""
@Time       : 2023/7/12 12:54
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging

from flask import g, request, Response
from flask_appbuilder.api import expose
from flask_appbuilder.security.decorators import protect, permission_name

from superset import event_logger
from superset.datasets.api_datasets.commands.create import CreateAPIDatasetCommand
from superset.datasets.api_datasets.schemas import APIDatasetPostSchema
from superset.views.base_api import (
    requires_json,
    statsd_metrics,
    BaseSupersetApi
)

logger = logging.getLogger(__name__)


class APIDatasetRestApi(BaseSupersetApi):
    resource_name = "dataset/api"
    allow_browser_login = True
    class_permission_name = "Dashboard"
    openapi_spec_component_schemas = (
        APIDatasetPostSchema,
    )

    @expose("/", methods=("POST",))
    @protect()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.post",
        log_to_statsd=False,
    )
    @requires_json
    @permission_name('read')
    def post(self) -> Response:
        """
        ---
        post:
          description: 新增API数据集
          requestBody:
            description:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/APIDatasetPostSchema'
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        item = APIDatasetPostSchema().load(request.json)
        dataset = CreateAPIDatasetCommand(g.user, item).run()
        return self.response(200, result=dataset.to_json())

    @expose("/<int:id>/cates", methods=["GET"])
    def get_cates(self, id):
        is_cross_field = int(request.args.get("is_cross_field"))

        # 连接到数据库
        import pymysql
        connection = pymysql.connect(
            host="47.109.87.172",
            port=3306,
            user="root",
            password="ch1qaz@WSX",
            db="sit_cabi",
            charset="utf8mb4"
        )

        try:
            # 执行数据库查询
            with connection.cursor() as cursor:
                sql = "SELECT first_cate_field, second_cate_field FROM aaa WHERE id=%s AND is_cross_field=%s"
                cursor.execute(sql, (id, is_cross_field))
                result = cursor.fetchall()

            # 构建结果字典
            response = {
                "count": len(result),
                "result": []
            }
            for row in result:
                response['result'].append({
                    "first_cate_field": row[0],
                    "second_cate_field": row[1]
                })

            return self.response(200, result=response)

        except Exception as e:
            return self.response(500, message=str(e))

        finally:
            # 关闭数据库连接
            connection.close()

    @expose("/<string:id>/cate/<string:cateLevel>/<string:cateName>/fields",methods=["GET"])
    def get_fields(self, id, cateLevel, cateName):
        # 连接到数据库
        import pymysql
        connection = pymysql.connect(
            host="47.109.87.172",
            port=3306,
            user="root",
            password="ch1qaz@WSX",
            db="sit_cabi",
            charset="utf8mb4"
        )

        try:
            # 执行数据库查询
            with connection.cursor() as cursor:
                sql = """
                    SELECT first_name, username, changed_by_name, changed_by_url, changed_on_delta_humanized,
                    changed_on_utc, database_name, id, datasource_type, default_endpoint, description, explore_url,
                    extra, kind, last_name, schema_name, sql_query, table_name,cateLevel,cateName
                    FROM aaaa
                    WHERE id = %s AND cateLevel = %s AND cateName = %s
                    """
                cursor.execute(sql, (id, cateLevel, cateName))
                result = cursor.fetchall()

            # 构建结果字典
            response = {
                "count": len(result),
                "result": []
            }
            for row in result:
                response['result'].append({
                    "changed_by": {
                        "first_name": row[0],
                        "username": row[1]
                    },
                    "changed_by_name": row[2],
                    "changed_by_url": row[3],
                    "changed_on_delta_humanized": row[4],
                    "changed_on_utc": row[5],
                    "database": {
                        "database_name": row[6],
                        "id": row[7]
                    },
                    "datasource_type": row[8],
                    "default_endpoint": row[9],
                    "description": row[10],
                    "explore_url": row[11],
                    "extra": row[12],
                    "id": row[7],
                    "kind": row[13],
                    "owners": {
                        "first_name": row[0],
                        "id": row[7],
                        "last_name": row[14],
                        "username": row[1]
                    },
                    "schema_name": row[15],
                    "sql_query": row[16],
                    "table_name": row[17],
                    "cateLevel": row[18],
                    "cateName": row[19]
                })

            return self.response(200, result=response)

        except Exception as e:
            return self.response(500, message=str(e))

        finally:
            # 关闭数据库连接
            connection.close()

