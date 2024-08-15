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
@Time       : 2023/9/11 9:53
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import base64
import json
import logging
from json import JSONDecodeError

import requests

from superset import conf
from superset.exceptions import HTTPError
from superset.global_messages import Messages

logger = logging.getLogger(__name__)


class IChangAnMessage:
    def __init__(self, **kwargs):
        self._cmp_login_url = kwargs.get("cmp_login_url", conf["CMP_LOGIN_URL"])
        self._cmp_login_id = kwargs.get("cmp_login_id", conf["CMP_LOGIN_ID"])
        self._cmp_login_password = kwargs.get("cmp_login_password",
                                              conf["CMP_LOGIN_PASSWORD"])
        self._client_ip = kwargs.get("client_ip", conf["CLIENT_IP"])
        self._send_msg_url = kwargs.get("ichangan_send_msg_url",
                                        conf["ICHANGAN_SEND_MSG_URL"])

    def _get_identity_token(self) -> str:
        data = {
            "loginId": self._cmp_login_id,
            "password": base64.b64encode(
                self._cmp_login_password.encode()).decode(),
            "clientIP": self._client_ip,
        }
        res = requests.post(self._cmp_login_url, data=data)
        res.encoding = 'utf8'
        if res.status_code == 200 or res.status_code == 201:
            logger.info("get identity token: %s", res.text)
            if res.text:
                try:
                    data = json.loads(res.text)
                    if data.get("data", {}).get("isSuccess", False):
                        return data["data"]["msg"]
                except JSONDecodeError:
                    logger.error(res.text)

        raise HTTPError(Messages.REQUEST_ERROR_MSG, 400, (res.status_code, res.text))

    def send_message(self, **kwargs) -> bool:
        headers = {
            "identityToken": self._get_identity_token()
        }
        _body = {
            "content": kwargs.get("content", ""),
            "extInfo": kwargs.get("ext_info", ""),
            "fromAppName": kwargs.get("from_app_name", ""),
            "sendByLoginId": kwargs.get("send_by_login_id", ""),
            "userLoginIds": kwargs.get("user_login_ids", "")
        }
        res = requests.post(self._send_msg_url,
                            headers=headers,
                            json=_body)
        res.encoding = 'utf8'
        if res.status_code == 200 or res.status_code == 201:
            logger.info("send message: %s", res.text)
            if res.text:
                res = json.loads(res.text)
                if res.get("isSuccess", False):
                    return True

        logger.error("send error: %s", res.text)
        return False
