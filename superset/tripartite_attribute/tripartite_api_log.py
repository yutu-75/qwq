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

from datetime import datetime
from functools import wraps
from flask import request
from flask_appbuilder.security.sqla.models import Role
from superset import db
from superset.models.app_attributes import AppLogRecord, AppAttribute
from superset.tripartite_attribute.schemas import RecordSchema
from superset.utils.core import time_function


def get_app_info(app_key: str):
    return db.session.query(AppAttribute).filter_by(
        app_key=app_key
    ).scalar()


def get_role_name(role_id):
    return db.session.query(Role.name).filter_by(
        id=role_id
    ).scalar()


def record_tripartite_api_log(func):
    """
    记录三方 api 调用日志
    """

    @wraps(func)
    def wrapped_function(self, *args, **kwargs):
        app_key = request.headers.get('appKey')
        if app_key:
            app_info = get_app_info(app_key)
            if not app_info:
                return self.response_401()
            else:
                role_name = get_role_name(app_info.role_id)
                if not role_name:
                    return self.response_401()
            datetime_now = datetime.now()
            app_record = {'request_path': request.url,
                          'request_size': request.content_length or 0,
                          'request_time': str(datetime_now), 'app_id': app_info.id,
                          'app_name': app_info.name, 'role_id': app_info.role_id,
                          'role_name': role_name}
            try:
                if request.method == 'GET':
                    params = str(request.args)
                else:
                    params = str(request.get_json())
                duration, response = time_function(func, self, *args, **kwargs)
                app_record['status_code'] = response.status_code
                app_record['ip'] = request.remote_addr
                app_record['request_params'] = params
                # app_record['response_return_data'] = response.data
                app_record['response_return_data'] = ""
                app_record['response_return_data_nums'] = response.json.get(
                    'count') if (
                    response.json and response.json.get('count')) else 0
                app_record['response_size'] = len(response.get_data())
                app_record[
                    'status'] = 'success' if 300 > response.status_code >= 200 else 'fail'
                app_record['service_latency'] = int(duration)
                return response
            except Exception as e:
                app_record['exception'] = e
                app_record['error_message'] = type(e)
                return self.response_500()
            finally:
                RecordSchema().load(app_record)
                self.datamodel.add(AppLogRecord(**app_record), raise_exception=True)
        else:
            return func(self, **kwargs)

    return wrapped_function
