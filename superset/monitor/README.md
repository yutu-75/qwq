# zerocap_monitor

# Directory Structure

```shell
|-- monitor_configs/
|  |-- celery_config.py
|  |-- celery.py
|  |-- config.py
|-- monitor_utils/
|  |-- execute_utils.py
|  |-- my_task.py
|  |-- report_client.py
|  |-- slack_service.py
|-- monitorlog/
|-- ...
|-- tasks/
|  |-- daily_handler/  # daily tasks
|  |-- health_check/  # health check tasks
|  |-- sync_data/  # sync data tasks
|  |-- ...
|  |-- main.py  # auto register tasks
|-- app.py  # application entry
|-- README.md
```

# Add a new task

1. Select or create a folder by task type in `${PROJECT_ROOT}/tasks` directory.
2. Create a task folder in the folder in step '1'.
3. Create a task config file in the folder in step '2', name must be 'task_config.py'.
4. Create a task file in the folder in step '2', name must be 'task.py'.
5. Restart the celery application.

> Note: The task config file must be named 'task_config.py', and the task file must be named 'task.py'
>
> Warning: task_name in task_config.py must be unique

```python
# Task config file
from celery.schedules import crontab

config = [
    {
        'task_name': 'TaskNameTime1',
        'schedule': crontab(hour=0, minute=0),
        'timeout': 60 * 10,
        'slack': 'SLACK_API_OPS'
    },
    {
        'task_name': 'TaskNameTime12',
        'schedule': crontab(hour=12, minute=0),
        'timeout': 60 * 10,
        'slack': 'SLACK_API_OPS'
    }
]

# Task file
# scripy code
```
#### start app


