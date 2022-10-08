"""
-- Core pandas
---- Filtering a DataFrame
------ Filtering by condition
-------- The isnull and notnull methods
"""
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])
employees["Mgmt"] = employees["Mgmt"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")
employees["Team"] = employees["Team"].astype("category")

print(employees["Team"].head())
# 0    Marketing
# 1          NaN
# 2      Finance
# 3      Finance
# 4           IT
# Name: Team, dtype: category
# Categories (10, object): ['Business Dev', 'Distribution', 'Engineering', 'Finance', ..., 'Legal',
#                           'Marketing', 'Product', 'Sales']

print(employees["Team"].isnull().head())
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False
# Name: Team, dtype: bool

print(employees["Start Date"].head())
# 0   1993-08-06
# 1   1996-03-31
# 2          NaT
# 3   2005-03-04
# 4   1998-01-24
# Name: Start Date, dtype: datetime64[ns]

print(employees["Start Date"].isnull().head())
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# Name: Start Date, dtype: bool

print(employees["Team"].notnull().head())
# 0     True
# 1    False
# 2     True
# 3     True
# 4     True
# Name: Team, dtype: bool

print((~employees["Team"].isnull()).head())
# 0     True
# 1    False
# 2     True
# 3     True
# 4     True
# Name: Team, dtype: bool

no_team = employees["Team"].isnull()
print(employees[no_team].head())
#    First Name  Gender Start Date    Salary   Mgmt Team
# 1      Thomas    Male 1996-03-31   61933.0   True  NaN
# 10     Louise  Female 1980-08-12   63241.0   True  NaN
# 23        NaN    Male 2012-06-14  125792.0   True  NaN
# 32        NaN    Male 1998-08-21  122340.0   True  NaN
# 91      James     NaN 2005-01-26  128771.0  False  NaN

has_name = employees["First Name"].notnull()
print(employees[has_name].tail())
#     First Name Gender Start Date    Salary   Mgmt          Team
# 995      Henry    NaN 2014-11-23  132483.0  False  Distribution
# 996    Phillip   Male 1984-01-31   42392.0  False       Finance
# 997    Russell   Male 2013-05-20   96914.0  False       Product
# 998      Larry   Male 2013-04-20   60500.0  False  Business Dev
# 999     Albert   Male 2012-05-15  129949.0   True         Sales