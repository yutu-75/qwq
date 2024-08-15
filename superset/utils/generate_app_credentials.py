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

import secrets
import string


def generate_app_key(length=16):
    """
     生成应用程序的秘密字符串。
    :param length:
    :return:
    """
    characters = string.ascii_letters + string.digits
    app_key = ''.join(secrets.choice(characters) for _ in range(length))
    return app_key


def generate_app_secret(length=32):
    """
    生成应用程序的秘密字符串。
    :param length:
    :return:
    """
    characters = string.ascii_letters + string.digits
    app_secret = ''.join(secrets.choice(characters) for _ in range(length))
    return app_secret


