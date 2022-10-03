"""
-- Applied pandas
---- The GroupBy object
------ Creating a GroupBy object from scratch
"""

import pandas as pd

food_data = {
    "Item": ["Banana", "Cucumber", "Orange", "Tomato", "Watermelon"],
    "Type": ["Fruit", "Vegetable", "Fruit", "Vegetable", "Fruit"],
    "Price": [0.99, 1.25, 0.25, 0.33, 3.00]
}
supermarket = pd.DataFrame(data=food_data)
print(supermarket)
#          Item       Type  Price
# 0      Banana      Fruit   0.99
# 1    Cucumber  Vegetable   1.25
# 2      Orange      Fruit   0.25
# 3      Tomato  Vegetable   0.33
# 4  Watermelon      Fruit   3.00

groups = supermarket.groupby("Type")
print(groups)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000028ECB53CEE0>

fruits = groups.get_group("Fruit")
print(fruits)
#          Item   Type  Price
# 0      Banana  Fruit   0.99
# 2      Orange  Fruit   0.25
# 4  Watermelon  Fruit   3.00
print(type(fruits))  # <class 'pandas.core.frame.DataFrame'>

vegetables = groups.get_group("Vegetable")
print(vegetables)
#        Item       Type  Price
# 1  Cucumber  Vegetable   1.25
# 3    Tomato  Vegetable   0.33

print(groups.mean())
#               Price
# Type
# Fruit      1.413333
# Vegetable  0.790000
