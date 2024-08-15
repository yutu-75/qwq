# -*- coding: utf-8 -*-

"""
@Time       : 2023/10/12 14:48
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from typing import Dict, Any, Optional

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.dashboard import Dashboard
from superset.constants import MANAGE
from superset.v2.dashboards.dao import DashboardV2DAO
from superset.v2.dashboards.group.dao import DashboardGroupDAO


class DashboardCopyCommand(BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._properties = data
        self._model_id = model_id
        self._model: Optional[Dashboard] = None

    def run(self) -> Model:
        self.validate()
        dash = DashboardV2DAO.create({
            "dashboard_title": self._properties["dashboard_title"],
            "position_json": self._model.position_json,
            "css": self._model.css,
            "certified_by": self._model.certified_by,
            "certification_details": self._model.certification_details,
            "json_metadata": self._model.json_metadata,
            "slug": self._model.slug,
            "published": self._model.published,
            "is_managed_externally": self._model.is_managed_externally,
            "external_url": self._model.external_url,
            "dashboard_group_id": self._properties["dashboard_group_id"],
            "mobile_type_name": self._model.mobile_type_name,
            "mobile_width": self._model.mobile_width,
            "mobile_height": self._model.mobile_height,
            "mobile_json_metadata": self._model.mobile_json_metadata,
            "mobile_position_json": self._model.mobile_position_json,
            "dashboard_config": self._model.dashboard_config,
            "third_tags": self._model.third_tags,
            "slices": self._model.slices,
        })
        return dash

    def validate(self):
        self._model = DashboardV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
        # 校验重名
        if not DashboardV2DAO.validate_uniqueness(
            self._properties["dashboard_title"],
            self._properties["dashboard_group_id"]
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

        # 查询分组是否存在
        group = DashboardGroupDAO.find_by_id(self._properties["dashboard_group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)
