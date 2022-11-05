#!/usr/bin/python3
"""
-- Applied pandas
---- Reshaping and pivoting
------ Stacking and unstacking index levels
"""
import pandas as pd

sales = pd.read_csv("../datasets/sales_by_employee.csv", parse_dates=["Date"])
print(sales.head())
#         Date   Name       Customer  Revenue  Expenses
# 0 2020-01-01  Oscar  Logistics XYZ     5250       531
# 1 2020-01-01  Oscar    Money Corp.     4406       661
# 2 2020-01-02  Oscar     PaperMaven     8661      1401
# 3 2020-01-03  Oscar    PaperGenius     7075       906
# 4 2020-01-04  Oscar    Paper Pound     2524      1767

by_name_and_date = sales.pivot_table(
    index="Name",
    columns="Date",
    values="Revenue",
    aggfunc="sum"
)
print(by_name_and_date)
# Date     2020-01-01  2020-01-02  2020-01-03  2020-01-04  2020-01-05
# Name
# Creed        4430.0     13214.0         NaN      3144.0       938.0
# Dwight       2639.0         NaN     11912.0         NaN      7771.0
# Jim          1864.0      8278.0      4226.0      6155.0         NaN
# Michael      7172.0      6362.0      5982.0      7917.0      7837.0
# Oscar        9656.0      8661.0      7075.0      2524.0      2793.0

print(by_name_and_date.stack().head(7))
# Name    Date
# Creed   2020-01-01     4430.0
#         2020-01-02    13214.0
#         2020-01-04     3144.0
#         2020-01-05      938.0
# Dwight  2020-01-01     2639.0
#         2020-01-03    11912.0
#         2020-01-05     7771.0
# dtype: float64

print(type(by_name_and_date.stack()))  # <class 'pandas.core.series.Series'>

sales_by_customer = sales.pivot_table(
    index=["Customer", "Name"],
    values="Revenue",
    aggfunc="sum"
)
print(sales_by_customer.head())
#                            Revenue
# Customer          Name
# Average Paper Co. Creed      13214
#                   Jim         2287
# Best Paper Co.    Dwight      2703
#                   Michael    15754
# Logistics XYZ     Dwight      9209

# Move the innermost level of the row index to the column index
print(sales_by_customer.unstack())
# Name                 Creed  Dwight     Jim  Michael   Oscar
# Customer
# Average Paper Co.  13214.0     NaN  2287.0      NaN     NaN
# Best Paper Co.         NaN  2703.0     NaN  15754.0     NaN
# Logistics XYZ          NaN  9209.0     NaN   7172.0  5250.0
# Money Corp.         5368.0     NaN  8278.0      NaN  4406.0
# Paper Pound            NaN  7771.0  4226.0      NaN  5317.0
# PaperGenius            NaN  2639.0  1864.0  12344.0  7075.0
# PaperMaven          3144.0     NaN  3868.0      NaN  8661.0