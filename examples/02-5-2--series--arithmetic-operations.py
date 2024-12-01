#!/usr/bin/python3
"""
-- Core pandas
---- The Series object
------ Mathematical operations
-------- Arithmetic operations
"""
import numpy as np
import pandas as pd

s1 = pd.Series(data=[5, np.nan, 15], index=["A", "B", "C"])
print(s1)
# A     5.0
# B     NaN
# C    15.0
# dtype: float64

print(s1 + 3)
# A     8.0
# B     NaN
# C    18.0
# dtype: float64

print(s1.add(3))
# A     8.0
# B     NaN
# C    18.0
# dtype: float64

# The three lines below are equivalent
s1 - 5
s1.sub(5)
s1.subtract(5)
print(s1 - 5)
# A     0.0
# B     NaN
# C    10.0
# dtype: float64

# The three lines below are equivalent
s1 * 2
s1.mul(2)
s1.multiply(2)
print(s1 * 2)
# A    10.0
# B     NaN
# C    30.0
# dtype: float64

# The three lines below are equivalent
s1 / 4
s1.div(4)
s1.divide(4)
print(s1 / 4)
# A    1.25
# B     NaN
# C    3.75
# dtype: float64

# The two lines below are equivalent
s1 // 4
s1.floordiv(4)
print(s1 // 4)
# A    1.0
# B    NaN
# C    3.0
# dtype: float64

# modulo: remainder of division
# The two lines below are equivalent
s1 % 2
s1.mod(2)
print(s1 % 2)
# A    1.0
# B    NaN
# C    1.0
# dtype: float64
