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

import json
import logging
import uuid
from typing import Any, Dict

from sqlalchemy.orm import Session

from superset.constants import DataSourceType, GRANT
from superset.models.core import Database
from superset.v2.datasources.api_datasources.dao import APITablesDAO
from superset.v2.datasources.dao import DataSourceDAO
from superset.v2.datasources.group.dao import DataSourceGroupDAO

logger = logging.getLogger(__name__)


def import_database(
    session: Session,
    config: Dict[str, Any],
    overwrite: bool = False,
    datasource_group_id: int = 0,
) -> Database:
    datasource = config.pop("datasource", {})
    d_type = datasource.get('d_type', DataSourceType.DATABASE)
    existing = session.query(Database).filter_by(uuid=config["uuid"]).first()
    if existing:
        if not overwrite and d_type == DataSourceType.DATABASE:
            return existing
        config["id"] = existing.id

    # https://github.com/apache/superset/pull/16756 renamed ``csv`` to ``file``.
    config["allow_file_upload"] = config.pop("allow_csv_upload")
    if "schemas_allowed_for_csv_upload" in config["extra"]:
        config["extra"]["schemas_allowed_for_file_upload"] = config["extra"].pop(
            "schemas_allowed_for_csv_upload"
        )

    # TODO (betodealmeida): move this logic to import_from_dict
    config["extra"] = json.dumps(config["extra"])

    database = Database.import_from_dict(session, config, recursive=False)
    if database.id is None:
        session.flush()

    # 选择分组不存在时
    if datasource_group_id == 0:
        group_path = datasource.pop("group_path", None)
        group = DataSourceGroupDAO.import_group(group_path)
        datasource_group_id = group.id

    # api数据集和文件数据集datasource is not None
    if datasource is None:
        return database

    # datasource存在，为新版的导出文件
    elif datasource:
        datasource["group_id"] = datasource_group_id
        datasource["database"] = database
        datasource["database_id"] = database.id
        api_tables = datasource.pop("api_tables", [])
        uuid_ = datasource["uuid"] or ""
        obj = DataSourceDAO.find_by_uuid(uuid_)
        if obj:
            obj = DataSourceDAO.update(obj, datasource, commit=False)
        else:
            datasource["uuid"] = uuid_ or uuid.uuid4()
            obj = DataSourceDAO.create(datasource, commit=False)

        session.flush()
        if obj.d_type == DataSourceType.API:
            for item in api_tables:
                APITablesDAO.insert_or_update(
                    {
                        'uuid': item['uuid'],
                        'name': item["name"],
                        'configuration': item['configuration'],
                        "data_path": item["data_path"],
                        "datasource_id": obj.id
                    },
                    {
                        'name': item["name"],
                        'configuration': item['configuration'],
                        "data_path": item["data_path"],
                        "datasource_id": obj.id
                    },
                    commit=False
                )

    # 如果本身存在数据源，旧版数据导入不新增数据源
    elif database.datasource:
        model = database.datasource[0]
        model.group_id = datasource_group_id
        DataSourceDAO.save(model, commit=False)

    # 旧版导出数据datasource为默认值{},且本身未关联数据源则新建
    else:
        DataSourceDAO.create({
            "name": database.database_name,
            "d_type": DataSourceType.DATABASE,
            "database_id": database.id,
            "group_id": datasource_group_id
        }, commit=False)

    if database.datasource:
        database.datasource[0].add_user_permission(GRANT)
    return database
