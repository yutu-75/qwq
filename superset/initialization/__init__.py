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
"""
修改：李洪浩-2022-12-20
修改内容:将UserJobInfoFilersModelView视图注册到导航栏行级别权限中
--------------------------------------------
修改：李洪浩-2023-03-09
修改内容:按照官方2.0.1修改行级权限视图
"""
from __future__ import annotations

import logging
import os
import sys
from typing import Any, Callable, Dict, TYPE_CHECKING

import wtforms_json
from deprecation import deprecated
from flask import Flask, redirect
from flask_appbuilder import expose, IndexView
from flask_babel import gettext as __
from flask_compress import Compress
from werkzeug.middleware.proxy_fix import ProxyFix

from superset.constants import CHANGE_ME_SECRET_KEY
from superset.databases.commands.exceptions import CustomSecurityManagerError
from superset.extensions import (
    _event_logger,
    APP_DIR,
    appbuilder,
    async_query_manager,
    cache_manager,
    celery_app,
    csrf,
    db,
    encrypted_field_factory,
    feature_flag_manager,
    machine_auth_provider_factory,
    manifest_processor,
    migrate,
    profiling,
    results_backend_manager,
    ssh_manager_factory,
    stats_logger_manager,
    talisman,
)
from superset.security import SupersetSecurityManager
from superset.superset_typing import FlaskResponse
from superset.tags.core import register_sqla_event_listeners
from superset.utils.core import is_test, pessimistic_connection_handling
from superset.utils.log import DBEventLogger, get_event_logger_from_cfg_value
from superset.v2.utils.menu import CustomMenu

if TYPE_CHECKING:
    from superset.app import SupersetApp

logger = logging.getLogger(__name__)


