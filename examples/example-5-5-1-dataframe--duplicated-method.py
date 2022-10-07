"""
-- Core pandas
---- The DataFrame Object
------ Dealing with Duplicates
-------- The duplicated Method
"""
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])

print(employees["Team"])
# 0          Marketing
# 1                NaN
# 2            Finance
# 3            Finance
# 4                 IT
#             ...
# 996          Finance
# 997          Product
# 998     Business Dev
# 999            Sales
# 1000             NaN
# Name: Team, Length: 1001, dtype: object

# Returns True any time it sees a value that
# it previously encountered in the Series
print(employees["Team"].duplicated())  # Default keep="first" (keep the first occurrence)
# 0       False
# 1       False
# 2       False
# 3        True
# 4       False
#         ...
# 996      True
# 997      True
# 998      True
# 999      True
# 1000     True
# Name: Team, Length: 1001, dtype: bool

print(employees["Team"].duplicated(keep="last"))
# 0        True
# 1        True
# 2        True
# 3        True
# 4        True
#         ...
# 996     False
# 997     False
# 998     False
# 999     False
# 1000    False
# Name: Team, Length: 1001, dtype: bool

first_one_in_team = ~employees["Team"].duplicated()
print(employees[first_one_in_team])
#    First Name  Gender Start Date    Salary   Mgmt          Team
# 0     Douglas    Male 1993-08-06       NaN   True     Marketing
# 1      Thomas    Male 1996-03-31   61933.0   True           NaN
# 2       Maria  Female        NaT  130590.0  False       Finance
# 4       Larry    Male 1998-01-24  101004.0   True            IT
# 5      Dennis    Male 1987-04-18  115163.0  False         Legal
# 6        Ruby  Female 1987-08-17   65476.0   True       Product
# 8      Angela  Female 2005-11-22   95570.0   True   Engineering
# 9     Frances  Female 2002-08-08  139852.0   True  Business Dev
# 12    Brandon    Male 1980-12-01  112807.0   True            HR
# 13       Gary    Male 2008-01-27  109831.0  False         Sales
# 40    Michael    Male 2008-10-10   99283.0   True  Distribution
