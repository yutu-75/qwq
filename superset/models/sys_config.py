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

# -*- coding: utf-8 -*-

"""
@Time       : 2023/6/16 14:11
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from flask_appbuilder import Model
from sqlalchemy import UniqueConstraint, Column, Integer, String, Boolean


class SysConfig(Model):
    __tablename__ = "sys_config"
    __table_args__ = (UniqueConstraint("param_key"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    config_type = Column(String(50), nullable=False, comment="系统设置类型")
    param_key = Column(String(128), nullable=False, comment="参数key")
    param_value = Column(String(255), nullable=False, comment="参数value")
    status = Column(Boolean, default=False, comment="状态")
