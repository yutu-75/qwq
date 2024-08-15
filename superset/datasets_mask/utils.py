import logging
from superset import db
from superset.connectors.sqla.models import DatasetMark
from superset.utils.common_wrap import ensure_data


logger = logging.getLogger(__name__)


def get_mask_status(dataset_id, user_id):
    """获取标记"""
    dataset_mark = db.session.query(DatasetMark.id).filter_by(
        table_id=dataset_id,
        mark_user_id=user_id,
        is_mark=True
    ).first()
    return dataset_mark.id if dataset_mark else False


@ensure_data
def handle_group_data(data, user_id):
    if data and user_id:
        datasets = data.get('datasets')
        if datasets:
            for dataset in datasets:
                dataset_id = dataset.get('dataset_id')
                dataset['mark'] = get_mask_status(dataset_id, user_id)
            datasets.sort(key=lambda x: x['mark'], reverse=True)

        children = data.get('children', [])
        for child in children:
            handle_group_data(child, user_id)


@ensure_data
def fix_handle_group_data(source_data, user_id):
    if source_data and user_id:
        for single in source_data:
            handle_group_data(single, user_id)

    return source_data


@ensure_data
def fix_sample_data(source_data, user_id):
    if source_data and user_id:
        for single in source_data:
            dataset_id = single.get('id')
            single['mark'] = get_mask_status(dataset_id, user_id)
        source_data.sort(key=lambda x: x['mark'], reverse=True)

    return source_data
