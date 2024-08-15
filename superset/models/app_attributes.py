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

import enum
from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import Role
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, Text, BigInteger, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship

from superset import db
from superset.models.helpers import AuditMixinNullable, ImportExportMixin
from superset.utils.generate_app_credentials import generate_app_key, \
    generate_app_secret


class AppAttribute(Model, AuditMixinNullable, ImportExportMixin):
    """
    第三方应用属性
    """

    __tablename__ = "app_attributes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, comment="应用名称")
    code = Column(String(255), nullable=False, comment="应用标识")
    app_desc = Column(Text(255), nullable=False, comment="描述")
    app_key = Column(String(255), nullable=False, comment="应用ID", default=generate_app_key())
    app_secret = Column(String(255), nullable=False, comment="应用密钥", default=generate_app_secret())
    enabled = Column(Boolean, nullable=False, comment="0 禁用 1 启用")
    is_delete = Column(Boolean, nullable=False,
                       comment="逻辑删除（0-未删除，1-已删除）", default=False)
    role_id = Column(Integer, ForeignKey("ab_role.id"), nullable=False,
                     comment="角色关联id")
    role = relationship('Role')

    def __repr__(self) -> str:
        return self.name


    @classmethod
    def get_role_models(cls, app_key):
        """
        通过appKey判断条件在关联AppAttribute,Role表获取Role模型对象
        :param app_key:
        :return:
        """
        qry = db.session.query(AppAttribute, Role).filter(
            AppAttribute.app_key == app_key).join(Role)

        for app_attribute, role in qry:
            return role


class STATUS(int, enum.Enum):
    FAIL = 0
    SUCCESS = 1


class AppLogRecord(Model, AuditMixinNullable):
    """
    三方 app 调用日志记录表
    """
    __tablename__ = "app_log_record"
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, nullable=False, comment='三方应用 id')
    role_id = Column(Integer, nullable=False, comment='三方应用对应的 role_id')
    role_name = Column(String(32), nullable=False, comment='三方应用对应的 role_name')
    app_name = Column(String(32), nullable=False, comment='三方应用 app_name')
    request_path = Column(String(255), nullable=False, comment='请求 URL')
    status_code = Column(String(32), nullable=True, comment='响应状态码')
    error_message = Column(String(255), nullable=True, comment='具体错误信息')
    exception = Column(Text, nullable=True, comment='后端异常位置')
    ip = Column(String(32), nullable=False, comment='请求 ip')
    request_params = Column(Text, nullable=True, comment='请求参数')
    response_return_data = Column(Text, nullable=True, comment='响应数据')
    response_return_data_nums = Column(Integer, nullable=True, comment='响应数据数量')
    request_size = Column(BigInteger, nullable=True, comment='请求大小, 单位: bytes')
    request_time = Column(DateTime, nullable=True, comment='请求时间')
    response_size = Column(BigInteger, nullable=False, comment='响应大小, 单位: bytes')
    # total_latency = Column(BigInteger, nullable=True, comment='请求总延迟')
    service_latency = Column(BigInteger, nullable=True, comment='后端耗时')
    status = Column(String(32), nullable=True, comment='请求任务结果')
