"""
-- Core pandas
---- The DataFrame Object
------ Filtering by a Single Condition
"""
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])
employees["Mgmt"] = employees["Mgmt"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")
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
#  3   Salary      999 non-null    float64
#  4   Mgmt        1001 non-null   bool
#  5   Team        957 non-null    category
# dtypes: bool(1), category(2), datetime64[ns](1), float64(1), object(1)
# memory usage: 27.0+ KB

print(employees["First Name"] == "Maria")
# 0       False
# 1       False
# 2        True
# 3       False
# 4       False
#         ...
# 996     False
# 997     False
# 998     False
# 999     False
# 1000    False
# Name: First Name, Length: 1001, dtype: bool

print(employees[employees["First Name"] == "Maria"])
#     First Name  Gender Start Date    Salary   Mgmt          Team
# 2        Maria  Female        NaT  130590.0  False       Finance
# 198      Maria  Female 1990-12-27   36067.0   True       Product
# 815      Maria     NaN 1986-01-18  106562.0  False            HR
# 844      Maria     NaN 1985-06-19  148857.0  False         Legal
# 936      Maria  Female 2003-03-14   96250.0  False  Business Dev
# 984      Maria  Female 2011-10-15   43455.0  False   Engineering

marias = employees["First Name"] == "Maria"
print(marias)
# 0       False
# 1       False
# 2        True
# 3       False
# 4       False
#         ...
# 996     False
# 997     False
# 998     False
# 999     False
# 1000    False
# Name: First Name, Length: 1001, dtype: bool

print(employees[marias])
#     First Name  Gender Start Date    Salary   Mgmt          Team
# 2        Maria  Female        NaT  130590.0  False       Finance
# 198      Maria  Female 1990-12-27   36067.0   True       Product
# 815      Maria     NaN 1986-01-18  106562.0  False            HR
# 844      Maria     NaN 1985-06-19  148857.0  False         Legal
# 936      Maria  Female 2003-03-14   96250.0  False  Business Dev
# 984      Maria  Female 2011-10-15   43455.0  False   Engineering

print(employees["Team"] != "Finance")
# 0        True
# 1        True
# 2       False
# 3       False
# 4        True
#         ...
# 996     False
# 997      True
# 998      True
# 999      True
# 1000     True
# Name: Team, Length: 1001, dtype: bool

print(employees[employees["Team"] != "Finance"])
#      First Name  Gender Start Date    Salary   Mgmt          Team
# 0       Douglas    Male 1993-08-06       NaN   True     Marketing
# 1        Thomas    Male 1996-03-31   61933.0   True           NaN
# 4         Larry    Male 1998-01-24  101004.0   True            IT
# 5        Dennis    Male 1987-04-18  115163.0  False         Legal
# 6          Ruby  Female 1987-08-17   65476.0   True       Product
# ...         ...     ...        ...       ...    ...           ...
# 995       Henry     NaN 2014-11-23  132483.0  False  Distribution
# 997     Russell    Male 2013-05-20   96914.0  False       Product
# 998       Larry    Male 2013-04-20   60500.0  False  Business Dev
# 999      Albert    Male 2012-05-15  129949.0   True         Sales
# 1000        NaN     NaN        NaT       NaN   True           NaN

print(employees[employees["Mgmt"]].head())
#   First Name  Gender Start Date    Salary  Mgmt       Team
# 0    Douglas    Male 1993-08-06       NaN  True  Marketing
# 1     Thomas    Male 1996-03-31   61933.0  True        NaN
# 3      Jerry     NaN 2005-03-04  138705.0  True    Finance
# 4      Larry    Male 1998-01-24  101004.0  True         IT
# 6       Ruby  Female 1987-08-17   65476.0  True    Product

high_earners = employees["Salary"] > 100000
print(high_earners.head())
# 0    False
# 1    False
# 2     True
# 3     True
# 4     True
# Name: Salary, dtype: bool

print(employees[high_earners].head())
#   First Name  Gender Start Date    Salary   Mgmt          Team
# 2      Maria  Female        NaT  130590.0  False       Finance
# 3      Jerry     NaN 2005-03-04  138705.0   True       Finance
# 4      Larry    Male 1998-01-24  101004.0   True            IT
# 5     Dennis    Male 1987-04-18  115163.0  False         Legal
# 9    Frances  Female 2002-08-08  139852.0   True  Business Dev