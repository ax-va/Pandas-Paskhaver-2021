#!/usr/bin/python3
"""
-- Applied pandas
---- Working with dates and times
------ Coding challenge
"""

import pandas as pd

# Not complete data from the original .csv, only abbreviated
citi_bike = pd.read_csv("../datasets/citibike.csv")
print(citi_bike.head())
#                  start_time                 stop_time
# 0  2020-06-01 00:00:03.3720  2020-06-01 00:17:46.2080
# 1  2020-06-01 00:00:03.5530  2020-06-01 01:03:33.9360
# 2  2020-06-01 00:00:09.6140  2020-06-01 00:17:06.8330
# 3  2020-06-01 00:00:12.1780  2020-06-01 00:03:58.8640
# 4  2020-06-01 00:00:21.2550  2020-06-01 00:24:18.9650

print(citi_bike.tail())
#                      start_time                 stop_time
# 10983  2020-06-20 14:59:55.7040  2020-06-20 15:24:20.1870
# 10984  2020-06-20 14:59:55.7300  2020-06-20 15:21:42.0820
# 10985  2020-06-20 14:59:56.1290  2020-06-20 15:20:09.6690
# 10986  2020-06-20 14:59:56.2940  2020-06-20 15:11:37.7820
# 10987  2020-06-20 14:59:56.7840  2020-06-20 15:24:33.5000

citi_bike.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10988 entries, 0 to 10987
# Data columns (total 2 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   start_time  10988 non-null  object
#  1   stop_time   10988 non-null  object
# dtypes: object(2)
# memory usage: 171.8+ KB

# Convert the start_time and stop_time columns to store datetime (Timestamp) values
for column in ["start_time", "stop_time"]:
    citi_bike[column] = pd.to_datetime(citi_bike[column])

citi_bike.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10988 entries, 0 to 10987
# Data columns (total 2 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   start_time  10988 non-null  datetime64[ns]
#  1   stop_time   10988 non-null  datetime64[ns]
# dtypes: datetime64[ns](2)
# memory usage: 171.8 KB

# Count the rides that occurred on each day of the week.
# Which weekday is the most popular for a bike ride?
print(citi_bike["start_time"].dt.day_name().head())
# 0    Monday
# 1    Monday
# 2    Monday
# 3    Monday
# 4    Monday
# Name: start_time, dtype: object

print(citi_bike["start_time"].dt.day_name().value_counts())
# Saturday    6742
# Monday      4246
# Name: start_time, dtype: int64

# Count the rides per week for each week within the month
print(citi_bike["start_time"].dt.dayofweek.head())
# 0    0
# 1    0
# 2    0
# 3    0
# 4    0
# Name: start_time, dtype: int64

days_away_from_monday = citi_bike["start_time"].dt.dayofweek
print(days_away_from_monday)
# 0        0
# 1        0
# 2        0
# 3        0
# 4        0
#         ..
# 10983    5
# 10984    5
# 10985    5
# 10986    5
# 10987    5

print(citi_bike["start_time"] - pd.to_timedelta(days_away_from_monday, unit="day"))
# 0       2020-06-01 00:00:03.372
# 1       2020-06-01 00:00:03.553
# 2       2020-06-01 00:00:09.614
# 3       2020-06-01 00:00:12.178
# 4       2020-06-01 00:00:21.255
#                   ...
# 10983   2020-06-15 14:59:55.704
# 10984   2020-06-15 14:59:55.730
# 10985   2020-06-15 14:59:56.129
# 10986   2020-06-15 14:59:56.294
# 10987   2020-06-15 14:59:56.784
# Name: start_time, Length: 10988, dtype: datetime64[ns]

dates_rounded_to_monday = citi_bike["start_time"] - pd.to_timedelta(days_away_from_monday, unit="day")
print(dates_rounded_to_monday.dt.date.head())
# 0    2020-06-01
# 1    2020-06-01
# 2    2020-06-01
# 3    2020-06-01
# 4    2020-06-01
# Name: start_time, dtype: object

print(dates_rounded_to_monday.dt.date.value_counts())
# 2020-06-15    6742
# 2020-06-01    4246
# Name: start_time, dtype: int64

# Calculate the duration of each ride, and save the results to a new duration column
citi_bike["duration"] = citi_bike["stop_time"] - citi_bike["start_time"]
print(citi_bike.head())
#                start_time               stop_time               duration
# 0 2020-06-01 00:00:03.372 2020-06-01 00:17:46.208 0 days 00:17:42.836000
# 1 2020-06-01 00:00:03.553 2020-06-01 01:03:33.936 0 days 01:03:30.383000
# 2 2020-06-01 00:00:09.614 2020-06-01 00:17:06.833 0 days 00:16:57.219000
# 3 2020-06-01 00:00:12.178 2020-06-01 00:03:58.864 0 days 00:03:46.686000
# 4 2020-06-01 00:00:21.255 2020-06-01 00:24:18.965 0 days 00:23:57.710000

# Find the average duration of a bike ride
print(citi_bike["duration"].mean())  # 0 days 00:37:26.853129413
print(repr(citi_bike["duration"].mean()))  # Timedelta('0 days 00:37:26.853129413')

# Extract the five longest bike rides by duration from the data set
print(citi_bike["duration"].sort_values(ascending=False).head())
# 414    20 days 13:17:07.344000
# 64     19 days 18:44:39.048000
# 624    18 days 18:50:56.971000
# 985     9 days 21:38:34.090000
# 1314    6 days 10:19:46.546000
# Name: duration, dtype: timedelta64[ns]

# Alternatively
print(citi_bike.nlargest(n=5, columns="duration"))
#                   start_time               stop_time                duration
# 414  2020-06-01 00:38:34.553 2020-06-21 13:55:41.897 20 days 13:17:07.344000
# 64   2020-06-01 00:06:25.041 2020-06-20 18:51:04.089 19 days 18:44:39.048000
# 624  2020-06-01 01:08:31.796 2020-06-19 19:59:28.767 18 days 18:50:56.971000
# 985  2020-06-01 02:17:50.264 2020-06-10 23:56:24.354  9 days 21:38:34.090000
# 1314 2020-06-01 04:28:24.674 2020-06-07 14:48:11.220  6 days 10:19:46.546000
