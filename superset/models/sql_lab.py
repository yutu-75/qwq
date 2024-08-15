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
"""A collection of ORM sqlalchemy models for SQL Lab"""

"""
修改人：李洪浩-2023-03-09
修改内容：修改模型TabState字段latest_query_id外键引用字段
"""
import inspect
import logging
import re
from datetime import datetime
from typing import Any, Dict, List, Optional, Type, TYPE_CHECKING

import simplejson as json
import sqlalchemy as sqla
from flask import current_app, Markup
from flask_appbuilder import Model
from flask_appbuilder.models.decorators import renders
from flask_babel import gettext as __
from humanize import naturaltime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import backref, relationship

from superset import security_manager
from superset.jinja_context import BaseTemplateProcessor, get_template_processor
from superset.models.helpers import (
    AuditMixinNullable,
    ExploreMixin,
    ExtraJSONMixin,
    ImportExportMixin,
)
from superset.sql_parse import CtasMethod, ParsedQuery, Table
from superset.sqllab.limiting_factor import LimitingFactor
from superset.utils.core import GenericDataType, QueryStatus, user_label

if TYPE_CHECKING:
    from superset.db_engine_specs import BaseEngineSpec


logger = logging.getLogger(__name__)


class Query(
    Model, ExtraJSONMixin, ExploreMixin
):  # pylint: disable=abstract-method,too-many-public-methods
    """ORM model for SQL query

    Now that SQL Lab support multi-statement execution, an entry in this
    table may represent multiple SQL statements executed sequentially"""

    __tablename__ = "query"
    type = "query"
    id = Column(Integer, primary_key=True)
    client_id = Column(String(11), unique=True, nullable=False, comment='查询标识')
    query_language = "sql"
    database_id = Column(Integer, ForeignKey("dbs.id"), nullable=False)

    # Store the tmp table into the DB only if the user asks for it.
    tmp_table_name = Column(String(256), comment='临时表名称')
    tmp_schema_name = Column(String(256), comment='临时 schema 名称')
    user_id = Column(Integer, ForeignKey("ab_user.id"), nullable=True)
    status = Column(String(16), default=QueryStatus.PENDING, comment='查询状态')
    tab_name = Column(String(256), comment='选项名称')
    sql_editor_id = Column(String(256), comment='sql 编辑器 id')
    schema = Column(String(256), comment='库名')
    sql = Column(LONGTEXT, comment='原始 sql 语句')
    # Query to retrieve the results,
    # used only in case of select_as_cta_used is true.
    select_sql = Column(LONGTEXT, comment='select_as_cta sql 语句')
    executed_sql = Column(LONGTEXT, comment='实际执行 sql 语句')
    # Could be configured in the superset config.
    limit = Column(Integer, comment='查询 limit')
    limiting_factor = Column(
        Enum(LimitingFactor), server_default=LimitingFactor.UNKNOWN, comment='limit 类型'
    )
    select_as_cta = Column(Boolean, comment='是否 select as create table')
    select_as_cta_used = Column(Boolean, default=False)
    ctas_method = Column(String(16), default=CtasMethod.TABLE, comment='create table as 类型')

    progress = Column(Integer, default=0, comment='进展')  # 1..100
    # # of rows in the result set or rows modified.
    rows = Column(Integer, comment='行数')
    error_message = Column(Text, comment='错误信息')
    # key used to store the results in the results backend
    results_key = Column(String(64), index=True, comment='缓存结果键')

    # Using Numeric in place of DateTime for sub-second precision
    # stored as seconds since epoch, allowing for milliseconds
    start_time = Column(Numeric(precision=20, scale=6), comment='开始时间')
    start_running_time = Column(Numeric(precision=20, scale=6), comment='开始运行时间')
    end_time = Column(Numeric(precision=20, scale=6), comment='结束时间')
    end_result_backend_time = Column(Numeric(precision=20, scale=6))
    tracking_url_raw = Column(Text, name="tracking_url")

    changed_on = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True, comment='更新时间'
    )

    database = relationship(
        "Database",
        foreign_keys=[database_id],
        backref=backref("queries", cascade="all, delete-orphan"),
    )
    user = relationship(security_manager.user_model, foreign_keys=[user_id])

    __table_args__ = (sqla.Index("ti_user_id_changed_on", user_id, changed_on),)

    def get_template_processor(self, **kwargs: Any) -> BaseTemplateProcessor:
        return get_template_processor(query=self, database=self.database, **kwargs)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "changedOn": self.changed_on,
            "changed_on": self.changed_on.isoformat(),
            "dbId": self.database_id,
            "db": self.database.database_name if self.database else None,
            "endDttm": self.end_time,
            "errorMessage": self.error_message,
            "executedSql": self.executed_sql,
            "id": self.client_id,
            "queryId": self.id,
            "limit": self.limit,
            "limitingFactor": self.limiting_factor,
            "progress": self.progress,
            "rows": self.rows,
            "schema": self.schema,
            "ctas": self.select_as_cta,
            "serverId": self.id,
            "sql": self.sql,
            "sqlEditorId": self.sql_editor_id,
            "startDttm": self.start_time,
            "state": self.status.lower(),
            "tab": self.tab_name,
            "tempSchema": self.tmp_schema_name,
            "tempTable": self.tmp_table_name,
            "userId": self.user_id,
            "user": user_label(self.user),
            "resultsKey": self.results_key,
            "trackingUrl": self.tracking_url,
            "extra": self.extra,
        }

    @property
    def name(self) -> str:
        """Name property"""
        ts = datetime.now().isoformat()
        ts = ts.replace("-", "").replace(":", "").split(".")[0]
        tab = self.tab_name.replace(" ", "_").lower() if self.tab_name else "notab"
        tab = re.sub(r"\W+", "", tab)
        return f"sqllab_{tab}_{ts}"

    @property
    def database_name(self) -> str:
        return self.database.name

    @property
    def username(self) -> str:
        return self.user.username

    @property
    def sql_tables(self) -> List[Table]:
        return list(ParsedQuery(self.sql).tables)

    @property
    def columns(self) -> List[Dict[str, Any]]:
        bool_types = ("BOOL",)
        num_types = (
            "DOUBLE",
            "FLOAT",
            "INT",
            "BIGINT",
            "NUMBER",
            "LONG",
            "REAL",
            "NUMERIC",
            "DECIMAL",
            "MONEY",
        )
        date_types = ("DATE", "TIME")
        str_types = ("VARCHAR", "STRING", "CHAR")
        columns = []
        col_type = ""
        for col in self.extra.get("columns", []):
            computed_column = {**col}
            col_type = col.get("type")

            if col_type and any(map(lambda t: t in col_type.upper(), str_types)):
                computed_column["type_generic"] = GenericDataType.STRING
            if col_type and any(map(lambda t: t in col_type.upper(), bool_types)):
                computed_column["type_generic"] = GenericDataType.BOOLEAN
            if col_type and any(map(lambda t: t in col_type.upper(), num_types)):
                computed_column["type_generic"] = GenericDataType.NUMERIC
            if col_type and any(map(lambda t: t in col_type.upper(), date_types)):
                computed_column["type_generic"] = GenericDataType.TEMPORAL

            computed_column["column_name"] = col.get("name")
            computed_column["groupby"] = True
            columns.append(computed_column)
        return columns

    @property
    def data(self) -> Dict[str, Any]:
        order_by_choices = []
        for col in self.columns:
            column_name = str(col.get("column_name") or "")
            order_by_choices.append(
                (json.dumps([column_name, True]), f"{column_name} " + __("[asc]"))
            )
            order_by_choices.append(
                (json.dumps([column_name, False]), f"{column_name} " + __("[desc]"))
            )

        return {
            "time_grain_sqla": [
                (g.duration, g.name) for g in self.database.grains() or []
            ],
            "filter_select": True,
            "name": self.tab_name,
            "columns": self.columns,
            "metrics": [],
            "id": self.id,
            "type": self.type,
            "sql": self.sql,
            "owners": self.owners_data,
            "database": {"id": self.database_id, "backend": self.database.backend},
            "order_by_choices": order_by_choices,
            "schema": self.schema,
        }

    def raise_for_access(self) -> None:
        """
        Raise an exception if the user cannot access the resource.

        :raises SupersetSecurityException: If the user cannot access the resource
        """

        security_manager.raise_for_access(query=self)

    @property
    def db_engine_spec(self) -> Type["BaseEngineSpec"]:
        return self.database.db_engine_spec

    @property
    def owners_data(self) -> List[Dict[str, Any]]:
        return []

    @property
    def uid(self) -> str:
        return f"{self.id}__{self.type}"

    @property
    def is_rls_supported(self) -> bool:
        return False

    @property
    def cache_timeout(self) -> int:
        return 0

    @property
    def column_names(self) -> List[Any]:
        return [col.get("column_name") for col in self.columns]

    @property
    def offset(self) -> int:
        return 0

    @property
    def main_dttm_col(self) -> Optional[str]:
        for col in self.columns:
            if col.get("is_dttm"):
                return col.get("column_name")
        return None

    @property
    def dttm_cols(self) -> List[Any]:
        return [col.get("column_name") for col in self.columns if col.get("is_dttm")]

    @property
    def schema_perm(self) -> str:
        return f"{self.database.database_name}.{self.schema}"

    @property
    def perm(self) -> str:
        return f"[{self.database.database_name}].[{self.tab_name}](id:{self.id})"

    @property
    def default_endpoint(self) -> str:
        return ""

    @staticmethod
    def get_extra_cache_keys(query_obj: Dict[str, Any]) -> List[str]:
        return []

    @property
    def tracking_url(self) -> Optional[str]:
        """
        Transfrom tracking url at run time because the exact URL may depends
        on query properties such as execution and finish time.
        """
        transform = current_app.config.get("TRACKING_URL_TRANSFORMER")
        url = self.tracking_url_raw
        if url and transform:
            sig = inspect.signature(transform)
            # for backward compatibility, users may define a transformer function
            # with only one parameter (`url`).
            args = [url, self][: len(sig.parameters)]
            url = transform(*args)
            logger.debug("Transformed tracking url: %s", url)
        return url

    @tracking_url.setter
    def tracking_url(self, value: str) -> None:
        self.tracking_url_raw = value

    def get_column(self, column_name: Optional[str]) -> Optional[Dict[str, Any]]:
        if not column_name:
            return None
        for col in self.columns:
            if col.get("column_name") == column_name:
                return col
        return None


