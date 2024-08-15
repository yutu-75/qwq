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

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import Role
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Sequence,
    UniqueConstraint,
)

from superset import db


class RoleV2(Role):
    __tablename__ = "ab_role"

    # id = Column(Integer, Sequence("ab_role_id_seq"), primary_key=True)
    # name = Column(String(64), unique=True, nullable=False)
    # permissions = relationship(
    #     "PermissionView",
    #     secondary=assoc_permissionview_role,
    #     backref="role1"
    # )
    creator_id = Column(Integer)

    def is_creator(self, user_id: int) -> bool:
        return user_id == self.creator_id

    def __repr__(self):
        return self.name


class UserRole(Model):
    __tablename__ = "ab_user_role"

    id = Column(Integer, Sequence("ab_user_role_id_seq"), primary_key=True)
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    role_id = Column(Integer, ForeignKey("ab_role.id"))
    # user = relationship(UserV2, backref="user")

    UniqueConstraint("user_id", "role_id")

    @classmethod
    def get_user_role_model(cls, user_id):
        qry = db.session.query(UserRole).filter(UserRole.user_id == user_id)
        return qry.one_or_none()
