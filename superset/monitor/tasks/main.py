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

import importlib
import sys
from pathlib import Path
from superset.monitor.monitor_configs.celery import app
from superset.monitor.monitor_configs.celery_config import PYTHON_VIRTUALENV
from superset.monitor.monitor_utils.my_task import MyTask
from superset.monitor.monitor_utils.execute_utils import execute_cmd


task_path = Path(Path(__file__).resolve().absolute().parent)

STATUS_SUCCESS = 0
STATUS_FAILED = 1
STATUS_WARNING = 2
STATUS_RUNNING = 3


def rename_func(name):
    def outer_wrapper(func_to_execute):
        def wrapper(*args, **kwargs):
            return func_to_execute(*args, **kwargs)

        wrapper.__name__ = name
        return wrapper

    return outer_wrapper


def get_all_tasks():
    global task_path
    res = []
    for project in task_path.iterdir():
        # project -> check_api
        if project.is_dir() and not project.name.startswith('__'):
            for child_task_path in project.iterdir():
                # task_path -> grpc
                if child_task_path.is_dir() and not child_task_path.name.startswith('__') and child_task_path.joinpath(
                        'task_config.py').is_file() and child_task_path.joinpath('task.py').is_file():
                    res.append({
                        'task_path': child_task_path,
                        'dyn_name': f'tasks.{project.name}.{child_task_path.name}'
                    })

    return res


def before_execute(slack, task_name):
    if slack:
        ...
        # slack_cli.send_text(
        #     channel=slack.get('channel'),
        #     subject=slack.get('subject'),
        #     content=f"{slack.get('subject')} started")


def after_execute(slack, res, task_name):
    if slack:
        ...
        # slack_cli.send_text(
        #     channel=slack.get('channel'),
        #     subject=slack.get('subject'),
        #     content=f"{slack.get('subject')} end")


def get_beat_schedule():
    beat_schedule_res = dict()
    tasks = get_all_tasks()
    print(f"{len(tasks)} jobs will be scheduled.")

    for task in tasks:
        for task_config in importlib.import_module(f"{task['dyn_name']}.task_config").config:

            task_name = task_config['task_name']
            schedule = task_config['schedule']
            options = {'queue': 'sh_beat'}

            beat_schedule_res[task_name] = {
                'task': f'tasks.main.{task_name}',
                "schedule": schedule,
                'options': options
            }

    return beat_schedule_res


app.conf.update(beat_schedule=get_beat_schedule())


def get_func(task, task_config):
    script_path = task['task_path'].joinpath('task.py')
    timeout = task_config.get('timeout', 60 * 10)
    task_name = task_config['task_name']

    @app.task(base=MyTask, bind=True)
    @rename_func(task_name)
    def func(_):
        cwd = task_config.get('cwd',
                              str(Path(__file__).resolve().absolute().parent))  # 脚本执行目录
        execute_cmd([PYTHON_VIRTUALENV, str(script_path)],
                                  function_name=task_name,
                                  timeout=timeout, cwd=cwd)

    return func


def register_tasks():
    tasks = get_all_tasks()

    for task in tasks:
        for task_config in importlib.import_module(f"{task['dyn_name']}.task_config").config:
            setattr(sys.modules[__name__], task_config['task_name'], get_func(task, task_config))


register_tasks()
