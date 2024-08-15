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

from typing import TYPE_CHECKING

from marshmallow import fields, Schema
from marshmallow.validate import Length


if TYPE_CHECKING:
    pass


chart_group_name_description = "The name of the chart_group."
chart_group_pid_description = "The pid of the chart_group."
chart_group_level_description = "The level of the chart_group."


class ChartGroupSchema(Schema):
    """
        Schema to dashboard_group.
    """

    name = fields.String(
        description=chart_group_name_description, required=True, validate=Length(1, 250)
    )
    pid = fields.Integer(description=chart_group_pid_description, required=True)
    level = fields.Integer(description=chart_group_level_description)


class ChartGroupPostSchema(Schema):
    """
        Schema to add a new dashboard_group.
    """

    name = fields.String(
        description=chart_group_name_description, required=True, validate=Length(1, 250)
    )
    pid = fields.Integer(description=chart_group_pid_description, required=True)
    level = fields.Integer(description=chart_group_level_description)


class ChartGroupSearchSchema(Schema):
    """
        分组过滤字段校验
    """
    group_name = fields.String()
    name = fields.String()
    creator = fields.String()
    viz_type = fields.String()
    force = fields.String()
