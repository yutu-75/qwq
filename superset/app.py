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
修改：陈果-2023-03-10
修改内容：修复使用过程中token过期问题
修改：陈果-2023-03-23
修改内容：还原seesion登录
"""

import logging
import os

from flask import Flask
from flask_cas import CAS
from superset.initialization import SupersetAppInitializer

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    app = SupersetApp(__name__)

    try:
        # Allow user to override our config completely
        # __ROOT__ = os.path.dirname(os.path.abspath(__file__))
        # os.environ["SUPERSET_CONFIG_PATH"] = __ROOT__ + "/superset_config.py"
        config_module = os.environ.get("SUPERSET_CONFIG", "superset.config_dev")
        app.config.from_object(config_module)
        CAS(app, '/cas')

        # 用于模板引擎前缀判断
        app.jinja_env.globals['STATIC_ASSETS_PREFIX'] = app.config.get("STATIC_ASSETS_PREFIX")
        app_initializer = app.config.get("APP_INITIALIZER", SupersetAppInitializer)(app)
        app_initializer.init_app()

        return app

    # Make sure that bootstrap errors ALWAYS get logged
    except Exception as ex:
        logger.exception("Failed to create app")
        raise ex


class SupersetApp(Flask):
    pass


# 本地测试
if __name__ == '__main__':
    superset_app = create_app()
    # print(superset_app.url_map)
    superset_app.run(
        host="0.0.0.0", port=5000, debug=True,
    )


