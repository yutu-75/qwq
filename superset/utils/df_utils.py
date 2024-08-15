import pandas as pd
from superset.utils.common_wrap import ensure_data

SPECIAL_VIZ = [
    'big_number',
    'pivot_table_v2'
]
DATE_UNIT = ['Y', 'Q', 'M', 'W', 'D']
QUARTER = '3M'
PD_QUARTER = 'Q'
PERCENT = 100
CALC_ATTR = {
    'VALUE': 'value',
    'RATE': 'rate'
}
CALC_TYPE = {
    'QOQ': 'qoq',
    'YOY': 'yoy'
}
CALC_COLUMN_NAME = '{}({}){}'
PCT_NAME = '占比({})(%)'
# POSITION = 1


def calc_col_name(calc_type, calc_attr, source_col):
    """显示计算列名称"""
    if calc_type == CALC_TYPE['QOQ']:
        return CALC_COLUMN_NAME.format(
            'QOQ',
            source_col,
            'Value' if calc_attr == CALC_ATTR['VALUE'] else 'Rate'
        )
    else:
        return CALC_COLUMN_NAME.format(
            'YOY',
            source_col,
            'Value' if calc_attr == CALC_ATTR['VALUE'] else 'Rate'
        )


def get_date_series(source_df, series, date_unit):
    """填充时间列"""
    if date_unit in DATE_UNIT:
        full_df = pd.DataFrame({date_unit: pd.period_range(start=min(series),
                                                           end=max(series),
                                                           freq=date_unit)})
        source_df[date_unit] = series.dt.to_period(date_unit)
        return pd.merge(
            source_df,
            full_df,
            on=date_unit,
            how='right'
        )
    return source_df


def deal_use_unit(time_grain):
    """获取可用的时间粒度"""
    if isinstance(time_grain, str) and time_grain[-1] in DATE_UNIT:
        return PD_QUARTER if time_grain[-2:] == QUARTER else time_grain[-1]


def qoq_basis(source_df, granularity, computed_column, use_unit, calc_attr, special):
    """环比"""
    source_df[granularity] = pd.to_datetime(source_df[granularity])
    source_df = get_date_series(source_df, source_df[granularity], use_unit)
    qoq_name = calc_col_name(CALC_TYPE['QOQ'], calc_attr, computed_column)
    if calc_attr == CALC_ATTR['VALUE']:
        source_df[qoq_name] = source_df[computed_column].diff()
    else:
        source_df[qoq_name] = (source_df[computed_column] /
                               source_df[computed_column].shift() - 1) * PERCENT
    if special:
        source_df = source_df.drop(computed_column, axis=1)
    return source_df.drop(use_unit, axis=1).dropna(subset=[granularity])


def yoy_basis(source_df, granularity, computed_column, use_unit, calc_attr, special):
    """同比"""
    source_df[granularity] = pd.to_datetime(source_df[granularity])
    source_df = get_date_series(source_df, source_df[granularity], use_unit)
    source_df = source_df.dropna(subset=[granularity]).set_index(granularity)
    yoy_name = calc_col_name(CALC_TYPE['YOY'], calc_attr, computed_column)
    is_leap_day = (source_df.index.month == 2) & (source_df.index.day == 29)
    volume_last_year = source_df.loc[~is_leap_day, computed_column].shift(
        freq=pd.DateOffset(years=1)
    )
    if calc_attr == CALC_ATTR['VALUE']:
        source_df[yoy_name] = source_df[computed_column] - volume_last_year
        source_df.loc[is_leap_day, yoy_name] = (
                source_df.loc[is_leap_day, computed_column] -
                volume_last_year.shift(freq=pd.DateOffset(days=1)))
    else:
        source_df[yoy_name] = (source_df[computed_column]
                               / volume_last_year - 1) * PERCENT
        source_df.loc[is_leap_day, yoy_name] = (source_df.loc[
                                                    is_leap_day, computed_column] /
                                                volume_last_year.shift(
                                                    freq=pd.DateOffset(days=1)) - 1
                                                ) * PERCENT
    if special:
        source_df = source_df.drop(computed_column, axis=1)
    return source_df.drop(use_unit, axis=1).reset_index()


def pct_basis(source_df, computed_column, x_axis, group_by, special):
    """占比"""
    if x_axis and group_by:
        source_df = source_df.set_index(x_axis)
        if isinstance(computed_column, str):
            filter_df = source_df.filter(like=computed_column)
        else:
            filter_df = source_df.filter(items=computed_column)
        result_df = (
            filter_df.div(filter_df.sum(axis=1), axis=0) * PERCENT
        ).rename(columns=lambda x: PCT_NAME.format(x)).reset_index()
        source_df = pd.merge(
            source_df.drop(columns=filter_df.columns.tolist()) if special else source_df,
            result_df,
            on=x_axis,
        )
    else:
        serials_sum = source_df[computed_column].sum()
        source_df[PCT_NAME.format(computed_column)] = (
            source_df[computed_column] / serials_sum * PERCENT
        )
        if special:
            source_df = source_df.drop(computed_column, axis=1)
    return source_df


CALC_MANAGER = {
    "qoq": qoq_basis,  # 环比
    "ratio": pct_basis,  # 占比
    "yoy": yoy_basis,  # 同比
}


@ensure_data
def extra_calculation(df, form_data, calc):
    if form_data:
        df_column_names = df.columns.tolist()
        special = True if form_data.get('viz_type') not in SPECIAL_VIZ else False
        x_axis = form_data.get('x_axis')
        use_unit = deal_use_unit(form_data.get('time_grain_sqla'))
        group_by = form_data.get('groupby')
        for item in calc:
            calc_type = item.get('calc_type', '')
            computed_column = item.get('column', {}).get('column_name')
            use_columns = [x for x in df_column_names if
                           computed_column in x.split(', ')]
            if not use_columns and group_by:
                use_columns = [x for x in df_column_names if x != x_axis]
            if (calc_type == 'qoq' or calc_type == 'yoy') and computed_column:
                for col in use_columns:
                    df = CALC_MANAGER.get(calc_type)(
                        df, x_axis, col, use_unit, item.get('calc_attr'), special
                    )
            elif calc_type == 'ratio' and computed_column:
                df = CALC_MANAGER.get(calc_type)(
                    df,
                    use_columns if use_columns and group_by else computed_column,
                    x_axis,
                    group_by,
                    special
                )
    return df


# @ensure_data
# def calc_preprocess(options, df):
#     if options.get('aggregates'):
#         df_columns = df.columns.tolist()
#         aggregate = list(options.get('aggregates').keys())
#         possible = [
#             'QOQ({})Rate',
#             'QOQ({})Value',
#             'YOY({})Rate',
#             'YOY({})Value',
#             '占比({})(%)'
#         ]
#
#         for key in aggregate:
#             exist = False
#             for col in df_columns:
#                 for fmat in possible:
#                     if fmat.format(key) == col:
#                         options['aggregates'][col] = options['aggregates'].get(key)
#                         exist = True
#             if exist and key not in df_columns:
#                 del options['aggregates'][key]
#
#     return options


@ensure_data
def count_preprocess(query_dict):
    if isinstance(query_dict.get('metrics'), list):
        query_dict['metrics'].append(
            {
                "expressionType": "SQL",
                "sqlExpression": "COUNT(*)",
                "label": "sample_count",
            }
        )
    return query_dict
