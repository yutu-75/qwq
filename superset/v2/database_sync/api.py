import json
import logging
import threading
from typing import Any

from flask import Response, request
from flask_appbuilder import permission_name
from flask_appbuilder.api import expose, protect, safe, ModelKeyType, rison, \
    merge_response_func, get_list_schema, get_item_schema
from flask_appbuilder.const import API_LIST_TITLE_RIS_KEY, API_ORDER_COLUMNS_RIS_KEY, \
    API_LABEL_COLUMNS_RIS_KEY, API_DESCRIPTION_COLUMNS_RIS_KEY, \
    API_LIST_COLUMNS_RIS_KEY, API_SHOW_COLUMNS_RIS_KEY, API_SHOW_TITLE_RIS_KEY
from flask_appbuilder.models.sqla.interface import SQLAInterface

from superset.app_attributes.filters import SearchSyncTextFilter
from superset.database_sync.utils.redis_queue import RedisQueue

from superset.extensions import event_logger, db
from superset.logs_messages import LogsMessages
from superset.models.database_sync import DatabaseSyncTask, DatabaseSync
from superset.utils.decorators import authenticated
from superset.views.base_api import (
    statsd_metrics, BaseSupersetModelRestApi,
)

logger = logging.getLogger(__name__)


class DataBaseSyncRestApi(BaseSupersetModelRestApi):
    version = "v2"
    datamodel = SQLAInterface(DatabaseSync)
    resource_name = "database_sync"
    allow_browser_login = True
    show_columns = [
        "id",
        "uuid",
        "name",
        "database_id",
        "database_type",
        "desc",
        "group_id",
    ]
    list_columns = [
        "id",
        "uuid",
        "name",
        "database_id",
        "database_type",
        "desc",
        "group_id",
    ]
    add_columns = [
        "id",
        "name",
        "database_id",
        "database_type",
        "desc",
        "group_id",
    ]
    search_columns = [
        "id",
        "name",
        "database_id",
        "database_type",
        "desc",
        "group_id",

    ]
    search_filters = {"name": [SearchSyncTextFilter]}
    edit_columns = add_columns

    @expose("/<int:pk>", methods=["GET"])
    @protect()
    @safe
    @permission_name("get")
    @rison(get_item_schema)
    # @merge_response_func(merge_show_label_columns, API_LABEL_COLUMNS_RIS_KEY)
    # @merge_response_func(merge_show_columns, API_SHOW_COLUMNS_RIS_KEY)
    # @merge_response_func(merge_description_columns, API_DESCRIPTION_COLUMNS_RIS_KEY)
    # @merge_response_func(merge_show_title, API_SHOW_TITLE_RIS_KEY)
    def get(self, pk: ModelKeyType, **kwargs: Any) -> Response:
        """
                获取指定ID的数据
                ---
                get:
                  parameters:
                    - in: path
                      name: pk
                      schema:
                        type: integer
                      required: true
                      description: The ID value
                  responses:
                    200:
                      description: Successful operation
                      content:
                        application/json:
                          schema:
                            $ref: '#/components/schemas/GetApiResponse'
                """
        response_data = self.get_headless(pk, **kwargs).get_data()

        response_json = json.loads(response_data)
        datasource_query = db.session.query(DatabaseSyncTask).filter(
            DatabaseSyncTask.database_sync_id == pk,
        ).all()

        response_json["result"]["database_sync_task"] = [i.to_json() for i in datasource_query]

        id = response_json["id"]
        result = [response_json["result"]]
        data = {"id": id, "result": result}
        return self.response(200, result=data)
        # return Response(json.dumps(data), mimetype="application/json")
