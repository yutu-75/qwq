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
@Time       : 2023/5/25 12:44
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
import logging
from typing import Optional

import pandas as pd
import simplejson
from flask_appbuilder import Model

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.v2.utils.req_utils import req

logger = logging.getLogger(__name__)


class ImportDataSourceCommand(BaseCommand):
    to_sql_kwargs = {
        "chunksize": 1000,
        "if_exists": "replace",
        "index": False,
    }

    def __init__(self, model: Model = None):
        self._model: Optional[Model] = model

    def run(self):
        self.validate()
        """数据写入数据库"""
        data = req(json.loads(self._model.configuration))
        if data is None:
            raise HTTPError(Messages.REQUEST_FAILURE, 400)

        data_path = self._model.data_path
        if isinstance(data_path, str):
            data_path = simplejson.loads(data_path.replace("'", '"'))

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

        self._model.df_to_sql(df, self.to_sql_kwargs)

    def validate(self) -> None:
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)
