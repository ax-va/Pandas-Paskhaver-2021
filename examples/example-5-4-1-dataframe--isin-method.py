"""
-- Core pandas
---- The DataFrame Object
------ Filtering by Condition
-------- The isin Method
"""
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])
employees["Mgmt"] = employees["Mgmt"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")
employees["Team"] = employees["Team"].astype("category")

sales = employees["Team"] == "Sales"
legal = employees["Team"] == "Legal"
mktg = employees["Team"] == "Marketing"
print(employees[sales | legal | mktg].head())
#    First Name  Gender Start Date    Salary   Mgmt       Team
# 0     Douglas    Male 1993-08-06       NaN   True  Marketing
# 5      Dennis    Male 1987-04-18  115163.0  False      Legal
# 11      Julie  Female 1997-10-26  102508.0   True      Legal
# 13       Gary    Male 2008-01-27  109831.0  False      Sales
# 20       Lois     NaN 1995-04-22   64714.0   True      Legal

all_star_teams = ["Sales", "Legal", "Marketing"]
print(employees[employees["Team"].isin(all_star_teams)])
#     First Name  Gender Start Date    Salary   Mgmt       Team
# 0      Douglas    Male 1993-08-06       NaN   True  Marketing
# 5       Dennis    Male 1987-04-18  115163.0  False      Legal
# 11       Julie  Female 1997-10-26  102508.0   True      Legal
# 13        Gary    Male 2008-01-27  109831.0  False      Sales
# 20        Lois     NaN 1995-04-22   64714.0   True      Legal
# ..         ...     ...        ...       ...    ...        ...
# 986      Donna  Female 1982-11-26   82871.0  False  Marketing
# 989     Justin     NaN 1991-02-10   38344.0  False      Legal
# 991       Rose  Female 2002-08-25  134505.0   True  Marketing
# 994     George    Male 2013-06-21   98874.0   True  Marketing
# 999     Albert    Male 2012-05-15  129949.0   True      Sales
#
# [280 rows x 6 columns]
