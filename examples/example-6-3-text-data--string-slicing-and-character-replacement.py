"""
-- Applied pandas
---- Working with Text Data
------ String Slicing and Character Replacement
"""
import pandas as pd
inspections = pd.read_csv("../datasets/chicago_food_inspections.csv")
inspections = inspections.dropna(subset=["Risk"])
inspections = inspections.replace(to_replace="All", value="Risk 4 (Extreme)")

print(inspections["Risk"].head())
# 0      Risk 1 (High)
# 1    Risk 2 (Medium)
# 2       Risk 3 (Low)
# 3      Risk 1 (High)
# 4      Risk 1 (High)
# Name: Risk, dtype: object

print(inspections["Risk"].str.slice(5, 6).head())
# 0    1
# 1    2
# 2    3
# 3    1
# 4    1
# Name: Risk, dtype: object

print(inspections["Risk"].str[5:6].head())
# 0    1
# 1    2
# 2    3
# 3    1
# 4    1
# Name: Risk, dtype: object

inspections["Risk"].info()
# <class 'pandas.core.series.Series'>
# RangeIndex: 153744 entries, 0 to 153809
# Series name: Risk
# Non-Null Count   Dtype
# --------------   -----
# 153744 non-null  object
# dtypes: object(1)
# memory usage: 2.3+ MB

print(inspections["Risk"].str.slice(8).head())
# 0      High)
# 1    Medium)
# 2       Low)
# 3      High)
# 4      High)
# Name: Risk, dtype: object

print(inspections["Risk"].str[8:].head())
# 0      High)
# 1    Medium)
# 2       Low)
# 3      High)
# 4      High)
# Name: Risk, dtype: object

print(inspections["Risk"].str.slice(8, -1).head())
# 0      High
# 1    Medium
# 2       Low
# 3      High
# 4      High
# Name: Risk, dtype: object

print(inspections["Risk"].str[8:-1].head())
# 0      High
# 1    Medium
# 2       Low
# 3      High
# 4      High
# Name: Risk, dtype: object

print(inspections["Risk"].str.slice(8).str.replace(")", "").head())
# 0      High
# 1    Medium
# 2       Low
# 3      High
# 4      High
# Name: Risk, dtype: object
# FutureWarning: The default value of regex will change from True to False in a future version. In addition, single character regular expressions will *not* be treated as literal strings when regex=True.