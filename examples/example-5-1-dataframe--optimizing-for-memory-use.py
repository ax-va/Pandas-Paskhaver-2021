"""
-- Core pandas
---- The DataFrame Object
------ Optimizing a Data Set for Memory Use
"""
import pandas as pd

employees1 = pd.read_csv("../datasets/employees.csv")
print(employees1)
#      First Name  Gender Start Date    Salary   Mgmt          Team
# 0       Douglas    Male     8/6/93       NaN   True     Marketing
# 1        Thomas    Male    3/31/96   61933.0   True           NaN
# 2         Maria  Female        NaN  130590.0  False       Finance
# 3         Jerry     NaN     3/4/05  138705.0   True       Finance
# 4         Larry    Male    1/24/98  101004.0   True            IT
# ...         ...     ...        ...       ...    ...           ...
# 996     Phillip    Male    1/31/84   42392.0  False       Finance
# 997     Russell    Male    5/20/13   96914.0  False       Product
# 998       Larry    Male    4/20/13   60500.0  False  Business Dev
# 999      Albert    Male    5/15/12  129949.0   True         Sales
# 1000        NaN     NaN        NaN       NaN    NaN           NaN
#
# [1001 rows x 6 columns]

employees2 = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])
print(employees2.head())
#   First Name  Gender Start Date    Salary   Mgmt       Team
# 0    Douglas    Male 1993-08-06       NaN   True  Marketing
# 1     Thomas    Male 1996-03-31   61933.0   True        NaN
# 2      Maria  Female        NaT  130590.0  False    Finance
# 3      Jerry     NaN 2005-03-04  138705.0   True    Finance
# 4      Larry    Male 1998-01-24  101004.0   True         IT

employees2.info()
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



