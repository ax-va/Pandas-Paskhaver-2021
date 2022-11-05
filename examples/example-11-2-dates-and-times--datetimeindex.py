#!/usr/bin/python3
"""
-- Applied pandas
---- Working with dates and times
------ Storing multiple timestamps in a DatetimeIndex
"""

import datetime as dt
import pandas as pd

print(pd.Series([1, 2, 3]).index)
# RangeIndex(start=0, stop=3, step=1)
print(pd.Series([1, 2, 3], index=["A", "B", "C"]).index)
# Index(['A', 'B', 'C'], dtype='object')

timestamps = [
    pd.Timestamp("2020-01-01"),
    pd.Timestamp("2020-02-01"),
    pd.Timestamp("2020-03-01"),
]
print(pd.Series([1, 2, 3], index=timestamps).index)
# DatetimeIndex(['2020-01-01', '2020-02-01', '2020-03-01'], dtype='datetime64[ns]', freq=None)

datetimes = [
    dt.datetime(2020, 1, 1),
    dt.datetime(2020, 2, 1),
    dt.datetime(2020, 3, 1),
]
print(pd.Series([1, 2, 3], index=datetimes).index)
# DatetimeIndex(['2020-01-01', '2020-02-01', '2020-03-01'], dtype='datetime64[ns]', freq=None)

string_dates = ["2018/01/02", "2016/04/12", "2009/09/07"]
print(pd.DatetimeIndex(data=string_dates))
# DatetimeIndex(['2018-01-02', '2016-04-12', '2009-09-07'], dtype='datetime64[ns]', freq=None)

mixed_dates = [dt.date(2018, 1, 2), "2016/04/12", pd.Timestamp(2009, 9, 7)]
dt_index = pd.DatetimeIndex(mixed_dates)
print(dt_index)
# DatetimeIndex(['2018-01-02', '2016-04-12', '2009-09-07'], dtype='datetime64[ns]', freq=None)

s = pd.Series(data=[100, 200, 300], index=dt_index)
print(s)
# 2018-01-02    100
# 2016-04-12    200
# 2009-09-07    300
# dtype: int64

print(s.sort_index())
# 2009-09-07    300
# 2016-04-12    200
# 2018-01-02    100
# dtype: int64

morning = pd.Timestamp("2020-01-01 11:23:22 AM")
evening = pd.Timestamp("2020-01-01 11:23:22 PM")
print(morning < evening)  # True
print(morning > evening)  # False
