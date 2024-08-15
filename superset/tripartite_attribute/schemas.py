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

from __future__ import annotations

import enum

from marshmallow import fields, Schema, validate

app_id_description = 'Tripartite application id'
role_id_description = 'Tripartite application corresponding role id'
role_name_description = 'Tripartite application corresponding role name'
app_name_description = 'Tripartite application corresponding app name'
request_path_description = 'Tripartite application request path'
status_code_description = 'Tripartite application response status code'
error_message_description = 'Tripartite application response error easy to understand'
exception_description = 'Tripartite application response error technical'
ip_description = 'Tripartite application request ip'
request_params_description = 'Tripartite application request params'
response_return_data_description = 'Tripartite application response data'
response_return_data_nums_description = 'Tripartite application response data count'
request_size_description = 'Tripartite application request request size(bytes)'
request_time_description = 'Tripartite application request request time Time to enter the back end'
response_size_description = 'Tripartite application response response size(bytes)'
service_latency_description = 'Tripartite application service latency'
status_description = 'Tripartite application request task result'


class STATUS(str, enum.Enum):
    FAIL = 'fail'
    SUCCESS = 'success'


class RecordSchema(Schema):
    """
    Schema to add a new record.
    """
    id = fields.Integer()
    app_id = fields.Integer(description=app_id_description, required=True)
    role_id = fields.Integer(description=role_id_description, required=True)
    role_name = fields.String(description=role_name_description, required=True)
    app_name = fields.String(description=app_name_description, required=True)
    request_path = fields.String(description=request_path_description, required=True)
    status_code = fields.Integer(description=status_code_description, required=True)
    error_message = fields.String(description=error_message_description)
    exception = fields.String(description=exception_description)
    ip = fields.String(description=ip_description, required=True)
    request_params = fields.String(description=request_params_description,
                                   required=True)
    response_return_data = fields.String(description=response_return_data_description,
                                         required=True)
    response_return_data_nums = fields.Integer(
        description=response_return_data_nums_description, required=True)
    request_size = fields.Integer(description=request_size_description, required=True)
    request_time = fields.DateTime(description=request_time_description, required=True)
    response_size = fields.Integer(description=response_size_description, required=True)
    service_latency = fields.Integer(description=service_latency_description,
                                    required=True)
    status = fields.String(description=status_description, required=True,
                           validate=validate.OneOf(choices=[ds.value for ds in STATUS]))
    created_on = fields.DateTime(required=False)
