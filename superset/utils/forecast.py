import json
import logging
import pandas as pd
import requests
from superset.utils.common_wrap import ensure_data
from superset.utils.df_utils import deal_use_unit


logger = logging.getLogger(__name__)
TIME_SERIES = 'ds'
SPECIAL_DATE_UNIT = ['W', 'D']


try:
    from flask import current_app
except ModuleNotFoundError:
    raise Exception("FORECAST_URL Cannot be None")


def forecast_cycle(start_date, freq, cycle):
    return pd.date_range(
        start=start_date,
        freq=f'{freq}S' if freq not in SPECIAL_DATE_UNIT else freq, periods=cycle+1
    )[1:]


def splice_data(source_df: pd.DataFrame, forecast_df: pd.DataFrame):
    columns_equal = source_df.columns.tolist().sort() == forecast_df.columns.tolist().sort()
    dtypes_equal = source_df.dtypes.tolist().sort() == forecast_df.dtypes.tolist().sort()
    if columns_equal and dtypes_equal:
        return pd.concat([source_df, forecast_df], ignore_index=True)
    else:
        return source_df


@ensure_data
def forecast_call(source_df: pd.DataFrame, x_axis, time_grain, calc: list):
    for i in calc:
        if i.get('calc_type') == 'forecast' and i.get('calc_attr'):
            cycle = i.get('calc_attr')
            break
    else:
        return source_df

    start_date = source_df.iloc[-1][x_axis]
    use_grain = deal_use_unit(time_grain)
    if len(source_df) < 3:
        for i in forecast_cycle(start_date, use_grain, cycle):
            source_df.append(pd.DataFrame({col: i if col == x_axis else None for col in source_df.columns}, index=[0]))

    else:
        forecast_url = current_app.config.get('FORECAST_URL')
        if forecast_url:
            op_source_df = source_df.copy()
            op_source_df.rename(columns={x_axis: TIME_SERIES}, inplace=True)
            source_json = op_source_df.to_json(orient='records', date_format='iso', date_unit='s')
            forecast_resp = requests.post(
                url=forecast_url,
                json={
                    'source_data': json.loads(source_json),
                    'cycle': cycle
                }
            )
            if forecast_resp.status_code != 200:
                raise Exception(forecast_resp.text or 'Forecast Server error!')
            else:
                forecast_json = forecast_resp.json()
                if forecast_json:
                    if forecast_json.get('code') == 200:
                        forecast_df = pd.DataFrame(json.loads(forecast_json.get('data')))
                        forecast_df[x_axis] = forecast_cycle(start_date, use_grain, cycle)
                        source_df = splice_data(source_df, forecast_df)
                    else:
                        logger.error(forecast_json.get('msg'))
                        raise Exception(forecast_json.get('msg'))

    return source_df
