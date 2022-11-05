#!/usr/bin/python3
"""
-- Applied pandas
---- Merging, joining, and concatenating
------ Inner joins
"""

import pandas as pd

groups1 = pd.read_csv("../datasets/meetup/groups1.csv")
groups2 = pd.read_csv("../datasets/meetup/groups2.csv")
categories = pd.read_csv("../datasets/meetup/categories.csv")
cities = pd.read_csv("../datasets/meetup/cities.csv", dtype={"zip": "string"})
groups = pd.concat(objs=[groups1, groups2], ignore_index=True)

groups.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 16330 entries, 0 to 16329
# Data columns (total 4 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   group_id     16330 non-null  int64
#  1   name         16329 non-null  object
#  2   category_id  16330 non-null  int64
#  3   city_id      16330 non-null  int64
# dtypes: int64(3), object(1)
# memory usage: 510.4+ KB

categories.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 27 entries, 0 to 26
# Data columns (total 2 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   category_id    27 non-null     int64
#  1   category_name  27 non-null     object
# dtypes: int64(1), object(1)
# memory usage: 560.0+ bytes

# The values in the category_id column appear in both groups and categories.
# An inner join identifies common elements in both data sets
# whether we apply the method to groups or categories.

groups.merge(categories, how="inner", on="category_id").info()
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 8037 entries, 0 to 8036
# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   group_id       8037 non-null   int64
#  1   name           8036 non-null   object
#  2   category_id    8037 non-null   int64
#  3   city_id        8037 non-null   int64
#  4   category_name  8037 non-null   object
# dtypes: int64(3), object(2)
# memory usage: 376.7+ KB

# You can also use a list of columns in the on argument for joins

categories.merge(groups, how="inner", on="category_id").info()
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 8037 entries, 0 to 8036
# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   category_id    8037 non-null   int64
#  1   category_name  8037 non-null   object
#  2   group_id       8037 non-null   int64
#  3   name           8036 non-null   object
#  4   city_id        8037 non-null   int64
# dtypes: int64(3), object(2)
# memory usage: 376.7+ KB

print(groups[groups["category_id"] == 14])
#        group_id  ... city_id
# 0          6388  ...   10001
# 52        54126  ...   10001
# 78        67776  ...   10001
# 121      111855  ...   10001
# 136      129277  ...   60601
# ...         ...  ...     ...
# 16174  26291539  ...   94101
# 16201  26299876  ...   10001
# 16248  26322976  ...   94101
# 16314  26366221  ...   94101
# 16326  26377698  ...   94101
#
# [870 rows x 4 columns]

print(categories[categories["category_id"] == 14])
#    category_id       category_name
# 8           14  Health & Wellbeing

# If in categories, there were three category_id of 14,
# for example, pandas would create 2610 rows (870 x 3)

# You can also use a list of columns in the on argument for joins