class SavedQuery(Model, AuditMixinNullable, ExtraJSONMixin, ImportExportMixin):
    """ORM model for SQL query"""

    __tablename__ = "saved_query"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("ab_user.id"), nullable=True)
    db_id = Column(Integer, ForeignKey("dbs.id"), nullable=True, comment="数据库ID")
    schema = Column(String(128), comment="数据库名")
    label = Column(String(256), comment="标签")
    description = Column(Text, comment="说明")
    sql = Column(LONGTEXT, comment="sql")
    template_parameters = Column(Text, comment="模板参数")
    user = relationship(
        security_manager.user_model,
        backref=backref("saved_queries", cascade="all, delete-orphan"),
        foreign_keys=[user_id],
    )
    database = relationship(
        "Database",
        foreign_keys=[db_id],
        backref=backref("saved_queries", cascade="all, delete-orphan"),
    )
    rows = Column(Integer, nullable=True, comment="总行数")
    last_run = Column(DateTime, nullable=True, comment="最后查询时间")

    export_parent = "database"
    export_fields = [
        "schema",
        "label",
        "description",
        "sql",
    ]

    def __repr__(self) -> str:
        return str(self.label)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
        }

    @property
    def pop_tab_link(self) -> Markup:
        return Markup(
            f"""
            <a href="/superset/sqllab?savedQueryId={self.id}">
                <i class="fa fa-link"></i>
            </a>
        """
        )

    @property
    def user_email(self) -> str:
        return self.user.email

    @property
    def sqlalchemy_uri(self) -> URL:
        return self.database.sqlalchemy_uri

    def url(self) -> str:
        return "/superset/sqllab?savedQueryId={0}".format(self.id)

    @property
    def sql_tables(self) -> List[Table]:
        return list(ParsedQuery(self.sql).tables)

    @property
    def last_run_humanized(self) -> str:
        return naturaltime(datetime.now() - self.changed_on)

    @property
    def _last_run_delta_humanized(self) -> str:
        return naturaltime(datetime.now() - self.changed_on)

    @renders("changed_on")
    def last_run_delta_humanized(self) -> str:
        return self._last_run_delta_humanized


