import json
import logging

from typing import Any

import prison
from flask import Response, request
from flask_appbuilder import permission_name
from flask_appbuilder.api import expose, protect, safe, ModelKeyType, rison, get_list_schema, get_item_schema
from flask_appbuilder.const import API_URI_RIS_KEY
from flask_appbuilder.models.sqla.interface import SQLAInterface

from superset.app_attributes.filters import SearchTaskTextFilter
from superset.database_sync.utils.redis_queue import RedisQueue

from superset.extensions import event_logger, db
from superset.models.database_sync import DatabaseSyncTask, DatabaseSyncTaskLogs

from superset.views.base_api import (
    statsd_metrics, BaseSupersetModelRestApi,
)

logger = logging.getLogger(__name__)


class DatabaseSyncTaskRestApi(BaseSupersetModelRestApi):
    version = "v2"
    datamodel = SQLAInterface(DatabaseSyncTask)
    resource_name = "database_sync_task"
    allow_browser_login = True
    show_columns = [
        "id",
        "uuid",
        "task_name",
        "task_code",
        "execute_type",
        "execute_status",
        "is_active",
        "source_name",
        "source_database_type",
        "source_database_name",
        "source_database_table_name",
        "source_dbs_id",
        "target_name",
        "target_database_type",
        "target_database_name",
        "target_database_table_name",
        "cron_expression",
        "cron_start_time",
        "cron_end_time",
        "database_sync_id",
        "update_type",
        "row_range_type",
        "row_range_data",
        "row_range_data_list",
        "column_range_data",
        "column_range_type"
    ]
    list_columns = [
        "id",
        "uuid",
        "task_name",
        "task_code",
        "execute_type",
        "execute_status",
        "is_active",
        "source_name",
        "source_database_type",
        "source_database_name",
        "source_database_table_name",
        "source_dbs_id",
        "target_name",
        "target_database_type",
        "target_database_name",
        "target_database_table_name",
        "cron_expression",
        "cron_start_time",
        "cron_end_time",
        "database_sync_id",
        "update_type",
        "row_range_type",
        "row_range_data",
        "row_range_data_list",
        "column_range_data",
        "column_range_type"
    ]
    add_columns = [
        "task_name",
        "task_code",
        "is_active",
        "update_type",
        "execute_type",
        "source_name",
        "source_database_type",
        "source_database_name",
        "source_database_table_name",
        "target_database_type",
        "target_database_name",
        "target_database_table_name",
        "source_dbs_id",
        "cron_expression",
        "cron_start_time",
        "cron_end_time",
        "database_sync_id",
        "row_range_type",
        "row_range_data",
        "row_range_data_list",
        "column_range_data",
        "column_range_type"
    ]
    search_columns = [
        "id",
        "task_name",
        "task_code",
        "execute_type",
        "execute_status",
        "is_active",
        "source_name",
        "source_database_type",
        "source_database_name",
        "source_database_table_name",
        "source_dbs_id",
        "target_name",
        "target_database_type",
        "target_database_name",
        "target_database_table_name",
        "cron_expression",
        "cron_start_time",
        "cron_end_time",
        "database_sync_id",
        "row_range_type",
        "row_range_data",
        "column_range_data",
        "column_range_type"

    ]
    search_filters = {"task_name": [SearchTaskTextFilter]}
    edit_columns = add_columns

    @expose("/", methods=["GET"])
    @protect()
    @safe
    @permission_name("get")
    @rison(get_list_schema)
    def get_list(self, **kwargs: Any) -> Response:
        """Get list of items from Model
        ---
        get:
          description: >-
            Get a list of models
          parameters:
          - in: query
            name: q
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/get_list_schema'
          responses:
            200:
              description: Items from Model
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      label_columns:
                        type: object
                        properties:
                          column_name:
                            description: >-
                              The label for the column name.
                              Will be translated by babel
                            example: A Nice label for the column
                            type: string
                      list_columns:
                        description: >-
                          A list of columns
                        type: array
                        items:
                          type: string
                      description_columns:
                        type: object
                        properties:
                          column_name:
                            description: >-
                              The description for the column name.
                              Will be translated by babel
                            example: A Nice description for the column
                            type: string
                      list_title:
                        description: >-
                          A title to render.
                          Will be translated by babel
                        example: List Items
                        type: string
                      ids:
                        description: >-
                          A list of item ids, useful when you don't know the column id
                        type: array
                        items:
                          type: string
                      count:
                        description: >-
                          The total record count on the backend
                        type: number
                      order_columns:
                        description: >-
                          A list of allowed columns to sort
                        type: array
                        items:
                          type: string
                      result:
                        description: >-
                          The result from the get list query
                        type: array
                        items:
                          $ref: '#/components/schemas/{{self.__class__.__name__}}.get_list'  # noqa
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        response_data = self.get_list_headless(**kwargs).get_data()
        response_json = json.loads(response_data)

        for i in response_json["result"]:
            log_models = DatabaseSyncTask.get_log_model_by_id(i["id"])
            if log_models and (log_models := log_models.to_json()):
                i["task_log"] = log_models.get("task_log")
                i["task_start_time"] = log_models.get("task_start_time")
                i["task_end_time"] = log_models.get("task_end_time")
                i["database_sync_task_id"] = log_models.get("database_sync_task_id")
                i["execute_result"] = log_models.get("execute_result")

        return self.response(200, **response_json)

    @expose("/<int:pk>", methods=["GET"])
    @protect()
    @safe
    @permission_name("get")
    @rison(get_item_schema)
    def get(self, pk: ModelKeyType, **kwargs: Any) -> Response:
        """Get data for a specific ID
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
              description: The data corresponding to the given ID
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: The ID of the data
                      result:
                        type: array
                        items:
                          $ref: '#/components/schemas/ResultSchema'
          """
        response_data = self.get_headless(pk, **kwargs).get_data()
        response_json = json.loads(response_data)
        id = response_json["id"]
        result = [response_json["result"]]
        data = {"id": id, "result": result}

        return Response(json.dumps(data), mimetype="application/json")

    @expose("/", methods=["POST"])
    @protect()
    @safe
    @permission_name("post")
    def post(self) -> Response:
        """Add new data
        ---
        post:
          responses:
            200:
              description: The result of adding new data
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/ResultSchema'
          """
        response = self.post_headless()
        response_data = response.get_data()
        response_json = json.loads(response_data)
        id_value = response_json.get("id")
        if id_value:
            # 立即执行任务
            redis_client = RedisQueue()
            if response_json.get("result").get("execute_type") == "immediately":
                redis_client.put(
                    json.dumps(
                        {
                            "execute_type": "immediately",
                            "task_id": id_value,
                        }
                    )
                )

            # 定时执行任务
            else:
                redis_client.put(
                    json.dumps(
                        {
                            "execute_type": "add",
                            "task_id": id_value,
                        }
                    )
                )
        response_json["code"] = 200
        return Response(json.dumps(response_json), mimetype="application/json")

    @expose("/<pk>", methods=["DELETE"])
    @protect()
    @safe
    @permission_name("delete")
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.delete",
        log_to_statsd=False,
    )
    def delete(self, pk: ModelKeyType) -> Response:
        """Delete data for a specific ID
        ---
        delete:
          parameters:
            - in: path
              name: pk
              schema:
                type: integer
              required: true
              description: The ID value
          responses:
            200:
              description: The deletion was successful
          """

        DatabaseSyncTaskLogs.delete_data_by_field(pk)

        response_data = self.get_headless(pk).get_data()
        response_json = json.loads(response_data)
        id_value = response_json["id"]
        redis_client = RedisQueue()
        redis_client.put(
            json.dumps(
                {
                    "execute_type": "del",
                    "task_id": id_value,
                }
            )
        )
        return self.delete_headless(pk)

    @expose("/<pk>", methods=["PUT"])
    @protect()
    @safe
    @permission_name("put")
    def put(self, pk: ModelKeyType) -> Response:
        """Update data for a specific ID
        ---
        put:
          parameters:
            - in: path
              name: pk
              schema:
                type: integer
              required: true
              description: The ID value
          responses:
            200:
              description: The update was successful
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/ResultSchema'
        """
        response_data = self.get_headless(pk).get_data()
        response_json = json.loads(response_data)
        id_value = response_json["id"]
        redis_client = RedisQueue()
        redis_client.put(
            json.dumps(
                {
                    "execute_type": "edit",
                    "task_id": id_value,
                }
            )
        )
        return self.put_headless(pk)

    @expose(url="/execute/", methods=("POST",))
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.post",
        log_to_statsd=False,
    )
    def execute(self) -> Response:
        """Execute a task
        ---
        post:
          responses:
            200:
              description: The task execution was successful
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/ExecutionResult'
            400:
              description: There was an error executing the task
              content:
                text/plain:
                  schema:
                    type: string
          """
        request_data = request.get_json()  # 获取请求的JSON数据
        id_param = request_data.get('id')  # 获取参数中的id值
        if id_param is None:
            return Response("参数id不存在", status=400)

        id_param = int(id_param)
        # 查询数据库中所有的id值
        ids_models = db.session.query(DatabaseSyncTask.id).where(
            DatabaseSyncTask.id == id_param).one()
        # 检查参数id是否在数据库id列表中
        if ids_models:
            redis_client = RedisQueue()
            redis_client.put(
                json.dumps(
                    {
                        "execute_type": "immediately",
                        "task_id": id_param,
                    }
                )
            )

            return self.response(200, result={
                "status": 200,
                "message": "Execution succeeded!"
            })

        # 返回响应
        return self.response(400, result={
            "status": 400,
            "message": f"The parameter id [{id_param}] does not exist in the database."
        })

    @expose("/logs/<int:pk>", methods=("GET",))
    @protect()
    @safe
    @permission_name("get_task_logs")
    def get_task_logs(self, pk, **kwargs: Any) -> Response:
        kwargs["rison"] = dict()
        value = request.args.get(API_URI_RIS_KEY, None)

        if value:
            kwargs["rison"] = prison.loads(value)

        prison.loads(value)
        query = db.session.query(
            DatabaseSyncTaskLogs,
        ).filter(
            DatabaseSyncTaskLogs.database_sync_task_id == pk
        ).order_by(
            DatabaseSyncTaskLogs.task_start_time.desc()
        )

        page_size = kwargs.get("rison", {}).get("page_size", 10)
        page = kwargs.get("rison", {}).get("page", 1) or 1

        results = query.limit(page_size).offset((page - 1) * page_size)
        response_json = {
            "total_count": query.count(),
            "results": [result.to_json() for result in results]
        }
        return self.response(200, **response_json)
