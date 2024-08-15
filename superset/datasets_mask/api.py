from flask_appbuilder.models.sqla.interface import SQLAInterface
from superset.connectors.sqla.models import DatasetMark
from superset.constants import MODEL_API_RW_METHOD_PERMISSION_MAP, RouteMethod
from superset.datasets.api import BaseSupersetModelRestApi


class DatasetMarkRestApi(BaseSupersetModelRestApi):
    datamodel = SQLAInterface(DatasetMark)
    resource_name = "dataset_mark"
    allow_browser_login = True
    class_permission_name = "Dataset"
    method_permission_name = MODEL_API_RW_METHOD_PERMISSION_MAP
    include_route_methods = {
        RouteMethod.POST,
        RouteMethod.DELETE
    }
    add_columns = [
        "id",
        "mark_user_id",
        "table_id",
        "is_mark",
    ]
