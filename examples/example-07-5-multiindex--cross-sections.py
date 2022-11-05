#!/usr/bin/python3
"""
-- Applied pandas
---- MultiIndex DataFrames
------ Cross-sections
"""
import pandas as pd

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv", index_col=[0, 1, 2], header=[0, 1])
neighborhoods.columns.names = ["Category", "Subcategory"]
neighborhoods = neighborhoods.sort_index(ascending=True)

# The two lines below are equivalent
neighborhoods.xs(key="Lake Nicole", level=1)
neighborhoods.xs(key="Lake Nicole", level="City")
print(neighborhoods.xs(key="Lake Nicole", level=1))
# Category                      Culture         Services
# Subcategory               Restaurants Museums   Police Schools
# State Street
# OR    650 Angela Track              D      C-        D       F
# WY    754 Weaver Turnpike           B      D-        B       D
#       933 Jennifer Burg             C      A+       A-       C

print(neighborhoods.xs(axis="columns", key="Museums", level="Subcategory").head())
# Category                                 Culture
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove         A-
#       Scottstad      082 Leblanc Freeway      C-
#                      114 Jones Garden         D-
#       Stevenshire    238 Andrew Rue            A
# AL    Clarkland      430 Douglas Mission       F

# The two lines below are equivalent
neighborhoods.xs(key=("AK", "238 Andrew Rue"), level=["State", "Street"])
neighborhoods.xs(key=("AK", "238 Andrew Rue"), level=[0, 2])
print(neighborhoods.xs(key=("AK", "238 Andrew Rue"), level=[0, 2]))
# Category        Culture         Services
# Subcategory Restaurants Museums   Police Schools
# City
# Stevenshire          D-       A       A-      A-
