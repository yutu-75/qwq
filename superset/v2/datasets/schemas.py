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
from marshmallow.validate import Length, Range

from superset.constants import IfExistType
from superset.datasets.schemas import DatasetPostSchema, DatasetPutSchema, \
    ImportV1DatasetSchema


class DatasetV2PostSchema(DatasetPostSchema):
    table_group_id = fields.Integer(required=True, validate=Range(min=0))
    type_classify = fields.Integer(validate=Range(min=0))
    sql = fields.String(validate=Length(1, 500), required=False)


class DatasetV2PutSchema(DatasetPutSchema):
    table_group_id = fields.Integer(validate=Range(min=0))


class DatasetV2PatchSchema(Schema):
    target_id = fields.Integer(validate=Range(min=0), required=True)
    new_title = fields.String(validate=Length(1, 500), required=True)


class DatasetV2TableColumsPutSchema(Schema):
    data = fields.List(
        fields.Dict(),
        example=[{
            "column_name": "",
            "id": "",
            "type": "",
            "verbose_name": "",
        }],
    )


class RelatedDatasetV2PostSchema(Schema):
    schema = fields.String(validate=Length(0, 250), required=True)
    database = fields.Integer(required=True)
    related_json = fields.Dict(required=True)
    table_name = fields.String(required=True, allow_none=False, validate=Length(1, 250))
    table_group_id = fields.Integer(required=True, validate=Range(min=0))
    sql = fields.String(validate=Length(1, 500), required=False)


class RelatedDatasetV2PutSchema(Schema):
    table_name = fields.String(allow_none=True, validate=Length(1, 250))
    related_json = fields.Dict()
    database_id = fields.Integer()
    sql = fields.String(allow_none=True)
    table_group_id = fields.Integer(validate=Range(min=0))


class RelatedDatasetV2PatchSchema(Schema):
    target_id = fields.Integer(validate=Range(min=0), required=True)
    new_title = fields.String(validate=Length(1, 500), required=True)


class ImportV2DatasetSchema(ImportV1DatasetSchema):
    group_name = fields.String()


class SqlLabVizSchema(Schema):
    schema = fields.String(validate=Length(1, 500), required=True)
    sql = fields.String(required=True)
    database_id = fields.Integer(validate=Range(min=1), required=True)
    table_name = fields.String(validate=Length(1, 500), required=True)
    columns = fields.List(fields.Dict, required=True)
    table_group_id = fields.String(validate=Length(0, 500), required=True)


class FileDatasetPutSchema(Schema):
    upload = fields.Raw(required=True)
    if_exists = fields.Enum(IfExistType, required=True)
