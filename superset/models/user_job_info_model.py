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
作者：李洪浩
创建时间：2022年12月20日
功能：用户组织信息表模型

"""

from flask_appbuilder import Model
from flask_appbuilder.models.decorators import renders
from markupsafe import Markup
from sqlalchemy import Column, Integer, String, Boolean, Sequence, SmallInteger
from superset.models.helpers import AuditMixinNullable


"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who

"""


class UserJobInfo(Model, AuditMixinNullable):
    __tablename__ = "user_job_info"
    id = Column(Integer, Sequence("user_job_info_id_seq"), primary_key=True)
    user_account = Column(String(128), unique=True, nullable=False)
    user_name = Column(String(256), nullable=True)
    user_type = Column(SmallInteger, default=0)
    position_name = Column(String(256), nullable=True)
    organization_code = Column(String(256), nullable=True)
    organization_name = Column(String(256), nullable=True)
    invest_code = Column(String(256), nullable=True)
    invest_name = Column(String(256), nullable=True)
    parent_dept_code = Column(String(256), nullable=True)
    dept_code = Column(String(256), nullable=True)
    dept_name = Column(String(256), nullable=True)
    dept_level = Column(String(256), nullable=True)
    active = Column(Boolean, default=True)
    remarks = Column(String(255))

    def __repr__(self):
        return self.user_account

    # # 自定义一个函数字段和渲染样式，供前端显示
    # @renders('user_name')
    # def my_name(self):
    #     return Markup('<b style="color:red">' + self.user_name + '</b>')

