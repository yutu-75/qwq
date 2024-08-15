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

import datetime
import logging
import random
import string
from typing import List

import jwt
from flask import current_app, g
from werkzeug.security import generate_password_hash, check_password_hash

logger = logging.getLogger(__name__)
base_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ',', '.', '~',
            '!', '@', '#', '$', '%', '^', '&', '*', ';', ':', '?']
number_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
small_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']
big_str = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
special_str = ['.', '/', '_', '!', '@', '#']


class Passwd:
    @staticmethod
    def random_choose(pwd_len: int = 16) -> List[str]:
        return random.sample(base_str, pwd_len)

    @staticmethod
    def random_choose_pwd(pwd_len: int = 12) -> List[str]:
        pwd = random.sample(small_str, pwd_len - 3)
        pwd.append(random.choice(number_str))
        pwd.append(random.choice(big_str))
        pwd.append(random.choice(special_str))
        return pwd

    @classmethod
    def create_password_pwd(cls, pwd_len: int = 12):
        return ''.join(cls.random_choose_pwd(pwd_len))

    @classmethod
    def create_password(cls, pwd_len: int = 16):
        return ''.join(cls.random_choose(pwd_len))

    @staticmethod
    def generate_password_hash(pwd: str) -> str:
        return generate_password_hash(pwd)

    @staticmethod
    def check_password_hash(pwd_hash: str, password: str) -> bool:
        return check_password_hash(pwd_hash, password)


class ShareToken:
    @staticmethod
    def generate_token(dashboard_id: int, share_user_id: int, exp: int = 300) -> str:
        payload = {
            'share_user_id': share_user_id,
            'dashboard_id': dashboard_id,
            'exp': datetime.datetime.now() + datetime.timedelta(seconds=exp)
        }
        token = jwt.encode(payload=payload,
                           key=current_app.config.get("SECRET_KEY"),
                           algorithm='HS256')
        return token

    @staticmethod
    def validate_token(token: str, appbuilder: "Appbuilder") -> bool:
        try:
            payload = jwt.decode(token,
                                 key=current_app.config.get("SECRET_KEY"),
                                 algorithms='HS256',
                                 options={"verify_signature": False})
        except Exception as e:
            logger.error(e)
            return False

        g.user = appbuilder.sm.get_user_by_id(payload["share_user_id"])
        return True


def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # 包含所有字母和数字的字符串
    random_string = ''.join(random.sample(characters, length))
    return random_string
