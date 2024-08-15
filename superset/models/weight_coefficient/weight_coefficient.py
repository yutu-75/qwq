import copy
import sqlalchemy as sa
from flask import request
from sqlalchemy import select, column, literal_column, func, case, and_


def reset_weighted_select(metrics_copy, metric):
    """
    开启权重系数后重新定义列select查询字段
    :param metrics_copy:
    :param metric:
    :return:
    """

    if metric.get("column"):
        copy_metric = copy.deepcopy(metric)
        metrics_copy.append(copy.deepcopy(metric))
        weights_column = request.get_json().get("form_data").get("weightsColumns")

        metric["column"]["column_name"] += f'_{metric["aggregate"]}'
        if metric["aggregate"] == "COUNT":
            metric["aggregate"] = "SUM"
            metric["column"]["column_name"] = weights_column
            metric["column"]["verbose_name"] = weights_column

        elif metric["aggregate"] == "COUNT_DISTINCT":
            metric["aggregate"] = "SUM"
            to_sqla = sa.func.sum(
                case(
                    [(
                        column(
                            f'{copy_metric.get("column").get("column_name")}_{copy_metric["aggregate"]}'
                        ) == 1,
                        column(
                            weights_column
                        ))],
                    else_=0
                )
            ).label(copy_metric.get("label"))

            return to_sqla


def reset_weighted_table(tbl, metrics, where_clause_and):
    """
    选择了显示权重后，循环增加了指标*权重系数列
    :param tbl: 表对象
    :param metrics: 原指标列数据列表  例:'SUM(年龄)'、'COUNT(年龄)'等
    :param where_clause_and:
    :return:
    """

    weights_column = request.get_json().get("form_data").get("weightsColumns")

    add_column_list = []
    for metric in metrics:
        if metric.get("aggregate") == "COUNT_DISTINCT":
            add_column_list.append(
                sa.func.row_number().over(partition_by=[
                    column(metric.get("column").get("column_name"))

                ]).label(
                    f'{metric.get("column").get("column_name")}_{metric["aggregate"]}'
                )
            )
        elif metric["aggregate"] == "COUNT":
            continue

        else:
            add_column_list.append(
                (
                    column(
                        metric.get("column").get("column_name")
                    ) * literal_column(weights_column)
                ).label(
                    f'{metric.get("column").get("column_name")}_{metric["aggregate"]}'
                )
            )
    select_list = [tbl, "*"]
    select_list.extend(add_column_list)
    tbl = select(select_list).where(and_(*where_clause_and))
    return tbl


def is_weights_enabled():
    """
    判断是否开启了显示权重
    :return:
    """
    try:
        sign = request.get_json().get("form_data").get("viewWeight")
        return sign
    except Exception as e:
        return False
