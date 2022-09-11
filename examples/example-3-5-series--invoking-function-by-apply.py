"""
-- Core pandas
---- Series methods
------ Invoke a function on every Series value with the apply method
"""
import pandas as pd

google = pd.read_csv("../datasets/google_stocks.csv", parse_dates=["Date"], index_col="Date").squeeze("columns")

func_list = [len, max, min]
for func in func_list:
    print(func(google))
# 3824
# 1287.58
# 49.82

# The function rounds a value above 0.5 up and any value below 0.5 down:
print(round(99.2))  # 99
print(round(99.49))  # 99
print(round(99.5))  # 100

# The two lines below are equivalent
s1 = google.apply(func=round)
s2 = google.apply(round)

print(s1)
# Date
# 2004-08-19      50
# 2004-08-20      54
# 2004-08-23      54
# 2004-08-24      52
# 2004-08-25      53
#               ...
# 2019-10-21    1246
# 2019-10-22    1243
# 2019-10-23    1259
# 2019-10-24    1261
# 2019-10-25    1265
# Name: Close, Length: 3824, dtype: int64

print(s2)
# Date
# 2004-08-19      50
# 2004-08-20      54
# 2004-08-23      54
# 2004-08-24      52
# 2004-08-25      53
#               ...
# 2019-10-21    1246
# 2019-10-22    1243
# 2019-10-23    1259
# 2019-10-24    1261
# 2019-10-25    1265
# Name: Close, Length: 3824, dtype: int64


def get_single_or_multi(pokemon_type):
    if "/" in pokemon_type:
        return "Multi"
    return "Single"


pokemon = pd.read_csv("../datasets/pokemon.csv", index_col="Pokemon").squeeze("columns")
print(pokemon.head())

# Pokemon
# Bulbasaur     Grass / Poison
# Ivysaur       Grass / Poison
# Venusaur      Grass / Poison
# Charmander              Fire
# Charmeleon              Fire
# Name: Type, dtype: object

print(pokemon.apply(get_single_or_multi))
# Pokemon
# Bulbasaur       Multi
# Ivysaur         Multi
# Venusaur        Multi
# Charmander     Single
# Charmeleon     Single
#                 ...
# Stakataka       Multi
# Blacephalon     Multi
# Zeraora        Single
# Meltan         Single
# Melmetal       Single
# Name: Type, Length: 809, dtype: object

print(pokemon.apply(get_single_or_multi).value_counts())
# Multi     405
# Single    404
# Name: Type, dtype: int64


