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
@Time       : 2023/9/11 16:34
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from superset import conf
from superset.v2.utils.ichangan_msg import IChangAnMessage


class WecomMessage(IChangAnMessage):
    def __init__(self, **kwargs):
        super(WecomMessage, self).__init__(**kwargs)
        self._send_msg_url = kwargs.get("wecom_send_msg_url",
                                        conf["WECOM_SEND_MSG_URL"])
