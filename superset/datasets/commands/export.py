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
# isort:skip_file
"""
fix: 陈果-2023-04-20
修复内容: 修复看板图表导出功能
update:陈超-升级合并官方版本2.1.0
"""
import json
import logging
from typing import Iterator, Tuple

import yaml

from superset import event_logger
from superset.commands.export.models import ExportModelsCommand
from superset.connectors.sqla.models import SqlaTable
from superset.datasets.commands.exceptions import DatasetNotFoundError
from superset.datasets.dao import DatasetDAO
from superset.utils.dict_import_export import EXPORT_VERSION
from superset.v2.datasets.group.dao import DatasetGroupDAO

from superset.v2.datasources.group.dao import DataSourceGroupDAO

logger = logging.getLogger(__name__)

JSON_KEYS = {"params", "template_params", "extra"}


class ExportDatasetsCommand(ExportModelsCommand):

    dao = DatasetDAO
    not_found = DatasetNotFoundError

    @staticmethod
    def _export(
        model: SqlaTable, export_related: bool = True
    ) -> Iterator[Tuple[str, str]]:
        database_slug = f"db_{model.database.id}"
        dataset_slug = f"dataset_{model.id}"
        file_name = f"datasets/{database_slug}/{dataset_slug}.yaml"

        payload = model.export_to_dict(
            recursive=True,
            include_parent_ref=False,
            include_defaults=True,
            export_uuids=True,
        )
        # TODO (betodealmeida): move this logic to export_to_dict once this
        # becomes the default export endpoint
        for key in JSON_KEYS:
            if payload.get(key):
                try:
                    payload[key] = json.loads(payload[key])
                except json.decoder.JSONDecodeError:
                    logger.info("Unable to decode `%s` field: %s", key, payload[key])
        for key in ("metrics", "columns"):
            for attributes in payload.get(key, []):
                if attributes.get("extra"):
                    try:
                        attributes["extra"] = json.loads(attributes["extra"])
                    except json.decoder.JSONDecodeError:
                        logger.info(
                            "Unable to decode `extra` field: %s", attributes["extra"]
                        )

        payload["version"] = EXPORT_VERSION
        payload["database_uuid"] = str(model.database.uuid)
        payload["group_path"] = DatasetGroupDAO.export_group(model.table_group_id)
        file_content = yaml.safe_dump(payload, sort_keys=False)

        event_logger.log_with_context(
            action="导出数据集",
            log_to_statsd=False,
            title=payload['custom_name']
        )  # pylint: disable=too-many-locals
        yield file_name, file_content

        # include database as well
        if export_related:
            file_name = f"databases/{database_slug}.yaml"

            payload = model.database.export_to_dict(
                recursive=False,
                include_parent_ref=False,
                include_defaults=True,
                export_uuids=True,
            )
            # TODO (betodealmeida): move this logic to export_to_dict once this
            # becomes the default export endpoint
            if payload.get("extra"):
                try:
                    payload["extra"] = json.loads(payload["extra"])
                except json.decoder.JSONDecodeError:
                    logger.info("Unable to decode `extra` field: %s", payload["extra"])

            payload["version"] = EXPORT_VERSION
            datasource = model.database.datasource
            if datasource:
                datasource = datasource[0]
                payload["datasource"] = {
                    "uuid": str(datasource.uuid),
                    "name": datasource.name,
                    "database_id": datasource.database_id,
                    "d_type": datasource.d_type,
                    "desc": datasource.desc or "",
                    "api_tables": [{
                        "uuid": str(item.uuid),
                        "name": item.name,
                        "configuration": item.configuration,
                        "data_path": item.data_path
                    } for item in datasource.api_tables],
                    "group_path": DataSourceGroupDAO.export_group(
                        datasource.group_id)
                }

            else:
                payload["datasource"] = None

            file_content = yaml.safe_dump(payload, sort_keys=False)
            yield file_name, file_content
