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
@Time       : 2023/7/19 14:56
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import pandas as pd
from superset.models.core import Database
from superset.sql_parse import Table
from superset.utils.requests import req


def api_data_to_df(configuration: dict, data_path: dict) -> [pd.DataFrame, None]:
    data = req(configuration)
    if data is None:
        return None

    if not data_path.get("record_path", False):
        data_path["record_path"] = None

    rename_columns = data_path.pop("columns")
    df = pd.json_normalize(data, **data_path)
    # 数据处理
    for item in df.columns:
        re_col = rename_columns.get(item, False)
        if re_col:
            df.rename(columns={item: re_col}, inplace=True)  # 字段重命名

        else:
            del df[item]  # 删除未选择的字段

    return df


def df_to_sql(
    df: pd.DataFrame,
    database: Database,
    table_name: str,
    schema: str,
    if_exists: str = 'replace'
) -> None:
    table = Table(table=table_name, schema=schema)
    database.db_engine_spec.df_to_sql(
        database,
        table,
        df,
        to_sql_kwargs={
            "chunksize": 1000,
            "if_exists": if_exists,
            "index": None,
            "index_label": None,
        },
    )
