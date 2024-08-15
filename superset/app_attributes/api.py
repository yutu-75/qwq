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
from flask import Response
from flask_appbuilder import has_access
from flask_appbuilder.api import expose, protect, safe, ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface

from superset import app
from superset.app_attributes.app_attribute_command import AppAttributeCommand
from superset.app_attributes.filters import AppAttributeFilter, SearchTextFilter
from superset.commands.exceptions import ForbiddenError, ObjectNotFoundError, \
    DeleteFailedError
from superset.extensions import event_logger
from superset.models.app_attributes import AppAttribute
from superset.views.base_api import (
    statsd_metrics, BaseSupersetApiMixin, BaseSupersetModelRestApi,
)

logger = logging.getLogger(__name__)
config = app.config


class AppAttributeRestApi(BaseSupersetModelRestApi):
    datamodel = SQLAInterface(AppAttribute)
    resource_name = "app_attribute"
    allow_browser_login = True
    show_columns = [
        "id",
        "name",
        "code",
        "app_desc",
        "app_key",
        "app_secret",
        "enabled",
        "is_delete",
        "changed_by.first_name",
        "changed_by.last_name",
        "changed_by.username",
        "changed_by.id",
        "changed_on_utc",
        "created_on_delta_humanized",
        "created_by.first_name",
        "created_by.username",
        "created_by.last_name",
        "role.name",
        "role.id",
    ]
    list_columns = [
        "id",
        "name",
        "code",
        "app_desc",
        "app_key",
        "app_secret",
        "enabled",
        "is_delete",
        "changed_by.first_name",
        "changed_by.last_name",
        "changed_by.username",
        "changed_by.id",
        "changed_on_utc",
        "created_on_delta_humanized",
        "created_by.first_name",
        "created_by.username",
        "created_by.last_name",
        "role.name",
        "role.id",
    ]
    add_columns = [
        "name",
        "code",
        "enabled",
        "app_desc",
        "role_id",
    ]
    search_columns = [
        "name",
        "code",

    ]
    search_filters = {"name": [SearchTextFilter]}
    edit_columns = add_columns

    base_filters = [['is_delete', AppAttributeFilter, False]]

    @expose("/<pk>", methods=["DELETE"])
    @protect()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.delete",
        log_to_statsd=False,
    )
    def delete(self, pk: int) -> Response:
        try:
            AppAttributeCommand(pk).run()
            return self.response(200, message="OK")
        except ObjectNotFoundError:
            return self.response_404()
        except ForbiddenError:
            return self.response_403()
        except DeleteFailedError as ex:
            logger.error(
                "Error deleting model %s: %s",
                self.__class__.__name__,
                str(ex),
                exc_info=True,
            )
            return self.response_422(message=str(ex))
