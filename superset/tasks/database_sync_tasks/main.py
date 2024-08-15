from celery.schedules import crontab
from celery.task.control import revoke
from superset import app, celery_app
from superset import db

class ScheduledTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    task_function = db.Column(db.String(255))
    schedule = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)

@celery_app.task(bind=True)
def my_task(self):
    # 执行您的定时任务逻辑
    pass

def add_task_to_beat(task):
    celery_app.add_periodic_task(
        crontab(**task.schedule),
        my_task.s(),
        name=task.name
    )

def stop_task(task):
    revoke(task.name, terminate=True)

def delete_task(task):
    stop_task(task)
    db.session.delete(task)
    db.session.commit()

if __name__ == '__main__':
    db.create_all()

    # 创建一个新的定时任务
    new_task = ScheduledTask(
        name='my_task',
        task_function='module_name.my_task',
        schedule={'minute': 0, 'hour': 0},
        is_active=True
    )
    db.session.add(new_task)
    db.session.commit()

    # 将任务添加到Celery Beat的调度中
    add_task_to_beat(new_task)

    # 停止任务
    stop_task(new_task)

    # 删除任务
    delete_task(new_task)

    celery_app.start()
