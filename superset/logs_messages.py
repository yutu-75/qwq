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


class LogsMessages(object):
    SUCCESS = '成功'
    FAIL = '失败'
    LM_ADD_DATA_SOURCE_GROUP = '新增数据源分组'
    LM_EDIT_DATA_SOURCE_GROUP = '编辑数据源分组'
    LM_DEL_DATA_SOURCE_GROUP = '删除数据源分组'
    LM_DEL_DATASOURCE = '删除数据源'

    LM_ADD_DASHBOARD = '新增看板'
    LM_MOVE_DASHBOARD = '移动/重命名看板'
    LM_COPY_DASHBOARD = '复制看板'
    LM_EDIT_DASHBOARD = '编辑看板'
    LM_DEL_DASHBOARD = '删除看板'
    LM_EXPORT_DASHBOARD = '导出看板'
    LM_IMPORT_DASHBOARD = '导入看板'
    LM_EXPLORE_DASHBOARD_IMG = '导出看板图片'

    LM_ADD_CHART = '新增图表'
    LM_MOVE_CHART = '移动/重命名图表'
    LM_COPY_CHART = '复制图表'
    LM_EDIT_CHART = '编辑图表'
    LM_DEL_CHART = '删除图表'
    LM_EXPORT_CHART = '导出图表'
    LM_IMPORT_CHART = '导入图表'

    LM_ADD_DATABASE = '新增数据库'
    LM_MOVE_DATABASE = '移动数据库'
    LM_EDIT_DATABASE = '编辑数据库'
    LM_DEL_DATABASE = '删除数据库'

    LM_ADD_DATASET = '新增数据集'
    LM_ADD_API_DATASET = '新增API数据集'
    LM_ADD_API_DATASET_TASK = '新增API数据集任务'
    LM_EDIT_API_DATASET_TASK = '编辑API数据集任务'
    LM_DEL_API_DATASET_TASK = '删除API数据集任务'
    LM_ADD_UNION_DATASET = '新增关联数据集'
    LM_ADD_FILE_DATASET = '新增离线文件数据集'
    LM_ADD_SQL_DATASET = '新增SQL数据集'
    LM_MOVE_DATASET = '移动数据集'
    LM_EDIT_DATASET = '编辑数据集'
    LM_DEL_DATASET = '删除数据集'
    LM_EDIT_DATASET_COLUMS = '编辑数据集字段'

    LM_ADD_DASHBOARD_GROUP = '新增看板分组'
    LM_EDIT_DASHBOARD_GROUP = '编辑看板分组'
    LM_DEL_DASHBOARD_GROUP = '删除看板分组'

    LM_ADD_CHART_GROUP = '新增图表分组'
    LM_EDIT_CHART_GROUP = '编辑图表分组'
    LM_DEL_CHART_GROUP = '删除图表分组'

    LM_ADD_DATABASE_GROUP = '新增数据库分组'
    LM_EDIT_DATABASE_GROUP = '编辑数据库分组'
    LM_DEL_DATABASE_GROUP = '删除数据库分组'

    LM_ADD_DATASET_GROUP = '新增数据集分组'
    LM_EDIT_DATASET_GROUP = '更新数据集分组'
    LM_DEL_DATASET_GROUP = '删除数据集分组'

    LM_ADD_DATABASE_SYNC_GROUP = '新增数据同步分组'
    LM_ADD_DATABASE_NAME_SYNC_GROUP = '新增数据源同步分组'
    LM_MOVE_DATABASE_NAME_SYNC_GROUP = '移动数据源同步分组'
    LM_EDIT_DATABASE_SYNC_GROUP = '更新数据同步分组'
    LM_DEL_DATABASE_SYNC_GROUP = '删除数据同步分组'
    LM_EXECUTE_DATABASE_SYNC_GROUP = '立即执行同步分组'

    LM_ADD_FAVSTAR = '新增收藏'
    LM_DEL_FAVSTAR = '删除收藏'

    # dept
    LM_ADD_DEPT = '新增组织'
    LM_ADD_DEPT_USERS = '新增组织用户'
    LM_EDIT_DEPT = '更新组织'
    LM_DEL_DEPT = '删除组织'
    LM_DEL_DEPT_USERS = '删除组织'

    LM_ADD_AUTH = '新增权限'
    LM_EDIT_AUTH = '权限设置'

    LM_ADD_API_DATA_SOURCE = '新增API数据源'
    LM_ADD_DATABASE_DATA_SOURCE = '新增数据库数据源'
    LM_EDIT_API_DATA_SOURCE = '编辑API数据源'
    LM_EDIT_DATABASE_DATA_SOURCE = '编辑数据库数据源'
    LM_MOVE_DATA_SOURCE = '移动数据源'
    LM_EDIT_DATA_SOURCE = '编辑数据源'

    # User
    LM_ADD_USER = '新增用户'
    LM_EDIT_USER = '编辑用户'
    LM_DEL_USER = '删除用户'
    LM_EXPORT_USER_IMPORT_TEMPLATE = '导出用户导入模板'

    LM_ADD_ROLE = '新增角色'
    LM_ADD_ROLE_USERS = '新增角色用户'
    LM_EDIT_ROLE = '编辑角色'
    LM_DEL_ROLE = '删除角色'
    LM_DEL_ROLE_USERS = '删除角色用户'

    IMPORT_USERS = '导入用户'

    # RLS
    LM_ADD_RLS = '新增行级权限'
    LM_EDIT_RLS = '编辑行级权限'
    LM_DEL_RLS = '删除行级权限'
    LM_COLSE_RLS = '关闭行级过滤'

    # CLS
    LM_ADD_CLS = '新增列级权限'
    LM_EDIT_CLS = '编辑列级权限'
    LM_DEL_CLS = '删除列级权限'

    # excel
    EXPLORE_CHART_EXCEL = '导出图表excel'
    EXPLORE_DASHBOARD_EXCEL = '导出看板excel'

    # CONFIG
    LM_EDIT_SYS_CONFIG = '编辑系统设置'

    # data masking
    LM_EDIT_MASKING_RULE = '编辑脱敏规则'

    # water mark
    LM_EDIT_WATER_MARK = '编辑水印配置'

