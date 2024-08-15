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

from marshmallow import fields, Schema
from marshmallow.validate import Length, Range

from superset.charts.schemas import ChartPostSchema, ChartPutSchema


class ChartV2PostSchema(ChartPostSchema):
    slice_group_id = fields.Integer(validate=Range(min=0))


class ChartV2PutSchema(ChartPutSchema):
    slice_group_id = fields.Integer(validate=Range(min=0))


class ChartV2PatchSchema(Schema):
    target_id = fields.Integer(validate=Range(min=0), required=True)
    new_title = fields.String(validate=Length(1, 500), required=True)


class ChartV2ExploreSchema(Schema):
    image_data = fields.String(required=False)
    explore_format = fields.String(required=False)


class ChartCopySchema(Schema):
    slice_group_id = fields.Integer(validate=Range(min=0), required=True)
    slice_name = fields.String(validate=Length(1, 100), required=True)
