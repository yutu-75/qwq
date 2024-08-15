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
@Time       : 2023/9/11 14:52
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import json
import logging

from flask_babel import gettext as __

from superset import conf
from superset.reports.models import ReportRecipientType
from superset.reports.notifications import BaseNotification
from superset.reports.notifications.exceptions import NotificationError
from superset.v2.utils.ichangan_msg import IChangAnMessage

logger = logging.getLogger(__name__)


class IChangAnNotification(BaseNotification):
    """
    发送ichangan消息
    """

    type = ReportRecipientType.ICHANGAN

    def _get_subject(self) -> str:
        return __(
            "%(prefix)s %(title)s",
            prefix=conf["EMAIL_REPORTS_SUBJECT_PREFIX"],
            title=self._content.name,
        )

    @property
    def _get_content(self):
        """消息内容"""
        return self._get_subject()

    @property
    def _get_ext_info(self):
        """扩展消息"""
        return self._content.url

    @property
    def _from_app_name(self):
        """消息源应用"""
        return "superset"

    @property
    def _send_by_login_id(self):
        """发送人"""
        return conf["CMP_LOGIN_ID"]

    @property
    def _user_login_ids(self):
        """接收人，逗号分割多个用户"""
        return json.loads(self._recipient.recipient_config_json)["target"]

    def send(self) -> None:
        """发送ichangan消息"""
        if IChangAnMessage().send_message(
            content=self._get_content,
            ext_info=self._get_ext_info,
            from_app_name=self._from_app_name,
            send_by_login_id=self._send_by_login_id,
            user_login_ids=self._user_login_ids,
        ):
            return

        raise NotificationError("failed")
