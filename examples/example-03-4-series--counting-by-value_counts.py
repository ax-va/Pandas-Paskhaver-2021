#!/usr/bin/python3
"""
-- Core pandas
---- Series methods
------ Count values with the value_counts method
"""
import pandas as pd

pokemon = pd.read_csv("../datasets/pokemon.csv", index_col="Pokemon").squeeze("columns")

print(pokemon.head())
# Pokemon
# Bulbasaur     Grass / Poison
# Ivysaur       Grass / Poison
# Venusaur      Grass / Poison
# Charmander              Fire
# Charmeleon              Fire
# Name: Type, dtype: object

s = pokemon.value_counts()  # new Series object
print(s)
# Normal                65
# Water                 61
# Grass                 38
# Psychic               35
# Fire                  30
#                       ..
# Fire / Psychic         1
# Normal / Ground        1
# Psychic / Fighting     1
# Dark / Ghost           1
# Fire / Ghost           1
# Name: Type, Length: 159, dtype: int64

# Equivalent:
print(len(pokemon.value_counts()))  # 159
print(pokemon.nunique())  # 159

print(pokemon.value_counts(ascending=True))
# Fire / Ghost         1
# Fighting / Dark      1
# Fighting / Steel     1
# Normal / Ground      1
# Fire / Psychic       1
#                     ..
# Fire                30
# Psychic             35
# Grass               38
# Water               61
# Normal              65
# Name: Type, Length: 159, dtype: int64

frequency = pokemon.value_counts(normalize=True)
print(frequency.head())
# Normal     0.080346
# Water      0.075402
# Grass      0.046972
# Psychic    0.043263
# Fire       0.037083
# Name: Type, dtype: float64

frequency_in_percentages = pokemon.value_counts(normalize=True) * 100
print(frequency_in_percentages.head())
# Normal     8.034611
# Water      7.540173
# Grass      4.697157
# Psychic    4.326329
# Fire       3.708282
# Name: Type, dtype: float64

print(frequency_in_percentages.round(2).head())
# Normal     8.03
# Water      7.54
# Grass      4.70
# Psychic    4.33
# Fire       3.71
# Name: Type, dtype: float64

google = pd.read_csv("../datasets/google_stocks.csv", parse_dates=["Date"], index_col="Date").squeeze("columns")
print(google.value_counts().head())
# 287.68    3
# 194.27    3
# 307.10    3
# 288.92    3
# 290.41    3
# Name: Close, dtype: int6

print(google.max())  # 1287.58
print(google.min())  # 49.82

buckets = [0, 200, 400, 600, 800, 1000, 1200, 1400]
print(google.value_counts(bins=buckets))
# (200.0, 400.0]      1568
# (-0.001, 200.0]      595
# (400.0, 600.0]       575
# (1000.0, 1200.0]     406
# (600.0, 800.0]       380
# (800.0, 1000.0]      207
# (1200.0, 1400.0]      93
# Name: Close, dtype: int64

# Next two methods are equivalent:
print(google.value_counts(bins=buckets).sort_index())
# (-0.001, 200.0]      595
# (200.0, 400.0]      1568
# (400.0, 600.0]       575
# (600.0, 800.0]       380
# (800.0, 1000.0]      207
# (1000.0, 1200.0]     406
# (1200.0, 1400.0]      93
# Name: Close, dtype: int64

print(google.value_counts(bins=buckets, sort=False))
# (-0.001, 200.0]      595
# (200.0, 400.0]      1568
# (400.0, 600.0]       575
# (600.0, 800.0]       380
# (800.0, 1000.0]      207
# (1000.0, 1200.0]     406
# (1200.0, 1400.0]      93
# Name: Close, dtype: int64


# Calculate the difference between the maximum and minimum values
# in the Series and divide the range into the specified number of bins.
print(google.value_counts(bins=6, sort=False))
# (48.581, 256.113]      1204
# (256.113, 462.407]     1104
# (462.407, 668.7]        507
# (668.7, 874.993]        380
# (874.993, 1081.287]     292
# (1081.287, 1287.58]     337
# Name: Close, dtype: int64

battles = pd.read_csv("../datasets/revolutionary_war.csv",
                      index_col="Start Date",
                      parse_dates=["Start Date"],
                      usecols=["State", "Start Date"]).squeeze("columns")

print(battles.head())
# Start Date
# 1774-09-01    Massachusetts
# 1774-12-14    New Hampshire
# 1775-04-19    Massachusetts
# 1775-04-19    Massachusetts
# 1775-04-20         Virginia
# Name: State, dtype: object

print(battles.value_counts().head())
# South Carolina    31
# New York          28
# New Jersey        24
# Virginia          21
# Massachusetts     11
# Name: State, dtype: int64

print(battles.value_counts(dropna=False).head())
# NaN               70
# South Carolina    31
# New York          28
# New Jersey        24
# Virginia          21
# Name: State, dtype: int64

print(battles.index)
# DatetimeIndex(['1774-09-01', '1774-12-14', '1775-04-19', '1775-04-19',
#                '1775-04-20', '1775-05-10', '1775-05-27', '1775-06-11',
#                '1775-06-17', '1775-08-08',
#                ...
#                '1782-08-08', '1782-08-15', '1782-08-19', '1782-08-26',
#                '1782-08-25', '1782-09-11', '1782-09-13', '1782-10-18',
#                '1782-12-06', '1783-01-22'],
#               dtype='datetime64[ns]', name='Start Date', length=232, freq=None)

print(battles.index.value_counts())
# 1781-04-25    2
# 1781-05-22    2
# 1780-08-18    2
# 1781-09-13    2
# 1782-03-16    2
#              ..
# 1778-06-30    1
# 1778-07-03    1
# 1778-07-27    1
# 1778-08-21    1
# 1783-01-22    1
# Name: Start Date, Length: 217, dtype: int64


