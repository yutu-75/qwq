from sqlalchemy import String, Text


def set_mysql_field(field_obj):
    """
    根据hive表的字段设置mysql的表字段
    :param field_obj: 字段对象
    :return:
    """

    # TODO hive其他字段匹配

    if isinstance(field_obj, String) and not field_obj.length:
        return Text()

    return field_obj


def truncate_table_and_reset_id(session, table_name):

    truncate_query = f"TRUNCATE TABLE {table_name}"
    session.execute(truncate_query)

    session.commit()