class TabState(Model, AuditMixinNullable, ExtraJSONMixin):

    __tablename__ = "tab_state"

    # basic info
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    label = Column(String(256), comment="标签")
    active = Column(Boolean, default=False, comment="是否激活")

    # selected DB and schema
    database_id = Column(Integer, ForeignKey("dbs.id", ondelete="CASCADE"))
    database = relationship("Database", foreign_keys=[database_id])
    schema = Column(String(256), comment="数据库名称")

    # tables that are open in the schema browser and their data previews
    table_schemas = relationship(
        "TableSchema",
        cascade="all, delete-orphan",
        backref="tab_state",
        passive_deletes=True,
    )

    # the query in the textarea, and results (if any)
    sql = Column(Text, comment="sql")
    query_limit = Column(Integer, comment="查询条数")

    # latest query that was run
    latest_query_id = Column(
        String(11), ForeignKey("query.client_id", ondelete="CASCADE"), nullable=True
    )
    latest_query = relationship("Query")

    # other properties
    autorun = Column(Boolean, default=False)
    template_params = Column(Text, comment="模板参数")
    hide_left_bar = Column(Boolean, default=False, comment="隐藏条")

    # any saved queries that are associated with the Tab State
    saved_query_id = Column(
        Integer, ForeignKey("saved_query.id", ondelete="SET NULL"), nullable=True
    )
    saved_query = relationship("SavedQuery", foreign_keys=[saved_query_id])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "label": self.label,
            "active": self.active,
            "database_id": self.database_id,
            "schema": self.schema,
            "table_schemas": [ts.to_dict() for ts in self.table_schemas],
            "sql": self.sql,
            "query_limit": self.query_limit,
            "latest_query": self.latest_query.to_dict() if self.latest_query else None,
            "autorun": self.autorun,
            "template_params": self.template_params,
            "hide_left_bar": self.hide_left_bar,
            "saved_query": self.saved_query.to_dict() if self.saved_query else None,
        }


class TableSchema(Model, AuditMixinNullable, ExtraJSONMixin):

    __tablename__ = "table_schema"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tab_state_id = Column(Integer, ForeignKey("tab_state.id", ondelete="CASCADE"))

    database_id = Column(
        Integer, ForeignKey("dbs.id", ondelete="CASCADE"), nullable=False
    )
    database = relationship("Database", foreign_keys=[database_id])
    schema = Column(String(256), comment="数据库名")
    table = Column(String(256), comment="表名称")

    # JSON describing the schema, partitions, latest partition, etc.
    description = Column(Text, comment="说明")

    expanded = Column(Boolean, default=False)

    def to_dict(self) -> Dict[str, Any]:
        try:
            description = json.loads(self.description)
        except json.JSONDecodeError:
            description = None

        return {
            "id": self.id,
            "tab_state_id": self.tab_state_id,
            "database_id": self.database_id,
            "schema": self.schema,
            "table": self.table,
            "description": description,
            "expanded": self.expanded,
        }
