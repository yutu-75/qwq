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
@Time       : 2023/5/10 9:12
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
import logging
from typing import Any, Dict, Optional

from flask_appbuilder.security.sqla.models import User

from superset.charts.schemas import ChartDataQueryContextSchema
from superset.commands.base import BaseCommand
from superset.constants import EXPORT
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.slice import Slice
from superset.v2.charts.dao import ChartV2DAO

from superset.v2.utils.explore_utils import (
    create_excel_response_by_base64_df,
    create_pdf_response_by_base64_df,
    query_context_to_df
)

logger = logging.getLogger(__name__)


class ChartExploreCommand(BaseCommand):
    def __init__(self, user: User, model_id: str, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._properties = data.copy()
        self._model: Optional[Slice] = None

    def validate(self) -> None:
        self._model = ChartV2DAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(EXPORT)

    def run(self) -> Any:
        self.validate()

        try:
            # 判断导出文件类型
            explore_format = self._properties.get('explore_format', None)

            # excel
            if explore_format == 'excel':
                # 获取查询内容，转json
                query_context = json.loads(self._model.query_context)
                query_context["datasource"]["id"] = self._model.table.id
                query_context = ChartDataQueryContextSchema().load(query_context)
                # 获取sql数据 转换成excel_data
                df = query_context_to_df(query_context)

                # 生成excel response
                resp = create_excel_response_by_base64_df(
                    df,
                    self._properties.get('image_data', '')
                )
                return resp
            # pdf
            elif explore_format == 'pdf':
                # 生成pdf response
                resp = create_pdf_response_by_base64_df(
                    self._properties.get('image_data', '')
                )
                return resp
            else:
                raise HTTPError(Messages.PARAMETER_ERROR, 400)
        except Exception as e:
            raise HTTPError(str(e), 400)
