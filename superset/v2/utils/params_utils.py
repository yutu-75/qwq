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
import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

logger = logging.getLogger(__name__)


def format_page_from_params(params):
    """
        判断 page_size 与 page_index
        并返回 int 类型
        默认值
            page_size： 20
            page_index： 1
    """
    if params.get('page_size') == '' or params.get('page_size') is None or int(params.get('page_size')) < 1:
        params['page_size'] = 20
    else:
        params['page_size'] = int(params.get('page_size'))

    if params.get('page_index') == '' or params.get('page_index') is None or int(params.get('page_index')) < 1:
        params['page_index'] = 1
    else:
        params['page_index'] = int(params.get('page_index'))

    return params


def sql_format(sqlalchemy_uri: str, sql: str) -> str:
    if sqlalchemy_uri.find("postgre") > -1:
        # postgre使用双引号
        sql = sql.replace('`', '"')

    return sql


def aes_decryption(encrypted_data: str) -> str:
    secret_key = b'PF28ohCnRt2UGqHh-lZqFnUqz6dD8jo='
    iv = b't2U4Gsdqh-lZsdqF'  # 16 bytes IV
    # 将加密后的数据从base64格式解码为字节
    encrypted_bytes = base64.b64decode(encrypted_data)

    # 创建AES解密器
    cipher = AES.new(secret_key, AES.MODE_CBC, iv=iv)

    # 解密数据
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # 去除填充
    original_text = unpad(decrypted_bytes, AES.block_size)

    return original_text.decode('utf-8')
