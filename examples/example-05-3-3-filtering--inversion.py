"""
-- Core pandas
---- Filtering a DataFrame
------ Filtering by multiple conditions
-------- Inversion with ~
"""
import numpy as np
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])
employees["Mgmt"] = employees["Mgmt"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")
employees["Team"] = employees["Team"].astype("category")

my_series = pd.Series([True, False, True])
print(my_series)
# 0     True
# 1    False
# 2     True
# dtype: bool

print(~my_series)
# 0    False
# 1     True
# 2    False
# dtype: bool

print(employees[~(employees["Salary"] >= 100000)].head())
#   First Name  Gender Start Date   Salary  Mgmt         Team
# 0    Douglas    Male 1993-08-06      NaN  True    Marketing
# 1     Thomas    Male 1996-03-31  61933.0  True          NaN
# 6       Ruby  Female 1987-08-17  65476.0  True      Product
# 7        NaN  Female 2015-07-20  45906.0  True      Finance
# 8     Angela  Female 2005-11-22  95570.0  True  Engineering

print(np.NaN > 100)  # False
print(np.NaN < 100)  # False
print(np.NaN == 100)  # False
