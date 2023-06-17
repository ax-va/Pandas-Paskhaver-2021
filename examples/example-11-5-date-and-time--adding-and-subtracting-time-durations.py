#!/usr/bin/python3
"""
-- Applied pandas
---- Working with dates and times
------ Adding and subtracting durations of time
"""

import pandas as pd

disney = pd.read_csv("../datasets/disney.csv", parse_dates=["Date"])

print(pd.DateOffset(days=5, months=4, years=3))
# <DateOffset: days=5, months=4, years=3>

print(disney["Date"].head())
# 0   1962-01-02
# 1   1962-01-03
# 2   1962-01-04
# 3   1962-01-05
# 4   1962-01-08
# Name: Date, dtype: datetime64[ns]

print((disney["Date"] + pd.DateOffset(days = 5)).head())
# 0   1962-01-07
# 1   1962-01-08
# 2   1962-01-09
# 3   1962-01-10
# 4   1962-01-13
# Name: Date, dtype: datetime64[ns]

print((disney["Date"] - pd.DateOffset(days=3)).head())
# 0   1961-12-30
# 1   1961-12-31
# 2   1962-01-01
# 3   1962-01-02
# 4   1962-01-05
# Name: Date, dtype: datetime64[ns]

print((disney["Date"] + pd.DateOffset(days=10, hours=6)).head())
# 0   1962-01-12 06:00:00
# 1   1962-01-13 06:00:00
# 2   1962-01-14 06:00:00
# 3   1962-01-15 06:00:00
# 4   1962-01-18 06:00:00
# Name: Date, dtype: datetime64[ns]

print((disney["Date"] - pd.DateOffset(years=1, months=3, days=10, hours=6, minutes=3)).head())
# 0   1960-09-21 17:57:00
# 1   1960-09-22 17:57:00
# 2   1960-09-23 17:57:00
# 3   1960-09-24 17:57:00
# 4   1960-09-27 17:57:00
# Name: Date, dtype: datetime64[ns]

# The DateOffset constructor supports additional keyword parameters for 'seconds', 'microseconds', and 'nanoseconds'
