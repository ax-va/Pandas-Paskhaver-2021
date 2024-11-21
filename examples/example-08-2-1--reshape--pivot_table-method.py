#!/usr/bin/python3
"""
-- Applied pandas
---- Reshaping and pivoting
------ Creating a pivot table from a DataFrame
-------- The pivot_table method
"""
import pandas as pd

print(pd.read_csv("../datasets/sales_by_employee.csv").head())
#      Date   Name       Customer  Revenue  Expenses
# 0  1/1/20  Oscar  Logistics XYZ     5250       531
# 1  1/1/20  Oscar    Money Corp.     4406       661
# 2  1/2/20  Oscar     PaperMaven     8661      1401
# 3  1/3/20  Oscar    PaperGenius     7075       906
# 4  1/4/20  Oscar    Paper Pound     2524      1767

sales = pd.read_csv("../datasets/sales_by_employee.csv", parse_dates=["Date"])
print(sales.tail())
#          Date   Name           Customer  Revenue  Expenses
# 21 2020-01-01  Creed        Money Corp.     4430       548
# 22 2020-01-02  Creed  Average Paper Co.     8026      1906
# 23 2020-01-02  Creed  Average Paper Co.     5188      1768
# 24 2020-01-04  Creed         PaperMaven     3144      1314
# 25 2020-01-05  Creed        Money Corp.      938      1053

# Average as default
# Two lines are equivalent
print(sales.pivot_table(index="Date"))
#                Expenses      Revenue
# Date
# 2020-01-01   637.500000  4293.500000
# 2020-01-02  1244.400000  7303.000000
# 2020-01-03  1313.666667  4865.833333
# 2020-01-04  1450.600000  3948.000000
# 2020-01-05  1196.250000  4834.750000

print(sales.pivot_table(index="Date", aggfunc="mean"))
#                Expenses      Revenue
# Date
# 2020-01-01   637.500000  4293.500000
# 2020-01-02  1244.400000  7303.000000
# 2020-01-03  1313.666667  4865.833333
# 2020-01-04  1450.600000  3948.000000
# 2020-01-05  1196.250000  4834.750000

print(sales.pivot_table(index="Date", aggfunc="sum"))
#             Expenses  Revenue
# Date
# 2020-01-01      3825    25761
# 2020-01-02      6222    36515
# 2020-01-03      7882    29195
# 2020-01-04      7253    19740
# 2020-01-05      4785    19339

print(sales.pivot_table(index="Date", values="Revenue", aggfunc="sum"))
#             Revenue
# Date
# 2020-01-01    25761
# 2020-01-02    36515
# 2020-01-03    29195
# 2020-01-04    19740
# 2020-01-05    19339

# We can pass values a list of columns

print(sales.pivot_table(index="Date", columns="Name", values="Revenue", aggfunc="sum"))
# Name          Creed   Dwight     Jim  Michael   Oscar
# Date
# 2020-01-01   4430.0   2639.0  1864.0   7172.0  9656.0
# 2020-01-02  13214.0      NaN  8278.0   6362.0  8661.0
# 2020-01-03      NaN  11912.0  4226.0   5982.0  7075.0
# 2020-01-04   3144.0      NaN  6155.0   7917.0  2524.0
# 2020-01-05    938.0   7771.0     NaN   7837.0  2793.0

print(sales.pivot_table(index="Date", columns="Name", values="Revenue", aggfunc="sum", fill_value=0))
# Name        Creed  Dwight   Jim  Michael  Oscar
# Date
# 2020-01-01   4430    2639  1864     7172   9656
# 2020-01-02  13214       0  8278     6362   8661
# 2020-01-03      0   11912  4226     5982   7075
# 2020-01-04   3144       0  6155     7917   2524
# 2020-01-05    938    7771     0     7837   2793

# Add totals for each row and column
print(
    sales.pivot_table(
        index="Date",
        columns="Name",
        values="Revenue",
        aggfunc="sum",
        fill_value=0,
        margins=True)
)
# Name                 Creed  Dwight    Jim  Michael  Oscar     All
# Date
# 2020-01-01 00:00:00   4430    2639   1864     7172   9656   25761
# 2020-01-02 00:00:00  13214       0   8278     6362   8661   36515
# 2020-01-03 00:00:00      0   11912   4226     5982   7075   29195
# 2020-01-04 00:00:00   3144       0   6155     7917   2524   19740
# 2020-01-05 00:00:00    938    7771      0     7837   2793   19339
# All                  21726   22322  20523    35270  30709  130550

print(
    sales.pivot_table(
        index="Date",
        columns="Name",
        values="Revenue",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="Total"
    )
)
# Name                 Creed  Dwight    Jim  Michael  Oscar   Total
# Date
# 2020-01-01 00:00:00   4430    2639   1864     7172   9656   25761
# 2020-01-02 00:00:00  13214       0   8278     6362   8661   36515
# 2020-01-03 00:00:00      0   11912   4226     5982   7075   29195
# 2020-01-04 00:00:00   3144       0   6155     7917   2524   19740
# 2020-01-05 00:00:00    938    7771      0     7837   2793   19339
# Total                21726   22322  20523    35270  30709  130550

