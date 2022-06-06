"""
Customize the Series index
"""
import pandas as pd

ice_cream_flavors = [
    "Chocolate",
    "Vanilla",
    "Strawberry",
    "Rum Raisin",
]
days_of_week = ("Monday", "Wednesday", "Friday", "Saturday")
# The two lines below are equivalent
s1 = pd.Series(ice_cream_flavors, days_of_week)
s2 = pd.Series(data=ice_cream_flavors, index=days_of_week)
print(s2)
# Monday        Chocolate
# Wednesday       Vanilla
# Friday       Strawberry
# Saturday     Rum Raisin
# dtype: object

print(s2[1])  # Vanilla
print(s2["Wednesday"])  # Vanilla

days_of_week = ("Monday", "Wednesday", "Friday", "Wednesday")
s2 = pd.Series(data=ice_cream_flavors, index=days_of_week)
print(s2)
# Monday        Chocolate
# Wednesday       Vanilla
# Friday       Strawberry
# Wednesday    Rum Raisin
# dtype: object

print(s2["Wednesday"])
# Wednesday       Vanilla
# Wednesday    Rum Raisin
# dtype: object

bunch_of_bools = [True, False, False]
print(pd.Series(bunch_of_bools))
# 0     True
# 1    False
# 2    False
# dtype: bool

stock_prices = [985.32, 950.44]
time_of_day = ["Open", "Close"]
print(pd.Series(data=stock_prices, index=time_of_day))
# Open     985.32
# Close    950.44
# dtype: float64

lucky_numbers = [4, 8, 15, 16, 23, 42]
print(pd.Series(lucky_numbers))
# 0     4
# 1     8
# 2    15
# 3    16
# 4    23
# 5    42
# dtype: int64

print(pd.Series(lucky_numbers, dtype="float"))
# 0     4.0
# 1     8.0
# 2    15.0
# 3    16.0
# 4    23.0
# 5    42.0
# dtype: float64
