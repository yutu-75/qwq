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
import subprocess
from superset.monitor.app import monitor_path

logger = logging.getLogger(__name__)


def check_shell(cmd_str):
    """
    检查cmd的安全性，过滤一些危险字符
    """
    black_char_list = (
        '&',
        ';'
    )
    for item in black_char_list:
        if item in cmd_str:
            raise Exception(f'command contains {item}')


def execute_cmd(cmd, function_name, timeout=60 * 10, cwd=monitor_path):
    """
    cmd: 对应命令或脚本，字符串或者list
    """
    try:
        assert isinstance(cmd, (list, str))
        logger.info(f'{function_name} start')
        logger.info(" ".join(cmd) if isinstance(cmd, list) else cmd)
        check_shell(" ".join(cmd) if isinstance(cmd, list) else cmd)
        ret = subprocess.run(cmd, encoding="utf-8", timeout=timeout, stderr=subprocess.STDOUT,
                             stdout=subprocess.PIPE, cwd=cwd)
        if ret.returncode:
            raise Exception(f"error: \n{ret.stderr} \noutput: \n {ret.stdout}")
        logger.info(ret.stdout)
        logger.info(f'{function_name} end')
        return 0, (ret.stdout or '') + (ret.stderr or '')
    except Exception as e:
        logger.exception(e)
        return 1, repr(e.__str__())
