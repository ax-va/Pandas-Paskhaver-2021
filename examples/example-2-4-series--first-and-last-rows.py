"""
-- Core pandas
---- The Series Object
------ Retrieving the First and Last Rows
"""
import pandas as pd

values = range(0, 500, 5)
nums = pd.Series(data=values)
print(nums)
# 0       0
# 1       5
# 2      10
# 3      15
# 4      20
#      ...
# 95    475
# 96    480
# 97    485
# 98    490
# 99    495
# Length: 100, dtype: int64

print(nums.head(3))
# 0     0
# 1     5
# 2    10
# dtype: int64

head = nums.head(3)
print(head)
# 0     0
# 1     5
# 2    10
# dtype: int64

print(type(head))  # <class 'pandas.core.series.Series'>
print(head.size)  # 3

print(nums.head())
# 0     0
# 1     5
# 2    10
# 3    15
# 4    20
# dtype: int64

print(nums.tail(6))
# 94    470
# 95    475
# 96    480
# 97    485
# 98    490
# 99    495
# dtype: int64

print(nums.tail())
# 95    475
# 96    480
# 97    485
# 98    490
# 99    495
# dtype: int64
