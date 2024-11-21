#!/usr/bin/python3
"""
-- Core pandas
---- Series methods
------ Overwriting a series with the inplace parameter
"""
import pandas as pd

battles = pd.read_csv("../datasets/revolutionary_war.csv",
                      index_col="Start Date",
                      parse_dates=["Start Date"],
                      usecols=["State", "Start Date"]).squeeze("columns")

print(battles.head(3))
# Start Date
# 1774-09-01    Massachusetts
# 1774-12-14    New Hampshire
# 1775-04-19    Massachusetts
# Name: State, dtype: object

print(battles.sort_values().head(3))
# Start Date
# 1781-09-06    Connecticut
# 1779-07-05    Connecticut
# 1777-04-27    Connecticut
# Name: State, dtype: object

print(battles.head(3))
# Start Date
# 1774-09-01    Massachusetts
# 1774-12-14    New Hampshire
# 1775-04-19    Massachusetts
# Name: State, dtype: object

battles_copy = battles.copy()
print(battles_copy.sort_values(inplace=True))
# None

print(battles_copy.head(3))
# Start Date
# 1781-09-06    Connecticut
# 1779-07-05    Connecticut
# 1777-04-27    Connecticut
# Name: State, dtype: object

print(battles.head(3))
# Start Date
# 1774-09-01    Massachusetts
# 1774-12-14    New Hampshire
# 1775-04-19    Massachusetts
# Name: State, dtype: object

# These two lines are technically equivalent:
battles_copy.sort_values(inplace=True)
print(battles_copy.head(3))
# Start Date
# 1781-09-06    Connecticut
# 1779-07-05    Connecticut
# 1777-04-27    Connecticut
# Name: State, dtype: object
sorted_battles = battles.sort_values()
print(sorted_battles.head(3))
# Start Date
# 1781-09-06    Connecticut
# 1779-07-05    Connecticut
# 1777-04-27    Connecticut
# Name: State, dtype: object

print(battles.head(3))
# Start Date
# 1774-09-01    Massachusetts
# 1774-12-14    New Hampshire
# 1775-04-19    Massachusetts
# Name: State, dtype: object

# The pandas development team has discussed removing
# the inplace parameter from the library in future versions.



