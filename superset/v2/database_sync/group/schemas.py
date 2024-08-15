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

from marshmallow import fields, Schema
from marshmallow.validate import Length

database_sync_group_name_description = "The name of the database_sync_group."
database_sync_group_pid_description = "The pid of the database_sync_group."
database_sync_group_level_description = "The level of the database_sync_group."
database_sync_group_group_id_description = "The level of the database_sync_group."

class DatabaseSyncGroupSchema(Schema):
    """
        Schema to  dataset_group.
    """

    name = fields.String(
        description=database_sync_group_name_description, required=True, validate=Length(1, 250)
    )
    pid = fields.Integer(description=database_sync_group_pid_description, required=True)
    level = fields.Integer(description=database_sync_group_level_description)


class DatabaseSyncGroupPostSchema(Schema):
    """
        Schema to add a new dataset_group.
    """

    name = fields.String(
        description=database_sync_group_name_description, required=True, validate=Length(1, 250)
    )
    pid = fields.Integer(description=database_sync_group_pid_description, required=True)


class DatabaseSyncGroupPutSchema(Schema):
    """
        Schema to update  dataset_group.
    """

    name = fields.String(
        description=database_sync_group_name_description, required=True, validate=Length(1, 250)
    )
    pid = fields.Integer(description=database_sync_group_pid_description, required=True)
    level = fields.Integer(description=database_sync_group_level_description)

class DatabaseNameSyncGroupPutSchema(Schema):
    """
        Schema to update  dataset_group.
    """

    name = fields.String(
        description=database_sync_group_name_description, required=True, validate=Length(1, 250)
    )
    level = fields.Integer(description=database_sync_group_level_description)
    group_id=fields.Integer(description=database_sync_group_group_id_description,required=True)

class DatabaseSyncGroupSearchSchema(Schema):
    """
        分组过滤字段校验
    """
    group_name = fields.String()
    name = fields.String()
    creator = fields.String()
    type_ = fields.Integer()
    force = fields.String()
