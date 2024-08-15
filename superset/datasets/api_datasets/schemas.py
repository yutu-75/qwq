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
@Time       : 2023/7/12 12:54
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class APIDatasetPostSchema(Schema):
    api_table_id = fields.Integer(required=True, validate=Range(min=1))
    table_name = fields.String(required=True, validate=Length(1, 250))
