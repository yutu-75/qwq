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
from flask_babel import gettext as __


class Messages(object):
    ERROR = __('error')
    SUCCESS = __('Success')
    PARAMETER_ERROR = __("Parameter error.")
    IS_EXIST = __('It already exist.')
    NOT_EXIST = __("It doesn't exist.")
    PARENT_NOT_EXIST = __("Parent doesn't exist.")
    GROUP_IS_EXIST = __("Group is exist.")
    GROUP_NOT_EXIST = __("Group doesn't exist.")
    CANNOT_MOVE_GROUP = __("Cannot move to the current group.")
    CANNOT_MOVE_ITSELF = __("Cannot move to itself.")
    CLOSE_SUPERADMIN_ERROR = __('Unable to close self administrator privileges')
    MOVE_TO_CHILDREN_ERR = __('Cannot move to its own subdirectory.')

    # LOGIN
    USERNAME_LOGIN_ERROR = __("User name does not exist.")
    USERNAME_OR_PASSWORD_ERROR = __("Incorrect username or password")
    LIMITED_LOGIN_TIMES = __("Multiple login failures. Please try again later")

    # dept
    DEPT_NOT_EXIST = __('The organization does not exist.')
    PARENT_DEPT_NOT_EXIST = __('Parent organization does not exist.')
    DEPT_EXIST = __('The current organization already exists.')
    DEPT_USER_EXIST = __('There are users who have joined this organization.')

    # auth
    FORBIDDEN = __('Forbidden')

    # datasource
    DATABASE_CONNECTION_ERR = __('Database connection error.')
    DATASOURCE_TYPE_ERR = __('Datasource type error.')
    DUPLICATE_NAME = __('Duplicate name.')
    FIRST_DEL_DATASET = __('There are datasets that use it.')
    REQUEST_FAILURE = __('request failure')
    REQUEST_ERROR_MSG = __('status code: %s, responese text: %s')
    DATA_PARSING_ERROR = __('data parsing error')
    API_DATASOURCE_TABLE_NAME_DUPLICATE = __('Duplicate API data source table name')
    DATASOURCE_DEL_ERROR = __(
        'There are datasets using this data source. Please delete all datasets '
        'associated with this data source first')

    # dataset
    DATASET_IS_REFERENCED = __('The dataset is referenced by the chart.')
    GROUP_HAVE_DATASET = __('The group have dataset.')
    DATASET_DEL_ERROR = __(
        'There are charts using this dataset. Please delete these charts first')
    FILE_NOT_UPLOADED = __('File not uploaded')
    DATASET_NAME_ERROR = __('Dataset name cannot be empty')
    UNION_DATASET_DB_ERROR = __(
        'Datasets that are not in the same database cannot be associated')
    DATASET_TYPE_ERROR = __('Cannot select associated dataset and SQL dataset')
    MISSING_UNION_DATASETS = __('Please select the dataset to associate')
    APPEND_DATA_FORNAT_ERROR = __(
        'The additional data does not match the original data column name')
    API_DATASOURCE_PARSE_ERROR = __('Data changes and parsing errors occur')
    API_DATASET_DEFINE_TASKS = __('API datasets are required to define tasks')
    UNOIN_ERR = __(
        'There are exceptions in the associated dataset. Please contact the '
        'administrator')

    # chart
    CHART_IS_REFERENCED = __('The chart is referenced by the dashboard.')
    GROUP_HAVE_CHART = __('The group have chart.')
    CHART_DEL_ERROR = __(
        'There is a dashboard using this chart. Please delete this chart dashboard '
        'from the dashboard first')

    # user import
    PWD_STRENGTH_ERROR = __(
        'The password must contain uppercase and lowercase letters, numbers, and the '
        'password length must be greater than or equal to 8 but less than or equal to '
        '16')
    USERNAME_OR_EMAIL_USED = __('Email or username already in use')
    FILE_TYPE_ERROR = __("file type error")
    DUPLICATE_USERNAME = __('username %s or email %s already exists')
    NAME_ERROR = __('The name in line %s cannot be empty')
    MAIL_ERROR = __('The email format in line %s is incorrect')
    USERNAME_ERROR = __('The username on line %s is incorrect')
    STATUS_ERROR = __('Account status can only be filled in as 0 and 1')
    IS_ADMIN_ERROR = __('Super administrators can only fill in 0 and 1')
    EXCEL_TEMPLATE_ERROR = __('excel template error')

    # dashboard
    FIRST_DEL_GROUPS_AND_DATA = __('Delete the groups and data in this group first')
    DEL_GROUP_ERROR = __(
        'There is a file in the group, please delete or move this file first')

    # IMPORT
    IM_DATASET_GROUP_NOT_EXIST = __('The imported dataset group does not exist')
    IM_DATASOURCE_GROUP_NOT_EXIST = __('The imported datasource group does not exist')
    IM_CHART_GROUP_NOT_EXIST = __('The imported chart group does not exist')
    IM_DASHBOARD_GROUP_NOT_EXIST = __('The imported dashboard group does not exist')

    # file dataset
    FILE_IS_NONE = __('Please check if there is data in this file')

    # role
    DEL_ROLE_ERR = __('Only super administrators and creators can delete')

    # database_sync
    DEL_SYNC_TASK_ERR = __(
        'There are synchronization tasks in this directory and cannot be deleted!')
    DEL_SYNC_GROUP_ERROR = __(
        'There are subdirectories/data sources in this directory and cannot be deleted!'
    )
