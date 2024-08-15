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
@Time       : 2023/7/12 13:57
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
from typing import Dict, Any
from flask_babel import gettext as _

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User

from superset import conf
from superset.commands.base import BaseCommand
from superset.datasets.dao import DatasetDAO
from superset.exceptions import HTTPError
from superset.utils.pd import api_data_to_df, df_to_sql
from superset.datasource.api_datasource.dao import APITablesDAO
from superset.v2.utils.data_save_db import get_save_default_db


class CreateAPIDatasetCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._api_table = None

    def run(self) -> Model:
        self.validate()
        print(self._api_table.configuration)
        print(type(self._api_table.configuration))
        df = api_data_to_df(
            json.loads(self._api_table.configuration),
            json.loads(self._api_table.data_path)
        )

        df_to_sql(
            df,
            self._properties["database"],
            self._properties["table_name"],
            self._properties["schema"],
        )
        # Creates SqlaTable (Dataset)
        dataset = DatasetDAO.create(self._properties, commit=False)
        # Updates columns and metrics from the dataset
        dataset.fetch_metadata()
        return dataset

    def validate(self) -> None:
        api_table_id = self._properties.pop("api_table_id")
        self._api_table = APITablesDAO.find_by_id(api_table_id)
        if self._api_table is None:
            raise HTTPError('The api datasource table does not exist', 400)

        datasource = self._api_table.datasource
        if datasource is None:
            raise HTTPError('The api datasource does not exist', 400)

        self._properties["database"] = get_save_default_db(self._actor)
        database_id = self._properties["database"].id
        table_name = self._api_table.table_name
        schema = conf["UPLOAD_SCHEMA"]

        # Validate uniqueness
        if not DatasetDAO.validate_uniqueness(database_id, schema, table_name):
            raise Exception(_('Duplicate table name'))

        self._properties["schema"] = schema
        self._properties["table_name"] = table_name
        self._properties['sql'] = 'SELECT * FROM ' + \
                                  self._properties['schema'] + '.' + \
                                  self._properties['table_name']
