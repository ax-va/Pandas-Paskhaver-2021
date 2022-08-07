"""
Sort a Series by its index
"""

import pandas as pd

pokemon = pd.read_csv("../datasets/pokemon.csv", index_col="Pokemon").squeeze("columns")
# The two lines below are equivalent
s1 = pokemon.sort_index()
s2 = pokemon.sort_index(ascending=True)
print(s2)
# Pokemon
# Abomasnow        Grass / Ice
# Abra                 Psychic
# Absol                   Dark
# Accelgor                 Bug
# Aegislash      Steel / Ghost
#                   ...
# Zoroark                 Dark
# Zorua                   Dark
# Zubat        Poison / Flying
# Zweilous       Dark / Dragon
# Zygarde      Dragon / Ground
# Name: Type, Length: 809, dtype: object


battles = pd.read_csv("../datasets/revolutionary_war.csv",
                      index_col="Start Date",
                      parse_dates=["Start Date"],
                      usecols=["State", "Start Date"]).squeeze("columns")
print(battles.sort_index())  # sort from the earliest date to the latest
# Start Date
# 1774-09-01    Massachusetts
# 1774-12-14    New Hampshire
# 1775-04-19    Massachusetts
# 1775-04-19    Massachusetts
# 1775-04-20         Virginia
#                   ...
# 1783-01-22         Virginia
# NaT              New Jersey
# NaT                Virginia
# NaT                     NaN
# NaT                     NaN
# Name: State, Length: 232, dtype: object

# NaT stands for not a time

# Display the NaT values first, followed by the sorted datetimes
print(battles.sort_index(na_position="first").head())
# Start Date
# NaT              New Jersey
# NaT                Virginia
# NaT                     NaN
# NaT                     NaN
# 1774-09-01    Massachusetts
# Name: State, dtype: object

print(battles.sort_index(ascending=False).head())
# Start Date
# 1783-01-22    Virginia
# 1782-12-06         NaN
# 1782-10-18         NaN
# 1782-09-13         NaN
# 1782-09-11    Virginia
# Name: State, dtype: object
