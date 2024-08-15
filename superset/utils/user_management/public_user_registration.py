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

import logging
import re

from superset import appbuilder

logger = logging.getLogger(__name__)


def register_user_publicly(cn_name="public_share"):
    try:
        role_public = appbuilder.sm.find_role(
            appbuilder.sm.auth_role_public
        )
        result = appbuilder.sm.add_user(
            username=cn_name,
            first_name=cn_name,
            last_name=cn_name,
            email=f"{cn_name}@{cn_name}.com",
            role=role_public,
            is_admin=False,
            cn_name=cn_name,
            password="t1)*>(T0mAjz",
        )

        return result
    except Exception as e:
        logger.error(f"register_user_publicly failed.>>>{e}")


# public 用户添加看板访问权限，用于移动端看板预览功能
def add_user_permissions(user_id, next_, auth_source_type):
    from superset.dao.base import BaseDAO
    from superset.sys_manager.permission.dao import SysAuthDAO
    try:
        auth_source = BaseDAO.find_source_perm_by_target(user_id, 'user',
                                                        auth_source_type)
        dash_id = re.search(r'id=(\d+)', next_)
        if dash_id:
            id_value = dash_id.group(1)
            if id_value not in auth_source.keys() or auth_source[int(id_value)] != 1:
                item = [{"auth_source_type": auth_source_type,
                         "auth_source": id_value,
                         "auth_target": user_id,
                         "auth_target_type": "user",
                         "privilege_value": 1
                         }]
                SysAuthDAO.save_auth(item)
    except Exception as e:
        logger.error(f"add_user_permissions failed.>>>{e}")
