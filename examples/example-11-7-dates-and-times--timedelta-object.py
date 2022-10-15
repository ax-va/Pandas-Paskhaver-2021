"""
-- Applied pandas
---- Working with dates and times
------ The Timedelta object
"""

import pandas as pd

duration = pd.Timedelta(days=8, hours=7, minutes=6, seconds=5)
print(duration)  # 8 days 07:06:05
print(repr(duration))  # Timedelta('8 days 07:06:05')

duration = pd.to_timedelta("3 hours, 5 minutes, 12 seconds")
print(duration)  # 0 days 03:05:12
print(repr(duration))  # Timedelta('0 days 03:05:12')

duration = pd.to_timedelta(5, unit="hour")
print(duration)  # 0 days 05:00:00
print(repr(duration))  # Timedelta('0 days 05:00:00')

durations = pd.to_timedelta([5, 10, 15], unit="day")
print(durations)
# TimedeltaIndex(['5 days', '10 days', '15 days'], dtype='timedelta64[ns]', freq=None)

print(pd.Timestamp("1999-02-05") - pd.Timestamp("1998-05-24"))
# 257 days 00:00:00
print(repr(pd.Timestamp("1999-02-05") - pd.Timestamp("1998-05-24")))
# Timedelta('257 days 00:00:00')

deliveries = pd.read_csv("../datasets/deliveries.csv")
print(deliveries)
#     order_date delivery_date
# 0      5/24/98        2/5/99
# 1      4/22/92        3/6/98
# 2      2/10/91       8/26/92
# 3      7/21/92      11/20/97
# 4       9/2/93       6/10/98
# ..         ...           ...
# 496    6/24/91        2/2/96
# 497     9/9/91       3/30/98
# 498   11/16/90       4/27/98
# 499     6/3/93       6/13/93
# 500     1/4/90       10/3/91
#
# [501 rows x 2 columns]

# deliveries["order_date"] = pd.to_datetime(deliveries["order_date"])
# deliveries["delivery_date"] = pd.to_datetime(deliveries["delivery_date"])
for column in ["order_date", "delivery_date"]:
    deliveries[column] = pd.to_datetime(deliveries[column])

print(deliveries.head())
#   order_date delivery_date
# 0 1998-05-24    1999-02-05
# 1 1992-04-22    1998-03-06
# 2 1991-02-10    1992-08-26
# 3 1992-07-21    1997-11-20
# 4 1993-09-02    1998-06-10

# Calculate the duration of each shipment
print((deliveries["delivery_date"] - deliveries["order_date"]).head())
# 0    257 days
# 1   2144 days
# 2    563 days
# 3   1948 days
# 4   1742 days
# dtype: timedelta64[ns]

deliveries["duration"] = deliveries["delivery_date"] - deliveries["order_date"]
print(deliveries.head())
#   order_date delivery_date  duration
# 0 1998-05-24    1999-02-05  257 days
# 1 1992-04-22    1998-03-06 2144 days
# 2 1991-02-10    1992-08-26  563 days
# 3 1992-07-21    1997-11-20 1948 days
# 4 1993-09-02    1998-06-10 1742 days

print(deliveries.dtypes)
# order_date        datetime64[ns]
# delivery_date     datetime64[ns]
# duration         timedelta64[ns]
# dtype: object

print((deliveries["delivery_date"] - deliveries["duration"]).head())
# 0   1998-05-24
# 1   1992-04-22
# 2   1991-02-10
# 3   1992-07-21
# 4   1993-09-02
# dtype: datetime64[ns]

print((deliveries["delivery_date"] - deliveries["duration"] == deliveries["order_date"]).head())
# 0    True
# 1    True
# 2    True
# 3    True
# 4    True
# dtype: bool

print((deliveries["order_date"] + deliveries["duration"]).head())
# 0   1999-02-05
# 1   1998-03-06
# 2   1992-08-26
# 3   1997-11-20
# 4   1998-06-10
# dtype: datetime64[ns]

print((deliveries["order_date"] + deliveries["duration"] == deliveries["delivery_date"]).head())
# 0    True
# 1    True
# 2    True
# 3    True
# 4    True
# dtype: bool

print(deliveries.sort_values("duration"))
#     order_date delivery_date  duration
# 454 1990-05-24    1990-06-01    8 days
# 294 1994-08-11    1994-08-20    9 days
# 10  1998-05-10    1998-05-19    9 days
# 499 1993-06-03    1993-06-13   10 days
# 143 1997-09-20    1997-10-06   16 days
# ..         ...           ...       ...
# 152 1990-09-18    1999-12-19 3379 days
# 62  1990-04-02    1999-08-16 3423 days
# 458 1990-02-13    1999-11-15 3562 days
# 145 1990-03-07    1999-12-25 3580 days
# 448 1990-01-20    1999-11-12 3583 days
#
# [501 rows x 3 columns]

print(deliveries["duration"].min())
# 8 days 00:00:00
print(repr(deliveries["duration"].min()))
# Timedelta('8 days 00:00:00')

print(deliveries["duration"].max())
# 3583 days 00:00:00
print(repr(deliveries["duration"].max()))
# Timedelta('3583 days 00:00:00')

print(deliveries["duration"].mean())
# 1217 days 22:53:53.532934128
print(repr(deliveries["duration"].mean()))
# Timedelta('1217 days 22:53:53.532934128')

# Filter the DataFrame for packages that took more than 365 days to deliver
# The two lines below are equivalent
print((deliveries["duration"] > pd.Timedelta(days=365)).head())
print((deliveries["duration"] > "365 days").head())
# 0    False
# 1     True
# 2     True
# 3     True
# 4     True
# Name: duration, dtype: bool

print(deliveries[deliveries["duration"] > "365 days"].head())
#   order_date delivery_date  duration
# 1 1992-04-22    1998-03-06 2144 days
# 2 1991-02-10    1992-08-26  563 days
# 3 1992-07-21    1997-11-20 1948 days
# 4 1993-09-02    1998-06-10 1742 days
# 6 1990-01-25    1994-10-02 1711 days

long_time = deliveries["duration"] > "2000 days, 8 hours, 4 minutes"
print(deliveries[long_time].head())
#    order_date delivery_date  duration
# 1  1992-04-22    1998-03-06 2144 days
# 7  1992-02-23    1998-12-30 2502 days
# 11 1992-10-17    1998-10-06 2180 days
# 12 1992-05-30    1999-08-15 2633 days
# 15 1990-01-20    1998-07-24 3107 days
