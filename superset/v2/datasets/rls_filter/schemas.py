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
@Time       : 2023/5/15 18:00
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class RLSPutDataSchema(Schema):
    name = fields.String()
    clause = fields.String(required=True, validate=Length(1, 10000))
    user_ids = fields.List(fields.Integer(validate=Range(min=0)), required=True)
    role_ids = fields.List(fields.Integer(validate=Range(min=0)), required=True)
    dept_ids = fields.List(fields.Integer(validate=Range(min=0)), required=True)
    white_list = fields.List(fields.Integer(validate=Range(min=0)), required=True)
    status = fields.Integer(required=True, validate=Range(min=0, max=1))


class RLSPostDataSchema(RLSPutDataSchema):
    dataset_id = fields.Integer(required=True, validate=Range(min=0))


class ChangeRLSStatusSchema(Schema):
    status = fields.Integer(required=True, validate=Range(min=0, max=1))
