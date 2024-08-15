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


from marshmallow import fields, Schema
from marshmallow.validate import Length, Range


class DatabaseSyncPatchSchema(Schema):
    name = fields.String(required=True, validate=Length(1, 50))
    group_id = fields.Integer(required=True, validate=Range(min=0))


class DatabaseSyncDataSourcePostSchema(Schema):
    name = fields.String(allow_none=True)
    database_type = fields.String(allow_none=True)
    database_id = fields.Integer(allow_none=True)
    group_id = fields.Integer(required=True, allow_none=True, validate=Range(min=0))


class DatabaseSyncTablesInfoResponseSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class DatabaseSyncResponseDataSchema(Schema):
    id = fields.Integer()
    database_id = fields.Integer()
    name = fields.String()
    d_type = fields.String()
    desc = fields.String()
    configuration = fields.String()
    data_path = fields.Dict()
    group_id = fields.Integer()


class DatabaseSyncPutSchema(Schema):
    table_name = fields.String(required=True, validate=Length(1, 254))
    comment = fields.String(required=False, validate=Length(0, 254))


class TableFieldsPatchSchema(Schema):
    table_name = fields.String(required=True, validate=Length(1, 50))
    dbs_id = fields.Integer(required=True, validate=Range(min=0))

class TableFieldsValueGroupPySchema(Schema):
    table_name = fields.String(required=True, validate=Length(1, 50))
    dbs_id = fields.Integer(required=True, validate=Range(min=0))
    field_name = fields.String(required=True, validate=Length(1, 50))
