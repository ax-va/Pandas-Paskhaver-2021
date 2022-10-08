"""
-- Core pandas
---- The DataFrame object
------ Similarities between Series and DataFrames
-------- Shared and exclusive attributes of Series and DataFrames
"""
import numpy as np
import pandas as pd

print(repr(pd.Series([1, 2, 3]).dtype))
# dtype('int64')
print(pd.Series([1, 2, 3].index))
# 0    <built-in method index of list object at 0x000...

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"])
print(nba.dtypes)
# Name                object
# Team                object
# Position            object
# Birthday    datetime64[ns]
# Salary               int64
# dtype: object

# Count the number of columns storing each data type
print(nba.dtypes.value_counts())
# object            3
# datetime64[ns]    1
# int64             1
# dtype: int64

print(nba.index)
# RangeIndex(start=0, stop=450, step=1)
# 'start' is inclusive, 'stop' is exclusive

print(nba.columns)
# Index(['Name', 'Team', 'Position', 'Birthday', 'Salary'], dtype='object')

print(nba.ndim)  # 2
print(nba.shape)  # (450, 5)  # 450 rows and 5 columns
print(nba.size)  # 2250  # included missing values
print(nba.count())  # excluding missing values
# Name        450
# Team        450
# Position    450
# Birthday    450
# Salary      450
# dtype: int64
print(nba.count().sum())  # 2250  # no missing values in the dataframe

data = {
    "A": [1, np.nan],
    "B": [2, 3],
}
df = pd.DataFrame(data)
print(df)
#      A  B
# 0  1.0  2
# 1  NaN  3
print(df.size)  # 4
print(df.count())
# A    1
# B    2
# dtype: int64
print(df.count().sum())  # 3
