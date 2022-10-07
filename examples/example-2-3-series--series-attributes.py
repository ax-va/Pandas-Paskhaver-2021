"""
-- Core pandas
---- The Series Object
------ Series Attributes
"""
import pandas as pd

calorie_info = {
    "Cereal": 125,
    "Chocolate Bar": 406,
    "Ice Cream Sundae": 342,
}
diet = pd.Series(calorie_info)
print(repr(diet.values))
# array([125, 406, 342], dtype=int64)

print(type(diet.values))
# <class 'numpy.ndarray'>

print(diet.index)
# Index(['Cereal', 'Chocolate Bar', 'Ice Cream Sundae'], dtype='object')

print(type(diet.index))
# <class 'pandas.core.indexes.base.Index'>

print(diet.dtype)  # int64
print(diet.size)  # 3
print(diet.shape)  # (3,)
print(diet.is_unique)  # True
print(pd.Series(data=[3, 3]).is_unique)  # False
print(pd.Series(data=[1, 3, 6]).is_monotonic)  # True
print(pd.Series(data=[1, 3, 3]).is_monotonic)  # True
print(pd.Series(data=[1, 4, 3]).is_monotonic)  # False
