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
@Time       : 2023/4/14 17:12
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import io
from datetime import datetime
from typing import Any
from urllib.request import urlopen

import pandas as pd
from flask import make_response

from superset.charts.data.commands.get_data_command import ChartDataCommand
from superset.exceptions import HTTPError
from superset.v2.utils.water_mark_utils import WaterMark
from superset.v2.utils.wkhtmltopdf_utils import wk_to_pdf_binary_by_html


def sql_data_to_excel_data(data_list: list) -> Any:
    """
        根据sql查询的结果，生成 excel数据
    """
    columns = []
    excel_data = []
    if data_list:
        # 添加index
        for key in data_list[0].keys():
            columns.append(key)

        # 添加excel_data
        for i in data_list:
            item = []
            for key, values in i.items():
                item.append(values)
            excel_data.append(item)

    df = pd.DataFrame(data=excel_data,
                      index=None,
                      columns=columns)

    return df


def create_excel_response(data=None) -> Any:
    """
        生成 excel response
    """
    resp = make_response(data)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S")
    resp.headers["Content-Type"] = "application/x-xlsx; charset=utf-8"
    resp.headers["Content-Disposition"] = f'attachment; filename={filename}.xlsx'
    resp.headers["Cache-Control"] = "no-cache"
    return resp


def create_pdf_response(data=None) -> Any:
    """
        生成 pdf response
    """
    resp = make_response(data)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S")
    resp.headers["Content-Type"] = "application/pdf; charset=utf-8"
    resp.headers["Content-Disposition"] = f'attachment; filename={filename}.pdf'
    resp.headers["Cache-Control"] = "no-cache"
    return resp


def query_context_to_df(query_context):
    """
       通过查询文本，生成 pandas df
    """
    try:
        pd_data = []
        # 根据查询条件，生成结果
        command = ChartDataCommand(query_context)
        result = command.run()

        # 添加columns
        columns = result["queries"][0]["colnames"]
        # 添加excel_data
        for i in result["queries"][0]["data"]:
            item = []
            for key, values in i.items():
                item.append(values)
            pd_data.append(item)

        return pd.DataFrame(data=pd_data,
                            index=None,
                            columns=columns)
    except Exception as e:
        raise HTTPError(str(e), 400)


def query_context_to_dfs(query_context_list):
    """
        通过查询文本，生成 pandas df列表
    """

    dfs = []
    for query_context in query_context_list:
        try:
            pd_data = []
            # 根据查询条件，生成结果
            command = ChartDataCommand(query_context)
            result = command.run()

            # 添加columns
            columns = result["queries"][0]["colnames"]
            # 添加excel_data
            for i in result["queries"][0]["data"]:
                item = []
                for key, values in i.items():
                    item.append(values)
                pd_data.append(item)

            dfs.append(pd.DataFrame(data=pd_data,
                                    index=None,
                                    columns=columns))
        except Exception as e:
            raise HTTPError(str(e), 400)
    return dfs


def create_excel_response_by_base64_df(df, image_data=None):
    """
        创建flask excel resp 通过base64图片，及df
    """
    try:
        # 创建io流
        out = io.BytesIO()
        writer = pd.ExcelWriter(out, engine='xlsxwriter')

        page = 1
        if image_data is not None:
            # 展示图片, sheet_1
            sheet = writer.book.add_worksheet(f'sheet_{page}')

            # 图片加水印
            image_data = WaterMark().add_mark(
                in_type='img_base64',
                out_type='img_base64',
                in_data=image_data
            )

            # 插入图片
            image_data = io.BytesIO(urlopen(image_data).read())

            sheet.insert_image('A1', '', {'image_data': image_data})
            page += 1

        # 生成excel
        df.to_excel(
            excel_writer=writer,
            sheet_name=f'sheet_{page}'
        )
        writer.save()
        writer.close()

        # 生成excel response
        resp = create_excel_response(out.getvalue())
        return resp
    except Exception as e:
        raise HTTPError(str(e), 400)


def create_excel_response_by_base64_dfs(dfs, image_data=None):
    """
        创建flask excel resp 通过base64图片，及df列表
    """
    try:
        # 创建io流
        out = io.BytesIO()
        writer = pd.ExcelWriter(out, engine='xlsxwriter')

        page = 1
        if image_data is not None:
            # 展示图片, sheet_1
            sheet = writer.book.add_worksheet(f'sheet_{page}')

            # 图片加水印
            image_data = WaterMark().add_mark(
                in_type='img_base64',
                out_type='img_base64',
                in_data=image_data
            )

            # 插入图片
            image_data = io.BytesIO(urlopen(image_data).read())
            sheet.insert_image('A1', '', {'image_data': image_data})
            page += 1

        # 循环生成 excel
        for df in dfs:
            df.to_excel(
                excel_writer=writer,
                sheet_name=f'sheet_{page}'
            )
            page += 1

        writer.save()
        writer.close()

        # 生成excel response
        resp = create_excel_response(out.getvalue())
        return resp
    except Exception as e:
        raise HTTPError(str(e), 400)


def create_pdf_response_by_base64_df(image_data=''):
    """
        创建flask pdf resp 通过base64图片
    """
    try:
        # 生成pdf
        # html_out = df.to_html()

        html_out = f'<img src="{image_data}"/>'

        # 通过html生成pdf 二进制流
        writer = wk_to_pdf_binary_by_html(html_out)

        # 加水印
        writer = WaterMark().add_mark(
            in_type='pdf_binary',
            out_type='pdf_binary',
            in_data=writer
        )

        # 生成pdf response
        resp = create_pdf_response(writer)
        return resp
    except Exception as e:
        raise HTTPError(str(e), 400)


def create_pdf_response_by_base64_dfs(image_data=''):
    """
        创建flask pdf resp 通过base64图片
    """
    try:
        html_out = f'<img src="{image_data}"/>'
        # html 转pdf

        # 通过html生成pdf 二进制流
        writer = wk_to_pdf_binary_by_html(html_out)

        # 加水印
        writer = WaterMark().add_mark(
            in_type='pdf_binary',
            out_type='pdf_binary',
            in_data=writer
        )

        # 生成pdf response
        resp = create_pdf_response(writer)
        return resp
    except Exception as e:
        raise HTTPError(str(e), 400)
