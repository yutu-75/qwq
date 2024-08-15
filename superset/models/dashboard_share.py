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
from __future__ import annotations

import logging
from datetime import datetime
from typing import Dict, Any

from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint, Boolean,
)
from sqlalchemy.orm import relationship, backref
import sqlalchemy as sa
from superset.models.helpers import AuditMixinNullable

metadata = Model.metadata

logger = logging.getLogger(__name__)


class DashboardShare(Model, AuditMixinNullable):
    __tablename__ = "dashboard_share"
    __table_args__ = (UniqueConstraint("dashboard_id"),)

    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False, comment='路由')
    dashboard_id = Column(Integer, ForeignKey("dashboards.id"), nullable=False)
    dashboard = relationship(
        "Dashboard",
        backref=backref("dashboard_share", cascade="all, delete-orphan"),
        foreign_keys=[dashboard_id],
    )
    password = Column(String(256), nullable=False, comment='密码')

    start_time = sa.Column(
        sa.DateTime, default=datetime.now, nullable=True, comment="有效期开始时间"
    )
    expiry = Column(Integer, nullable=True, default=f'{60*60*24*30}', comment='有效期是多少秒')
    is_permanent = Column(Boolean, default=False, comment='是否启用永久有效')

    def __repr__(self):
        return "(%s, %s, %s)" % (self.dashboard_id, self.url, self.password)

    @property
    def data(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "url": self.url,
            "dashboard_id": self.dashboard_id,
        }
