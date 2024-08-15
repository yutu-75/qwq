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

from kombu import Queue, Exchange

#from superset.config_prod import SUPERSET_REDIS_PASSWORD, SUPERSET_REDIS_HOST, SUPERSET_REDIS_PORT

SUPERSET_REDIS_HOST = "124.222.172.192"
SUPERSET_REDIS_PORT = "6379"
SUPERSET_REDIS_PASSWORD = "yanilo315*"


result_backend = f'redis://:{SUPERSET_REDIS_PASSWORD}@{SUPERSET_REDIS_HOST}:{SUPERSET_REDIS_PORT}/3'
broker_url = f'redis://:{SUPERSET_REDIS_PASSWORD}@{SUPERSET_REDIS_HOST}:{SUPERSET_REDIS_PORT}/4'

# 指定任务序列化方式
task_serializer = 'json'
# 指定结果序列化方式
result_serializer = 'json'
# 指定任务接受的序列化类型.
accept_content = ['json']

worker_hijack_root_logger = False
worker_redirect_stdouts = False
task_ignore_result = True
worker_concurrency = 1  # worker的并发数，默认是服务器的内核项目，也是命令行-c的指定数目目
worker_max_tasks_per_child = 200  # 每个worker执行多少任务后自动杀死，防止内存溢出

beat_exchange = Exchange('sh_beat', type='topic')

task_queues = (
    Queue('sh_beat', exchange=beat_exchange, routing_key='*.sh_beat.*', delivery_mode=1),
)

PYTHON_VIRTUALENV = r"F:\python_virtualenv\superset_uat\Scripts\python"

