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
from typing import Any, Dict, Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User

from superset import db
from superset.commands.base import BaseCommand
from superset.constants import MANAGE
from superset.exceptions import HTTPError, SupersetGenericDBErrorException
from superset.global_messages import Messages
from superset.models.datasource import DataSource
from superset.v2.databases.dao import DatabaseV2DAO
from superset.v2.datasources.dao import DataSourceDAO

logger = logging.getLogger(__name__)


class UpdateDatabaseDataSourceCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[Model] = None

    def run(self) -> Model:
        self.validate()
        DataSourceDAO.update(
            self._model, {"name": self._properties["database_name"]}, commit=False)
        database = DatabaseV2DAO.update(
            self._model.database, self._properties, commit=False)
        database.set_sqlalchemy_uri(database.sqlalchemy_uri)
        db.session.commit()
        return self._model

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
        if not DataSourceDAO.validate_uniqueness(
            self._properties["database_name"],
            self._properties["group_id"],
        ):
            raise HTTPError(Messages.DUPLICATE_NAME, 400)


class UpdateDataSourceCommand(BaseCommand):
    def __init__(self, user: User, model_id: str, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[DataSource] = None

    def run(self):
        self.validate()
        table_name = self._properties.get('table_name')
        comment = self._properties.get('comment')
        schema = self._model.database.parameters.get('database')

        db_engine_spec = self._model.database.db_engine_spec
        try:
            with self._model.database.get_raw_connection() as conn:
                cursor = conn.cursor()
                query = f"ALTER TABLE {schema}.{table_name} COMMENT '{comment}'"
                cursor.execute(query)
                db_engine_spec.execute(cursor, query)
                return

        except Exception as ex:
            raise SupersetGenericDBErrorException(message=str(ex)) from ex

    def validate(self) -> None:
        self._model = DataSourceDAO.find_by_id(self._model_id)
        if not self._model:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
