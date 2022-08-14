"""
Import CSV
"""

import pandas as pd

# The two lines below are equivalent
pd.read_csv(filepath_or_buffer="../datasets/pokemon.csv")  # DataFrame
d = pd.read_csv("../datasets/pokemon.csv")  # DataFrame
print(d)
#          Pokemon            Type
# 0      Bulbasaur  Grass / Poison
# 1        Ivysaur  Grass / Poison
# 2       Venusaur  Grass / Poison
# 3     Charmander            Fire
# 4     Charmeleon            Fire
# ..           ...             ...
# 804    Stakataka    Rock / Steel
# 805  Blacephalon    Fire / Ghost
# 806      Zeraora        Electric
# 807       Meltan           Steel
# 808     Melmetal           Steel
#
# [809 rows x 2 columns]

d = pd.read_csv("../datasets/pokemon.csv", index_col="Pokemon")  # DataFrame
print(d)
#                        Type
# Pokemon
# Bulbasaur    Grass / Poison
# Ivysaur      Grass / Poison
# Venusaur     Grass / Poison
# Charmander             Fire
# Charmeleon             Fire
# ...                     ...
# Stakataka      Rock / Steel
# Blacephalon    Fire / Ghost
# Zeraora            Electric
# Meltan                Steel
# Melmetal              Steel
#
# [809 rows x 1 columns]

s = pd.read_csv("../datasets/pokemon.csv", index_col="Pokemon").squeeze("columns")  # Series
print(s)
# Pokemon
# Bulbasaur      Grass / Poison
# Ivysaur        Grass / Poison
# Venusaur       Grass / Poison
# Charmander               Fire
# Charmeleon               Fire
#                     ...
# Stakataka        Rock / Steel
# Blacephalon      Fire / Ghost
# Zeraora              Electric
# Meltan                  Steel
# Melmetal                Steel
# Name: Type, Length: 809, dtype: object

d = pd.read_csv("../datasets/google_stocks.csv").head()
print(d)
#          Date  Close
# 0  2004-08-19  49.98
# 1  2004-08-20  53.95
# 2  2004-08-23  54.50
# 3  2004-08-24  52.24
# 4  2004-08-25  52.80

d = pd.read_csv("../datasets/google_stocks.csv",
                parse_dates=["Date"]).head()  # convert to date
print(d)
#         Date  Close
# 0 2004-08-19  49.98
# 1 2004-08-20  53.95
# 2 2004-08-23  54.50
# 3 2004-08-24  52.24
# 4 2004-08-25  52.80

# Datatime as index
s = pd.read_csv("../datasets/google_stocks.csv",
                parse_dates=["Date"],
                index_col="Date").squeeze("columns").head()
print(s)
# 2004-08-19    49.98
# 2004-08-20    53.95
# 2004-08-23    54.50
# 2004-08-24    52.24
# 2004-08-25    52.80
# Name: Close, dtype: float64

d = pd.read_csv("../datasets/revolutionary_war.csv").tail()
print(d)
#                          Battle  Start Date     State
# 227         Siege of Fort Henry   9/11/1782  Virginia
# 228  Grand Assault on Gibraltar   9/13/1782       NaN
# 229   Action of 18 October 1782  10/18/1782       NaN
# 230   Action of 6 December 1782   12/6/1782       NaN
# 231   Action of 22 January 1783   1/22/1783  Virginia

d = pd.read_csv("../datasets/revolutionary_war.csv",
                index_col="Start Date",
                parse_dates=["Start Date"]).tail()
print(d)
#                                 Battle     State
# Start Date
# 1782-09-11         Siege of Fort Henry  Virginia
# 1782-09-13  Grand Assault on Gibraltar       NaN
# 1782-10-18   Action of 18 October 1782       NaN
# 1782-12-06   Action of 6 December 1782       NaN
# 1783-01-22   Action of 22 January 1783  Virginia

d = pd.read_csv("../datasets/revolutionary_war.csv",
                index_col="Start Date",
                parse_dates=["Start Date"],
                usecols=["State", "Start Date"]).squeeze("columns").tail()
print(d)
# Start Date
# 1782-09-11    Virginia
# 1782-09-13         NaN
# 1782-10-18         NaN
# 1782-12-06         NaN
# 1783-01-22    Virginia
# Name: State, dtype: object

