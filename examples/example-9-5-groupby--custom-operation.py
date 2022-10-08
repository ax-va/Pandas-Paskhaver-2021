"""
-- Applied pandas
---- The GroupBy object
------ Applying a custom operation to all groups
"""

import pandas as pd
fortune = pd.read_csv("../datasets/fortune1000.csv")
sectors = fortune.groupby("Sector")

print(fortune.nlargest(n=5, columns="Profits"))
#                Company  ...                                  Industry
# 3                Apple  ...               Computers, Office Equipment
# 2   Berkshire Hathaway  ...  Insurance: Property and Casualty (Stock)
# 15             Verizon  ...                        Telecommunications
# 8                 AT&T  ...                        Telecommunications
# 19      JPMorgan Chase  ...                          Commercial Banks
#
# [5 rows x 6 columns]

# print(sectors.nlargest(n=5, columns="Profits"))
# AttributeError: 'DataFrameGroupBy' object has no attribute 'nlargest'


def get_largest_row(df):
    return df.nlargest(1, "Revenues")


print(sectors.apply(get_largest_row).head())
#                                Company  ...               Industry
# Sector                                  ...
# Aerospace & Defense 26          Boeing  ...  Aerospace and Defense
# Apparel             88            Nike  ...                Apparel
# Business Services   142  ManpowerGroup  ...         Temporary Help
# Chemicals           46       DowDuPont  ...              Chemicals
# Energy              1      Exxon Mobil  ...     Petroleum Refining
#
# [5 rows x 6 columns]
