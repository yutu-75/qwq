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
@Time       : 2023/7/13 16:12
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Dict, Any

from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.constants import DatasetType
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.datasets.dao import DatasetV2DAO
from superset.v2.utils.params_utils import sql_format

logger = logging.getLogger(__name__)


union_method = {
    'LEFT': 'LEFT JOIN',
    'RIGHT': 'RIGHT JOIN',
    'INNER': 'INNER JOIN',
}


class TestUnionDatasetCommand(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self, **kwargs: Any) -> dict:
        self.validate()

        def columns_rename(cols):
            re_cols = []
            label_cols = {}
            for index, col in enumerate(cols):
                new_col_name = f'f_{index}'
                re_cols.append(f'{col["field"]} AS {new_col_name}')
                label_cols[new_col_name] = col["label"]

            return re_cols, label_cols

        limit = kwargs.get('limit', 20)
        columns, label_columns = columns_rename(self._properties['columns'])
        union_datasets = self._properties['union_datasets']
        first_dataset = DatasetV2DAO.find_by_id(
            self._properties["first_dataset_id"]
        )
        if first_dataset is None:
            raise HTTPError(Messages.NOT_EXIST, 400)
        # 不能使用SQL数据集和关联数据集
        if first_dataset.type_classify in {DatasetType.SQL, DatasetType.UNION}:
            raise HTTPError(Messages.DATASET_TYPE_ERROR, 400)

        fields = ",".join(columns)
        table = f'''`{first_dataset.schema}`.`{first_dataset.table_name}`'''
        sql = f'''SELECT {fields} FROM {table}'''
        for item in union_datasets:
            dataset = DatasetV2DAO.find_by_id(item["dataset_id"])
            if dataset is None:
                continue
            # 不能是不同数据库
            if dataset.database_id != first_dataset.database_id:
                raise HTTPError(Messages.UNION_DATASET_DB_ERROR, 400)
            # 不能使用SQL数据集和关联数据集
            if dataset.type_classify in {DatasetType.SQL, DatasetType.UNION}:
                raise HTTPError(Messages.DATASET_TYPE_ERROR, 400)

            _method = union_method.get(item["method"], 'LEFT JOIN')
            _table = f'''`{dataset.schema}`.`{dataset.table_name}`'''
            _on = " AND ".join(item["on"])
            sql += f''' {_method} {_table} ON {_on}'''

        sql = sql_format(dataset.database.sqlalchemy_uri, sql)
        logger.debug(sql)
        sql_limit = sql + f' LIMIT {limit}'  # 减少数据量
        try:
            df = first_dataset.database.get_df(sql_limit)
        except Exception as ex:
            logger.error(ex)
            raise HTTPError(Messages.UNOIN_ERR, 400)

        return {
            "sql": sql,
            "database_id": first_dataset.database_id,
            "schema": first_dataset.schema,
            "label_columns": label_columns,
            "data": df.to_dict(orient="records")
        }

    def validate(self) -> None:
        if not self._properties['union_datasets']:
            raise HTTPError(Messages.MISSING_UNION_DATASETS, 400)


class UnionDatasetInfoCommand(BaseCommand):
    def __init__(self, user: User, model_id: int):
        self._actor = user
        self._model_id = model_id
        self._model = None

    def run(self, **kwargs: Any) -> dict:
        self.validate()
        return self._model.to_json()

    def validate(self) -> None:
        self._model = DatasetV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        if self._model.type_classify != DatasetType.UNION:
            raise HTTPError(Messages.NOT_EXIST, 400)
