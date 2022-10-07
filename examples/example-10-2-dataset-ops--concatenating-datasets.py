"""
-- Applied pandas
---- Merging, Joining, and Concatenating
------ Concatenating Data Sets
"""

import pandas as pd

groups1 = pd.read_csv("../datasets/meetup/groups1.csv")
groups2 = pd.read_csv("../datasets/meetup/groups2.csv")
categories = pd.read_csv("../datasets/meetup/categories.csv")
cities = pd.read_csv("../datasets/meetup/cities.csv", dtype={"zip": "string"})

groups1.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 7999 entries, 0 to 7998
# Data columns (total 4 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   group_id     7999 non-null   int64
#  1   name         7998 non-null   object
#  2   category_id  7999 non-null   int64
#  3   city_id      7999 non-null   int64
# dtypes: int64(3), object(1)
# memory usage: 250.1+ KB

groups2.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 8331 entries, 0 to 8330
# Data columns (total 4 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   group_id     8331 non-null   int64
#  1   name         8331 non-null   object
#  2   category_id  8331 non-null   int64
#  3   city_id      8331 non-null   int64
# dtypes: int64(3), object(1)
# memory usage: 260.5+ KB

groups = pd.concat(objs=[groups1, groups2])
print(groups)
#       group_id  ... city_id
# 0         6388  ...   10001
# 1         6510  ...   10001
# 2         8458  ...   10001
# 3         8940  ...   10001
# 4        10104  ...   10001
# ...        ...  ...     ...
# 8326  26377464  ...   94101
# 8327  26377698  ...   94101
# 8328  26378067  ...   60601
# 8329  26378128  ...   10001
# 8330  26378470  ...   60601
#
# [16330 rows x 4 columns]

# The groups DataFrame contains index duplicates

assert len(groups1) + len(groups2) == len(groups)

groups = pd.concat(objs=[groups1, groups2], ignore_index=True)
print(groups)
#        group_id  ... city_id
# 0          6388  ...   10001
# 1          6510  ...   10001
# 2          8458  ...   10001
# 3          8940  ...   10001
# 4         10104  ...   10001
# ...         ...  ...     ...
# 16325  26377464  ...   94101
# 16326  26377698  ...   94101
# 16327  26378067  ...   60601
# 16328  26378128  ...   10001
# 16329  26378470  ...   60601
#
# [16330 rows x 4 columns]

# Concatenation with MultiIndex
groups = pd.concat(objs=[groups1, groups2], keys=["G1", "G2"])
print(groups)
#          group_id  ... city_id
# G1 0         6388  ...   10001
#    1         6510  ...   10001
#    2         8458  ...   10001
#    3         8940  ...   10001
#    4        10104  ...   10001
# ...           ...  ...     ...
# G2 8326  26377464  ...   94101
#    8327  26377698  ...   94101
#    8328  26378067  ...   60601
#    8329  26378128  ...   10001
#    8330  26378470  ...   60601
#
# [16330 rows x 4 columns]

print(groups.loc["G1"])
#       group_id  ... city_id
# 0         6388  ...   10001
# 1         6510  ...   10001
# 2         8458  ...   10001
# 3         8940  ...   10001
# 4        10104  ...   10001
# ...        ...  ...     ...
# 7994  18875285  ...   10001
# 7995  18876571  ...   10001
# 7996  18876811  ...   60601
# 7997  18877490  ...   10001
# 7998  18878056  ...   10001
#
# [7999 rows x 4 columns]
