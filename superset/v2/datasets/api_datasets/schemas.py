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
@Time       : 2023/7/12 12:54
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

from superset.constants import DatasetType, IfExistType


class APIDatasetPostSchema(Schema):
    datasource_id = fields.Integer(required=True, validate=Range(min=1))
    api_table_id = fields.Integer(required=True, validate=Range(min=1))
    custom_name = fields.String(required=True, validate=Length(1, 255))
    table_group_id = fields.Integer(validate=Range(min=0))
    type_classify = fields.Integer(required=False, default=DatasetType.API)


class APITableTaskPostSchema(Schema):
    name = fields.String(required=True, validate=Length(1, 50))
    update_type = fields.Enum(IfExistType, required=True)
    rate = fields.Integer(required=True, validate=Range(min=0, max=2))
    cron = fields.String()
    start_time = fields.Integer()
    end_time = fields.Integer()
    extra_data = fields.String()
    end = fields.String()
