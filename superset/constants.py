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

# ATTENTION: If you change any constants, make sure to also change utils/common.js

# string to use when None values *need* to be converted to/from strings
from enum import Enum

USER_AGENT = "Apache Superset"

NULL_STRING = "<NULL>"
EMPTY_STRING = "<empty string>"

CHANGE_ME_SECRET_KEY = "tG5esXIVqp1TlnOF40zWW4zWxh7998zZy6M6aNIVCZNwSRn2T7kLfA2u"

# UUID for the examples database
EXAMPLES_DB_UUID = "a2dc77af-e654-49bb-b321-40f6b559a1ee"

PASSWORD_MASK = "X" * 10

NO_TIME_RANGE = "No filter"

QUERY_CANCEL_KEY = "cancel_query"
QUERY_EARLY_CANCEL_KEY = "early_cancel_query"

LRU_CACHE_MAX_SIZE = 256

GET_DASHBOARD_VIEW_URL_FORMAT = "/superset/dashboard/{}/"


class RouteMethod:  # pylint: disable=too-few-public-methods
    """
    Route methods are a FAB concept around ModelView and RestModelView
    classes in FAB. Derivatives can define `include_route_method` and
    `exclude_route_methods` class attribute as a set of methods that
    will or won't get exposed.

    This class is a collection of static constants to reference common
    route methods, namely the ones defined in the base classes in FAB
    """

    # ModelView specific
    ACTION = "action"
    ACTION_POST = "action_post"
    ADD = "add"
    API_CREATE = "api_create"
    API_DELETE = "api_delete"
    API_GET = "api_get"
    API_READ = "api_read"
    API_UPDATE = "api_update"
    DELETE = "delete"
    DOWNLOAD = "download"
    EDIT = "edit"
    LIST = "list"
    SHOW = "show"
    INFO = "info"

    # RestModelView specific
    EXPORT = "export"
    IMPORT = "import_"
    GET = "get"
    GET_LIST = "get_list"
    POST = "post"
    PUT = "put"
    RELATED = "related"
    DISTINCT = "distinct"

    # Commonly used sets
    API_SET = {API_CREATE, API_DELETE, API_GET, API_READ, API_UPDATE}
    CRUD_SET = {ADD, LIST, EDIT, DELETE, ACTION_POST, SHOW}
    RELATED_VIEW_SET = {ADD, LIST, EDIT, DELETE}
    REST_MODEL_VIEW_CRUD_SET = {DELETE, GET, GET_LIST, POST, PUT, INFO}
    READ_ONLY = {GET, GET_LIST, LIST}


MODEL_VIEW_RW_METHOD_PERMISSION_MAP = {
    "add": "write",
    "api": "read",
    "api_column_add": "write",
    "api_column_edit": "write",
    "api_create": "write",
    "api_delete": "write",
    "api_get": "read",
    "api_read": "read",
    "api_readvalues": "read",
    "api_update": "write",
    "annotation": "read",
    "delete": "write",
    "download": "read",
    "download_dashboards": "read",
    "edit": "write",
    "list": "read",
    "muldelete": "write",
    "mulexport": "read",
    "show": "read",
    "new": "write",
    "yaml_export": "read",
    "refresh": "write",
}

MODEL_API_RW_METHOD_PERMISSION_MAP = {
    "bulk_delete": "write",
    "delete": "write",
    "distinct": "read",
    "get": "read",
    "get_list": "read",
    "info": "read",
    "post": "write",
    "put": "write",
    "related": "read",
    "related_objects": "read",
    "tables": "read",
    "schemas": "read",
    "select_star": "read",
    "table_metadata": "read",
    "table_extra_metadata": "read",
    "test_connection": "read",
    "validate_parameters": "read",
    "favorite_status": "read",
    "thumbnail": "read",
    "import_": "write",
    "refresh": "write",
    "cache_screenshot": "read",
    "screenshot": "read",
    "data": "read",
    "data_from_cache": "read",
    "get_charts": "read",
    "get_datasets": "read",
    "function_names": "read",
    "available": "read",
    "validate_sql": "read",
    "get_data": "read",
    "samples": "read",
    "delete_ssh_tunnel": "write",
    "get_updated_since": "read",
    "stop_query": "read",
}

EXTRA_FORM_DATA_APPEND_KEYS = {
    "adhoc_filters",
    "filters",
    "interactive_groupby",
    "interactive_highlight",
    "interactive_drilldown",
    "custom_form_data",
}

EXTRA_FORM_DATA_OVERRIDE_REGULAR_MAPPINGS = {
    "granularity": "granularity",
    "granularity_sqla": "granularity",
    "time_column": "time_column",
    "time_grain": "time_grain",
    "time_range": "time_range",
    "time_grain_sqla": "time_grain_sqla",
}

