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
@Time       : 2023/7/12 13:52
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import pandas as pd
import simplejson
from flask_appbuilder.security.sqla.models import User

from superset import conf
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.key_value.utils import get_uuid_namespace
from superset.models.core import Database
from superset.sql_parse import Table
from superset.v2.databases.commands.create import CreateDatabaseV2Command
from superset.v2.databases.dao import DatabaseV2DAO
from superset.v2.datasources.api_datasources.dao import APITablesDAO
from superset.v2.utils.dynamic_token.auth_token import gen_token
from superset.v2.utils.req_utils import req


gen_token_func = {
    "#{{authToken}}": gen_token
}


def get_save_default_db(user: User) -> Database:
    database_name = get_uuid_namespace(conf['UPLOAD_DATABASE_URI']).hex
    database = DatabaseV2DAO.find_by_name(database_name)
    if database is None:
        database = CreateDatabaseV2Command(
            user,
            {
                "database_name": database_name,
                "sqlalchemy_uri": conf["UPLOAD_DATABASE_URI"],
            }
        ).run()

    return database


def get_api_token(token_api: dict) -> str:
    """动态获取API TOKEN"""
    api_table_id = token_api.get("api_table_id")
    api_table = APITablesDAO.find_by_id(api_table_id)
    if api_table:
        df = api_data_to_df(api_table.configuration, api_table.data_path)
        if df is None:
            raise HTTPError('Token not obtained', 400)

        if len(df.columns) == 0:
            return ""

        return str(df[df.columns[0]][0])


def get_dynamic_token(configuration):
    """获取token"""
    if isinstance(configuration, str):
        configuration = simplejson.loads(configuration)

    data = configuration.get("data")
    if isinstance(data, dict):
        configuration["data"] = simplejson.dumps(data)

    # 由token生成策略动态生成token
    # for k, v in configuration.get("headers", {}).items():
    #     if isinstance(v, str) and v.find("#{{") == 0:
    #         func = gen_token_func.get(v, False)
    #         if func:
    #             configuration["headers"][k] = func()

    # 由API获取TOKEN
    token_api = configuration.pop("token_api", False)
    if token_api:
        value = token_api.get("value")
        token = get_api_token(value)
        key_ = token_api.get("key")
        if key_ and token:
            configuration["headers"][key_] = token

    return configuration


def api_data_to_df(configuration: [dict, str], data_path: [dict, str]) -> pd.DataFrame:
    configuration = get_dynamic_token(configuration)
    data, headers = req(configuration, response_headers=True)
    if data is None:
        raise HTTPError(Messages.REQUEST_FAILURE, 400)

    if isinstance(data_path, str):
        data_path = simplejson.loads(data_path.replace("'", '"'))

    if data_path.get("record_path", False):
        data_path["record_prefix"] = ".".join(data_path["record_path"]) + "."
    else:
        data_path["record_path"] = None

    rename_columns = data_path.pop("columns")
    try:
        df = pd.json_normalize({"headers": headers, "result": data}, **data_path)
    except KeyError as ex:
        raise HTTPError(Messages.API_DATASOURCE_PARSE_ERROR, 400)
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
):
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

