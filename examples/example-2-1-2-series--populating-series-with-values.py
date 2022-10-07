"""
-- Core pandas
---- The Series Object
------ Overview of a Series
-------- Populate Series with Values
"""
import pandas as pd

ice_cream_flavors = [
    "Chocolate",
    "Vanilla",
    "Strawberry",
    "Rum Raisin",
]
print(pd.Series(ice_cream_flavors))
# 0     Chocolate
# 1       Vanilla
# 2    Strawberry
# 3    Rum Raisin
# dtype: object

pd.Series(
    data=None,
    index=None,
    dtype=None,
    name=None,
    copy=False,
    fastpath=False,
)
# FutureWarning: The default dtype for empty Series will be 'object' instead of
# 'float64' in a future version. Specify a dtype explicitly to silence this warning.

print(pd.Series(data=ice_cream_flavors))
# 0     Chocolate
# 1       Vanilla
# 2    Strawberry
# 3    Rum Raisin
# dtype: object

