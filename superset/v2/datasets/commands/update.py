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
@Time       : 2023/7/4 8:53
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User
from sqlalchemy.exc import OperationalError
from werkzeug.datastructures import FileStorage

from superset import db, conf
from superset.commands.base import BaseCommand
from superset.constants import DatasetType
from superset.datasets.dao import DatasetDAO
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.sql_parse import Table
from superset.utils.read_file import formdata_to_df
from superset.v2.utils.data_save_db import get_save_default_db


class UpdateFileDatasetCommand(BaseCommand):
    def __init__(
        self,
        user: User,
        model_id: int,
        upload: FileStorage,
        if_exists: str
    ):
        self._actor = user
        self._model_id = model_id
        self._model = None
        self._upload = upload
        self._if_exists = if_exists

    def run(self, **kwargs) -> Model:
        self.validate()
        df = formdata_to_df(self._upload)
        if isinstance(df, dict):
            sheet_name = kwargs.get("sheet_name")  # excel多个sheet时
            df = df.get(sheet_name, None)
            if df is None:
                raise HTTPError("请选择一个sheet", 400)

        dataset = DatasetDAO.update(self._model, {}, commit=False)
        database = self._model.database
        table = Table(
            table=self._model.table_name,
            schema=self._model.schema
        )
        try:
            database.db_engine_spec.df_to_sql(
                database,
                table,
                df,
                to_sql_kwargs={
                    "chunksize": 1000,
                    "if_exists": self._if_exists,
                    "index": None,
                    "index_label": None,
                },
            )
        except OperationalError as ex:
            db.session.rollback()
            raise HTTPError(Messages.APPEND_DATA_FORNAT_ERROR, 400)

        # Updates columns and metrics from the dataset
        dataset.fetch_metadata()
        return dataset

    def validate(self) -> None:
        self._model = DatasetDAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        if not isinstance(self._upload, FileStorage):
            raise HTTPError(Messages.FILE_NOT_UPLOADED, 400)

        self._model.type_classify = DatasetType.EXCEL
        self._model.database = get_save_default_db(self._actor)
        self._model.schema = conf["UPLOAD_SCHEMA"]
        self._model.sql = 'SELECT * FROM ' + \
                          self._model.schema + '.' + \
                          self._model.table_name
