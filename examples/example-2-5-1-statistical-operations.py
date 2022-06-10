"""
Statistical operations
"""
import numpy as np
import pandas as pd

numbers = pd.Series([1, 2, 3, np.nan, 4, 5])
print(numbers)
# 0    1.0
# 1    2.0
# 2    3.0
# 3    NaN
# 4    4.0
# 5    5.0
# dtype: float64

print(repr(numbers))
# 0    1.0
# 1    2.0
# 2    3.0
# 3    NaN
# 4    4.0
# 5    5.0
# dtype: float64

print(numbers.count())  # 5
print(numbers.sum())  # 15.0
print(numbers.sum(skipna=False))  # nan
print(numbers.sum(min_count=3))  # 15.0
print(numbers.sum(min_count=6))  # nan

print(numbers.product())  # 120.0
print(numbers.product(skipna=False))  # nan
print(numbers.product(min_count=3))  # 120.0
print(numbers.product(min_count=6))  # nan

# cumulative sum
print(numbers.cumsum())
# 0     1.0
# 1     3.0
# 2     6.0
# 3     NaN
# 4    10.0
# 5    15.0
# dtype: float64

print(numbers.cumsum(skipna=False))
# 0    1.0
# 1    3.0
# 2    6.0
# 3    NaN
# 4    NaN
# 5    NaN
# dtype: float64

# percent change:
# the current index's value minus the last index's value
# and then divide the sum by the last index's value
print(numbers.pct_change())
# 0         NaN
# 1    1.000000
# 2    0.500000
# 3    0.000000
# 4    0.333333
# 5    0.250000
# dtype: float64

# forward-fill: pandas replaces a nan value with the last valid observation
# The three lines below are equivalent.
numbers.pct_change()
numbers.pct_change(fill_method="pad")
numbers.pct_change(fill_method="ffill")

# backfill: pandas replaces a nan value with the next valid observation
# The two lines below are equivalent
numbers.pct_change(fill_method="bfill")
numbers.pct_change(fill_method="backfill")
print(numbers.pct_change(fill_method="backfill"))
# 0         NaN
# 1    1.000000
# 2    0.500000
# 3    0.333333
# 4    0.000000
# 5    0.250000
# dtype: float64

print(numbers.mean())  # 3.0
# The values from the first half <= median,
# and the values from the second half > median
print(numbers.median())  # 3.0
print(pd.Series([1, 2, 3, 4, 5, 6]).median())  # 3.5
print(pd.Series([1, 2, 3, 4, 5]).median())  # 3.0

# standard deviation
print(numbers.std())  # 1.5811388300841898
print(numbers.min())  # 1.0
print(numbers.max())  # 5.0

animals = pd.Series(["koala", "aardvark", "ab", "aaaaaaaa", "zebra"])
print(animals)
# 0       koala
# 1    aardvark
# 2       zebra
# dtype: object

# sort lexicographically
print(animals.min())  # aaaaaaaa
print(animals.max())  # zebra

print(numbers.describe())
# count    5.000000
# mean     3.000000
# std      1.581139
# min      1.000000
# 25%      2.000000
# 50%      3.000000
# 75%      4.000000
# max      5.000000
# dtype: float64

# random samples
print(numbers.sample(3))
# 0    1.0
# 5    5.0
# 2    3.0
# dtype: float64

print(numbers.sample(3))
# 4    4.0
# 1    2.0
# 3    NaN
# dtype: float64

authors = pd.Series(["Hemingway", "Orwell", "Dostoevsky", "Orwell", "Remarque"])
# unique values as ndarray
print(repr(authors.unique()))
# array(['Hemingway', 'Orwell', 'Dostoevsky', 'Remarque'], dtype=object)

# number of unique values
print(authors.nunique())  # 4
