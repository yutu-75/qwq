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
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from marshmallow import fields, Schema
from marshmallow.validate import Range

from superset.models.core import Log


class LogV2GetResponseSchema(Schema):
    model_cls = Log
    id = fields.Int()
    user_id = fields.Int()
    dashboard_id = fields.Int()
    slice_id = fields.Int()
    duration_ms = fields.Int()
    action = fields.String()
    referrer = fields.String()
    json = fields.String()
    dttm = fields.DateTime()


class LogV2SearchSchema(Schema):
    action = fields.String(required=False)
    dttm_start = fields.DateTime(required=False)
    dttm_end = fields.DateTime(required=False)
    user_id = fields.String(required=False)
    page_size = fields.Integer(required=False, validate=Range(min=0))
    page_index = fields.Integer(required=False, validate=Range(min=0))


class LogPostSchema(Schema):
    action = fields.String(required=True)
    extra = fields.Dict(required=True)
