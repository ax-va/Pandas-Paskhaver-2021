"""
-- Applied pandas
---- Merging, joining, and concatenating
------ Left joins
"""

import pandas as pd

groups1 = pd.read_csv("../datasets/meetup/groups1.csv")
groups2 = pd.read_csv("../datasets/meetup/groups2.csv")
categories = pd.read_csv("../datasets/meetup/categories.csv")
cities = pd.read_csv("../datasets/meetup/cities.csv", dtype={"zip": "string"})
groups = pd.concat(objs=[groups1, groups2], ignore_index=True)

print(groups.head(3))
#    group_id                       name  category_id  city_id
# 0      6388     Alternative Health NYC           14    10001
# 1      6510  Alternative Energy Meetup            4    10001
# 2      8458          NYC Animal Rights           26    10001

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

print(categories.head(3))
#    category_id            category_name
# 0            1           Arts & Culture
# 1            3       Cars & Motorcycles
# 2            4  Community & Environment

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

print(groups.merge(categories, how="left", on="category_id").head())
#    group_id                           name  ...  city_id            category_name
# 0      6388         Alternative Health NYC  ...    10001       Health & Wellbeing
# 1      6510      Alternative Energy Meetup  ...    10001  Community & Environment
# 2      8458              NYC Animal Rights  ...    10001                      NaN
# 3      8940  The New York City Anime Group  ...    10001         Sci-Fi & Fantasy
# 4     10104             NYC Pit Bull Group  ...    10001                      NaN
#
# [5 rows x 5 columns]

groups.merge(categories, how="left", on="category_id").info()
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 16330 entries, 0 to 16329
# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   group_id       16330 non-null  int64
#  1   name           16329 non-null  object
#  2   category_id    16330 non-null  int64
#  3   city_id        16330 non-null  int64
#  4   category_name  8037 non-null   object
# dtypes: int64(3), object(2)
# memory usage: 765.5+ KB

groups.merge(categories, how="right", on="category_id").info()  # default: how="right"
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 8038 entries, 0 to 8037
# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   group_id       8037 non-null   float64
#  1   name           8036 non-null   object
#  2   category_id    8038 non-null   int64
#  3   city_id        8037 non-null   float64
#  4   category_name  8038 non-null   object
# dtypes: float64(2), int64(1), object(2)
# memory usage: 376.8+ KB
