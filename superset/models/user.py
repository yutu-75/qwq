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

from flask_appbuilder.security.sqla.models import User
from sqlalchemy import String, Column, Boolean
from typing import Union
from superset import db
from superset.utils.models_utils import id_or_slug_filter


class UserV2(User):
    __tablename__ = "ab_user"
    cn_name = Column(String(64), nullable=True, comment="中文名称")
    is_admin = Column(Boolean, nullable=False, default=False, comment="是否超级管理员")

    @classmethod
    def get(cls, id_or_slug: Union[str, int]):
        query = db.session.query(UserV2).filter(id_or_slug_filter(UserV2, id_or_slug))
        return query.one_or_none()

    @classmethod
    def get_user_by_cn_name(cls, cn_name: Union[str]):
        query = db.session.query(UserV2).filter(UserV2.cn_name == cn_name)
        return query.one_or_none()

    @classmethod
    def get_model_by_username(cls, username: Union[str]):
        query = db.session.query(UserV2).filter(UserV2.username == username)
        return query.one_or_none()

    @classmethod
    def get_zzfx_user(cls):
        query = db.session.query(UserV2).filter(UserV2.cn_name.like('%zzfx-%'))
        return query.all()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return self.username
