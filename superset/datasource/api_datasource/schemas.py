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
@Time       : 2023/7/18 14:50
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from enum import Enum

from marshmallow import fields, Schema
from marshmallow.validate import Length, Equal


class MethodType(str, Enum):
    GET = "get"
    POST = "post"


class DataPathSchema(Schema):
    record_path = fields.List(fields.String, required=True, allow_none=True)
    meta = fields.List(fields.List(fields.String))
    columns = fields.Dict(required=True, allow_none=False)


class APIDataSourceListResponseSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    d_type = fields.String()
    description = fields.String()


class APIDataSourceTableSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    configuration = fields.String()
    data_path = fields.Nested(DataPathSchema, required=True)


class ApiDataSourceTestSchema(Schema):
    url = fields.String(required=True, validate=Length(10, 1024))
    method = fields.String(required=True, validate=lambda x: x in [e.value for e in MethodType])
    headers = fields.Dict(required=False)
    params = fields.Dict(required=False)
    data = fields.Dict(required=False)
    json = fields.Dict(required=False)


class ApiTablePostSchema(Schema):
    name = fields.String(required=True, validate=Length(1, 50))
    configuration = fields.Nested(ApiDataSourceTestSchema, required=True)
    data_path = fields.Nested(DataPathSchema, required=True)


class ApiDataSourcePostSchema(Schema):
    name = fields.String(required=True, validate=Length(1, 100))
    description = fields.String(required=False, validate=Length(0, 200))
    d_type = fields.String(required=True, validate=Equal('api'))
    tables = fields.List(fields.Nested(ApiTablePostSchema))


class ApiDataSourcePutSchema(Schema):
    name = fields.String(required=True, validate=Length(1, 100))
    description = fields.String(required=False, validate=Length(0, 200))
    tables = fields.List(fields.Nested(ApiTablePostSchema))
