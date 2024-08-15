# -*- coding: utf-8 -*-

"""
@Time       : 2023/10/12 15:46
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import logging
from typing import Any, Dict, Optional

from flask_appbuilder.models.sqla import Model
from flask_appbuilder.security.sqla.models import User

from superset.commands.base import BaseCommand, CreateMixin
from superset.exceptions import HTTPError
from superset.global_messages import Messages
from superset.models.slice import Slice
from superset.constants import MANAGE
from superset.v2.charts.dao import ChartV2DAO
from superset.v2.charts.group.dao import ChartGroupDAO

logger = logging.getLogger(__name__)


class CopyChartCommand(CreateMixin, BaseCommand):
    def __init__(self, user: User, model_id: int, data: Dict[str, Any]):
        self._actor = user
        self._model_id = model_id
        self._model: Optional[Slice] = None
        self._properties = data

    def run(self) -> Model:
        self.validate()
        ChartV2DAO.create({
            "slice_name": self._properties["slice_name"],
            "datasource_id": self._model.datasource_id,
            "datasource_type": self._model.datasource_type,
            "datasource_name": self._model.datasource_name,
            "viz_type": self._model.viz_type,
            "params": self._model.params,
            "query_context": self._model.query_context,
            "description": self._model.description,
            "cache_timeout": self._model.cache_timeout,
            "perm": self._model.perm,
            "schema_perm": self._model.schema_perm,
            "last_saved_at": self._model.last_saved_at,
            "last_saved_by_fk": self._model.last_saved_by_fk,
            "certified_by": self._model.certified_by,
            "certification_details": self._model.certification_details,
            "is_managed_externally": self._model.is_managed_externally,
            "external_url": self._model.external_url,
            "slice_group_id": self._properties["slice_group_id"],
        })
        return self._model

    def validate(self) -> None:
        self._model = ChartV2DAO.find_by_id(self._model_id)
        if self._model is None:
            raise HTTPError(Messages.NOT_EXIST, 400)

        self._model.can_access(MANAGE)
        # 校验重名
        if not ChartV2DAO.validate_uniqueness(
            self._properties["slice_name"],
            self._properties["slice_group_id"]
        ):
            raise HTTPError(Messages.IS_EXIST, 400)

        # 查询分组是否存在
        group = ChartGroupDAO.find_by_id(self._properties["slice_group_id"])
        if group is None:
            raise HTTPError(Messages.GROUP_NOT_EXIST, 400)

