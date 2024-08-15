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
@Time       : 2023/7/18 14:58
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
from typing import Any

import requests


def req(params: dict) -> Any:
    res = requests.request(**params)
    res.encoding = 'utf8'
    if res.status_code == 200 or res.status_code == 201:
        if res.text:
            return json.loads(res.text)

    return None
