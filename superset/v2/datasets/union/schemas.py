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
@Time       : 2023/7/12 15:45
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from marshmallow import fields, Schema
from marshmallow.validate import Length, Range

from superset.constants import IfExistType
from superset.datasets.schemas import DatasetPostSchema, DatasetPutSchema, \
    ImportV1DatasetSchema


class DatasetSchema(Schema):
    dataset_id = fields.Integer(required=True, validate=Range(min=1))
    method = fields.String(required=True)
    on = fields.List(fields.String, required=True)


class UnionDatasetColumnSchema(Schema):
    field = fields.String(required=True, validate=Length(1, 200))
    label = fields.String(required=True, validate=Length(1, 200))


class UnionDatasetSchema(Schema):
    first_dataset_id = fields.Integer(required=True, validate=Range(min=1))
    columns = fields.List(fields.Nested(UnionDatasetColumnSchema), required=True)
    union_datasets = fields.List(fields.Nested(DatasetSchema), required=True)


class UnionDatasetPostSchema(Schema):
    custom_name = fields.String(required=True, validate=Length(1, 200))
    table_group_id = fields.Integer(required=True, validate=Range(min=1))
    configuration = fields.String(required=True, validate=Length(1, 65535))
    union_detail = fields.Nested(UnionDatasetSchema)


class UnionDatasetPutSchema(Schema):
    custom_name = fields.String(required=True, validate=Length(1, 200))
    configuration = fields.String(required=True, validate=Length(1, 65535))
    union_detail = fields.Nested(UnionDatasetSchema)