class SupersetAppInitializer:  # pylint: disable=too-many-public-methods
    def __init__(self, app: SupersetApp) -> None:
        super().__init__()

        self.superset_app = app
        self.config = app.config
        self.manifest: Dict[Any, Any] = {}

    @deprecated(details="use self.superset_app instead of self.flask_app")  # type: ignore
    @property
    def flask_app(self) -> SupersetApp:
        return self.superset_app

    def pre_init(self) -> None:
        """
        Called before all other init tasks are complete
        """
        wtforms_json.init()

        if not os.path.exists(self.config["DATA_DIR"]):
            os.makedirs(self.config["DATA_DIR"])

    def post_init(self) -> None:
        """
        Called after any other init tasks
        """

    def configure_celery(self) -> None:
        celery_app.config_from_object(self.config["CELERY_CONFIG"])
        celery_app.set_default()
        superset_app = self.superset_app

        # Here, we want to ensure that every call into Celery task has an app context
        # setup properly
        task_base = celery_app.Task

        class AppContextTask(task_base):  # type: ignore
            # pylint: disable=too-few-public-methods
            abstract = True

            # Grab each call into the task and set up an app context
            def __call__(self, *args: Any, **kwargs: Any) -> Any:
                with superset_app.app_context():
                    return task_base.__call__(self, *args, **kwargs)

        celery_app.Task = AppContextTask

    def init_views(self) -> None:
        #
        # We're doing local imports, as several of them import
        # models which in turn try to import
        # the global Flask app
        #
        # pylint: disable=import-outside-toplevel,too-many-locals,too-many-statements
        from superset.advanced_data_type.api import AdvancedDataTypeRestApi
        from superset.annotation_layers.annotations.api import AnnotationRestApi
        from superset.annotation_layers.api import AnnotationLayerRestApi
        from superset.async_events.api import AsyncEventsRestApi
        from superset.available_domains.api import AvailableDomainsRestApi
        from superset.cachekeys.api import CacheRestApi
        from superset.charts.api import ChartRestApi
        from superset.tripartite_attribute.api import RecordRestApi
        from superset.datasets_mask.api import DatasetMarkRestApi
        from superset.charts.data.api import ChartDataRestApi
        from superset.connectors.sqla.views import (
            RowLevelSecurityFiltersModelView,
            SqlMetricInlineView,
            TableColumnInlineView,
            TableModelView,
        )
        from superset.css_templates.api import CssTemplateRestApi
        from superset.dashboards.api import DashboardRestApi
        from superset.dashboards.filter_sets.api import FilterSetRestApi
        from superset.dashboards.filter_state.api import DashboardFilterStateRestApi
        from superset.dashboards.permalink.api import DashboardPermalinkRestApi
        from superset.dashboards.share.api import DashboardsShareRestApi
        from superset.dashboards.user_access_level.api import \
            DashboardsUserAccessLevelRestApi
        from superset.aliyun_oss.api import UploadFileRestApi
        from superset.databases.api import DatabaseRestApi
        from superset.datasets.api import DatasetRestApi
        from superset.datasets.columns.api import DatasetColumnsRestApi
        from superset.datasets.metrics.api import DatasetMetricRestApi
        from superset.datasource.api import DatasourceRestApi
        from superset.embedded.api import EmbeddedDashboardRestApi
        from superset.embedded.view import EmbeddedView
        from superset.explore.api import ExploreRestApi
        from superset.explore.form_data.api import ExploreFormDataRestApi
        from superset.explore.permalink.api import ExplorePermalinkRestApi
        from superset.importexport.api import ImportExportRestApi
        from superset.queries.api import QueryRestApi
        from superset.queries.saved_queries.api import SavedQueryRestApi
        from superset.reports.api import ReportScheduleRestApi
        from superset.reports.logs.api import ReportExecutionLogRestApi
        from superset.security.api import SecurityRestApi
        from superset.sqllab.api import SqlLabRestApi
        from superset.app_attributes.api import AppAttributeRestApi

        from superset.views.access_requests import AccessRequestsModelView
        from superset.views.alerts import AlertView, ReportView
        from superset.views.annotations import AnnotationLayerView
        from superset.views.api import Api
        from superset.views.chart.views import SliceAsync, SliceModelView
        from superset.views.record.views import RecordModelView
        from superset.views.core import Superset
        from superset.views.css_templates import (
            CssTemplateAsyncModelView,
            CssTemplateModelView,
        )
        from superset.views.dashboard.views import (
            Dashboard,
            DashboardModelView,
            DashboardModelViewAsync,
        )
        from superset.views.database.views import (
            ColumnarToDatabaseView,
            CsvToDatabaseView,
            DatabaseView,
            ExcelToDatabaseView,
        )
        from superset.views.datasource.views import DatasetEditor, Datasource
        from superset.views.dynamic_plugins import DynamicPluginsView
        from superset.views.explore import ExplorePermalinkView, ExploreView
        from superset.views.key_value import KV
        from superset.views.log.api import LogRestApi
        from superset.views.log.views import LogModelView
        from superset.views.redirects import R
        from superset.views.sql_lab.views import (
            SavedQueryView,
            SavedQueryViewApi,
            SqlLab,
            TableSchemaView,
            TabStateView,
        )
        from superset.views.tags import TagView
        from superset.views.users.api import CurrentUserRestApi
        from superset.views.users.api import UserRestApi
        from superset.views.user_job_info import UserJobInfoFiltersModelView
        from superset.views.app_attributes.views import AppAttributeModelView
        from superset.views.database_sync.api import DatabaseSyncModelView

        # 临时接口，方便更新前端代码 管理服务的接口
        from superset.service_management.api import ServiceManagementApi
        appbuilder.add_api(ServiceManagementApi)

        #
        # Setup API views
        #
        appbuilder.add_api(AnnotationRestApi)
        appbuilder.add_api(AnnotationLayerRestApi)
        appbuilder.add_api(AsyncEventsRestApi)
        appbuilder.add_api(AdvancedDataTypeRestApi)
        appbuilder.add_api(AvailableDomainsRestApi)
        appbuilder.add_api(CacheRestApi)
        appbuilder.add_api(ChartRestApi)
        appbuilder.add_api(RecordRestApi)
        appbuilder.add_api(DatasetMarkRestApi)
        appbuilder.add_api(ChartDataRestApi)
        appbuilder.add_api(CssTemplateRestApi)
        appbuilder.add_api(CurrentUserRestApi)
        appbuilder.add_api(UserRestApi)
        appbuilder.add_api(DashboardFilterStateRestApi)
        appbuilder.add_api(DashboardPermalinkRestApi)
        appbuilder.add_api(DashboardsShareRestApi)
        appbuilder.add_api(DashboardsUserAccessLevelRestApi)
        appbuilder.add_api(UploadFileRestApi)
        appbuilder.add_api(DashboardRestApi)
        appbuilder.add_api(DatabaseRestApi)
        appbuilder.add_api(DatasetRestApi)
        appbuilder.add_api(DatasetColumnsRestApi)
        appbuilder.add_api(DatasetMetricRestApi)
        appbuilder.add_api(DatasourceRestApi)
        appbuilder.add_api(EmbeddedDashboardRestApi)
        appbuilder.add_api(ExploreRestApi)
        appbuilder.add_api(ExploreFormDataRestApi)
        appbuilder.add_api(ExplorePermalinkRestApi)
        appbuilder.add_api(FilterSetRestApi)
        appbuilder.add_api(ImportExportRestApi)
        appbuilder.add_api(QueryRestApi)
        appbuilder.add_api(ReportScheduleRestApi)
        appbuilder.add_api(ReportExecutionLogRestApi)
        appbuilder.add_api(SavedQueryRestApi)
        appbuilder.add_api(SqlLabRestApi)
        appbuilder.add_api(AppAttributeRestApi)
        #
        # 新增API
        #
        from superset.v2.dashboards.group.api import DashboardGroupRestApi
        appbuilder.add_api(DashboardGroupRestApi)
        from superset.v2.dashboards.api import DashboardV2RestApi
        appbuilder.add_api(DashboardV2RestApi)
        from superset.v2.datasources.api import DataSourcesRestApi
        appbuilder.add_api(DataSourcesRestApi)
        from superset.v2.datasets.api_datasets.api import APIDatasetRestApi
        appbuilder.add_api(APIDatasetRestApi)
        from superset.v2.datasets.union.api import UnionDatasetRestApi
        appbuilder.add_api(UnionDatasetRestApi)
        from superset.v2.datasources.api_datasources.api import \
            APIDataSourcesRestApi
        appbuilder.add_api(APIDataSourcesRestApi)
        from superset.v2.datasources.database.api import \
            DataSourcesDatabaseRestApi
        appbuilder.add_api(DataSourcesDatabaseRestApi)
        from superset.v2.datasources.group.api import DataSourcesGroupRestApi
        appbuilder.add_api(DataSourcesGroupRestApi)
        from superset.v2.datasets.api import DatasetV2RestApi
        appbuilder.add_api(DatasetV2RestApi)
        from superset.v2.datasets.group.api import DatasetGroupRestApi
        appbuilder.add_api(DatasetGroupRestApi)
        from superset.v2.charts.api import ChartV2RestApi
        appbuilder.add_api(ChartV2RestApi)
        from superset.v2.charts.group.api import ChartGroupRestApi
        appbuilder.add_api(ChartGroupRestApi)
        from superset.v2.user.api import UserV2RestApi
        appbuilder.add_api(UserV2RestApi)
        from superset.v2.role.api import RoleV2RestApi
        appbuilder.add_api(RoleV2RestApi)
        from superset.sys_manager.sys_config.api import SysConfigRestApi
        appbuilder.add_api(SysConfigRestApi)
        from superset.v2.databases.api import DatabaseV2RestApi
        appbuilder.add_api(DatabaseV2RestApi)
        from superset.v2.datasets.rls_filter.api import DatasetRLSFilterApi
        appbuilder.add_api(DatasetRLSFilterApi)
        from superset.v2.datasets.cls_filter.api import DatasetCLSFilterApi
        appbuilder.add_api(DatasetCLSFilterApi)
        from superset.v2.datasets.data_masking.api import DataMaskingApi
        appbuilder.add_api(DataMaskingApi)
        from superset.v2.log.api import LogV2RestApi
        appbuilder.add_api(LogV2RestApi)
        from superset.v2.water_mark.api import WaterMarkV2RestApi
        appbuilder.add_api(WaterMarkV2RestApi)

        from superset.sys_manager.dept.api import SysDeptRestApi
        appbuilder.add_api(SysDeptRestApi)
        from superset.sys_manager.permission.api import SysAuthRestApi
        appbuilder.add_api(SysAuthRestApi)
        from superset.sys_manager.menus.api import SysMenuRestApi
        appbuilder.add_api(SysMenuRestApi)
        from superset.v2.login.api import LoginRestApi
        appbuilder.add_api(LoginRestApi)

        from superset.v2.database_sync.group.api import DatabaseSyncGroupRestApi
        appbuilder.add_api(DatabaseSyncGroupRestApi)

        from superset.v2.database_sync.api import DataBaseSyncRestApi
        appbuilder.add_api(DataBaseSyncRestApi)

        from superset.v2.database_sync.database_sync_task.api import DatabaseSyncTaskRestApi
        appbuilder.add_api(DatabaseSyncTaskRestApi)

        from superset.v2.database_sync.database.api import DataSourcesDatabaseSyncRestApi
        appbuilder.add_api(DataSourcesDatabaseSyncRestApi)




        #
        # Setup regular views
        #
        appbuilder.add_link(
            "Home",
            label=__("Home"),
            href=self.config["STATIC_ASSETS_PREFIX"] + "/superset/welcome/",
            cond=lambda: bool(appbuilder.app.config["LOGO_TARGET_PATH"]),
        )

        appbuilder.add_view(
            DatabaseView,
            "Databases",
            label=__("Database Connections"),
            icon="fa-database",
            category="Data",
            category_label=__("Data"),
        )

        # # 设置 -> 数据 -> api连接
        # appbuilder.add_link(
        #     "Databases",
        #     label=__("API Connection"),
        #     href=self.config["STATIC_ASSETS_PREFIX"] + "/apiconnection/",
        #     icon="fa-database",
        #     category="Data",
        #     category_label=__("Data"),
        # )
        # 设置 -> 对外API -> 应用管理
        appbuilder.add_view(
            AppAttributeModelView,
            "Application management",
            label=__("Application management"),
            icon="",
            category="External API",
            category_label=__("External API"),
        )

        # 数据库同步
        appbuilder.add_view(
            DatabaseSyncModelView,
            "Database Sync",
            label=__("Database Sync"),
            icon="",
            category="",
            category_label="",
        )

        appbuilder.add_view(
            DashboardModelView,
            "Dashboards",
            label=__("Dashboards"),
            icon="fa-dashboard",
            category="",
            category_icon="",
        )
        appbuilder.add_view(
            SliceModelView,
            "Charts",
            label=__("Charts"),
            icon="fa-bar-chart",
            category="",
            category_icon="",
        )
        appbuilder.add_view(
            RecordModelView,
            "Records",
            label=__("Records"),
            icon="fa-bar-record",
            category="",
            category_icon="",
        )

        appbuilder.add_link(
            "Datasets",
            label=__("Datasets"),
            href="/tablemodelview/list/",
            icon="fa-table",
            category="",
            category_icon="",
        )

        appbuilder.add_view(
            DynamicPluginsView,
            "Plugins",
            label=__("Plugins"),
            category="Manage",
            category_label=__("Manage"),
            icon="fa-puzzle-piece",
            menu_cond=lambda: feature_flag_manager.is_feature_enabled(
                "DYNAMIC_PLUGINS"
            ),
        )
        appbuilder.add_view(
            CssTemplateModelView,
            "CSS Templates",
            label=__("CSS Templates"),
            icon="fa-css3",
            category="Manage",
            category_label=__("Manage"),
            category_icon="",
        )
        appbuilder.add_view(
            RowLevelSecurityFiltersModelView,
            "Row Level Security",
            label=__("Row Level Security"),
            category="Security",
            category_label=__("Security"),
            icon="fa-lock",
        )
        appbuilder.add_view(
            UserJobInfoFiltersModelView,
            "User Job Info Filters",
            label=__("User Job Info Filters"),
            category="Security",
            icon="fa-comment",
            category_label=__("Security"),
            category_icon="",
            menu_cond=lambda: feature_flag_manager.is_feature_enabled(
                "ROW_LEVEL_SECURITY"
            ),
        )

        #
        # Setup views with no menu
        #



        appbuilder.add_view_no_menu(Api)
        appbuilder.add_view_no_menu(CssTemplateAsyncModelView)
        appbuilder.add_view_no_menu(CsvToDatabaseView)
        appbuilder.add_view_no_menu(ExcelToDatabaseView)
        appbuilder.add_view_no_menu(ColumnarToDatabaseView)
        appbuilder.add_view_no_menu(Dashboard)
        appbuilder.add_view_no_menu(DashboardModelViewAsync)
        appbuilder.add_view_no_menu(Datasource)
        appbuilder.add_view_no_menu(DatasetEditor)
        appbuilder.add_view_no_menu(EmbeddedView)
        appbuilder.add_view_no_menu(ExploreView)
        appbuilder.add_view_no_menu(ExplorePermalinkView)
        appbuilder.add_view_no_menu(KV)
        appbuilder.add_view_no_menu(R)
        appbuilder.add_view_no_menu(SavedQueryView)
        appbuilder.add_view_no_menu(SavedQueryViewApi)
        appbuilder.add_view_no_menu(SliceAsync)
        appbuilder.add_view_no_menu(SqlLab)
        appbuilder.add_view_no_menu(SqlMetricInlineView)
        appbuilder.add_view_no_menu(Superset)
        appbuilder.add_view_no_menu(TableColumnInlineView)
        appbuilder.add_view_no_menu(TableModelView)
        appbuilder.add_view_no_menu(TableSchemaView)
        appbuilder.add_view_no_menu(TabStateView)
        appbuilder.add_view_no_menu(TagView)
        appbuilder.add_view_no_menu(ReportView)

        #
        # Add links
        #
        appbuilder.add_link(
            "Import Dashboards",
            label=__("Import Dashboards"),
            href=self.config["STATIC_ASSETS_PREFIX"] + "/superset/import_dashboards/",
            icon="fa-cloud-upload",
            category="Manage",
            category_label=__("Manage"),
            category_icon="fa-wrench",
            cond=lambda: not feature_flag_manager.is_feature_enabled(
                "VERSIONED_EXPORT"
            ),
        )
        appbuilder.add_link(
            "SQL Editor",
            label=__("SQL Lab"),
            href=self.config["STATIC_ASSETS_PREFIX"] + "/superset/sqllab/",
            category_icon="fa-flask",
            icon="fa-flask",
            category="SQL Lab",
            category_label=__("SQL"),
        )
        appbuilder.add_link(
            "Saved Queries",
            label=__("Saved Queries"),
            href=self.config["STATIC_ASSETS_PREFIX"] + "/savedqueryview/list/",
            icon="fa-save",
            category="SQL Lab",
            category_label=__("SQL"),
        )
        appbuilder.add_link(
            "Query Search",
            label=__("Query History"),
            href=self.config["STATIC_ASSETS_PREFIX"] + "/superset/sqllab/history/",
            icon="fa-search",
            category_icon="fa-flask",
            category="SQL Lab",
            category_label=__("SQL"),
        )

        appbuilder.add_api(LogRestApi)
        appbuilder.add_view(
            LogModelView,
            "Action Log",
            label=__("Action Log"),
            category="Security",
            category_label=__("Security"),
            icon="fa-list-ol",
            menu_cond=lambda: (
                self.config["FAB_ADD_SECURITY_VIEWS"]
                and self.config["SUPERSET_LOG_VIEW"]
            ),
        )
        appbuilder.add_api(SecurityRestApi)
        #
        # Conditionally setup email views
        #

        appbuilder.add_view(
            AlertView,
            "Alerts & Report",
            label=__("Alerts & Reports"),
            category="Manage",
            category_label=__("Manage"),
            icon="fa-exclamation-triangle",
            menu_cond=lambda: feature_flag_manager.is_feature_enabled("ALERT_REPORTS"),
        )

        appbuilder.add_view(
            AnnotationLayerView,
            "Annotation Layers",
            label=__("Annotation Layers"),
            href=self.config["STATIC_ASSETS_PREFIX"] + "/annotationlayer/list/",
            icon="fa-comment",
            category_icon="",
            category="Manage",
            category_label=__("Manage"),
        )

        appbuilder.add_view(
            AccessRequestsModelView,
            "Access requests",
            label=__("Access requests"),
            category="Security",
            category_label=__("Security"),
            icon="fa-table",
            menu_cond=lambda: bool(self.config["ENABLE_ACCESS_REQUEST"]),
        )

        from superset.v2.views.datasets.views import DatasetBaseView
        appbuilder.add_view(
            DatasetBaseView,
            "Dataset",
            label=__("Dataset"),
            icon="fa-table",
            category="",
            category_icon="",
        )

        from superset.v2.views.sys_manager.views import SysManagerBaseView
        appbuilder.add_view(
            SysManagerBaseView,
            "System Manager",
            label=__("System Manager"),
            icon="fa-dashboard",
            category="",
            category_icon="",
        )

    def init_app_in_ctx(self) -> None:
        """
        Runs init logic in the context of the app
        """
        self.configure_fab()
        self.configure_url_map_converters()
        self.configure_data_sources()
        self.configure_auth_provider()
        self.configure_async_queries()
        self.configure_ssh_manager()
        self.configure_stats_manager()

        # Hook that provides administrators a handle on the Flask APP
        # after initialization
        flask_app_mutator = self.config["FLASK_APP_MUTATOR"]
        if flask_app_mutator:
            flask_app_mutator(self.superset_app)

        if feature_flag_manager.is_feature_enabled("TAGGING_SYSTEM"):
            register_sqla_event_listeners()

        self.init_views()

    def check_secret_key(self) -> None:
        def log_default_secret_key_warning() -> None:
            top_banner = 80 * "-" + "\n" + 36 * " " + "WARNING\n" + 80 * "-"
            bottom_banner = 80 * "-" + "\n" + 80 * "-"
            logger.warning(top_banner)
            logger.warning(
                "A Default SECRET_KEY was detected, please use superset_config.py "
                "to override it.\n"
                "Use a strong complex alphanumeric string and use a tool to help"
                " you generate \n"
                "a sufficiently random sequence, ex: openssl rand -base64 42"
            )
            logger.warning(bottom_banner)

        if self.config["SECRET_KEY"] == CHANGE_ME_SECRET_KEY:
            if (
                self.superset_app.debug
                or self.superset_app.config["TESTING"]
                or is_test()
            ):
                logger.warning("Debug mode identified with default secret key")
                log_default_secret_key_warning()
                return
            log_default_secret_key_warning()
            logger.error("Refusing to start due to insecure SECRET_KEY")
            sys.exit(1)

    def init_app(self) -> None:
        """
        Main entry point which will delegate to other methods in
        order to fully init the app
        """
        self.pre_init()
        # 临时注释：密钥检查
        # self.check_secret_key()
        # Configuration of logging must be done first to apply the formatter properly
        self.configure_logging()
        # Configuration of feature_flags must be done first to allow init features
        # conditionally
        self.configure_feature_flags()
        self.configure_db_encrypt()
        self.setup_db()
        self.configure_celery()
        self.enable_profiling()
        self.setup_event_logger()
        self.setup_bundle_manifest()
        self.register_blueprints()
        self.configure_wtf()
        self.configure_middlewares()
        self.configure_cache()

        with self.superset_app.app_context():
            self.init_app_in_ctx()
            # db.create_all()

        self.post_init()

    def configure_auth_provider(self) -> None:
        machine_auth_provider_factory.init_app(self.superset_app)

    def configure_ssh_manager(self) -> None:
        ssh_manager_factory.init_app(self.superset_app)

    def configure_stats_manager(self) -> None:
        stats_logger_manager.init_app(self.superset_app)

    def setup_event_logger(self) -> None:
        _event_logger["event_logger"] = get_event_logger_from_cfg_value(
            self.superset_app.config.get("EVENT_LOGGER", DBEventLogger())
        )

    def configure_data_sources(self) -> None:
        # Registering sources
        module_datasource_map = self.config["DEFAULT_MODULE_DS_MAP"]
        module_datasource_map.update(self.config["ADDITIONAL_MODULE_DS_MAP"])

        # todo(hughhhh): fully remove the datasource config register
        for module_name, class_names in module_datasource_map.items():
            class_names = [str(s) for s in class_names]
            __import__(module_name, fromlist=class_names)

    def configure_cache(self) -> None:
        cache_manager.init_app(self.superset_app)
        results_backend_manager.init_app(self.superset_app)

    def configure_feature_flags(self) -> None:
        feature_flag_manager.init_app(self.superset_app)

    def configure_fab(self) -> None:
        if self.config["SILENCE_FAB"]:
            logging.getLogger("flask_appbuilder").setLevel(logging.ERROR)

        custom_sm = self.config["CUSTOM_SECURITY_MANAGER"] or SupersetSecurityManager
        if not issubclass(custom_sm, SupersetSecurityManager):
            raise CustomSecurityManagerError(
                """Your CUSTOM_SECURITY_MANAGER must now extend SupersetSecurityManager,
                 not FAB's security manager.
                 See [4565] in UPDATING.md"""
            )

        appbuilder.indexview = SupersetIndexView
        appbuilder.base_template = "superset/base.html"
        appbuilder.security_manager_class = custom_sm
        appbuilder.menu = CustomMenu()
        appbuilder.init_app(self.superset_app, db.session)

    def configure_url_map_converters(self) -> None:
        #
        # Doing local imports here as model importing causes a reference to
        # app.config to be invoked and we need the current_app to have been setup
        #
        # pylint: disable=import-outside-toplevel
        from superset.utils.url_map_converters import (
            ObjectTypeConverter,
            RegexConverter,
        )

        self.superset_app.url_map.converters["regex"] = RegexConverter
        self.superset_app.url_map.converters["object_type"] = ObjectTypeConverter

    def configure_middlewares(self) -> None:
        if self.config["ENABLE_CORS"]:
            # pylint: disable=import-outside-toplevel
            from flask_cors import CORS

            CORS(self.superset_app, **self.config["CORS_OPTIONS"])

        if self.config["ENABLE_PROXY_FIX"]:
            self.superset_app.wsgi_app = ProxyFix(  # type: ignore
                self.superset_app.wsgi_app, **self.config["PROXY_FIX_CONFIG"]
            )

        if self.config["ENABLE_CHUNK_ENCODING"]:

            class ChunkedEncodingFix:  # pylint: disable=too-few-public-methods
                def __init__(self, app: Flask) -> None:
                    self.app = app

                def __call__(
                    self, environ: Dict[str, Any], start_response: Callable[..., Any]
                ) -> Any:
                    # Setting wsgi.input_terminated tells werkzeug.wsgi to ignore
                    # content-length and read the stream till the end.
                    if environ.get("HTTP_TRANSFER_ENCODING", "").lower() == "chunked":
                        environ["wsgi.input_terminated"] = True
                    return self.app(environ, start_response)

            self.superset_app.wsgi_app = ChunkedEncodingFix(  # type: ignore
                self.superset_app.wsgi_app  # type: ignore
            )

        if self.config["UPLOAD_FOLDER"]:
            try:
                os.makedirs(self.config["UPLOAD_FOLDER"])
            except OSError:
                pass

        for middleware in self.config["ADDITIONAL_MIDDLEWARE"]:
            self.superset_app.wsgi_app = middleware(  # type: ignore
                self.superset_app.wsgi_app
            )

        # Flask-Compress
        Compress(self.superset_app)

        # Talisman
        talisman_enabled = self.config["TALISMAN_ENABLED"]
        talisman_config = self.config["TALISMAN_CONFIG"]
        csp_warning = self.config["CONTENT_SECURITY_POLICY_WARNING"]

        if talisman_enabled:
            talisman.init_app(self.superset_app, **talisman_config)

        show_csp_warning = False
        if (
            csp_warning
            and not self.superset_app.debug
            and (
                not talisman_enabled
                or not talisman_config
                or not talisman_config.get("content_security_policy")
            )
        ):
            show_csp_warning = True

        if show_csp_warning:
            logger.warning(
                "We haven't found any Content Security Policy (CSP) defined in "
                "the configurations. Please make sure to configure CSP using the "
                "TALISMAN_ENABLED and TALISMAN_CONFIG keys or any other external "
                "software. Failing to configure CSP have serious security implications. "
                "Check https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP for more "
                "information. You can disable this warning using the "
                "CONTENT_SECURITY_POLICY_WARNING key."
            )

    def configure_logging(self) -> None:
        self.config["LOGGING_CONFIGURATOR"].configure_logging(
            self.config, self.superset_app.debug
        )

    def configure_db_encrypt(self) -> None:
        encrypted_field_factory.init_app(self.superset_app)

    def setup_db(self) -> None:
        db.init_app(self.superset_app)

        with self.superset_app.app_context():
            pessimistic_connection_handling(db.engine)

        migrate.init_app(self.superset_app, db=db, directory=APP_DIR + "/migrations")

    def configure_wtf(self) -> None:
        if self.config["WTF_CSRF_ENABLED"]:
            csrf.init_app(self.superset_app)
            csrf_exempt_list = self.config["WTF_CSRF_EXEMPT_LIST"]
            for ex in csrf_exempt_list:
                csrf.exempt(ex)

    def configure_async_queries(self) -> None:
        if feature_flag_manager.is_feature_enabled("GLOBAL_ASYNC_QUERIES"):
            async_query_manager.init_app(self.superset_app)

    def register_blueprints(self) -> None:
        for bp in self.config["BLUEPRINTS"]:
            try:
                logger.info("Registering blueprint: %s", bp.name)
                self.superset_app.register_blueprint(bp)
            except Exception:  # pylint: disable=broad-except
                logger.exception("blueprint registration failed")

    def setup_bundle_manifest(self) -> None:
        manifest_processor.init_app(self.superset_app)

    def enable_profiling(self) -> None:
        if self.config["PROFILING"]:
            profiling.init_app(self.superset_app)


class SupersetIndexView(IndexView):
    @expose("/")
    def index(self) -> FlaskResponse:
        return redirect(self.appbuilder.app.config["STATIC_ASSETS_PREFIX"] +
                        "/superset/welcome/")
