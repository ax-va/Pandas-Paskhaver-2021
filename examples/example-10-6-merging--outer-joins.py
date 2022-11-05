#!/usr/bin/python3
"""
-- Applied pandas
---- Merging, joining, and concatenating
------ Outer joins
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

cities.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 13 entries, 0 to 12
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   id      13 non-null     int64
#  1   city    13 non-null     object
#  2   state   13 non-null     object
#  3   zip     13 non-null     string
# dtypes: int64(1), object(2), string(1)
# memory usage: 544.0+ bytes

# An outer join combines all records across two data sets

print(groups.merge(cities, how="outer", left_on="city_id", right_on="id"))
#          group_id                                     name  ...  state    zip
# 0          6388.0                   Alternative Health NYC  ...     NY  10001
# 1          6510.0                Alternative Energy Meetup  ...     NY  10001
# 2          8458.0                        NYC Animal Rights  ...     NY  10001
# 3          8940.0            The New York City Anime Group  ...     NY  10001
# 4         10104.0                       NYC Pit Bull Group  ...     NY  10001
# ...           ...                                      ...  ...    ...    ...
# 16329  24303427.0  Midwest FPGA/AI/Machine Learning Meetup  ...     IL  60064
# 16330         NaN                                      NaN  ...     NY  13417
# 16331         NaN                                      NaN  ...     IN  46312
# 16332         NaN                                      NaN  ...     MN  56567
# 16333         NaN                                      NaN  ...     CA  95712
#
# [16334 rows x 8 columns]

print(set(groups["city_id"]))
# {94080, 60064, 10001, 94101, 60185, 7093, 60601, 60411, 60415}
print(set(cities["id"]))
# {60064, 94080, 95712, 60601, 46312, 13417, 10001, 7093, 94101, 56567, 60185, 60411, 60415}
print(set(cities["id"]).difference(set(groups["city_id"])))
# {95712, 13417, 46312, 56567}

# The cities DataFrame contains four rows more than the groups DataFrame

print(groups.merge(cities, how="outer", left_on="city_id", right_on="id", indicator=True))
#          group_id                                     name  ...    zip      _merge
# 0          6388.0                   Alternative Health NYC  ...  10001        both
# 1          6510.0                Alternative Energy Meetup  ...  10001        both
# 2          8458.0                        NYC Animal Rights  ...  10001        both
# 3          8940.0            The New York City Anime Group  ...  10001        both
# 4         10104.0                       NYC Pit Bull Group  ...  10001        both
# ...           ...                                      ...  ...    ...         ...
# 16329  24303427.0  Midwest FPGA/AI/Machine Learning Meetup  ...  60064        both
# 16330         NaN                                      NaN  ...  13417  right_only
# 16331         NaN                                      NaN  ...  46312  right_only
# 16332         NaN                                      NaN  ...  56567  right_only
# 16333         NaN                                      NaN  ...  95712  right_only
#
# [16334 rows x 9 columns]

outer_join = groups.merge(cities, how="outer", left_on="city_id", right_on="id", indicator=True)
in_right_only = outer_join["_merge"] == "right_only"
print(outer_join[in_right_only])
#        group_id name  category_id  ...  state    zip      _merge
# 16330       NaN  NaN          NaN  ...     NY  13417  right_only
# 16331       NaN  NaN          NaN  ...     IN  46312  right_only
# 16332       NaN  NaN          NaN  ...     MN  56567  right_only
# 16333       NaN  NaN          NaN  ...     CA  95712  right_only
#
# [4 rows x 9 columns]



