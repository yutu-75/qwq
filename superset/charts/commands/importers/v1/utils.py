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
from typing import Any, Dict

from flask import g
from sqlalchemy.orm import Session

from superset.constants import GRANT
from superset.models.slice import Slice
from superset.v2.charts.group.dao import ChartGroupDAO


logger = logging.getLogger(__name__)


def import_chart(
    session: Session,
    config: Dict[str, Any],
    overwrite: bool = False,
    slice_group_id: int = 0,
) -> Slice:
    existing = session.query(Slice).filter_by(uuid=config["uuid"]).first()
    if existing:
        if not overwrite:
            return existing
        config["id"] = existing.id

    # TODO (betodealmeida): move this logic to import_from_dict
    config["params"] = json.dumps(config["params"])

    if slice_group_id == 0:
        group_path = config.pop("group_path", None)
        group = ChartGroupDAO.import_group(group_path)
        slice_group_id = group.id

    config["slice_group_id"] = slice_group_id
    chart = Slice.import_from_dict(session, config, recursive=False)
    if chart.id is None:
        session.flush()

    if hasattr(g, "user") and g.user:
        chart.owners.append(g.user)

    chart.add_user_permission(GRANT)
    return chart
