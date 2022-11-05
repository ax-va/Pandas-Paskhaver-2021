#!/usr/bin/python3
"""
-- Applied pandas
---- Working with dates and times
------ Introducing the Timestamp object
-------- How Python works with datetimes
"""

import datetime as dt

# The two lines below are equivalent
birthday = dt.date(1991, 4, 12)
birthday = dt.date(year=1991, month=4, day=12)
print(birthday)  # 1991-04-12
print(repr(birthday))  # datetime.date(1991, 4, 12)
print(birthday.year)  # 1991
print(birthday.month)  # 4
print(birthday.day)  # 12

# birthday.month = 10
# AttributeError: attribute 'month' of 'datetime.date' objects is not writable

# print(dt.date())
# TypeError: function missing required argument 'year' (pos 1)

# The two lines below are equivalent
alarm_clock1 = dt.time(6, 43, 25)
alarm_clock2 = dt.time(hour=6, minute=43, second=25)
print(alarm_clock1)  # 06:43:25
print(repr(alarm_clock2))  # datetime.time(6, 43, 25)
print(dt.time())  # 00:00:00
print(dt.time(hour=9, second=42))  # 09:00:42
print(alarm_clock1.hour)  # 6
print(alarm_clock1.minute)  # 43
print(alarm_clock1.second)  # 25

# The two lines below are equivalent
moon_landing1 = dt.datetime(1969, 7, 20, 22, 56, 20)
moon_landing2 = dt.datetime(year=1969, month=7, day=20, hour=22, minute=56, second=20)
print(moon_landing1)  # 1969-07-20 22:56:20
print(repr(moon_landing2))  # datetime.datetime(1969, 7, 20, 22, 56, 20)
print(dt.datetime(2020, 1, 1))  # 2020-01-01 00:00:00

time_delta = dt.timedelta(weeks=8, days=6, hours=3, minutes=58, seconds=12)
print(time_delta)  # 62 days, 3:58:12
print(repr(time_delta))  # datetime.timedelta(days=62, seconds=14292)
print(moon_landing1 + time_delta)  # 1969-09-21 02:54:32
print(moon_landing1 - time_delta)  # 1969-05-19 18:58:08

