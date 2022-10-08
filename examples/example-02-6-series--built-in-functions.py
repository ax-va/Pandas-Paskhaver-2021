"""
-- Core pandas
---- The Series object
------ Passing the Series to Python’s built-in functions
"""
import numpy as np
import pandas as pd

cities = pd.Series(data=["San Francisco", "Los Angeles", "Las Vegas", np.nan])
print(cities)
# 0    San Francisco
# 1      Los Angeles
# 2        Las Vegas
# 3              NaN
# dtype: object

print(len(cities))  # 4
print(type(cities))  # <class 'pandas.core.series.Series'>
print(dir(cities))
print(list(cities))
# ['San Francisco', 'Los Angeles', 'Las Vegas', nan]
print(dict(cities))
# {0: 'San Francisco', 1: 'Los Angeles', 2: 'Las Vegas', 3: nan}

print("Las Vegas" in cities)  # False
print(2 in cities)  # True
print("Las Vegas" in cities.values)  # True
print(100 not in cities)  # True
print("Paris" not in cities.values)  # True