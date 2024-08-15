from datetime import datetime


def sync_table_wrapper(task_models,
                       is_time_check_enabled=False, new_record=None):
    """
    执行同步操作的代码
    :param task_models:
    :param is_time_check_enabled:
    :param new_record: 
    :return:
    """
    from superset import conf, db, create_app

    flask_app = create_app()

    from superset.database_sync.database_sync import DataSync
    from superset.models.database_sync import DatabaseSyncTask, ExecuteResultEnum, \
        DatabaseSyncTaskLogs

    with flask_app.app_context():

        try:

            if isinstance(task_models, int):
                task_models = db.session.query(
                    DatabaseSyncTask
                ).filter(
                    DatabaseSyncTask.id == task_models
                ).first()

            if is_time_check_enabled:
                now_time = datetime.now()
                if (
                        task_models.cron_start_time > now_time if
                        task_models.cron_start_time else False
                ) or (
                        task_models.cron_end_time > now_time if
                        task_models.cron_end_time else False
                ):
                    return
            if not new_record:
                new_record = DatabaseSyncTaskLogs(
                    database_sync_task_id=task_models.id,
                    task_start_time=datetime.now(),
                    task_log=""
                )  # 创建一个新的记录，并设置task_start_time字段为当前时间

                db.session.add(new_record)  # 将新记录添加到数据库会话中
                db.session.commit()  # 提交更改，将新记录保存到数据库

            task_models.execute_status = False
            # task_models.start_time = datetime.now()

            new_record.task_log = f"start task_name:[{task_models.task_name}] id:[{task_models.id}] >>>> \n"
            db.session.commit()  # 提交更改，将新记录保存到数据库

            data = {
                str(task_models.source_dbs_id): [task_models.source_database_table_name]
            }

            target_db_url = conf.get("UPLOAD_DATABASE_URI")
            data_sync = DataSync(data, target_db_url, task_models, new_record)
            data_sync.sync_tables()

            new_record.task_end_time = datetime.now()
            new_record.execute_result = ExecuteResultEnum.SUCCESS
            new_record.task_log += str(ExecuteResultEnum.SUCCESS)
            db.session.commit()  # 提交更改，将新记录保存到数据库

        except Exception as e:
            print(e)
            new_record.task_end_time = datetime.now()
            new_record.execute_result = ExecuteResultEnum.FAILURE
            new_record.task_log += str(e)
            db.session.commit()
            raise Exception(e)


def main_test():
    sync_table_wrapper(29)
    return
    source_db_data = {
        # "24": ["ab_role"],
        # "2": ["ab_user", "ab_role"],
        "1": ["test"],
    }
    # "5"是dbs表的id，["test_table"]是这个库下的表名称
    target_db_url = conf.get("UPLOAD_DATABASE_URI")
    data_sync = DataSync(source_db_data, target_db_url)
    data_sync.sync_tables()

# if __name__ == '__main__':
#     from superset import create_app, conf, db
#
#     flask_app = create_app()
#     from superset.database_sync.database_sync import DataSync
#
#     with flask_app.app_context():
#         main_test()
