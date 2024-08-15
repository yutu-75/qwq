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

import re

from marshmallow import fields, Schema, validate, validates, ValidationError
from marshmallow.validate import Length


class DashboardsShareResetPWDSchema(Schema):
    password = fields.String(allow_none=False, validate=Length(min=12, max=16))


class DashboardsShareResetPWDSchemaMax20(Schema):
    password = fields.String(allow_none=False, validate=Length(min=12, max=20))


class DashboardsShareResetExpirySchema(Schema):

    expiry = fields.Integer(allow_none=False)
    is_permanent = fields.Boolean(allow_none=True, default=False)


class DashboardsShareGetSchema(Schema):
    id = fields.Int()
    url = fields.String()
    dashboard_id = fields.Integer()
    password = fields.String()


class DashboardsShareSetPWDSchema(Schema):
    password = fields.String()

    @validates('password')
    def validate_password(self, value):
        if len(value) < 12 or len(value) > 20 or \
            not re.search(r'[A-Z]', value) or not re.search(r'[a-z]', value) \
            or not re.search(r'\d', value) or not re.search(r'[./_!@#]', value):
            raise ValidationError(
                '注意：密码需大于等于12位字符，不超过20位字符，且至少包含大写字母、小写字母、数字、特殊字符（.  /  _   !  @  #）四类字符。')
