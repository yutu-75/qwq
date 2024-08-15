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
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from flask import request
from sqlalchemy.exc import SQLAlchemyError

from superset.dao.base import BaseDAO
from superset.dashboards.commands.exceptions import DashboardNotFoundError
from superset.extensions import db
from superset.models.app_attributes import AppAttribute
from superset.models.core import FavStar, FavStarClassName
from superset.models.dashboard import Dashboard, id_or_slug_filter, DashboardRoles, \
    dashboard_user, dashboard_slices
from superset.models.slice import Slice
from superset.utils.core import get_user_id
from superset.utils.dashboard_filter_scopes_converter import copy_filter_scopes
from sqlalchemy import select

from superset.v2.models.user_role import UserRole

logger = logging.getLogger(__name__)


class DashboardDAO(BaseDAO):
    model_cls = Dashboard

    @classmethod
    def get_dashboard_by_id(cls, dashboard_id: int) -> Dashboard:
        query = db.session.query(cls.model_cls).filter(
            cls.model_cls.id == dashboard_id
        )
        return query.one_or_none()

    @classmethod
    def get_title(cls, dashboard_id: int):
        query = db.session.query(cls.model_cls.dashboard_title).filter(
            cls.model_cls.id == dashboard_id
        )
        return query.one_or_none()

    @staticmethod
    def get_by_id_or_slug(id_or_slug: Union[int, str]) -> Dashboard:
        # query = (
        #     db.session.query(Dashboard)
        #     .filter(id_or_slug_filter(id_or_slug))
        #     .outerjoin(Slice, Dashboard.slices)
        #     .outerjoin(Slice.table)
        #     .outerjoin(Dashboard.owners)
        #     .outerjoin(Dashboard.roles)
        # )
        # Apply dashboard base filters
        # query = DashboardAccessFilter("id", SQLAInterface(Dashboard, db.session)).apply(
        #     query, None
        # )
        # dashboard = query.one_or_none()
        dashboard = db.session.query(Dashboard).filter(
            id_or_slug_filter(id_or_slug)
        ).one_or_none()
        if not dashboard:
            raise DashboardNotFoundError()

        dashboard.can_access()
        return dashboard

    @staticmethod
    def get_datasets_for_dashboard(id_or_slug: str) -> List[Any]:
        dashboard = DashboardDAO.get_by_id_or_slug(id_or_slug)
        return dashboard.datasets_trimmed_for_slices()

    @staticmethod
    def get_charts_for_dashboard(id_or_slug: str) -> List[Slice]:
        return DashboardDAO.get_by_id_or_slug(id_or_slug).slices

    @staticmethod
    def get_dashboard_changed_on(
        id_or_slug_or_dashboard: Union[str, Dashboard]
    ) -> datetime:
        """
        Get latest changed datetime for a dashboard.

        :param id_or_slug_or_dashboard: A dashboard or the ID or slug of the dashboard.
        :returns: The datetime the dashboard was last changed.
        """

        dashboard: Dashboard = (
            DashboardDAO.get_by_id_or_slug(id_or_slug_or_dashboard)
            if isinstance(id_or_slug_or_dashboard, str)
            else id_or_slug_or_dashboard
        )
        # drop microseconds in datetime to match with last_modified header
        return dashboard.changed_on.replace(microsecond=0)

    @staticmethod
    def get_dashboard_and_slices_changed_on(  # pylint: disable=invalid-name
        id_or_slug_or_dashboard: Union[str, Dashboard]
    ) -> datetime:
        """
        Get latest changed datetime for a dashboard. The change could be a dashboard
        metadata change, or a change to one of its dependent slices.

        :param id_or_slug_or_dashboard: A dashboard or the ID or slug of the dashboard.
        :returns: The datetime the dashboard was last changed.
        """

        dashboard = (
            DashboardDAO.get_by_id_or_slug(id_or_slug_or_dashboard)
            if isinstance(id_or_slug_or_dashboard, str)
            else id_or_slug_or_dashboard
        )
        dashboard_changed_on = DashboardDAO.get_dashboard_changed_on(dashboard)
        slices = dashboard.slices
        slices_changed_on = max(
            [slc.changed_on for slc in slices]
            + ([datetime.fromtimestamp(0)] if len(slices) == 0 else [])
        )
        # drop microseconds in datetime to match with last_modified header
        return max(dashboard_changed_on, slices_changed_on).replace(microsecond=0)

    @staticmethod
    def get_dashboard_and_datasets_changed_on(  # pylint: disable=invalid-name
        id_or_slug_or_dashboard: Union[str, Dashboard]
    ) -> datetime:
        """
        Get latest changed datetime for a dashboard. The change could be a dashboard
        metadata change, a change to one of its dependent datasets.

        :param id_or_slug_or_dashboard: A dashboard or the ID or slug of the dashboard.
        :returns: The datetime the dashboard was last changed.
        """

        dashboard = (
            DashboardDAO.get_by_id_or_slug(id_or_slug_or_dashboard)
            if isinstance(id_or_slug_or_dashboard, str)
            else id_or_slug_or_dashboard
        )
        dashboard_changed_on = DashboardDAO.get_dashboard_changed_on(dashboard)
        datasources = dashboard.datasources
        datasources_changed_on = max(
            [datasource.changed_on for datasource in datasources]
            + ([datetime.fromtimestamp(0)] if len(datasources) == 0 else [])
        )
        # drop microseconds in datetime to match with last_modified header
        return max(dashboard_changed_on, datasources_changed_on).replace(microsecond=0)

    @staticmethod
    def validate_slug_uniqueness(slug: str) -> bool:
        if not slug:
            return True
        dashboard_query = db.session.query(Dashboard).filter(Dashboard.slug == slug)
        return not db.session.query(dashboard_query.exists()).scalar()

    @staticmethod
    def validate_update_slug_uniqueness(dashboard_id: int, slug: Optional[str]) -> bool:
        if slug is not None:
            dashboard_query = db.session.query(Dashboard).filter(
                Dashboard.slug == slug, Dashboard.id != dashboard_id
            )
            return not db.session.query(dashboard_query.exists()).scalar()
        return True

    @staticmethod
    def update_charts_owners(model: Dashboard, commit: bool = True) -> Dashboard:
        owners = list(model.owners)
        for slc in model.slices:
            slc.owners = list(set(owners) | set(slc.owners))
        if commit:
            db.session.commit()
        return model

    @staticmethod
    def bulk_delete(models: Optional[List[Dashboard]], commit: bool = True) -> None:
        item_ids = [model.id for model in models] if models else []
        # bulk delete, first delete related data
        if models:
            for model in models:
                model.slices = []
                model.owners = []
                model.embedded = []
                db.session.merge(model)
        # bulk delete itself
        try:
            db.session.query(Dashboard).filter(Dashboard.id.in_(item_ids)).delete(
                synchronize_session="fetch"
            )
            if commit:
                db.session.commit()
        except SQLAlchemyError as ex:
            db.session.rollback()
            raise ex

    @staticmethod
    def set_dash_metadata(
            dashboard: Dashboard,
            data: Dict[Any, Any],
            old_to_new_slice_ids: Optional[Dict[int, int]] = None,
            commit: bool = False,
    ) -> Dashboard:
        positions = data.get("positions")
        new_filter_scopes = {}
        md = dashboard.params_dict
        md1 = dashboard.params_dict

        if positions is not None:
            # find slices in the position data
            slice_ids = [
                value.get("meta", {}).get("chartId")
                for value in positions.values()
                if isinstance(value, dict)
            ]

            session = db.session()
            current_slices = session.query(Slice).filter(Slice.id.in_(slice_ids)).all()

            dashboard.slices = current_slices

            # add UUID to positions
            uuid_map = {slice.id: str(slice.uuid) for slice in current_slices}
            for obj in positions.values():
                if (
                        isinstance(obj, dict)
                        and obj["type"] == "CHART"
                        and obj["meta"]["chartId"]
                ):
                    chart_id = obj["meta"]["chartId"]
                    obj["meta"]["uuid"] = uuid_map.get(chart_id)

            # remove leading and trailing white spaces in the dumped json
            dashboard.position_json = json.dumps(
                positions, indent=None, separators=(",", ":"), sort_keys=True
            )

            if "filter_scopes" in data:
                # replace filter_id and immune ids from old slice id to new slice id:
                # and remove slice ids that are not in dash anymore
                slc_id_dict: Dict[int, int] = {}
                if old_to_new_slice_ids:
                    slc_id_dict = {
                        old: new
                        for old, new in old_to_new_slice_ids.items()
                        if new in slice_ids
                    }
                else:
                    slc_id_dict = {sid: sid for sid in slice_ids}
                new_filter_scopes = copy_filter_scopes(
                    old_to_new_slc_id_dict=slc_id_dict,
                    old_filter_scopes=json.loads(data["filter_scopes"] or "{}")
                    if isinstance(data["filter_scopes"], str)
                    else data["filter_scopes"],
                )

            default_filters_data = json.loads(data.get("default_filters", "{}"))
            applicable_filters = {
                key: v
                for key, v in default_filters_data.items()
                if int(key) in slice_ids
            }
            md["default_filters"] = json.dumps(applicable_filters)

            # positions have its own column, no need to store it in metadata
            md.pop("positions", None)

        # The css and dashboard_title properties are not part of the metadata
        # TODO (geido): remove by refactoring/deprecating save_dash endpoint
        if data.get("css") is not None:
            dashboard.css = data.get("css")
        if data.get("dashboard_title") is not None:
            dashboard.dashboard_title = data.get("dashboard_title")

        if new_filter_scopes:
            md["filter_scopes"] = new_filter_scopes
        else:
            md.pop("filter_scopes", None)

        md.setdefault("timed_refresh_immune_slices", [])

        if data.get("color_namespace") is None:
            md.pop("color_namespace", None)
        else:
            md["color_namespace"] = data.get("color_namespace")

        md["expanded_slices"] = data.get("expanded_slices", {})
        md["refresh_frequency"] = data.get("refresh_frequency", 0)
        md["color_scheme"] = data.get("color_scheme", "")
        md["label_colors"] = data.get("label_colors", {})
        md["shared_label_colors"] = data.get("shared_label_colors", {})
        md["color_scheme_domain"] = data.get("color_scheme_domain", [])
        md["cross_filters_enabled"] = data.get("cross_filters_enabled", True)
        dashboard.json_metadata = json.dumps(md)
        md1["color_namespace"]=data.get("mobile_json_metadata",{}).get("color_namespace","")
        md1["color_scheme"]=data.get("mobile_json_metadata",{}).get("color_scheme","")
        md1["positions"]=data.get("mobile_json_metadata",{}).get("positions",{})
        md1["refresh_frequency"]=data.get("mobile_json_metadata",{}).get("refresh_frequency",0)
        md1["shared_label_colors"]=data.get("mobile_json_metadata",{}).get("shared_label_colors", {})
        md1["default_filters"]=data.get("mobile_json_metadata",{}).get("default_filters", {})
        md1["filter_scopes"]=data.get("mobile_json_metadata",{}).get("filter_scopes", {})
        md1["chart_configuration"]=data.get("mobile_json_metadata",{}).get("chart_configuration", {})

        dashboard.mobile_json_metadata = json.dumps(md1)
        if commit:
            db.session.commit()
        return dashboard

    @staticmethod
    def favorited_ids(dashboards: List[Dashboard]) -> List[FavStar]:
        ids = [dash.id for dash in dashboards]
        return [
            star.obj_id
            for star in db.session.query(FavStar.obj_id)
            .filter(
                FavStar.class_name == FavStarClassName.DASHBOARD,
                FavStar.obj_id.in_(ids),
                FavStar.user_id == get_user_id(),
            )
            .all()
        ]

    @staticmethod
    def get_app_attribute_models():
        app_key = request.headers.get("appKey")
        query = db.session.query(AppAttribute).filter(
            AppAttribute.app_key == app_key,
        ).first()
        return query

    @staticmethod
    def get_dashboard_ids():
        query = DashboardDAO.get_app_attribute_models()
        if query:
            # 存在数据，取出某个字段的值
            role_id = query.role_id
            users = db.session.query(UserRole.user_id).filter(
                UserRole.role_id == role_id).all()
            # 提取用户ID列表
            user_ids = [user[0] for user in users]

            dashboard_ids = db.session.query(Dashboard).filter(
                Dashboard.created_by_fk.in_(user_ids)).all()
            return dashboard_ids
        else:
            # 数据不存在
            return None

    @staticmethod
    def set_permissions(users, current_role, dashboard_id):

        query = DashboardDAO.get_app_attribute_models()
        if query:
            # 存在数据，取出某个字段的值
            role_id = query.role_id

            try:
                for user_id in users:
                    select_stmt = select([dashboard_user]).where(
                        dashboard_user.c.user_id == str(user_id.get("id")),
                        dashboard_user.c.dashboard_id == dashboard_id
                    )
                    existing_data = db.session.execute(select_stmt).first()

                    if existing_data is None:
                        data = {
                            "dashboard_id": dashboard_id,
                            "user_id": user_id.get("id"),
                        }
                        # 数据不存在，插入新数据
                        db.session.execute(dashboard_user.insert().values(data))
                        db.session.commit()

                if current_role:

                    # 查询数据是否存在
                    select_stmt = select([DashboardRoles]).where(
                        DashboardRoles.c.role_id == str(role_id),
                        DashboardRoles.c.dashboard_id == dashboard_id
                    )
                    existing_data = db.session.execute(select_stmt).first()

                    if existing_data is None:
                        data = {
                            "dashboard_id": dashboard_id,
                            "role_id": role_id,
                        }
                        # 数据不存在，插入新数据
                        db.session.execute(DashboardRoles.insert().values(data))
                        db.session.commit()

                else:

                    db.session.execute(DashboardRoles.delete().
                    where(
                        DashboardRoles.c.role_id == str(role_id),
                        DashboardRoles.c.dashboard_id == dashboard_id
                    ))
                    db.session.commit()
                return "ok"

            except Exception as e:
                # 回滚事务
                db.session.rollback()
                return e

            finally:
                # 关闭会话
                db.session.close()
        else:
            # 数据不存在
            return False

    @staticmethod
    def delete_data(pk):
        try:
            data = db.session.query(Dashboard).filter_by(id=pk).first()
            if data:
                db.session.delete(data)
                db.session.commit()
                return "ok"
            else:
                return "No matching data found."

        except Exception as e:
            return e

    @staticmethod
    def copy_data(pk, users_models):
        try:
            data = Dashboard().get(pk)

            if data:
                # 复制看板
                dashboard_id = models_copy(
                    Dashboard.__table__.columns,
                    Dashboard(),
                    users_models,
                    data
                )

                # 复制图表
                for i in data.slices:
                    slice_id = models_copy(
                        Slice.__table__.columns,
                        Slice(),
                        users_models,
                        i
                    )

                    # 添加关联关系
                    values = [
                        {"dashboard_id": dashboard_id, "slice_id": slice_id}]
                    db.session.execute(dashboard_slices.insert(), values)
                    db.session.commit()

                return "ok"
            else:
                return "No matching data found."

        except Exception as e:
            logger.error(str(e))


def models_copy(models_columns, models_data, users_models, data):
    try:

        for column in models_columns:
            if column.name in ["uuid", "created_on", "changed_on", "id"]:
                continue
            if column.name in ["created_by_fk", "changed_by_fk"]:
                setattr(models_data, column.name, users_models.id)
            else:
                setattr(models_data, column.name, getattr(data, column.name))
        # 添加新实例到会话中
        db.session.add(models_data)
        db.session.commit()

        return models_data.id
    except Exception as e:
        logger.error(str(e))

