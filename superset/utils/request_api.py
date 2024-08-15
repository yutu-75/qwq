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
@Time       : 2023/7/11 15:16
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
import logging
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlparse, parse_qs
from superset import conf, cache_manager

logger = logging.getLogger(__name__)


def get_upm_user_name(url: str, x_token: str, usid: str) -> [dict, None]:
    headers = {
        'X-Token': x_token,
        'Cookie': 'usid=' + usid + ';X-Token=' + x_token
    }
    logger.info(f">>>>>headers:{headers},url:{url}")
    response = requests.get(url, headers=headers)
    logger.info(f">>>>>response_text{response.text}")
    if response.status_code == 200:
        data = json.loads(response.text).get("data", None)
        if data:
            return data.get('loginId', None)

    return None


def get_yuntu_user_info(token: str) -> [dict]:
    url = conf["YUNTU_CHECK_TOKEN_URL"]
    username = conf["YUNTU_APP_KEY"]
    password = conf["YUNTU_SECRET_KEY"]
    res = requests.post(
        url=url,
        auth=HTTPBasicAuth(username, password),
        json={'token': token},
        timeout=5
    )
    logger.info(res.text)
    if res.status_code == 200:
        return res.json()

    return None


def get_caps_user_info(token: str) -> dict or None:
    """
    渝北工厂门户token校验
    :param token: 渝北工厂门户网站token
    :return:
    """
    url = conf["CAPS_CHECK_TOKEN_URL"]

    res = requests.get(
        url=url,
        headers={
            "appCode": conf["APP_CODE"],
            "apim-appcode-key": conf["APP_CODE_KEY"]
        },
        params={
            'token': token
        },
        timeout=5
    )
    logger.info(res.text)
    if res.status_code == 200:
        return res.json().get("data")

    return None


def get_caps_url_permission(username: str) -> set:
    """
    渝北工厂嵌入页面权限查询
    :param username: 工号
    :return:
    """
    cache_key = f'caps:url:permission:{username}'
    cache = cache_manager.cache_read_client
    urls = cache.smembers(cache_key)
    if urls:
        return {item.decode() for item in urls}

    url = conf["CAPS_USER_PERMISSION"]
    res = requests.get(
        url=url,
        headers={
            "appCode": conf["CAPS_APP_CODE"],
            "appkey": conf["CAPS_APP_KEY"]
        },
        params={
            'userId': username
        },
        timeout=5
    )
    logger.info(res.text)
    if res.status_code == 200:
        data = res.json().get("data", {})
        btn_perm = data.get("btnPermission") or []
        uri_perm = data.get("uriPermission") or []
        urls = btn_perm + uri_perm
        cache.sadd(cache_key, *urls)
        cache.expire(cache_key, 10)
        return set(urls)

    return set()


def get_token(url: str) -> str:
    query_str = urlparse(url).query
    params = parse_qs(query_str)
    _token = params.get("token", [""])
    if _token == [""]:
        _token = params.get("IdentityToken", [""])
    token = str(_token[0]).strip().split("Bearer ")[-1]
    return token


def get_cmp_user_by_token(token: str) -> dict or None:
    """
    cds门户token校验
    :param token: cds门户网站token
    :return:
    """
    url = conf["CMP_GET_USER_BY_TOKEN"]
    res = requests.get(
        url=url,
        params={
            'identityToken': token
        },
        timeout=20
    )
    if res.status_code == 200:
        return res.json().get("data")

    return None


def get_cds_user_info(token: str) -> dict or None:
    """
    cds门户token校验
    :param token: cds门户网站token
    :return:
    """
    url = conf["CDS_CHECK_TOKEN_URL"]
    res = requests.post(
        url=url,
        json={
            'token': token
        },
        timeout=20
    )
    logger.info(res.text)
    if res.status_code == 200:
        return res.json().get("data")

    return None

