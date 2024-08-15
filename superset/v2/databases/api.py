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

import logging

from flask import g, Response, request
from flask_appbuilder.api import expose, rison, safe
from typing import Any

from superset import event_logger
from superset.databases.commands.exceptions import (
    DatabaseNotFoundError,
    DatabaseTablesUnexpectedError,
)
from superset.databases.schemas import database_tables_query_schema
from superset.exceptions import SupersetException
from superset.superset_typing import FlaskResponse
from superset.utils.decorators import authenticated
from superset.v2.databases.commands.get_data_command import DatabaseListDataCommand
from superset.v2.databases.commands.tables import TablesDatabaseCommand
from superset.views.base_api import (
    statsd_metrics, BaseSupersetBaseApi
)

logger = logging.getLogger(__name__)


class DatabaseV2RestApi(BaseSupersetBaseApi):
    resource_name = "database"

    @expose(url="/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def databases(self) -> Response:
        """Response
        查询用户有权查看的数据库.
        ---
        get:
          parameters:
          - in: query
            name: name
            description: 查询以name开头的数据源
            schema:
              type: string
          responses:
            200:
              $ref: '#/components/responses/200'
        """
        data = DatabaseListDataCommand(g.user).run(**request.args)
        return self.format_response(200, data=data)

    @expose("/<int:pk>/tables/")
    @authenticated()
    @safe
    @rison(database_tables_query_schema)
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}" f".tables",
        log_to_statsd=False,
    )
    def tables(self, pk: int, **kwargs: Any) -> FlaskResponse:
        """Get a list of tables for given database
        ---
        get:
          summary: Get a list of tables for given database
          parameters:
          - in: path
            schema:
              type: integer
            name: pk
            description: The database id
          - in: query
            name: q
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/database_tables_query_schema'
          responses:
            200:
              description: Tables list
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      count:
                        type: integer
                      result:
                        description: >-
                          A List of tables for given database
                        type: array
                        items:
                          $ref: '#/components/schemas/DatabaseTablesResponse'
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            422:
              $ref: '#/components/responses/422'
            500:
              $ref: '#/components/responses/500'
        """
        force = kwargs["rison"].get("force", False)
        schema_name = kwargs["rison"].get("schema_name", "")

        try:
            command = TablesDatabaseCommand(g.user, pk, schema_name, force)
            payload = command.run(**request.args)
            return self.response(200, **payload)
        except DatabaseNotFoundError:
            return self.response_404()
        except SupersetException as ex:
            return self.response(ex.status, message=ex.message)
        except DatabaseTablesUnexpectedError as ex:
            return self.response_422(ex.message)
