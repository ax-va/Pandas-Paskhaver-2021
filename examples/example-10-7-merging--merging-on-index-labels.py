#!/usr/bin/python3
"""
-- Applied pandas
---- Merging, joining, and concatenating
------ Merging on index labels
"""

import pandas as pd

groups1 = pd.read_csv("../datasets/meetup/groups1.csv")
groups2 = pd.read_csv("../datasets/meetup/groups2.csv")
categories = pd.read_csv("../datasets/meetup/categories.csv")
cities = pd.read_csv("../datasets/meetup/cities.csv", dtype={"zip": "string"})
groups = pd.concat(objs=[groups1, groups2], ignore_index=True)

cities = cities.set_index("id")
print(cities)
#                       city state    zip
# id
# 7093         West New York    NJ  07093
# 10001             New York    NY  10001
# 13417       New York Mills    NY  13417
# 46312         East Chicago    IN  46312
# 56567       New York Mills    MN  56567
# 60064        North Chicago    IL  60064
# 60185         West Chicago    IL  60185
# 60411      Chicago Heights    IL  60411
# 60415        Chicago Ridge    IL  60415
# 60601              Chicago    IL  60290
# 94080  South San Francisco    CA  94080
# 94101        San Francisco    CA  94101
# 95712         Chicago Park    CA  95712


print(groups.merge(cities, how="left", left_on="city_id", right_index=True))
#        group_id                                               name  ...  state    zip
# 0          6388                             Alternative Health NYC  ...     NY  10001
# 1          6510                          Alternative Energy Meetup  ...     NY  10001
# 2          8458                                  NYC Animal Rights  ...     NY  10001
# 3          8940                      The New York City Anime Group  ...     NY  10001
# 4         10104                                 NYC Pit Bull Group  ...     NY  10001
# ...         ...                                                ...  ...    ...    ...
# 16325  26377464                                            Shinect  ...     CA  94101
# 16326  26377698  The art of getting what you want [conference s...  ...     CA  94101
# 16327  26378067                        Streeterville Running Group  ...     IL  60290
# 16328  26378128                                     Just Dance NYC  ...     NY  10001
# 16329  26378470           FREE Arabic Chicago Evanston North Burbs  ...     IL  60290
#
# [16330 rows x 7 columns]

# There is also left_index
