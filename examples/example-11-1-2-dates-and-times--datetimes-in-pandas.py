"""
-- Applied pandas
---- Working with dates and times
------ Introducing the Timestamp object
-------- How pandas works with datetimes
"""

import datetime as dt
import pandas as pd

# The two lines below are equivalent
timestamp = pd.Timestamp(1991, 4, 12)
timestamp = pd.Timestamp(year=1991, month=4, day=12)
print(timestamp)  # 1991-04-12 00:00:00
print(repr(timestamp))  # Timestamp('1991-04-12 00:00:00')
print(pd.Timestamp(year=1991, month=4, day=12) == dt.date(year=1991, month=4, day=12))  # True
# FutureWarning:
# Comparison of Timestamp with datetime.date is deprecated in order to match the standard library behavior.
# In a future version these will be considered non-comparable.
# Use 'ts == pd.Timestamp(date)' or 'ts.date() == date' instead.
print(pd.Timestamp(year=1991, month=4, day=12, minute=2) == dt.datetime(year=1991, month=4, day=12, minute=2))  # True
print(pd.Timestamp(year=1991, month=4, day=12, minute=2) == dt.datetime(year=1991, month=4, day=12, minute=1))  # False
# YYYY-MM-DD
print(pd.Timestamp("2015-03-31"))  # 2015-03-31 00:00:00
print(pd.Timestamp("2015/03/31"))  # 2015-03-31 00:00:00
# MM/DD/YYYY
print(pd.Timestamp("03/31/2015"))  # 2015-03-31 00:00:00
print(pd.Timestamp("2021-03-08 08:35:15"))  # 2021-03-08 08:35:15
print(pd.Timestamp("2021-03-08 6:13:29 PM"))  # 2021-03-08 18:13:29
print(pd.Timestamp(dt.date(2000, 2, 3)))  # 2000-02-03 00:00:00
print(pd.Timestamp(dt.datetime(2000, 2, 3, 21, 35, 22)))  # 2000-02-03 21:35:22

my_time = pd.Timestamp(dt.datetime(2000, 2, 3, 21, 35, 22))
print(my_time.year)  # 2000
print(my_time.month)  # 2
print(my_time.day)  # 3
print(my_time.hour)  # 21
print(my_time.minute)  # 35
print(my_time.second)  # 22
