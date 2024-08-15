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
@Time       : 2023/7/10 16:50
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import pandas as pd
import simplejson

from superset import conf
from superset.exceptions import HTTPError
from superset.global_messages import Messages


def formdata_to_df(file):
    file_type = file.filename.split(".")[-1]
    # EXCEL
    if file_type in conf["EXCEL_EXTENSIONS"]:
        try:
            df = pd.read_excel(io=file, sheet_name=None)
        except ValueError:
            raise HTTPError(Messages.FILE_IS_NONE, 400)
    # CSV
    elif file_type in conf["CSV_EXTENSIONS"]:
        df = pd.read_csv(file)
    # JSON
    elif file_type == 'json':
        data = file.stream.read()
        df = pd.json_normalize(simplejson.loads(data))

    else:
        raise HTTPError(Messages.FILE_TYPE_ERROR, 400)

    def format_datetime64(df_):
        for col in df_.columns:
            if df_[col].dtype == 'datetime64[ns]':
                df_[col] = df_[col].apply(str)

    if isinstance(df, dict):
        for sheet, _ in df.items():
            format_datetime64(_)

    else:
        format_datetime64(df)

    return df
