#!/usr/bin/python3
"""
-- Core pandas
---- Series methods
------ Sorting a Series
-------- Sorting by values with the sort_values method
"""
import pandas as pd

google = pd.read_csv("../datasets/google_stocks.csv", parse_dates=["Date"], index_col="Date").squeeze("columns")
print(google.sort_values())  # sort prices in ascending order

# Date
# 2004-09-03      49.82
# 2004-09-01      49.94
# 2004-08-19      49.98
# 2004-09-02      50.57
# 2004-09-07      50.60
#                ...
# 2019-04-23    1264.55
# 2019-10-25    1265.13
# 2018-07-26    1268.33
# 2019-04-26    1272.18
# 2019-04-29    1287.58
# Name: Close, Length: 3824, dtype: float64

pokemon = pd.read_csv("../datasets/pokemon.csv", index_col="Pokemon").squeeze("columns")
print(pokemon.sort_values())  # sort strings in alphabetical order
# Pokemon
# Illumise                Bug
# Silcoon                 Bug
# Pinsir                  Bug
# Burmy                   Bug
# Wurmple                 Bug
#                   ...
# Tirtouga       Water / Rock
# Relicanth      Water / Rock
# Corsola        Water / Rock
# Carracosta     Water / Rock
# Empoleon      Water / Steel
# Name: Type, Length: 809, dtype: object

print(pd.Series(data=["Adam", "adam", "Ben"]).sort_values())
# 0    Adam
# 2     Ben
# 1    adam
# dtype: object

print(google.sort_values(ascending=False).head())  # sort values in descending order
# Date
# 2019-04-29    1287.58
# 2019-04-26    1272.18
# 2018-07-26    1268.33
# 2019-10-25    1265.13
# 2019-04-23    1264.55
# Name: Close, dtype: float64

print(pokemon.sort_values(ascending=False).head())
# Pokemon
# Empoleon      Water / Steel
# Corsola        Water / Rock
# Relicanth      Water / Rock
# Carracosta     Water / Rock
# Tirtouga       Water / Rock
# Name: Type, dtype: object

battles = pd.read_csv("../datasets/revolutionary_war.csv",
                      index_col="Start Date",
                      parse_dates=["Start Date"],
                      usecols=["State", "Start Date"]).squeeze("columns")

s1 = battles.sort_values()
s2 = battles.sort_values(na_position="last")  # NaN position, "last" as default
print(s1)
# Start Date
# 1781-09-06    Connecticut
# 1779-07-05    Connecticut
# 1777-04-27    Connecticut
# 1777-09-03       Delaware
# 1777-05-17        Florida
#                  ...
# 1782-08-08            NaN
# 1782-08-25            NaN
# 1782-09-13            NaN
# 1782-10-18            NaN
# 1782-12-06            NaN
# Name: State, Length: 232, dtype: object

s3 = battles.sort_values(na_position="first")  # NaN position
print(s3)
# Start Date
# 1775-09-17         NaN
# 1775-12-31         NaN
# 1776-03-03         NaN
# 1776-03-25         NaN
# 1776-05-18         NaN
#                 ...
# 1781-07-06    Virginia
# 1781-07-01    Virginia
# 1781-06-26    Virginia
# 1781-04-25    Virginia
# 1783-01-22    Virginia
# Name: State, Length: 232, dtype: object

print(battles.dropna().sort_values())  # drop values with NaN
# Start Date
# 1781-09-06    Connecticut
# 1779-07-05    Connecticut
# 1777-04-27    Connecticut
# 1777-09-03       Delaware
# 1777-05-17        Florida
#                  ...
# 1781-07-06       Virginia
# 1781-07-01       Virginia
# 1781-06-26       Virginia
# 1781-04-25       Virginia
# 1783-01-22       Virginia
# Name: State, Length: 162, dtype: object

