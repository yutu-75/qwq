# -*- coding: utf-8 -*-

"""
@Time       : 2023/7/28 16:59
@Author     : lys
@Software   : PyCharm
@Description:
"""
import pandas as pd


def yoy_calc_all(df: pd.DataFrame, calc_type: str, calc_col: str,
                 label: str, date_type: str, merge_type: str) -> pd.DataFrame:
    """日同比增长率,按年计算 or 按月计算
    月同比增长率，按年计算"""
    df[label] = pd.to_datetime(df[label])
    df = df.set_index(label)
    df['year'] = df.index.year
    df['month'] = df.index.month
    # 若上传数据的时间格式为Y-M，此处会自动加上天数的日期，并自动取值为01，后面匹配时间时或许会报错
    df['day'] = df.index.day
    df['month_day'] = df.apply(lambda x: f"{x['month']}-{x['day']}", axis=1)
    # 将时间序列还原为列数据
    df = df.reset_index()
    # 获取本期和前期的数据
    test = []
    # 修复月份列全为相同的情况
    is_column_same = df['month'].nunique() == 1
    if is_column_same:
        date_type = 'year'
    for i in range(min(df[f'{date_type}']), max(df[f'{date_type}'])):
        df_par = df[df[f'{date_type}'] == i]  # 前期,例如:1月
        df_tag = df[df[f'{date_type}'] == i + 1]  # 本期,例如:2月
        # 合并本期和前期的数据，根据日份进行匹配
        df_combined = pd.merge(df_tag, df_par, on=f'{merge_type}',
                               suffixes=('_tag', '_par'))
        if calc_type in ['9', '6']:
            # 计算同比增长率
            df_combined[f'YOY({calc_col})Rate'] = (df_combined[f'{calc_col}_tag'] -
                                                   df_combined[
                                                       f'{calc_col}_par']) / \
                                                  df_combined[f'{calc_col}_par'] * 100
        elif calc_type in ['10', '7']:
            df_combined[f'YOY({calc_col})Value'] = (df_combined[f'{calc_col}_tag'] -
                                                    df_combined[f'{calc_col}_par'])
        test.append(df_combined)  # 保存结果
    if test:
        result_df = pd.concat(test).reset_index()  # 合并结果并更新索引
        # 选择需要的数据
        selected_columns = result_df.filter(like='YOY').columns.tolist()
        result_df = result_df[[f'{label}_tag'] + selected_columns]
        df = df[[label]]
        # 合并原始数据和结果数据
        merged_df = pd.merge(df, result_df, left_on=label, right_on=f'{label}_tag',
                             how='outer')
        return merged_df[[label] + selected_columns]
    else:
        return df[[label]]


# 同比
def yoy_calc(
    df: pd.DataFrame,  # 原始数据 :df
    granularity: str,  # 粒度 :ds
    calc_type: str,  # 计算类型：1-增长率，2-增长值，3-数据值
    calc_col: str,  # 计算列
    time_grain: str  # x轴序列：p1m
) -> pd.DataFrame:
    # 同比 = （今年同期 - 去年同期） / 去年同期，日同比，按月、年计算，月同比按年计算增长率、增长值
    df.sort_values(granularity, inplace=True)
    if time_grain == 'P1D' and calc_type in ['6', '7']:
        df = yoy_calc_all(df, calc_type, calc_col, granularity, 'month', 'day')
    elif time_grain == 'P1D' and calc_type in ['9', '10']:
        df = yoy_calc_all(df, calc_type, calc_col, granularity, 'year', 'month_day')
    elif time_grain == 'P1M' and calc_type in ['9', '10']:
        df = yoy_calc_all(df, calc_type, calc_col, granularity, 'year', 'month')
    selected_columns = df.filter(like='YOY').columns.tolist()
    return df[[granularity] + selected_columns]


# 环比
def qoq_calc(
    df: pd.DataFrame,
    granularity: str,
    calc_type: str,
    calc_col: str,
    time_grain: str,
) -> pd.DataFrame:
    # 环比 =（本周期 - 上周期） / 上周期，分别按日、月、年计算
    df.sort_values(granularity, inplace=True)
    df[granularity] = pd.to_datetime(df[granularity])
    time_grain = time_grain[-1]
    # 按照规定的日期粒度对数据进行分组求和
    df[granularity] = df[granularity].dt.to_period(time_grain).dt.to_timestamp()
    df = df.groupby(granularity).sum()
    # 将时间序列还原为一列数据
    df = df.reset_index()
    if calc_type == '1':
        df[f'{time_grain}_QOQ({calc_col})Rate'] = (df[calc_col] -
                                                  df[calc_col].shift(1)) / \
                                                 df[calc_col].shift(1) * 100
        return df[[granularity, f'{time_grain}_QOQ({calc_col})Rate']]
    if calc_type == '2':
        df[f'{time_grain}_QOQ({calc_col})Value'] = df[calc_col] - df[calc_col].shift(1)
        return df[[granularity, f'{time_grain}_QOQ({calc_col})Value']]


# 占比
def ratio_calc(
    df: pd.DataFrame,
    granularity: str = None,
    calc_type: str = None,
    calc_col: str = None,
    time_grain: str = None,
) -> pd.DataFrame:
    # 占比 = 本季度 / 总数
    total = df[calc_col].sum()
    df[f'RATIO({calc_col})'] = (df[calc_col] / total) * 100
    return df[[granularity, f'RATIO({calc_col})']]


# 看板中透视表使用占比功能
def ratio_calc_v2(
    df: pd.DataFrame,
    column: list,
    calc_col: str = None,
) -> pd.DataFrame:
    # 占比 = 本季度 / 总数
    df['Sum'] = df.groupby(column)[calc_col].transform('sum')
    df[f'占比({calc_col})(%)'] = df[calc_col] / df['Sum'] * 100
    # df[f'占比({calc_col})(%)'] = df[f'占比({calc_col})(%)'].round(2)
    return df
