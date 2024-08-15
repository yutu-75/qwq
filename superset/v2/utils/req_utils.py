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
import os
import json
import logging
from json.decoder import JSONDecodeError
from typing import Any

import requests
from requests.auth import HTTPBasicAuth

from superset import conf
from superset.exceptions import HTTPError
from superset.global_messages import Messages

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


logger = logging.getLogger(__name__)


def req(params: dict, response_headers: bool = False) -> Any:
    logger.info(params)
    if params.get("auth", False):
        username = params.get('username', '')
        password = params.get('password', '')
        params["auth"] = HTTPBasicAuth(username, password)

    res = requests.request(**params)
    res.encoding = 'utf8'
    if res.status_code == 200 or res.status_code == 201:
        if res.text:
            try:
                data = json.loads(res.text)
                if response_headers:
                    return data, dict(res.headers)

                return data
            except JSONDecodeError:
                logger.error(res.text)

    raise HTTPError(Messages.REQUEST_ERROR_MSG, 400, (res.status_code, res.text))


def get_cas_user_info(username: str, password: str) -> [dict, None]:
    url = conf['CAS_USER_INFO_URL']
    # pwd = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    # 外网访问CAS登陆接口，密码RSA加密
    pwd = rsa_encrypt(password)
    res = requests.post(
        url=url,
        data={
            "username": username,
            "password": pwd,
            "encryptionMethod": "RSA"
        }
    )
    logger.info(res.text)
    if res.status_code == 200 or res.status_code == 201:
        data = res.json()
        return data["authentication"]["principal"]["attributes"]

    return None


# RSA加密
def rsa_encrypt(plaintext):
    try:
        current_path = os.path.dirname(__file__)
        public_key_path = conf["CAS_PUBLIC_KEY"]
        with open(current_path + public_key_path, encoding="utf8") as f:
            public_key = f.read()
        rsa_key = RSA.import_key(public_key)
        cipher = PKCS1_v1_5.new(rsa_key)
        cipher_text = cipher.encrypt(plaintext.encode())
        return base64.b64encode(cipher_text)
    except FileNotFoundError:
        print("File not found or path incorrect.")

