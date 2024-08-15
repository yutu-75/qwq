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

from celery import Task

logger = logging.getLogger(__name__)


class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        """Success handler"""
        # print('result: {0}'.format(retval))
        # print(self.get_log_files())

        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        """Retry handler"""
        pass

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Error handler"""
        content = """
            error:{exc};
            |-------------------------
            task_id:{task_id};
            |-------------------------
            args:{args};
            |-------------------------
            kwargs:{kwargs};
            |-------------------------
            einfo:{einfo};
        """.format(exc=exc, task_id=task_id, args=args, kwargs=kwargs, einfo=einfo)
        logger.error(content)

        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)
