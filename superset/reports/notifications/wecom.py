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
@Time       : 2023/9/11 16:38
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from superset.reports.models import ReportRecipientType
from superset.reports.notifications import IChangAnNotification
from superset.reports.notifications.exceptions import NotificationError
from superset.v2.utils.Wecom_msg import WecomMessage


class WecomNotification(IChangAnNotification):
    """
    发送企业微信消息
    """

    type = ReportRecipientType.WECOM

    def send(self) -> None:
        """发送ichangan消息"""
        if WecomMessage().send_message(
            content=self._get_content,
            ext_info=self._get_ext_info,
            from_app_name=self._from_app_name,
            send_by_login_id=self._send_by_login_id,
            user_login_ids=self._user_login_ids,
        ):
            return

        raise NotificationError("failed")
