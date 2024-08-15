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

import time
import logging
from datetime import datetime
from hashlib import md5

from flask import (
    jsonify,
    request,
)

from superset.dashboards.dao import DashboardDAO

log = logging.getLogger(__name__)


def is_timestamp(string):
    try:
        datetime.fromtimestamp(float(string))
        return True
    except Exception:
        return False


def api_validate_decorator(func):
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前执行的逻辑
        # 在这里进行身份验证、权限检查等操作
        # 获取请求头部中的验证信息

        headers = request.headers
        app_key = headers.get('AppKey') or headers.get('appKey')
        frontend_sign = headers.get('Sign') or headers.get('sign')
        timestamp = headers.get('Timestamp') or headers.get('timestamp')
        dashboard_user_access_levels_models = DashboardDAO.get_app_attribute_models()

        if (not is_timestamp(timestamp) and timestamp is None) \
            or (int(timestamp) + 60 * 15 * 1000 < round(time.time() * 1000)):
            return jsonify({
                "message": "The timestamp parameter is incorrect or has expired",
                "status": "Failed"
            }), 401  # 返回验证失败的响应

        if not dashboard_user_access_levels_models and dashboard_user_access_levels_models is None:
            return jsonify({
                "message": "No appKey",
                "status": "Failed"
            }), 401  # 返回验证失败的响应
        app_secret = dashboard_user_access_levels_models.app_secret

        sign = md5(
            f"{app_key}_{app_secret}_{timestamp}".encode('utf-8').upper()).hexdigest()

        # 进行验证逻辑
        if frontend_sign != sign:
            return jsonify({
                "message": "Sign authentication failed, please calibrate the sign",
                "status": "Failed"
            }), 401  # 返回验证失败的响应

        result = func(*args, **kwargs)  # 执行被装饰的函数

        return result

    return wrapper
