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
# "AS IS" BASIS, WITHOUT     OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import json
import logging

from flask import Response, request
from flask_appbuilder.api import expose, safe
from flask_appbuilder.security.decorators import has_access

from superset.service_management.concurrent_operations import execute_command, TIMEOUT
from superset.service_management.redis_client import cache

from superset.views.base import BaseSupersetView, json_success

logger = logging.getLogger(__name__)


class ServiceManagementApi(BaseSupersetView):
    """
    系统服务管理接口
    """
    route_base = "/service"
    include_route_methods = {
        "update_frontend_code",
    }

    @has_access
    @expose("/update_frontend_code/", methods=("GET", "POST",))
    @safe
    def update_frontend_code(self) -> Response:
        """
        get 方法返回html页面、状态、shell脚本执行成功或者失败的日志
        post 执行shell脚本，更改状态
        update_frontend_code_status 0为更新失败， 1为更新成功， 2为正在更新
        :return:
        """
        if request.method == "GET":
            status = cache.get('update_frontend_code_status')
            message = cache.get('update_frontend_code_message')
            # 创建 Response 对象，设置 HTML 内容
            response = self.render_template(
                "service_management.html",
                url=request.url,
                status=status,
                message=message
            )
            return response
        else:

            status = cache.get('update_frontend_code_status')
            if status is None:
                cache.set('update_frontend_code_status', 1, timeout=TIMEOUT)

            if status == 0 or status == 1 or status is None:
                execute_command()

            return json_success(json.dumps(
                "请稍等,正在更新前端代码..."
            ))
