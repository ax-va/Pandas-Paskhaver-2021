#!/usr/bin/python3
"""
-- Applied pandas
---- Merging, joining, and concatenating
------ Missing values in concatenated DataFrames
"""

import pandas as pd

sports_champions_A = pd.DataFrame(
    data=[
        ["New England Patriots", "Houston Astros"],
        ["Philadelphia Eagles", "Boston Red Sox"]
    ],
    columns=["Football", "Baseball"],
    index=[2017, 2018]
)

print(sports_champions_A)
#                   Football        Baseball
# 2017  New England Patriots  Houston Astros
# 2018   Philadelphia Eagles  Boston Red Sox

sports_champions_B = pd.DataFrame(
    data=[
        ["New England Patriots", "St. Louis Blues"],
        ["Kansas City Chiefs", "Tampa Bay Lightning"]
    ],
    columns=["Football", "Hockey"],
    index=[2019, 2020]
)
print(sports_champions_B)
#                   Football               Hockey
# 2019  New England Patriots      St. Louis Blues
# 2020    Kansas City Chiefs  Tampa Bay Lightning

print(pd.concat(objs=[sports_champions_A, sports_champions_B]))
#                   Football        Baseball               Hockey
# 2017  New England Patriots  Houston Astros                  NaN
# 2018   Philadelphia Eagles  Boston Red Sox                  NaN
# 2019  New England Patriots             NaN      St. Louis Blues
# 2020    Kansas City Chiefs             NaN  Tampa Bay Lightning

sports_champions_C = pd.DataFrame(
    data=[
        ["Pittsburgh Penguins", "Golden State Warriors"],
        ["Washington Capitals", "Golden State Warriors"]
    ],
    columns=["Hockey", "Basketball"],
    index=[2017, 2018]
)
print(sports_champions_C)
#                    Hockey             Basketball
# 2017  Pittsburgh Penguins  Golden State Warriors
# 2018  Washington Capitals  Golden State Warriors

# index duplicates of 2017 and 2018

print(pd.concat(objs=[sports_champions_A, sports_champions_C]))
#                   Football  ...             Basketball
# 2017  New England Patriots  ...                    NaN
# 2018   Philadelphia Eagles  ...                    NaN
# 2017                   NaN  ...  Golden State Warriors
# 2018                   NaN  ...  Golden State Warriors
#
# [4 rows x 4 columns]

# The two lines below are equivalent
pd.concat(objs=[sports_champions_A, sports_champions_C], axis=1)
pd.concat(objs=[sports_champions_A, sports_champions_C], axis="columns")

print(pd.concat(objs=[sports_champions_A, sports_champions_C], axis="columns"))
#                   Football  ...             Basketball
# 2017  New England Patriots  ...  Golden State Warriors
# 2018   Philadelphia Eagles  ...  Golden State Warriors
#
# [2 rows x 4 columns]

