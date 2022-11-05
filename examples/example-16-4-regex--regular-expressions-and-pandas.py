#!/usr/bin/python3
"""
-- Appendix E
---- Regular expressions
------ Regular expressions and pandas
"""

import re
import pandas as pd

ice_cream = pd.read_csv("../datasets/ice_cream.csv")
print(ice_cream.head())
#              Brand  ...                                        Description
# 0  Ben and Jerry's  ...  Sweet Cream Ice Cream with Blonde Brownies & a...
# 1  Ben and Jerry's  ...  Peanut Butter Ice Cream with Sweet & Salty Pre...
# 2  Ben and Jerry's  ...  A Cold Mess of Chocolate Ice Cream with Fudge ...
# 3  Ben and Jerry's  ...  Mascarpone Ice Cream with Fudge-Covered Pastry...
# 4  Ben and Jerry's  ...  Toasted Marshmallow Ice Cream with Chocolate C...
#
# [5 rows x 3 columns]

print(ice_cream["Description"].str.extract(r"(\bChocolate\s\w+)").head())
#                   0
# 0               NaN
# 1               NaN
# 2     Chocolate Ice
# 3               NaN
# 4  Chocolate Cookie

print(ice_cream["Description"].str.extract(r"(\bChocolate\s\w+)").dropna().head())
#                    0
# 2      Chocolate Ice
# 4   Chocolate Cookie
# 8      Chocolate Ice
# 9      Chocolate Ice
# 13  Chocolate Cookie

print(type(ice_cream["Description"].str.extract(r"(\bChocolate\s\w+)").dropna()))
# <class 'pandas.core.frame.DataFrame'>

print(type(ice_cream["Description"].str.extract(r"(\bChocolate\s\w+)").dropna().squeeze()))
# <class 'pandas.core.series.Series'>

print(ice_cream["Description"].str.extract(r"(\bChocolate\s\w+)").dropna().squeeze().head())
# 2        Chocolate Ice
# 4     Chocolate Cookie
# 8        Chocolate Ice
# 9        Chocolate Ice
# 13    Chocolate Cookie
# Name: 0, dtype: object

chocolate_flavors = ice_cream["Description"].str.extract(r"(\bChocolate\s\w+)").dropna().squeeze()

print(chocolate_flavors.str.split(r"\s").head())
# 2        [Chocolate, Ice]
# 4     [Chocolate, Cookie]
# 8        [Chocolate, Ice]
# 9        [Chocolate, Ice]
# 13    [Chocolate, Cookie]
# Name: 0, dtype: object

print(chocolate_flavors.str.split(r"\s").str.get(1).head())
# 2        Ice
# 4     Cookie
# 8        Ice
# 9        Ice
# 13    Cookie
# Name: 0, dtype: object

print(chocolate_flavors.str.split(r"\s").str.get(1).value_counts())
# Ice         11
# Cookie       4
# Chip         3
# Sandwich     2
# Cookies      2
# Malt         1
# Mint         1
# Name: 0, dtype: int64
