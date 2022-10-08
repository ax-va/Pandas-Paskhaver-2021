"""
-- Applied pandas
---- Merging, joining, and concatenating
------ Introducing the data sets
"""

import pandas as pd

groups1 = pd.read_csv("../datasets/meetup/groups1.csv")
print(groups1.head())
#    group_id                           name  category_id  city_id
# 0      6388         Alternative Health NYC           14    10001
# 1      6510      Alternative Energy Meetup            4    10001
# 2      8458              NYC Animal Rights           26    10001
# 3      8940  The New York City Anime Group           29    10001
# 4     10104             NYC Pit Bull Group           26    10001

# category_id and city_id are foreign keys

groups2 = pd.read_csv("../datasets/meetup/groups2.csv")
print(groups2.head(1))
#    group_id          name  category_id  city_id
# 0  18879327  BachataMania            5    10001

categories = pd.read_csv("../datasets/meetup/categories.csv")
print(categories.head())
#    category_id            category_name
# 0            1           Arts & Culture
# 1            3       Cars & Motorcycles
# 2            4  Community & Environment
# 3            5                  Dancing
# 4            6     Education & Learning

cities = pd.read_csv("../datasets/meetup/cities.csv")
print(cities.head())
#       id            city state    zip
# 0   7093   West New York    NJ   7093
# 1  10001        New York    NY  10001
# 2  13417  New York Mills    NY  13417
# 3  46312    East Chicago    IN  46312
# 4  56567  New York Mills    MN  56567

cities = pd.read_csv("../datasets/meetup/cities.csv", dtype={"zip": "string"})
print(cities.head())
#       id            city state    zip
# 0   7093   West New York    NJ  07093
# 1  10001        New York    NY  10001
# 2  13417  New York Mills    NY  13417
# 3  46312    East Chicago    IN  46312
# 4  56567  New York Mills    MN  56567

