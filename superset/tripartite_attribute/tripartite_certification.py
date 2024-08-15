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

from functools import wraps

from flask_appbuilder.security.sqla.models import Role

from superset.models.app_attributes import AppAttribute
from superset import db
import hashlib
from flask import request

from superset.models.dashboard import DashboardRoles, Dashboard, dashboard_slices
from superset.models.slice import Slice
from superset.utils.dates import now_as_float

QUARTER_HOUR = 15 * 60 * 1000


def tripartite_certification(func):
    @wraps(func)
    def wrapped_function(self, **kwargs):
        args = kwargs.get('rison', {})
        is_valid = verify_signature(args, request.headers)
        if is_valid and request.headers:
            role_id = get_role(request.headers.get('appKey'))
            if role_id:
                kwargs.update({'role_id': role_id})
        kwargs.update({'tripartite': is_valid, 'api_func': func})
        return func(self, **kwargs)
    return wrapped_function


def generate_signature(params: dict, app_key: str, timestamp: str,
                       secret_key: str) -> str:
    """
    params: query_dict
    secret_key: 秘钥
    """
    sorted_params = sorted(params.items(), key=lambda x: x[0])
    query_string = "&".join(f"{key}={value}" for key, value in sorted_params).upper()
    return hashlib.md5(
        f"{app_key}_{secret_key}_{timestamp}".encode('utf-8').upper()).hexdigest()
    # return hashlib.md5(
    #     (query_string + f"&secret_key={secret_key}").encode()).hexdigest()


def get_secret(app_key: str) -> str:
    return db.session.query(AppAttribute.app_secret).filter_by(
        app_key=app_key
    ).scalar()


def get_role(app_key: str) -> int:
    return db.session.query(AppAttribute.role_id).filter_by(
        app_key=app_key
    ).scalar()


def verify_slice_role(slices_or_pk, role_id) -> [list, bool]:
    dbs = db.session.query(DashboardRoles).filter_by(
        role_id=role_id
    ).all()
    sls = [db.session.query(dashboard_slices).filter_by(
        dashboard_id=i[1]
    ).all() for i in dbs]
    if isinstance(slices_or_pk, list):
        return [chart for chart in slices_or_pk if
                chart.get('id') in [a[2] for j in sls for a in j]]
    else:
        return slices_or_pk in [a[2] for j in sls for a in j]


def verify_slice_delete(role_id, obj_pk):
    dbs = db.session.query(DashboardRoles.dashboard_id).filter_by(
        role_id=role_id
    ).all()


def verify_signature(params: dict, headers: dict) -> bool:
    """
    params: query_dict
    sign: hash sign
    """
    app_key = headers.get('appKey')
    sign = headers.get('sign')
    timestamp = headers.get('timestamp')

    if timestamp and now_as_float() - QUARTER_HOUR <= float(timestamp):
        generated_signature = generate_signature(params, app_key, timestamp,
                                                 get_secret(app_key))
        return sign == generated_signature
    else:
        return False
