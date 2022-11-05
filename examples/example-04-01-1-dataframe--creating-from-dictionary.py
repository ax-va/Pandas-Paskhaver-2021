#!/usr/bin/python3
"""
-- Core pandas
---- The DataFrame object
------ Overview of a DataFrame
-------- Creating a DataFrame from a dictionary
"""
import pandas as pd

city_data = {
    "City": ["New York City", "Paris", "Barcelona", "Rome"],
    "Country": ["United States", "France", "Spain", "Italy"],
    "Population": [8600000, 2141000, 5515000, 2873000]
}

cities = pd.DataFrame(city_data)
print(cities)
#             City        Country  Population
# 0  New York City  United States     8600000
# 1          Paris         France     2141000
# 2      Barcelona          Spain     5515000
# 3           Rome          Italy     2873000


# The two lines below are equivalent
d1 = cities.transpose()
d2 = cities.T

print(d1)
#                         0        1          2        3
# City        New York City    Paris  Barcelona     Rome
# Country     United States   France      Spain    Italy
# Population        8600000  2141000    5515000  2873000

print(d2)
#                         0        1          2        3
# City        New York City    Paris  Barcelona     Rome
# Country     United States   France      Spain    Italy
# Population        8600000  2141000    5515000  2873000
