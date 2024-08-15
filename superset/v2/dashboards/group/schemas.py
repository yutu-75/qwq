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
@Time       : 2023/3/29 12:37
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class DashboardGroupPostSchema(Schema):
    """
        Schema to add a new dashboard group.
    """

    name = fields.String(required=True, validate=Length(1, 250))
    pid = fields.Integer(required=True, validate=Range(min=0))


class DashboardResponseSchema(Schema):
    dashboard_id = fields.Int()
    dashboard_title = fields.String()


class DashboardGroupResponseSchema(Schema):
    id = fields.Int()
    pid = fields.Int()
    level = fields.Int()
    name = fields.String()
    dashboards = fields.List(fields.Nested(DashboardResponseSchema))
    children = fields.List(fields.String)