EXTRA_FORM_DATA_OVERRIDE_EXTRA_KEYS = {
    "relative_start",
    "relative_end",
}

EXTRA_FORM_DATA_OVERRIDE_KEYS = (
    set(EXTRA_FORM_DATA_OVERRIDE_REGULAR_MAPPINGS.values())
    | EXTRA_FORM_DATA_OVERRIDE_EXTRA_KEYS
)


class PandasAxis(int, Enum):
    ROW = 0
    COLUMN = 1


class PandasPostprocessingCompare(str, Enum):
    DIFF = "difference"
    PCT = "percentage"
    RAT = "ratio"


class CacheRegion(str, Enum):
    DEFAULT = "default"
    DATA = "data"
    THUMBNAIL = "thumbnail"


VIEW = 1
ALL_VIEW = 1.5
EXPORT = 2
ALL_EXPORT = 3
MANAGE = 4
ALL_MANAGE = 5
GRANT = 8
ALL_GRANT = 9
ROW_COL_SECURITY = 6
ALL_ROW_COL_SECURITY = 7


class AuthSourceType(str, Enum):
    DASHBOARD = "dashboard"
    DASHBOARD_GROUP = "dashboard_group"
    CHART = "chart"
    CHART_GROUP = "chart_group"
    DATASET = "dataset"
    DATASET_GROUP = "dataset_group"
    DATABASE_SYNC = "database sync"
    DATABASE_SYNC_GROUP = "database sync_group"
    DATASOURCE = "datasource"
    DATASOURCE_GROUP = "datasource_group"
    MENU = "menu"


class AuthTargetType(str, Enum):
    DEPT = "dept"
    ROLE = "role"
    USER = "user"


class DatabaseAuthType(str, Enum):
    DB_SCHEMA = "db_schema"
    DB_SCHEMA_TABLE = "db_schema_table"


class AuthType(str, Enum):
    DEPT = "dept"
    ROLE = "role"
    USER = "user"
    DASHBOARD = "dashboard"
    CHART = "chart"
    DATASOURCE = "datasource"
    DATASET = "dataset"
    DATABASE_SYNC = "database sync"
    MENU = "menu"
    DATABASE = "database"


class PrivilegeNameType(str, Enum):
    VIEW = "view"
    EXPORT = "export"
    MANAGE = "manage"
    GRANT = "grant"


class DirectionType(str, Enum):
    SOURCE = "source"
    TARGET = "target"


class DatasetType:
    """
        0：数据库数据集    db
        1：SQL数据集       sql
        2：Excel数据集     excel
        3：关联数据集      UNION
        4：API数据集       api
    """
    DATABASE = 0
    SQL = 1
    EXCEL = 2
    UNION = 3
    API = 4


class DatabaseSyncType:
    """
        0：数据库数据集    db
    """
    DATABASE = 0



class DataSourceType(str, Enum):
    DATABASE = "database"
    API = "api"
    TOKEN_API = "token_api"
class DataBaseType(str, Enum):
    DATABASE = "hive" or "mysql"
    API = "api"
    TOKEN_API = "token_api"

class MenuName(str, Enum):
    """菜单名称"""
    DASHBOARD = "Dashboard"
    CHART = "Chart"
    SQL_LAB = "SQL Lab"
    DATASOURCE = "Datasource"
    DATASET = "Dataset"
    DATABASE_SYNC = "Database Sync"
    PERMISSION_MANAGEMENT = "Permission Management"
    SYSTEM_MANAGER = "System Manager"
    USER_MANAGEMENT = "User Management"
    ROLE_MANAGEMENT = "Role Management"
    DEPT_MANAGEMENT = "Dept Management"
    SYSTEM_CONFIGURATION = "System Configuration"


class SystemLoginType(str, Enum):
    LOGIN_CAS = "LOGIN_CAS"
    LOGIN_LDAP = "LOGIN_LDAP"


class SystemConfigType(str, Enum):
    """系统设置类别"""
    LOGIN = SystemLoginType
    WATER_MARK = "WATER_MARK"  # 水印配置参数
    APPEARANCE = "APPEARANCE"  # 登录页配置参数
    SYSTEM_PARAM = "SYSTEM_PARAM"  # 登录参数设置（失败次数等）


class IfExistType(str, Enum):
    FAIL = "fail"
    REPLACE = "replace"
    APPEND = "append"


class LoginMethod(str, Enum):
    DB = "db"
    LDAP = "ldap"
    CAS = "cas"


class TimeGrainType(str, Enum):
    YEAR = "year"
    MONTH = "month"
    DAY = "day"
    WEEK = "week"
    QUARTER = "quarter"


class AdaptationEquipment(str, Enum):
    pc = "pc"
    mobile = "mobile"
