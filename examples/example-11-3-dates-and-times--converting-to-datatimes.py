"""
-- Applied pandas
---- Working with dates and times
------ Converting column or index values to datetimes
"""

import pandas as pd

disney = pd.read_csv("../datasets/disney.csv")
print(disney)
#              Date        High         Low        Open       Close
# 0      1962-01-02    0.096026    0.092908    0.092908    0.092908
# 1      1962-01-03    0.094467    0.092908    0.092908    0.094155
# 2      1962-01-04    0.094467    0.093532    0.094155    0.094155
# 3      1962-01-05    0.094779    0.093844    0.094155    0.094467
# 4      1962-01-08    0.095714    0.092285    0.094467    0.094155
# ...           ...         ...         ...         ...         ...
# 14722  2020-06-26  111.199997  108.019997  110.949997  109.099998
# 14723  2020-06-29  111.570000  108.099998  109.000000  111.519997
# 14724  2020-06-30  112.050003  109.930000  111.500000  111.510002
# 14725  2020-07-01  115.599998  112.290001  112.820000  113.010002
# 14726  2020-07-02  115.099998  112.000000  115.000000  112.180000
#
# [14727 rows x 5 columns]

print(disney.dtypes)
# Date      object
# High     float64
# Low      float64
# Open     float64
# Close    float64
# dtype: object

disney = pd.read_csv("../datasets/disney.csv", parse_dates=["Date"])
print(disney.head())
#         Date      High       Low      Open     Close
# 0 1962-01-02  0.096026  0.092908  0.092908  0.092908
# 1 1962-01-03  0.094467  0.092908  0.092908  0.094155
# 2 1962-01-04  0.094467  0.093532  0.094155  0.094155
# 3 1962-01-05  0.094779  0.093844  0.094155  0.094467
# 4 1962-01-08  0.095714  0.092285  0.094467  0.094155

print(disney.dtypes)
# Date     datetime64[ns]
# High            float64
# Low             float64
# Open            float64
# Close           float64
# dtype: object

string_dates = ["2015-01-01", "2016-02-02", "2017-03-03"]
dt_index = pd.to_datetime(string_dates)
print(dt_index)
# DatetimeIndex(['2015-01-01', '2016-02-02', '2017-03-03'], dtype='datetime64[ns]', freq=None)

print(pd.to_datetime(disney["Date"]))
# 0       1962-01-02
# 1       1962-01-03
# 2       1962-01-04
# 3       1962-01-05
# 4       1962-01-08
#            ...
# 14722   2020-06-26
# 14723   2020-06-29
# 14724   2020-06-30
# 14725   2020-07-01
# 14726   2020-07-02
# Name: Date, Length: 14727, dtype: datetime64[ns]

disney["Date"] = pd.to_datetime(disney["Date"])
print(disney.dtypes)
# Date     datetime64[ns]
# High            float64
# Low             float64
# Open            float64
# Close           float64
# dtype: object