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
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def delete_chart_entries_job():
    """
    定时任务清除15天后未引入的数据集
    :return:
    """
    from superset import create_app

    flask_app = create_app()

    with flask_app.app_context():
        from superset.models.slice import Slice
        from superset.extensions import db
        from superset.utils.core import DatasourceType
        from superset.datasets.dao import DatasetDAO
        from superset.connectors.sqla.models import SqlaTable

        tables_models_all = db.session.query(SqlaTable).all()
        for table_models in tables_models_all:
            charts = db.session.query(Slice).filter(
                    Slice.datasource_id == table_models.id,
                    Slice.datasource_type == DatasourceType.TABLE,
                ).all()

            current_time = datetime.now()
            time_threshold = table_models.changed_on + timedelta(days=15)

            if not charts and time_threshold < current_time:
                DatasetDAO.delete(table_models, commit=False)
                db.session.commit()


def run():
    try:
        delete_chart_entries_job()

    except Exception as e:
        print(e)
        logger.error(e)


if __name__ == '__main__':
    run()
