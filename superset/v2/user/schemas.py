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
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask_appbuilder.security.sqla.apis.user.schema import UserPostSchema
from flask_appbuilder.security.sqla.models import User
from flask_appbuilder.validators import PasswordComplexityValidator
from marshmallow import fields, Schema
from marshmallow.validate import Range, Length

active_description = (
    "Is user active?" "It's not a good policy to remove a user, just make it inactive"
)
email_description = "The user's email"
first_name_description = "The user's first name"
last_name_description = "The user's last name"
password_description = "The user's password for authentication"
roles_description = "The user's roles"
username_description = "The user's username"
cn_name_description = "The user's cn_name"


class UserV2GetResponseSchema(Schema):
    model_cls = User
    id = fields.Int()
    first_name = fields.String(description=first_name_description)
    last_name = fields.String(description=last_name_description)
    username = fields.String(description=username_description)
    cn_name = fields.String(description=cn_name_description)
    password = fields.String(description=password_description)
    active = fields.Boolean(description=active_description)
    email = fields.String(description=email_description)
    last_login = fields.DateTime()
    login_count = fields.Int()
    fail_login_count = fields.Int()
    created_on = fields.DateTime()
    changed_on = fields.DateTime()
    roles = fields.List(
        fields.Integer,
        description=roles_description,
    )


class UserV2PostSchema(UserPostSchema):
    is_admin = fields.Boolean(required=True, default=False)
    dept_id = fields.List(fields.Integer, required=True)
    email = fields.Email(required=True)
    first_name = fields.String(allow_none=True)
    last_name = fields.String(allow_none=True)
    username = fields.String(required=True, validate=[Length(1, 64)])
    cn_name = fields.String(required=True, validate=Length(min=1, max=64))


class UserV2PutSchema(Schema):
    active = fields.Boolean(required=False, description=active_description)
    email = fields.Email(required=True)
    first_name = fields.String(allow_none=True)
    last_name = fields.String(allow_none=True)
    username = fields.String(required=True, validate=[Length(1, 64)])
    cn_name = fields.String(required=True, validate=Length(min=1, max=64))
    password = fields.String(
        required=False,
        validate=[PasswordComplexityValidator()],
        description=password_description,
    )
    roles = fields.List(
        fields.Integer,
        required=False,
    )
    is_admin = fields.Boolean(required=False, default=False)
    dept_id = fields.List(fields.Integer, required=False)


class UserActivePatchSchema(Schema):
    active = fields.Integer(required=False, validate=Range(min=0, max=1))


class UserSearchSchema(Schema):
    username = fields.String(required=False, validate=Length(0, 200))
    page_size = fields.Integer(required=False, validate=Range(min=0))
    page_index = fields.Integer(required=False, validate=Range(min=0))
    role_id = fields.Integer(required=False, validate=Range(min=0))
    dept_id = fields.Integer(required=False, validate=Range(min=0))
    filter_role_id = fields.Integer(required=False, validate=Range(min=0))
    filter_dept_id = fields.Integer(required=False, validate=Range(min=0))
