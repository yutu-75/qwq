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

import logging
import platform

import pdfkit
from flask import current_app


def wk_to_pdf_binary_by_html(html: str, output_path=False):
    """
        wkhtmltopdf
        通过html 生成pdf二进制流
    """
    try:
        # html 转pdf
        if platform.system() == "Windows":
            path_wk = r'D:/soft/wkhtmltopdf/bin/wkhtmltopdf.exe'
        else:
            path_wk = current_app.config["WK_BIN_PATH_PDF"]

        config = pdfkit.configuration(wkhtmltopdf=path_wk)
        options = {
            'page-size': 'B4',
            'encoding': 'UTF-8',
        }
        return pdfkit.from_string(input=html,
                                  output_path=output_path,
                                  configuration=config,
                                  options=options,
                                  )
    except Exception as e:
        logging.exception(e)


def wk_to_pdf_binary_by_url(url: str, output_path=False):
    """
        wkhtmltopdf
        通过url 生成pdf二进制流
    """

    try:
        # html 转pdf
        if platform.system() == "Windows":
            path_wk = r'D:/soft/wkhtmltopdf/bin/wkhtmltopdf.exe'
        else:
            path_wk = current_app.config["WK_BIN_PATH_PDF"]
        config = pdfkit.configuration(wkhtmltopdf=path_wk)

        options = {
            'page-size': 'B4',
            'encoding': 'UTF-8'
        }
        return pdfkit.from_url(url=url,
                               output_path=output_path,
                               configuration=config,
                               options=options,
                               )
    except Exception as e:
        logging.exception(e)
