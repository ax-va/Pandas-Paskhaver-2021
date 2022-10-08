"""
-- Applied pandas
---- Working with text data
------ Unique text format
"""
import pandas as pd
inspections = pd.read_csv("../datasets/chicago_food_inspections.csv")

print(inspections["Risk"].head())
# 0      Risk 1 (High)
# 1    Risk 2 (Medium)
# 2       Risk 3 (Low)
# 3      Risk 1 (High)
# 4      Risk 1 (High)
# Name: Risk, dtype: object

print(len(inspections))  # 153810 (rows)
print(repr(inspections["Risk"].unique()))
# array(['Risk 1 (High)', 'Risk 2 (Medium)', 'Risk 3 (Low)', 'All', nan],
#       dtype=object)

inspections = inspections.dropna(subset=["Risk"])
print(repr(inspections["Risk"].unique()))
# array(['Risk 1 (High)', 'Risk 2 (Medium)', 'Risk 3 (Low)', 'All'],
#       dtype=object)

inspections = inspections.replace(to_replace="All", value="Risk 4 (Extreme)")
print(repr(inspections["Risk"].unique()))
# array(['Risk 1 (High)', 'Risk 2 (Medium)', 'Risk 3 (Low)',
#        'Risk 4 (Extreme)'], dtype=object)

