"""
-- Core pandas
---- Filtering a DataFrame
------ Filtering by multiple conditions
-------- The AND condition
"""
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])
employees["Mgmt"] = employees["Mgmt"].astype(bool)
employees["Gender"] = employees["Gender"].astype("category")
employees["Team"] = employees["Team"].astype("category")

is_female = employees["Gender"] == "Female"
in_biz_dev = employees["Team"] == "Business Dev"
print(employees[is_female & in_biz_dev].head())
#    First Name  Gender Start Date    Salary   Mgmt          Team
# 9     Frances  Female 2002-08-08  139852.0   True  Business Dev
# 33       Jean  Female 1993-12-18  119082.0  False  Business Dev
# 36     Rachel  Female 2009-02-16  142032.0  False  Business Dev
# 38  Stephanie  Female 1986-09-13   36844.0   True  Business Dev
# 61     Denise  Female 2001-11-06  106862.0  False  Business Dev

is_manager = employees["Mgmt"]
print(employees[is_female & in_biz_dev & is_manager].head())
#     First Name  Gender Start Date    Salary  Mgmt          Team
# 9      Frances  Female 2002-08-08  139852.0  True  Business Dev
# 38   Stephanie  Female 1986-09-13   36844.0  True  Business Dev
# 66       Nancy  Female 2012-12-15  125250.0  True  Business Dev
# 92       Linda  Female 2000-05-25  119009.0  True  Business Dev
# 111     Bonnie  Female 1999-12-17   42153.0  True  Business Dev