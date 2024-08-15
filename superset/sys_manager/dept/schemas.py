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
from marshmallow.validate import Length, Range


class SysDeptPostSchema(Schema):
    title = fields.String(required=True, validate=Length(1, 250))
    pid = fields.Integer(required=True, validate=Range(min=0))


class SysDeptUserPostSchema(Schema):
    user_ids = fields.List(fields.Integer(validate=Range(min=1)), required=True)


class SysDeptResponseSchema(Schema):
    title = fields.String()
    pid = fields.Integer()
    level = fields.Integer()


class UserSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    username = fields.String()


class SysDeptUsersResponseSchema(Schema):
    data = fields.List(fields.Nested(UserSchema))
