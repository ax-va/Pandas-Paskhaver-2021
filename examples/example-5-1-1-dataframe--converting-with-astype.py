"""
-- Core pandas
---- The DataFrame Object
------ Optimizing a Data Set for Memory Use
-------- Converting Data Types with the astype Method
"""
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])

print(employees["Mgmt"])
# 0        True
# 1        True
# 2       False
# 3        True
# 4        True
#         ...
# 996     False
# 997     False
# 998     False
# 999      True
# 1000      NaN
# Name: Mgmt, Length: 1001, dtype: object

# Pandas converts NaNs to True values
print(employees["Mgmt"].astype(bool))
# 0        True
# 1        True
# 2       False
# 3        True
# 4        True
#         ...
# 996     False
# 997     False
# 998     False
# 999      True
# 1000     True
# Name: Mgmt, Length: 1001, dtype: bool

employees.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1001 entries, 0 to 1000
# Data columns (total 6 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   First Name  933 non-null    object
#  1   Gender      854 non-null    object
#  2   Start Date  999 non-null    datetime64[ns]
#  3   Salary      999 non-null    float64
#  4   Mgmt        933 non-null    object
#  5   Team        957 non-null    object
# dtypes: datetime64[ns](1), float64(1), object(4)
# memory usage: 47.0+ KB

employees["Mgmt"] = employees["Mgmt"].astype(bool)
employees.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1001 entries, 0 to 1000
# Data columns (total 6 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   First Name  933 non-null    object
#  1   Gender      854 non-null    object
#  2   Start Date  999 non-null    datetime64[ns]
#  3   Salary      999 non-null    float64
#  4   Mgmt        1001 non-null   bool
#  5   Team        957 non-null    object
# dtypes: bool(1), datetime64[ns](1), float64(1), object(3)
# memory usage: 40.2+ KB

print(employees.tail())
#      First Name Gender Start Date    Salary   Mgmt          Team
# 996     Phillip   Male 1984-01-31   42392.0  False       Finance
# 997     Russell   Male 2013-05-20   96914.0  False       Product
# 998       Larry   Male 2013-04-20   60500.0  False  Business Dev
# 999      Albert   Male 2012-05-15  129949.0   True         Sales
# 1000        NaN    NaN        NaT       NaN   True           NaN

# employees["Salary"].astype(int)
# pandas.errors.IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer

print(employees["Salary"].fillna(0).tail())
# 996      42392.0
# 997      96914.0
# 998      60500.0
# 999     129949.0
# 1000         0.0
# Name: Salary, dtype: float64

print(employees["Salary"].fillna(0).astype(int).tail())
# 996      42392
# 997      96914
# 998      60500
# 999     129949
# 1000         0
# Name: Salary, dtype: int32

employees["Salary"] = employees["Salary"].fillna(0).astype(int)
print(employees.tail())
#      First Name Gender Start Date  Salary   Mgmt          Team
# 996     Phillip   Male 1984-01-31   42392  False       Finance
# 997     Russell   Male 2013-05-20   96914  False       Product
# 998       Larry   Male 2013-04-20   60500  False  Business Dev
# 999      Albert   Male 2012-05-15  129949   True         Sales
# 1000        NaN    NaN        NaT       0   True           NaN

# Note that it excludes missing values (NaN) from the count by default
print(employees.nunique())
# First Name    200
# Gender          2
# Start Date    971
# Salary        995
# Mgmt            2
# Team           10
# dtype: int64

print(employees["Gender"].astype("category"))
# 0         Male
# 1         Male
# 2       Female
# 3          NaN
# 4         Male
#          ...
# 996       Male
# 997       Male
# 998       Male
# 999       Male
# 1000       NaN
# Name: Gender, Length: 1001, dtype: category
# Categories (2, object): ['Female', 'Male']

# Pandas has identified two unique categories: "Female" and "Male"
employees["Gender"] = employees["Gender"].astype("category")
employees.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1001 entries, 0 to 1000
# Data columns (total 6 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   First Name  933 non-null    object
#  1   Gender      854 non-null    category
#  2   Start Date  999 non-null    datetime64[ns]
#  3   Salary      1001 non-null   int32
#  4   Mgmt        1001 non-null   bool
#  5   Team        957 non-null    object
# dtypes: bool(1), category(1), datetime64[ns](1), int32(1), object(2)
# memory usage: 29.6+ KB

employees["Team"] = employees["Team"].astype("category")
employees.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1001 entries, 0 to 1000
# Data columns (total 6 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   First Name  933 non-null    object
#  1   Gender      854 non-null    category
#  2   Start Date  999 non-null    datetime64[ns]
#  3   Salary      1001 non-null   int32
#  4   Mgmt        1001 non-null   bool
#  5   Team        957 non-null    category
# dtypes: bool(1), category(2), datetime64[ns](1), int32(1), object(1)
# memory usage: 23.1+ KB
