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
@Time       : 2023/3/29 13:39
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class DashboardV2PostSchema(Schema):
    dashboard_title = fields.String(required=True, validate=Length(1, 500))
    dashboard_group_id = fields.Integer(required=True, validate=Range(min=0))


class DashboardV2ExploreSchema(Schema):
    image_data = fields.String(required=False)
    explore_format = fields.String(required=False)


class DashboardResponseSchema(Schema):
    id = fields.Integer()
    dashboard_title = fields.String()
    published = fields.Boolean()
    changed_on_delta_humanized = fields.String()
    last_modified_time = fields.Integer()
    perm = fields.Integer()
