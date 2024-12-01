#!/usr/bin/python3
"""
-- Core pandas
---- Filtering a DataFrame
------ Filtering by condition
-------- The between method
"""
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])
employees["Mgmt"] = employees["Mgmt"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")
employees["Team"] = employees["Team"].astype("category")

higher_than_80 = employees["Salary"] >= 80000
lower_than_90 = employees["Salary"] < 90000
print(employees[higher_than_80 & lower_than_90].head())
#    First Name  Gender Start Date   Salary   Mgmt         Team
# 19      Donna  Female 2010-07-22  81014.0  False      Product
# 31      Joyce     NaN 2005-02-20  88657.0  False      Product
# 35    Theresa  Female 2006-10-10  85182.0  False        Sales
# 45      Roger    Male 1980-04-17  88010.0   True        Sales
# 54       Sara  Female 2007-08-15  83677.0  False  Engineering

# The lower bound is inclusive, and the upper bound is exclusive
between_80k_and_90k = employees["Salary"].between(80000, 90000)
print(employees[between_80k_and_90k].head())
#    First Name  Gender Start Date   Salary   Mgmt         Team
# 19      Donna  Female 2010-07-22  81014.0  False      Product
# 31      Joyce     NaN 2005-02-20  88657.0  False      Product
# 35    Theresa  Female 2006-10-10  85182.0  False        Sales
# 45      Roger    Male 1980-04-17  88010.0   True        Sales
# 54       Sara  Female 2007-08-15  83677.0  False  Engineering

eighties_folk = employees["Start Date"].between(left="1980-01-01", right="1990-01-01")
print(employees[eighties_folk].head())
#    First Name  Gender Start Date    Salary   Mgmt     Team
# 5      Dennis    Male 1987-04-18  115163.0  False    Legal
# 6        Ruby  Female 1987-08-17   65476.0   True  Product
# 10     Louise  Female 1980-08-12   63241.0   True      NaN
# 12    Brandon    Male 1980-12-01  112807.0   True       HR
# 17      Shawn    Male 1986-12-07  111737.0  False  Product

name_starts_with_r = employees["First Name"].between("R", "S")
print(employees[name_starts_with_r].head())
#    First Name  Gender Start Date    Salary   Mgmt          Team
# 6        Ruby  Female 1987-08-17   65476.0   True       Product
# 36     Rachel  Female 2009-02-16  142032.0  False  Business Dev
# 45      Roger    Male 1980-04-17   88010.0   True         Sales
# 67     Rachel  Female 1999-08-16   51178.0   True       Finance
# 78      Robin  Female 1983-06-04  114797.0   True         Sales
