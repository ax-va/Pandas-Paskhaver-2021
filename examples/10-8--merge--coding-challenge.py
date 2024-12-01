#!/usr/bin/python3
"""
-- Applied pandas
---- Merging, joining, and concatenating
------ Coding challenge
"""

import pandas as pd

print(pd.read_csv("../datasets/restaurant/week_1_sales.csv").head())
#    Customer ID  Food ID
# 0          537        9
# 1           97        4
# 2          658        1
# 3          202        2
# 4          155        9

week1 = pd.read_csv("../datasets/restaurant/week_1_sales.csv")
week2 = pd.read_csv("../datasets/restaurant/week_2_sales.csv")
print(week1)
#      Customer ID  Food ID
# 0            537        9
# 1             97        4
# 2            658        1
# 3            202        2
# 4            155        9
# ..           ...      ...
# 245          413        9
# 246          926        6
# 247          134        3
# 248          396        6
# 249          535       10

print(week2)
#      Customer ID  Food ID
# 0            688       10
# 1            813        7
# 2            495       10
# 3            189        5
# 4            267        3
# ..           ...      ...
# 245          783       10
# 246          556       10
# 247          547        9
# 248          252        9
# 249          249        6

customers = pd.read_csv("../datasets/restaurant/customers.csv", index_col="ID")
print(customers)
#      First Name Last Name  Gender       Company                     Occupation
# ID
# 1        Joseph   Perkins    Male       Dynazzy  Community Outreach Specialist
# 2      Jennifer   Alvarez  Female          DabZ        Senior Quality Engineer
# 3         Roger     Black    Male       Tagfeed              Account Executive
# 4        Steven     Evans    Male          Fatz               Registered Nurse
# 5          Judy  Morrison  Female       Demivee                Legal Assistant
# ...         ...       ...     ...           ...                            ...
# 996       Debra    Garcia  Female  Dazzlesphere            Structural Engineer
# 997     Douglas    Bishop    Male      Livepath                    Developer I
# 998       Frank  Franklin    Male    Brainverse             Nurse Practicioner
# 999     Jessica     Burns  Female    Babbleblab              Financial Advisor
# 1000      Brian   Daniels    Male         Tazzy     Physical Therapy Assistant
#
# [1000 rows x 5 columns]

foods = pd.read_csv("../datasets/restaurant/foods.csv", index_col="Food ID")
print(foods)
#           Food Item  Price
# Food ID
# 1             Sushi   3.99
# 2           Burrito   9.99
# 3              Taco   2.99
# 4        Quesadilla   4.25
# 5             Pizza   2.49
# 6             Pasta  13.99
# 7             Steak  24.99
# 8             Salad  11.25
# 9             Donut   0.99
# 10            Drink   1.75

# Concatenate the two weeks of sales data into one DataFrame
print(pd.concat(objs = [week1, week2], keys = ["Week 1", "Week 2"]))
#             Customer ID  Food ID
# Week 1 0            537        9
#        1             97        4
#        2            658        1
#        3            202        2
#        4            155        9
# ...                 ...      ...
# Week 2 245          783       10
#        246          556       10
#        247          547        9
#        248          252        9
#        249          249        6
#
# [500 rows x 2 columns]

# Find the customers who ate at the restaurant both weeks
print(week1.merge(right=week2, how="inner", on="Customer ID").head())
#    Customer ID  Food ID_x  Food ID_y
# 0          537          9          5
# 1          155          9          3
# 2          155          1          3
# 3          503          5          8
# 4          503          5          9

# There are duplicates (customers 155 and 503).
# Drop duplicate customers.
print(week1.merge(right=week2, how="inner", on="Customer ID").drop_duplicates(subset=["Customer ID"]).head())
#    Customer ID  Food ID_x  Food ID_y
# 0          537          9          5
# 1          155          9          3
# 3          503          5          8
# 5          550          6          7
# 6          101          7          4

# Find the customers who ate at the restaurant both weeks and ordered the same item each week
print(week1.merge(right=week2, how="inner", on=["Customer ID", "Food ID"]))
#    Customer ID  Food ID
# 0          304        3
# 1          540        3
# 2          937       10
# 3          233        3
# 4           21        4
# 5           21        4
# 6          922        1
# 7          578        5
# 8          578        5

# Identify which customers came in only on Week 1 and only on Week 2
weeks = week1.merge(right=week2, how="outer", on="Customer ID", indicator=True)
print(weeks)
#      Customer ID  Food ID_x  Food ID_y      _merge
# 0            537        9.0        5.0        both
# 1             97        4.0        NaN   left_only
# 2            658        1.0        NaN   left_only
# 3            202        2.0        NaN   left_only
# 4            155        9.0        3.0        both
# ..           ...        ...        ...         ...
# 449          855        NaN        4.0  right_only
# 450          559        NaN       10.0  right_only
# 451          276        NaN        4.0  right_only
# 452          556        NaN       10.0  right_only
# 453          252        NaN        9.0  right_only
#
# [454 rows x 4 columns]

only_in_week_1 = weeks[weeks["_merge"] == "left_only"]
print(only_in_week_1["Customer ID"])
# 1       97
# 2      658
# 3      202
# 6      213
# 7      600
#       ...
# 252    413
# 253    926
# 254    134
# 255    396
# 256    535
# Name: Customer ID, Length: 195, dtype: int64

only_in_week_2 = weeks[weeks["_merge"] == "right_only"]
print(only_in_week_2["Customer ID"])
# 257    688
# 258    813
# 259    495
# 260    495
# 261    495
#       ...
# 449    855
# 450    559
# 451    276
# 452    556
# 453    252
# Name: Customer ID, Length: 197, dtype: int64

# For each row in the week1 DataFrame, pull in the customer’s information from the customers DataFrame
print(week1.merge(right=customers, how="left", left_on="Customer ID", right_index=True).head())
#    Customer ID  Food ID  ...    Company                     Occupation
# 0          537        9  ...   Zoombeat               Registered Nurse
# 1           97        4  ...        Ozu            Account Coordinator
# 2          658        1  ...  Browsebug  Community Outreach Specialist
# 3          202        2  ...  Rhynoodle     Account Representative III
# 4          155        9  ...   Gigazoom     Database Administrator III
