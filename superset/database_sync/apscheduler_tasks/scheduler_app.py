import logging
from datetime import datetime
from typing import Union

from pytz import utc
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from superset import create_app

flask_app = create_app()

from superset import conf, db
from superset.database_sync.tasks.task import delete_chart_entries_job
from superset.database_sync.tasks.task_config import other_task_config
from superset.database_sync.utils.redis_queue import RedisQueue
from superset.database_sync.database_sync_api import sync_table_wrapper
from superset.models.database_sync import DatabaseSyncTask, ExecuteEnum, DatabaseSyncTaskLogs

from superset.database_sync.utils.safe_stop_thread import \
    SafeStopThread

logger = logging.getLogger(__name__)


class DatabaseSyncClientProcess(SafeStopThread):
    def __init__(self):
        SafeStopThread.__init__(self, loop_sleep_time=5, log=logger)

        logger.info(f">>>>>> {self.__class__.__name__} Launched >>>>>>")

        self.redis_client = RedisQueue()
        self.scheduler = self.get_scheduler_client()

    def init_server(self):
        self.redis_client = RedisQueue()
        self.scheduler = self.get_scheduler_client()

    @staticmethod
    def get_scheduler_client():
        redis_data = dict(
            host=conf.get("SUPERSET_REDIS_HOST", "127.0.0.1"),
            port=conf.get("SUPERSET_REDIS_PORT", "6379"),
            password=conf.get("SUPERSET_REDIS_PASSWORD", ""),
            db=conf.get("DATABASE_SYNC_QUEUE_REDIS_DB", 15),
        )

        scheduler = BackgroundScheduler()
        job_stores = {
            'redis': RedisJobStore(**redis_data)
        }

        executors = {
            'default': {'type': 'threadpool', 'max_workers': 20},
            'processpool': ProcessPoolExecutor(max_workers=5)
        }

        job_defaults = {
            'coalesce': False,
            'max_instances': 3
        }

        scheduler.configure(jobstores=job_stores, executors=executors,
                            job_defaults=job_defaults, timezone=utc)

        return scheduler

    @staticmethod
    def sync_task(task_id):
        """
        :param task_id: database_sync_task表的id
        :return:
        """
        logger.info(f">>>>>> Synchronization task ID [{task_id}] starts running >>>>>>")
        sync_table_wrapper(task_id, is_time_check_enabled=True)

    @staticmethod
    def get_database_sync_task_id_models(t_id):
        """
        通过id获取当前这条数据的models模型
        :param t_id:
        :return:
        """
        query = db.session.query(DatabaseSyncTask).filter(
            DatabaseSyncTask.id == t_id
        )

        return query.one_or_none()

    def add_all_tasks(self):
        """
        从 database_sync_task表中获取所有的任务，并添加到调度器里
        循环取出需要同步的任务模型，此方法只会在启动时执行一次
        :return:
        """
        tasks_models_data = db.session.query(DatabaseSyncTask).filter(
            DatabaseSyncTask.is_active == True,
            DatabaseSyncTask.execute_type != ExecuteEnum.IMMEDIATELY,
            DatabaseSyncTask.cron_expression.isnot(None)
        ).all()

        for task_models in tasks_models_data:
            self.add_job_task(task_models)

    def other_all_tasks(self):
        # TODO 自动导入其他所有的任务
        crontab_str = other_task_config["delete_chart_entries_job"]["schedule"]
        trigger = CronTrigger.from_crontab(crontab_str)
        self.scheduler.add_job(
            delete_chart_entries_job,
            trigger=trigger,

        )

    def add_job_task(self, task_models):
        try:
            trigger = CronTrigger.from_crontab(task_models.cron_expression)

            job = self.scheduler.add_job(
                self.sync_task,
                trigger=trigger,
                args=(int(task_models.id),),
            )

            info_str = f">>>>>> Add synchronization task ID [{task_models.id}] successfully\n"
            logger.info(info_str)
            task_models.task_id = job.id
            db.session.commit()
        except Exception as e:
            error_str = f">>>>>> Add synchronization task ID [{task_models.id}] ERROR:{e}\n"
            logger.error(error_str)
            db.session.commit()

    def edit_job_task(self, task_models: Union[DatabaseSyncTask]):
        try:

            if task_models.is_active and self.scheduler.get_job(task_models.task_id) is None:
                self.add_job_task(task_models)
            elif not task_models.is_active and self.scheduler.get_job(task_models.task_id):
                self.scheduler.remove_job(task_models.task_id)
            elif task_models.is_active and self.scheduler.get_job(task_models.task_id):
                self.scheduler.modify_job(
                    task_models.task_id,
                    trigger=task_models.cron_expression
                )

        except Exception as e:
            error_str = f">>>>>> Edit synchronization task ID [{task_models.id}] ERROR:{e}\n"
            logger.error(error_str)

    def get_task_from_queue(self):
        """
        从 Redis 队列获取任务信息
        :return:
        """

        try:
            # 启动前清空累计队列，避免重复添加
            self.redis_client.clear()

            while True:
                logger.info(">>>>>> Process Queue Launched >>>>>>")
                print(">>>>等待队列", self.scheduler.get_jobs(), datetime.now())
                logger.info(f">>>>等待队列 {self.scheduler.get_jobs()}")
                data = self.redis_client.get_with_block_mode(is_dict_mode=True)
                logger.info(f"queue_data:>>>>>>{data}")
                self.process_task(data)
        except Exception as e:
            logger.info(f">>>>>> Process Queue Launched  ERROR: {e}>>>>>>")
            raise e

    def process_task(self, data):
        """
        根据任务信息执行相应的操作
        data = {
             "execute_type": "add",
             "task_id": 1,
        }
        :return:
        """

        task_models = self.get_database_sync_task_id_models(data["task_id"])

        # 删除任务
        if data.get("execute_type") == "del" and task_models.task_id:
            self.scheduler.remove_job(task_models.task_id)

        # 添加任务
        elif data.get("execute_type") == "add":
            self.add_job_task(task_models)

        # 编辑任务
        elif data.get("execute_type") == "edit":
            self.edit_job_task(task_models)
            # self.scheduler.modify_job(
            #     task_models.task_id,
            #     trigger=task_models.cron_expression
            # )
        elif data.get("execute_type") == "immediately":
            self.scheduler.add_job(
                self.sync_task,
                trigger="date",
                args=(int(task_models.id),)
                )

    def run_once(self):
        """
        连接
        """
        try:
            with flask_app.app_context():
                self.init_server()
                logger.info(">>>>>> apscheduler Launched >>>>>>")
                self.scheduler.start()
                self.other_all_tasks()
                self.add_all_tasks()
                self.get_task_from_queue()

        except Exception as e:
            print(f">>>>>> apscheduler Launched ERROR: {e} >>>>>>")
            logger.info(f">>>>>> apscheduler Launched ERROR: {e} >>>>>>")


if __name__ == '__main__':
    with flask_app.app_context():
        database_sync_client_process = DatabaseSyncClientProcess()
        database_sync_client_process.start()
        database_sync_client_process.join()
        # database_sync_client_process.scheduler.shutdown(wait=True)
        # time.sleep(30)

        # 关闭调度器
