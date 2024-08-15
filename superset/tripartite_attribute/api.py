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

import logging

from flask_appbuilder.api import expose, safe
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.decorators import protect

from superset import app
from superset.constants import MODEL_API_RW_METHOD_PERMISSION_MAP, RouteMethod
from superset.models.app_attributes import AppLogRecord
from superset.tripartite_attribute.filters import RecordAllTextFilter
from superset.tripartite_attribute.schemas import RecordSchema
from superset.views.base_api import (
    BaseSupersetModelRestApi, statsd_metrics
)
logger = logging.getLogger(__name__)
config = app.config


class RecordRestApi(BaseSupersetModelRestApi):
    datamodel = SQLAInterface(AppLogRecord)
    resource_name = "record"
    allow_browser_login = True
    include_route_methods = RouteMethod.READ_ONLY
    class_permission_name = "Record"
    method_permission_name = MODEL_API_RW_METHOD_PERMISSION_MAP
    show_columns = [
        "role_name",
        "app_name",
        "request_path",
        "status_code",
        "error_message",
        "exception",
        "ip",
        "request_params",
        "id",
        "response_return_data",
        "response_return_data_nums",
        "request_size",
        "request_time",
        "response_size",
        "service_latency",
        "status",
        "changed_on",
        "created_on",
        "created_by.username",
        "changed_by.username",
    ]
    list_columns = [
        "role_name",
        "app_name",
        "request_path",
        "status_code",
        "error_message",
        "exception",
        "ip",
        "request_params",
        "id",
        "response_return_data",
        "response_return_data_nums",
        "request_size",
        "request_time",
        "response_size",
        "service_latency",
        "status",
    ]

    order_columns = [
        "changed_on",
    ]
    search_columns = [
        "id",
        "role_name",
        "app_name",
        "request_url",
        "created_on",
        "status_code",
        "status",
        "error_message",
    ]
    base_order = ("changed_on", "desc")
    search_filters = {"error_message": [RecordAllTextFilter]}
    add_model_schema = RecordSchema()
    list_model_schema = RecordSchema(many=True)





