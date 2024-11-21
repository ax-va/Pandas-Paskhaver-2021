#!/usr/bin/python3
"""
-- Core pandas
---- The Series object
------ Mathematical operations
-------- Broadcasting
"""
import numpy as np
import pandas as pd

s1 = pd.Series([1, 2, 3], index=["A", "B", "C"])
s2 = pd.Series([4, 5, 6], index=["A", "B", "C"])

print(s1 + s2)
# A    5
# B    7
# C    9
# dtype: int64

s1 = pd.Series(data=[3, 6, np.nan, 12])
s2 = pd.Series(data=[2, 6, np.nan, 12])

# The two lines below are equivalent
print(s1 == s2)
# 0    False
# 1     True
# 2    False
# 3     True
# dtype: bool

print(s1.eq(s2))
# 0    False
# 1     True
# 2    False
# 3     True
# dtype: bool

# The two lines below are equivalent
print(s1 != s2)
# 0     True
# 1    False
# 2     True
# 3    False
# dtype: bool

print(s1.ne(s2))
# 0     True
# 1    False
# 2     True
# 3    False
# dtype: bool

s1 = pd.Series(data=[5, 10, 15], index=["A", "B", "C"])
s2 = pd.Series(data=[4, 8, 12, 14], index=["B", "C", "D", "E"])

print(s1 + s2)
# A     NaN
# B    14.0
# C    23.0
# D     NaN
# E     NaN
# dtype: float64
