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

import os
import sys
monitor_path = os.path.dirname(__file__)
sys.path.append(monitor_path)
os.chdir(monitor_path)


def commander(command_str):
    os.system(command_str)


if __name__ == '__main__':
    # path => C:\Users\xiao3\Desktop\prod\superset\superset\monitor

    # Linux启动
    commander("celery -A tasks.main worker -B -l info")

    # window启动,再去运行app_copy.py 或者 在当前文件路径执行命令
    # commander("celery -A tasks.main worker -l info -P eventlet")



