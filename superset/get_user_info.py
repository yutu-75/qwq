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
新增：李洪浩-202212-20
新增内容：提供用户行级权限查询接口，从行级权限新增的user_job_info表获取组织信息
"""

import logging
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)

# _database_uri = 'mysql://cabi:Tpml0L1iu@10.64.9.21/dev_cabi?charset=UTF8'


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            src = super(Singleton, cls)
            cls._instance = src.__new__(cls)
        return cls._instance


class MysqlDbConnect(Singleton):
    def __init__(self, database_uri):
        self.database_uri = database_uri

    def create_engine(self):
        _engine = create_engine(self.database_uri, max_overflow=5)
        return _engine


def user_info_get(user_account, database_uri):
    """Gets detailed user information and returns."""

    if "sqlite" in database_uri:
        logger.warning(
            "SQLite Database support for metadata databases will be removed \
            in a future version of Superset."
        )

    try:
        engine = MysqlDbConnect(database_uri).create_engine()
        # _session = sessionmaker(bind=engine)
        sql_query = "select * from user_job_info where user_account = {} order by id;".format(user_account)
        df = pd.read_sql_query(sql_query, engine)
        _res_index = df.columns.values
        _res_values = df.values[0]

        res = dict(zip(_res_index, _res_values))

        for key, value in res.items():
            if res[key] == "":
                res[key] = None

        return res

    except Exception as e:
        logger.warning("获取详细用户信息失败: " + str(e))

