from datetime import datetime, date
from uuid import UUID

from flask_appbuilder import Model
from enum import Enum

from superset import conf, db
from superset.constants import AuthSourceType
from superset.models.helpers import AuditMixinNullable, ImportExportMixin
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Enum as EnumType,
    Boolean, UniqueConstraint, ForeignKey, desc

)


class ExecuteEnum(Enum):
    IMMEDIATELY = 'immediately'  # 立即执行
    CRON = 'cron'  # 定时执行
    SIMPLE = 'simple'  # 简单执行


class ExecuteResultEnum(Enum):
    SUCCESS = 'success'
    FAILURE = 'failed'


class ExecuteStatusEnum(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'


class UpdateTypeEnum(Enum):
    COMPLETE_UPDATE = "complete_update"
    INCREMENTAL_UPDATE = "incremental_update"


class ColumnRangeTypeEnum(Enum):
    ALL_COLUMNS = "all_columns"
    SELECTED_COLUMNS = "selected_columns"


class RowRangeTypeEnum(Enum):
    ALL_ROWS = "all_rows"
    CONDITIONAL_SELECTED_ROWS = "conditional_selected_rows"


class DatabaseSyncTaskLogs(Model, AuditMixinNullable, ImportExportMixin):
    __tablename__ = "database_sync_task_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)

    task_log = Column(Text, nullable=True, comment='任务日志')
    task_function = Column(String(50), nullable=True,
                           comment='任务关联的函数或方法的名称')
    task_start_time = Column(DateTime, default=None, nullable=True,
                             comment="开始时间")
    task_end_time = Column(
        DateTime, default=None, onupdate=None, nullable=True,
        comment="结束时间"
    )
    database_sync_task_id = Column(
        Integer,
        ForeignKey("database_sync_task.id"),
        nullable=False
    )
    execute_result = Column(
        EnumType(ExecuteResultEnum, nullable=True, create_constraint=False),
        comment='任务结果', default=None
    )

    @classmethod
    def delete_data_by_field(cls, database_sync_task_id):
        # 查询符合条件的数据
        query = db.session.query(DatabaseSyncTaskLogs).filter_by(database_sync_task_id=database_sync_task_id)
        # 删除符合条件的数据
        query.delete()
        # 提交事务
        db.session.commit()

    def to_json(self):
        result = dict()
        for key in self.__mapper__.c.keys():
            col = getattr(self, key)
            if isinstance(col, datetime) or isinstance(col, date):
                col = col.isoformat()
            elif isinstance(col, UUID):
                col = str(col)
            elif isinstance(col, Enum):
                col = col.value
            result[key] = col
        return result


class DatabaseSyncTask(Model, AuditMixinNullable, ImportExportMixin):
    __tablename__ = "database_sync_task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(50), nullable=True, comment='任务id')
    task_name = Column(String(50), unique=True, comment='任务名称')
    task_code = Column(String(50), comment='任务编码')
    execute_type = Column(EnumType(ExecuteEnum), comment='执行效率(执行类型)')

    update_type = Column(EnumType(UpdateTypeEnum), comment='更新方式')
    execute_status = Column(Boolean, default=False, comment='任务状态')

    is_active = Column(Boolean, default=True, comment='是否启用')

    source_name = Column(String(50), comment='同步数据源名称')

    source_database_type = Column(String(50), nullable=True, comment='源数据库类型')

    source_database_name = Column(String(50), nullable=False, comment='源数据库名称')

    source_database_table_name = Column(String(50), nullable=False,
                                        comment='源数据表名称')
    source_dbs_id = Column(Integer, nullable=False,
                           comment='dbs表的关联id')

    target_name = Column(String(50), default=conf["UPLOAD_SCHEMA"],
                         comment='目标数据源名称')
    target_database_type = Column(String(50), default='mysql',
                                  comment='目标数据库类型')
    target_database_name = Column(String(50), default=conf["UPLOAD_SCHEMA"],
                                  comment='目标数据库名称')
    target_database_table_name = Column(String(255), nullable=True,
                                        comment='目标数据表名称')

    cron_expression = Column(String(50), nullable=True, comment='cron表达式')
    cron_start_time = Column(DateTime, default=None, nullable=True,
                             comment="cron表达式执行的开始时间")
    cron_end_time = Column(DateTime, default=None, nullable=True,
                           comment="cron表达式执行的结束时间")

    column_range_type = Column(EnumType(ColumnRangeTypeEnum),
                               default=ColumnRangeTypeEnum.ALL_COLUMNS,
                               nullable=True, comment='数据列范围类型')
    column_range_data = Column(String(3000), comment='数据列范围的列名数据')
    row_range_type = Column(EnumType(RowRangeTypeEnum),
                            default=RowRangeTypeEnum.ALL_ROWS,
                            nullable=True, comment='数据行范围类型')
    row_range_data = Column(String(1000),
                            comment='数据行范围的sql筛选条件数据')
    row_range_data_list = Column(String(1000),
                            comment='数据行范围的sql筛选条件数据,原格式')
    database_sync_id = Column(Integer, ForeignKey("database_sync.id"), nullable=False)

    @classmethod
    def get_log_model_by_id(cls, dst_id):
        query = db.session.query(DatabaseSyncTaskLogs).filter(
            DatabaseSyncTaskLogs.database_sync_task_id == dst_id
        ).order_by(desc(DatabaseSyncTaskLogs.created_on))
        return query.first()

    def add_user_permission(self, privilege_value: int = 1):
        """新增用户权限，在新增数据时调用"""
        self._add_user_permission(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATABASE_SYNC,
            privilege_value=privilege_value,
        )

    def can_access(self, privilege_value: int = 1):
        """验证当前用户是否有权限"""
        self._can_access(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATABASE_SYNC,
            privilege_value=privilege_value,
        )

    def __repr__(self) -> str:
        return f"DatabaseSyncTask id={self.id} name={self.task_name}"


class DatabaseSyncGroup(Model, AuditMixinNullable, ImportExportMixin):
    """The database_sync_group!"""

    __tablename__ = "database_sync_group"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, comment="分组名称")
    pid = Column(Integer, nullable=False, default=0, index=True, comment="父分组ID")
    level = Column(Integer, nullable=False, default=0, comment="分组等级")

    def __repr__(self) -> str:
        return f"<DatabaseSyncGroup id={self.id} name={self.name}"

    def add_user_permission(self, privilege_value: int = 1):
        """新增用户权限，在新增数据时调用"""
        self._add_user_permission(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATABASE_SYNC_GROUP,
            privilege_value=privilege_value,
        )

    def can_access(self, privilege_value: int = 1):
        """验证当前用户是否有权限"""
        self._can_access(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATABASE_SYNC_GROUP,
            privilege_value=privilege_value,
        )

    def to_json(self):
        result = dict()
        for key in self.__mapper__.c.keys():
            col = getattr(self, key)
            if isinstance(col, datetime) or isinstance(col, date):
                col = col.isoformat()
            elif isinstance(col, UUID):
                col = str(col)
            result[key] = col
        return result


class DatabaseSync(Model, AuditMixinNullable, ImportExportMixin):
    """The database_sync!"""

    __tablename__ = "database_sync"

    __table_args__ = (UniqueConstraint("name", "group_id"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, comment='名称')
    database_id = Column(Integer, ForeignKey("dbs.id"))
    database_type = Column(String(20), nullable=False, comment='类型')
    desc = Column(String(1000), nullable=True, comment='描述')
    group_id = Column(Integer, ForeignKey("database_sync_group.id"))

    def __repr__(self) -> str:
        return f"DatabaseSync id={self.id} name={self.name}"

    def add_user_permission(self, privilege_value: int = 1):
        """新增用户权限，在新增数据时调用"""
        self._add_user_permission(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATABASE_SYNC_GROUP,
            privilege_value=privilege_value,
        )

    def can_access(self, privilege_value: int = 1):
        """验证当前用户是否有权限"""
        self._can_access(
            auth_source=self.id,
            auth_source_type=AuthSourceType.DATABASE_SYNC_GROUP,
            privilege_value=privilege_value,
        )
