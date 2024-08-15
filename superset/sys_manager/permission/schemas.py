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

"""
@Time       : 2023/3/16 9:53
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from marshmallow import fields, Schema
from marshmallow.validate import Range, Length
from marshmallow_enum import EnumField

from superset.constants import (
    AuthTargetType,
    PrivilegeNameType,
    AuthSourceType,
    AuthType,
    DirectionType,
    DatabaseAuthType
)


class SysAuthDetailSchema(Schema):
    privilege_name = fields.String(required=True, validate=Length(1, 50))
    privilege_value = fields.Integer(required=True, validate=Range(min=0, max=1))


class SysAuthSchema(Schema):
    auth_source_type = EnumField(AuthSourceType, required=True, by_value=True)
    auth_source = fields.Integer(required=True, validate=Range(min=1))
    auth_target_type = EnumField(AuthTargetType, required=True, by_value=True)
    auth_target = fields.Integer(required=True, validate=Range(min=1))
    privilege_value = fields.Integer(required=True, validate=Range(min=0, max=15))


class DatabaseAuthSchema(Schema):
    auth_source_type = EnumField(DatabaseAuthType, required=True, by_value=True)
    datasource_id = fields.Integer(required=True, validate=Range(min=1))
    database_id = fields.Integer(required=True, validate=Range(min=1))
    schema = fields.String(required=True, validate=Length(1, 100))
    table_name = fields.String(required=False, validate=Length(1, 100))
    auth_target_type = EnumField(AuthTargetType, required=True, by_value=True)
    auth_target = fields.Integer(required=True, validate=Range(min=1))
    privilege_value = fields.Integer(required=True, validate=Range(min=0, max=15))


class BatchChangeGroupAuthSchema(Schema):
    auth_source_type = EnumField(AuthSourceType, required=True, by_value=True)
    auth_sources = fields.List(fields.Integer(required=True, validate=Range(min=1)), required=True)
    auth_target_type = EnumField(AuthTargetType, required=True, by_value=True)
    auth_target = fields.Integer(required=True, validate=Range(min=1))
    privilege_value = fields.Integer(required=True, validate=Range(min=0, max=15))


class BatchChangeDataAuthSchema(Schema):
    auth_source_type = EnumField(AuthSourceType, required=True, by_value=True)
    auth_sources = fields.List(fields.Integer(required=True, validate=Range(min=1)), required=True)
    auth_target_type = EnumField(AuthTargetType, required=True, by_value=True)
    auth_target = fields.Integer(required=True, validate=Range(min=1))
    privilege_value = fields.Integer(required=True, validate=Range(min=0, max=15))


class BatchChangeAuthSchema(Schema):
    group = fields.Nested(BatchChangeGroupAuthSchema)
    data = fields.Nested(BatchChangeDataAuthSchema)


class SysAuthPostSchema(Schema):
    perm = fields.List(fields.Nested(SysAuthSchema, required=True), required=True)


class DatabaseAuthPostSchema(Schema):
    perm = fields.List(fields.Nested(DatabaseAuthSchema, required=True), required=True)


class SysAuthDetailPostSchema(Schema):
    auth_id = fields.Integer(required=True, validate=Range(min=1))
    privilege_name = fields.List(EnumField(PrivilegeNameType, by_value=True), required=True)


class SysAuthTypeSchema(Schema):
    auth_type = EnumField(AuthType, by_value=True, required=True)


class SysAuthDetailGetSchema(Schema):
    direction = EnumField(DirectionType, by_value=True, required=True)
    auth_target = fields.Integer(validate=Range(min=1))
    auth_target_type = EnumField(AuthTargetType, by_value=True)
    auth_source_type = fields.String()
    auth_source = fields.Integer(validate=Range(min=1))


class DatabaseSchemaAuthSchema(Schema):
    auth_source_type = EnumField(DatabaseAuthType, required=True, by_value=True)
    auth_target_type = EnumField(AuthTargetType, required=True, by_value=True)
    auth_target = fields.Integer(required=True, validate=Range(min=1))
