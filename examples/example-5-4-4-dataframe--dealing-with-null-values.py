"""
-- Core pandas
---- The DataFrame object
------ Filtering by condition
-------- Dealing with null values
"""
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])
print(employees)
#      First Name  Gender Start Date    Salary   Mgmt          Team
# 0       Douglas    Male 1993-08-06       NaN   True     Marketing
# 1        Thomas    Male 1996-03-31   61933.0   True           NaN
# 2         Maria  Female        NaT  130590.0  False       Finance
# 3         Jerry     NaN 2005-03-04  138705.0   True       Finance
# 4         Larry    Male 1998-01-24  101004.0   True            IT
# ...         ...     ...        ...       ...    ...           ...
# 996     Phillip    Male 1984-01-31   42392.0  False       Finance
# 997     Russell    Male 2013-05-20   96914.0  False       Product
# 998       Larry    Male 2013-04-20   60500.0  False  Business Dev
# 999      Albert    Male 2012-05-15  129949.0   True         Sales
# 1000        NaN     NaN        NaT       NaN    NaN           NaN
#
# [1001 rows x 6 columns]

# The dropna method removes DataFrame rows that hold any NaN values
print(employees.dropna())  # default how="any"
#     First Name  Gender Start Date    Salary   Mgmt          Team
# 4        Larry    Male 1998-01-24  101004.0   True            IT
# 5       Dennis    Male 1987-04-18  115163.0  False         Legal
# 6         Ruby  Female 1987-08-17   65476.0   True       Product
# 8       Angela  Female 2005-11-22   95570.0   True   Engineering
# 9      Frances  Female 2002-08-08  139852.0   True  Business Dev
# ..         ...     ...        ...       ...    ...           ...
# 994     George    Male 2013-06-21   98874.0   True     Marketing
# 996    Phillip    Male 1984-01-31   42392.0  False       Finance
# 997    Russell    Male 2013-05-20   96914.0  False       Product
# 998      Larry    Male 2013-04-20   60500.0  False  Business Dev
# 999     Albert    Male 2012-05-15  129949.0   True         Sales
#
# [761 rows x 6 columns]

print(employees.dropna(how="all").tail())
#     First Name Gender Start Date    Salary   Mgmt          Team
# 995      Henry    NaN 2014-11-23  132483.0  False  Distribution
# 996    Phillip   Male 1984-01-31   42392.0  False       Finance
# 997    Russell   Male 2013-05-20   96914.0  False       Product
# 998      Larry   Male 2013-04-20   60500.0  False  Business Dev
# 999     Albert   Male 2012-05-15  129949.0   True         Sales

print(employees.dropna(subset=["Gender"]).tail())
#     First Name Gender Start Date    Salary   Mgmt          Team
# 994     George   Male 2013-06-21   98874.0   True     Marketing
# 996    Phillip   Male 1984-01-31   42392.0  False       Finance
# 997    Russell   Male 2013-05-20   96914.0  False       Product
# 998      Larry   Male 2013-04-20   60500.0  False  Business Dev
# 999     Albert   Male 2012-05-15  129949.0   True         Sales

# Pandas will remove a row if it has a missing value in any of the specified columns
print(employees.dropna(subset=["Start Date", "Salary"]).head())
#   First Name  Gender Start Date    Salary   Mgmt     Team
# 1     Thomas    Male 1996-03-31   61933.0   True      NaN
# 3      Jerry     NaN 2005-03-04  138705.0   True  Finance
# 4      Larry    Male 1998-01-24  101004.0   True       IT
# 5     Dennis    Male 1987-04-18  115163.0  False    Legal
# 6       Ruby  Female 1987-08-17   65476.0   True  Product

# The thresh parameter specifies a minimum threshold of
# non-null values that a row must have for pandas to keep it
print(employees.dropna(how="any", thresh=4).head())
#   First Name  Gender Start Date    Salary   Mgmt       Team
# 0    Douglas    Male 1993-08-06       NaN   True  Marketing
# 1     Thomas    Male 1996-03-31   61933.0   True        NaN
# 2      Maria  Female        NaT  130590.0  False    Finance
# 3      Jerry     NaN 2005-03-04  138705.0   True    Finance
# 4      Larry    Male 1998-01-24  101004.0   True         IT
