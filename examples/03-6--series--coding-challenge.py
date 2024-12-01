#!/usr/bin/python3
"""
-- Core pandas
---- Series methods
------ Coding challenge
"""
import datetime as dt
import pandas as pd

day = dt.datetime(2020, 12, 26)
print(day.strftime("%A"))  # Saturday

battles_dataframe = pd.read_csv("../datasets/revolutionary_war.csv").head()
print(battles_dataframe)
#                               Battle  Start Date          State
# 0                       Powder Alarm    9/1/1774  Massachusetts
# 1  Storming of Fort William and Mary  12/14/1774  New Hampshire
# 2   Battles of Lexington and Concord   4/19/1775  Massachusetts
# 3                    Siege of Boston   4/19/1775  Massachusetts
# 4                 Gunpowder Incident   4/20/1775       Virginia


days_of_war_series = pd.read_csv(
    filepath_or_buffer="../datasets/revolutionary_war.csv",
    parse_dates=["Start Date"],
    usecols=["Start Date"]
).squeeze("columns")

print(days_of_war_series.head())
# 0   1774-09-01
# 1   1774-12-14
# 2   1775-04-19
# 3   1775-04-19
# 4   1775-04-20
# Name: Start Date, dtype: datetime64[ns]


def get_day_of_week(date):
    return date.strftime("%A")


# print(days_of_war_series.apply(get_day_of_week))
# # ValueError: NaTType does not support strftime

print(days_of_war_series.dropna().apply(get_day_of_week))
# 0       Thursday
# 1      Wednesday
# 2      Wednesday
# 3      Wednesday
# 4       Thursday
#          ...
# 227    Wednesday
# 228       Friday
# 229       Friday
# 230       Friday
# 231    Wednesday
# Name: Start Date, Length: 228, dtype: object

print(days_of_war_series.dropna().apply(get_day_of_week).value_counts())
# Saturday     39
# Friday       39
# Wednesday    32
# Thursday     31
# Sunday       31
# Tuesday      29
# Monday       27
# Name: Start Date, dtype: int64








