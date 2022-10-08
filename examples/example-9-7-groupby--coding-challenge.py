"""
-- Applied pandas
---- The GroupBy object
------ Coding challenge
"""

import pandas as pd
cereals = pd.read_csv("../datasets/cereals.csv")
print(cereals)
#                          Name    Manufacturer  Type  Calories  Fiber  Sugars
# 0                   100% Bran         Nabisco  Cold        70   10.0       6
# 1           100% Natural Bran     Quaker Oats  Cold       120    2.0       8
# 2                    All-Bran       Kellogg's  Cold        70    9.0       5
# 3   All-Bran with Extra Fiber       Kellogg's  Cold        50   14.0       0
# 4              Almond Delight  Ralston Purina  Cold       110    1.0       8
# ..                        ...             ...   ...       ...    ...     ...
# 72                    Triples   General Mills  Cold       110    0.0       3
# 73                       Trix   General Mills  Cold       110    0.0      12
# 74                 Wheat Chex  Ralston Purina  Cold       100    3.0       3
# 75                   Wheaties   General Mills  Cold       100    3.0       3
# 76        Wheaties Honey Gold   General Mills  Cold       110    1.0       8
#
# [77 rows x 6 columns]

# Group the cereals, using the Manufacturer column’s values
manufacturers = cereals.groupby("Manufacturer")
print(manufacturers)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002304F48B6D0>

# Determine the total number of groups, and the number of cereals per group
print(len(manufacturers))  # 7
print(manufacturers.size())
# Manufacturer
# American Home Food Products     1
# General Mills                  22
# Kellogg's                      23
# Nabisco                         6
# Post                            9
# Quaker Oats                     8
# Ralston Purina                  8
# dtype: int64

# Extract the cereals that belong to the manufacturer/group "Nabisco"
print(manufacturers.get_group("Nabisco"))
#                          Name Manufacturer  Type  Calories  Fiber  Sugars
# 0                   100% Bran      Nabisco  Cold        70   10.0       6
# 20     Cream of Wheat (Quick)      Nabisco   Hot       100    1.0       0
# 63             Shredded Wheat      Nabisco  Cold        80    3.0       0
# 64     Shredded Wheat 'n'Bran      Nabisco  Cold        90    4.0       0
# 65  Shredded Wheat spoon size      Nabisco  Cold        90    3.0       0
# 68    Strawberry Fruit Wheats      Nabisco  Cold        90    3.0       5

# Calculate the average of values in the numeric columns for each manufacturer
print(manufacturers.mean())
# Manufacturer
# American Home Food Products  100.000000  0.000000  3.000000
# General Mills                111.363636  1.272727  7.954545
# Kellogg's                    108.695652  2.739130  7.565217
# Nabisco                       86.666667  4.000000  1.833333
# Post                         108.888889  2.777778  8.777778
# Quaker Oats                   95.000000  1.337500  5.250000
# Ralston Purina               115.000000  1.875000  6.125000

# Find the maximum value in the Sugars column for each manufacturer
print(manufacturers["Sugars"].max())
# Manufacturer
# American Home Food Products     3
# General Mills                  14
# Kellogg's                      15
# Nabisco                         6
# Post                           15
# Quaker Oats                    12
# Ralston Purina                 11
# Name: Sugars, dtype: int64

# Find the minimum value in the Fiber column for each manufacturer
print(manufacturers["Fiber"].min())
# Manufacturer
# American Home Food Products    0.0
# General Mills                  0.0
# Kellogg's                      0.0
# Nabisco                        1.0
# Post                           0.0
# Quaker Oats                    0.0
# Ralston Purina                 0.0
# Name: Fiber, dtype: float64

# Extract the cereal with the lowest amount of grams of sugar per manufacturer


def smallest_sugar_row(df):
    return df.nsmallest(1, "Sugars")


print(manufacturers.apply(smallest_sugar_row))
#                                                      Name  ... Sugars
# Manufacturer                                               ...
# American Home Food Products 43                      Maypo  ...      3
# General Mills               11                   Cheerios  ...      1
# Kellogg's                   3   All-Bran with Extra Fiber  ...      0
# Nabisco                     20     Cream of Wheat (Quick)  ...      0
# Post                        33                 Grape-Nuts  ...      3
# Quaker Oats                 57             Quaker Oatmeal  ...     -1
# Ralston Purina              61                  Rice Chex  ...      2
#
# [7 rows x 6 columns]
