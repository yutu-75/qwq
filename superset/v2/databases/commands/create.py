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
from typing import Any, Dict, List, Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User
from marshmallow import ValidationError

from superset.commands.base import BaseCommand
from superset.dao.exceptions import DAOCreateFailedError
from superset.databases.commands.exceptions import (
    DatabaseConnectionFailedError,
    DatabaseCreateFailedError,
    DatabaseExistsValidationError,
    DatabaseInvalidError,
    DatabaseRequiredFieldValidationError,
)
from superset.databases.commands.test_connection import TestConnectionDatabaseCommand
from superset.databases.dao import DatabaseDAO
from superset.exceptions import HTTPError
from superset.extensions import db, event_logger, security_manager
from superset.global_messages import Messages

logger = logging.getLogger(__name__)


class CreateDatabaseV2Command(BaseCommand):
    def __init__(self, user: User, data: Dict[str, Any]):
        self._actor = user
        self._properties = data

    def run(self) -> Model:
        self.validate()

        try:
            # Test connection before starting create transaction
            TestConnectionDatabaseCommand(self._properties).run()
        except Exception as ex:
            event_logger.log_with_context(
                action=f"db_creation_failed.{ex.__class__.__name__}",
                engine=self._properties.get("sqlalchemy_uri", "").split(":")[0],
            )
            raise DatabaseConnectionFailedError() from ex

        try:
            database = DatabaseDAO.create(self._properties, commit=False)
            database.set_sqlalchemy_uri(database.sqlalchemy_uri)
            db.session.commit()
        except DAOCreateFailedError as ex:
            db.session.rollback()
            event_logger.log_with_context(
                action=f"db_creation_failed.{ex.__class__.__name__}",
                engine=database.db_engine_spec.__name__,
            )
            raise DatabaseCreateFailedError() from ex
        return database

    def validate(self) -> None:
        if not DatabaseDAO.validate_uniqueness(self._properties["database_name"]):
            raise HTTPError(Messages.IS_EXIST, 400)
