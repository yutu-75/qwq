from flask import Response, g, request
from flask_appbuilder.api import expose

from superset import event_logger
from superset.logs_messages import LogsMessages
from superset.utils.decorators import authenticated
from superset.v2.database_sync.commands.create import DatabaseSyncName
from superset.v2.database_sync.commands.delete import \
    DeleteDatabaseSyncCommand
from superset.v2.database_sync.commands.eclect_create_list import \
    GetDatabase
from superset.v2.database_sync.commands.move import MoveDataBaseNameCommand

from superset.v2.database_sync.schemas import DatabaseSyncPatchSchema, \
    DatabaseSyncDataSourcePostSchema, \
    TableFieldsPatchSchema, TableFieldsValueGroupPySchema

from superset.v2.datasources.schemas import DataSourcePatchSchema
from superset.views.base_api import statsd_metrics, requires_json, BaseSupersetBaseApi


class DataSourcesDatabaseSyncRestApi(BaseSupersetBaseApi):
    resource_name = "database_sync/database"
    openapi_spec_component_schemas = (
        DatabaseSyncDataSourcePostSchema,
    )

    # 展示可选数据源
    @expose(url="/elect/", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def list_elect_name(self) -> Response:
        """展示可选数据源
        ---
        get:
          description: >-
            展示可选数据源
          responses:
            200:
              description: The current user
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/UserResponseSchema'
            401:
              $ref: '#/components/responses/401'
        """
        data = GetDatabase(g.user).run()
        return self.format_response(200, data=data)

    # 展示可选数据源
    @expose(url="/elect/<int:dbs_id>", methods=("GET",))
    @authenticated()
    @statsd_metrics
    def list_elect(self, dbs_id: int) -> Response:
        """Get data for a specific database ID
        ---
        get:
          description: >-
            Get data for a specific database ID.
            Requires authentication.
            Returns the database data corresponding to the given ID.
          parameters:
            - in: path
              name: dbs_id
              schema:
                type: integer
              required: true
              description: The ID of the database
          responses:
            200:
              description: The database data
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/DatabaseDataResponseSchema'
            401:
              $ref: '#/components/responses/401'
        """
        data = GetDatabase(g.user).get_database_data(dbs_id)
        return self.format_response(200, data=data)

    @expose(url="/elect/table_fields/", methods=("GET",))
    @authenticated()
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DATABASE_NAME_SYNC_GROUP,
        log_to_statsd=False,
    )
    @statsd_metrics
    def list_elect_table_fields(self) -> Response:
        """Get table fields for database
        ---
        get:
          description: >-
            Get table fields for a database.
            Requires authentication.
            Expects query parameters for specifying the database and other options.
          parameters:
            - in: query
              name: database_id
              schema:
                type: integer
              required: true
              description: The ID of the database
            # Add more query parameters as needed

          responses:
            200:
              description: The database table fields
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/DatabaseTableFieldsResponseSchema'
            401:
              $ref: '#/components/responses/401'
        """
        item = TableFieldsPatchSchema().load(request.args)
        data = GetDatabase(g.user).get_database_table_fields(item)
        return self.response(200, data=data)


    @expose(url="/elect/table_fields_value_group_by/", methods=("GET",))
    @authenticated()
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DATABASE_NAME_SYNC_GROUP,
        log_to_statsd=False,
    )
    @statsd_metrics
    def table_fields_value_group_by(self) -> Response:
        """Get table fields for database
        ---
        get:
          description: >-
            Get table fields for a database.
            Requires authentication.
            Expects query parameters for specifying the database and other options.
          parameters:
            - in: query
              name: database_id
              schema:
                type: integer
              required: true
              description: The ID of the database
            # Add more query parameters as needed

          responses:
            200:
              description: The database table fields
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/DatabaseTableFieldsResponseSchema'
            401:
              $ref: '#/components/responses/401'
        """
        item = TableFieldsValueGroupPySchema().load(request.args)
        data = GetDatabase(g.user).get_field_value_data(item)
        return self.response(200, data=data)

    # 新增数据源
    @expose(url="/", methods=("POST",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_ADD_DATABASE_NAME_SYNC_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def post_name(self) -> Response:
        """Add a database name for synchronization
        ---
        post:
          description: >-
            Add a database name for synchronization.
            Requires authentication.
            Expects a JSON payload with the database name.
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DatabaseSyncDataSourcePostSchema'
          responses:
            200:
              description: The synchronized database
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/DatabaseSyncNameResponseSchema'
            401:
              $ref: '#/components/responses/401'
        """
        item = DatabaseSyncDataSourcePostSchema().load(request.json)
        database_sync = DatabaseSyncName(g.user, item).run()
        return self.format_response(200, data=database_sync.to_json())

    @expose(url="/<int:database_sync_id>/", methods=("PATCH",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_MOVE_DATABASE_NAME_SYNC_GROUP,
        log_to_statsd=False,
    )
    @requires_json
    def put(self, database_sync_id: int) -> Response:
        """Move a database name synchronization group
        ---
        patch:
          description: >-
            Move a database name synchronization group.
            Requires authentication.
            Moves the synchronization group with the given ID to a new location.
          parameters:
            - in: path
              name: database_sync_id
              schema:
                type: integer
              required: true
              description: The ID of the synchronization group
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/DataSourcePatchSchema'
          responses:
            200:
              description: The moved synchronization group
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        $ref: '#/components/schemas/DataSourceJsonSchema'
            401:
              $ref: '#/components/responses/401'
        """
        item = DatabaseSyncPatchSchema().load(request.json)
        database_sync = MoveDataBaseNameCommand(
            g.user, database_sync_id, item
        ).run()
        return self.format_response(200, data=database_sync.to_json())

    @expose("/<int:database_sync_id>/", methods=("DELETE",))
    @authenticated()
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=LogsMessages.LM_DEL_DATABASE_SYNC_GROUP,
        log_to_statsd=False,
    )
    def delete(self, database_sync_id: int) -> Response:
        """Delete a database name synchronization group
        ---
        delete:
          description: >-
            Delete a database name synchronization group.
            Requires authentication.
            Deletes the synchronization group with the given ID.
          parameters:
            - in: path
              name: database_sync_id
              schema:
                type: integer
              required: true
              description: The ID of the synchronization group
          responses:
            200:
              description: The deletion was successful
            401:
              $ref: '#/components/responses/401'
        """
        DeleteDatabaseSyncCommand(g.user, database_sync_id).run()
        return self.format_response(200)
