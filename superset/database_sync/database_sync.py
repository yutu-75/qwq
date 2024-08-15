import json
import logging

from superset import db
from superset.database_sync.utils.mysql_tool import set_mysql_field, \
    truncate_table_and_reset_id
from superset.models.core import Database

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import inspect, create_engine, MetaData, Table, Column

from superset.models.database_sync import ColumnRangeTypeEnum, RowRangeTypeEnum, \
    UpdateTypeEnum

logger = logging.getLogger(__name__)


class DataSync:
    def __init__(self, source_db_data, target_db_url, task_models=None, task_models_log=None):

        self.task_models = task_models
        self.task_models_log = task_models_log

        # 源库
        self.source_db_data = source_db_data
        self.source_engine = None
        self.source_session = None
        self.source_metadata = None

        # 目标库
        self.target_db_url = target_db_url
        self.target_engine = create_engine(target_db_url)
        self.target_session = sessionmaker(bind=self.target_engine)()
        self.target_metadata = MetaData(bind=self.target_engine)

        # 查询分割
        self.limit = 100000

        logger.info(
            f"Syncing table {list(source_db_data.values())[0]} "
            f"in database id {list(source_db_data.keys())[0]} >>>>>>>")

    def get_databases(self):

        source_db_ids = [int(i) for i in self.source_db_data]

        return db.session.query(Database).filter(Database.id.in_(source_db_ids)).all()

    @staticmethod
    def get_mysql_table_count(table_name):
        """
        获取 MySQL 数据库表的行数的
        :param table_name:  表名
        :return:
        """
        select_query = f"SELECT COUNT(*) FROM {table_name};"
        result = db.session.execute(select_query)
        # 获取查询结果的数据部分
        data = result.fetchone()
        return data[0]

    def create_mysql_table(self, table_name, columns):

        # 获取原表的表结构
        inspector = inspect(self.target_engine)

        new_table = None

        if inspector.has_table(table_name):
            # Table(table_name, self.target_metadata, autoload=True)
            # self.target_metadata.drop_all()
            existing_table = Table(table_name, self.target_metadata, autoload=True)
            existing_table.drop(bind=self.target_engine)  # 删除已存在的表

        if self.task_models.column_range_type == ColumnRangeTypeEnum.SELECTED_COLUMNS and self.task_models.column_range_data:
            column_range_data = json.loads(self.task_models.column_range_data)
            columns_list = []
            for _ in columns:
                if _['name'] in column_range_data:
                    columns_list.append(_)

            columns = columns_list

        self.target_metadata = MetaData(bind=self.target_engine)

        # 表不存在，创建表
        if not inspector.has_table(table_name):

            # MYSQL 中 VARCHAR可以存65535字节， utf8mb4需要四个字节 大约能存10923中文字符，约等于 0.0625 MB
            # 定义新表的结构
            new_table = Table(
                table_name,
                self.target_metadata,
                *(
                    Column(
                        column['name'],
                        set_mysql_field(column['type']),
                        column['default'],
                    )
                    for column in columns
                )
            )

            # # 判断是否存在id字段
            # has_id_column = any(
            #     column['name'] == 'id' for column in columns)

            # # 如果不存在id字段，则添加自增的id字段
            # if not has_id_column:
            #     new_table.append_column(
            #         Column('id', Integer, primary_key=True, autoincrement=True))

            # 创建新表
            self.target_metadata.create_all()
            self.target_metadata = MetaData(bind=self.target_engine)
            status = True
            log_str = f"Table '{table_name}' created successfully!\n"
            logger.info(log_str)
            self.task_models_log.task_log += log_str
            db.session.commit()  # 提交更改，将新记录保存到数据库
        else:

            status = False
            log_str = f"Table '{table_name}' already exists!\n"
            logger.info(log_str)
            self.task_models_log.task_log += log_str
            db.session.commit()  # 提交更改，将新记录保存到数据库
        return status, new_table

    def upsert_data_to_db(self, table_name, to_db_data, columns):

        # 创建目标数据库表对象
        target_table = Table(
            table_name,
            self.target_metadata,
            autoload_with=self.target_engine,
            # autoload=True,
        )

        index = 0
        for row in to_db_data:

            # 检查目标表中是否存在匹配的 ID
            existing_row = self.target_session.query(target_table).filter_by(
                id=row.get("id")).first() \
                if "id" in [i["name"] for i in columns] else None

            if existing_row is None:
                # 在目标表中插入新数据
                statement_sql = target_table.insert().values(**row)
            else:
                # 在目标表中更新现有数据
                statement_sql = target_table.update().values(**row).where(
                    target_table.c.id == row['id'])

            self.target_session.execute(statement_sql)
            self.target_session.commit()

            index += 1
            # 日志量太大可以删除
            log_str = f"insert_index  >>>{index}\n"
            self.task_models_log.task_log += log_str
            db.session.commit()  # 提交更改，将新记录保存到数据库

    def set_source_information(self, source_db_url):

        self.source_engine = create_engine(source_db_url)
        self.source_metadata = MetaData(bind=self.source_engine)

        # 开启事务
        self.source_session = sessionmaker(bind=self.source_engine)()

    def sync_table(self, database, table_name):
        """
        将源表中的数据同步到目标表中。它使用分页查询的方式逐步处理数据，
        并在每一页处理后将数据更新或插入到目标表中。
        如果发生异常，会回滚事务并关闭数据库会话.
        :param database:
        :param table_name:
        :return:
        """

        columns = database.get_columns(table_name)

        # 创建目标库表，有则跳过
        self.create_mysql_table(table_name, columns)

        # 没有主键则不能做更新操作，只能清空表重新同步
        if ("id" not in [i["name"] for i in columns]
                or self.task_models.update_type == UpdateTypeEnum.COMPLETE_UPDATE):
            truncate_table_and_reset_id(self.target_session, table_name)

        try:
            offset = 0
            while True:

                if (self.task_models.column_range_data and
                        self.task_models.column_range_type == ColumnRangeTypeEnum.SELECTED_COLUMNS):
                    column_range_data = json.loads(self.task_models.column_range_data)

                    cols_dict_list = [{"name": _} for _ in column_range_data]
                    columns = cols_dict_list
                # 构建分页查询语句
                select_query = database.select_star(
                    table_name,
                    limit=self.limit,
                    show_cols=True,
                    cols=locals().get('cols_dict_list')
                )
                if self.task_models.row_range_type == RowRangeTypeEnum.CONDITIONAL_SELECTED_ROWS:

                    select_query = select_query.replace(
                        "LIMIT",
                        f"WHERE {self.task_models.row_range_data} LIMIT"
                    )

                select_query = f"{select_query} OFFSET {offset}"

                # 获取查询结果的数据部分
                result = self.source_session.execute(select_query)

                # 查询的数据转换成字典
                to_db_data = [dict(i) for i in result.fetchall()]

                # 如果没有数据了，跳出循环
                if not to_db_data:
                    return

                # 更新或者插入数据
                self.upsert_data_to_db(table_name, to_db_data, columns)

                to_db_data.clear()

                # 增加偏移量，准备下一页查询
                offset += self.limit

                log_str = f"query >>>{select_query}"
                self.task_models_log.task_log += log_str
                db.session.commit()  # 提交更改，将新记录保存到数据库

        except SQLAlchemyError as e:
            error_str = f"Error syncing table {database.database_name}.{table_name}: {str(e)}\n"
            self.target_session.rollback()
            logging.error(error_str)
            self.task_models_log.task_log += error_str
            db.session.commit()  # 提交更改，将新记录保存到数据库
            raise Exception(e)

        except Exception as e:
            self.target_session.rollback()
            self.target_session.close()
            logging.error(f"Error:{str(e)}")
            self.task_models_log.task_log += f"Error:{str(e)}\n"
            db.session.commit()  # 提交更改，将新记录保存到数据库
            raise Exception(e)

    def sync_tables(self):

        # 获取的所有库的信息
        databases = self.get_databases()

        for database in databases:

            # 设置源库信息,开启事务
            self.set_source_information(database.sqlalchemy_uri_decrypted)

            for table in self.source_db_data.get(str(database.id), []):
                self.sync_table(database, table)
                # if database.db_engine_spec.engine_name == "Apache Hive":
                #     self.hive_sync_table(database, table)
                #
                # elif database.db_engine_spec.engine_name == "MySQL":
                #     self.mysql_sync_table(database, table)
