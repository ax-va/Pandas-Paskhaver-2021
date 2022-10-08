"""
-- Applied pandas
---- Reshaping and pivoting
------ Creating a pivot table from a DataFrame
-------- Additional options for pivot tables
"""
import pandas as pd

sales = pd.read_csv("../datasets/sales_by_employee.csv", parse_dates=["Date"])

print(
    sales.pivot_table(
        index="Date",
        columns="Name",
        values="Revenue",
        aggfunc="count"
    )
)
# Name        Creed  Dwight  Jim  Michael  Oscar
# Date
# 2020-01-01    1.0     1.0  1.0      1.0    2.0
# 2020-01-02    2.0     NaN  1.0      1.0    1.0
# 2020-01-03    NaN     3.0  1.0      1.0    1.0
# 2020-01-04    1.0     NaN  2.0      1.0    1.0
# 2020-01-05    1.0     1.0  NaN      1.0    1.0

# Argument          Description
# max               The largest value in the grouping
# min               The smallest value in the grouping
# std               The standard deviation of the values in the grouping
# median            The median (midpoint) of the values in the grouping
# size              The number of values in the grouping (equivalent to count)

print(
    sales.pivot_table(
        index="Date",
        columns="Name",
        values="Revenue",
        aggfunc=["sum", "count"],
        fill_value=0
    )
)
#               sum                            count
# Name        Creed Dwight   Jim Michael Oscar Creed Dwight Jim Michael Oscar
# Date
# 2020-01-01   4430   2639  1864    7172  9656     1      1   1       1     2
# 2020-01-02  13214      0  8278    6362  8661     2      0   1       1     1
# 2020-01-03      0  11912  4226    5982  7075     0      3   1       1     1
# 2020-01-04   3144      0  6155    7917  2524     1      0   2       1     1
# 2020-01-05    938   7771     0    7837  2793     1      1   0       1     1

print(
    sales.pivot_table(
        index="Date",
        columns="Name",
        values=["Revenue", "Expenses"],
        fill_value=0,
        aggfunc={"Revenue": "min", "Expenses": "max"}
    )
)
#            Expenses                       ... Revenue
# Name          Creed Dwight   Jim Michael  ...  Dwight   Jim Michael Oscar
# Date                                      ...
# 2020-01-01      548    368  1305     412  ...    2639  1864    7172  4406
# 2020-01-02     1906      0   462     685  ...       0  8278    6362  8661
# 2020-01-03        0   1321  1923    1772  ...    2703  4226    5982  7075
# 2020-01-04     1314      0  1889    1857  ...       0  2287    7917  2524
# 2020-01-05     1053   1475     0    1633  ...    7771     0    7837  2793
#
# [5 rows x 10 columns]

# Equivalent
print(
    sales.pivot_table(
        index="Date",
        columns="Name",
        fill_value=0,
        aggfunc={"Revenue": "min", "Expenses": "max"}
    )
)
#            Expenses                       ... Revenue
# Name          Creed Dwight   Jim Michael  ...  Dwight   Jim Michael Oscar
# Date                                      ...
# 2020-01-01      548    368  1305     412  ...    2639  1864    7172  4406
# 2020-01-02     1906      0   462     685  ...       0  8278    6362  8661
# 2020-01-03        0   1321  1923    1772  ...    2703  4226    5982  7075
# 2020-01-04     1314      0  1889    1857  ...       0  2287    7917  2524
# 2020-01-05     1053   1475     0    1633  ...    7771     0    7837  2793
#
# [5 rows x 10 columns]

# Use MultiIndex
print(
    sales.pivot_table(
        index=["Name", "Date"],
        values="Revenue",
        aggfunc="sum"
    ).head(10)
)
#                    Revenue
# Name   Date
# Creed  2020-01-01     4430
#        2020-01-02    13214
#        2020-01-04     3144
#        2020-01-05      938
# Dwight 2020-01-01     2639
#        2020-01-03    11912
#        2020-01-05     7771
# Jim    2020-01-01     1864
#        2020-01-02     8278
#        2020-01-03     4226

print(
    sales.pivot_table(
        index=["Date", "Name"],
        values="Revenue",
        aggfunc="sum"
    ).head(10)
)
#                     Revenue
# Date       Name
# 2020-01-01 Creed       4430
#            Dwight      2639
#            Jim         1864
#            Michael     7172
#            Oscar       9656
# 2020-01-02 Creed      13214
#            Jim         8278
#            Michael     6362
#            Oscar       8661
# 2020-01-03 Dwight     11912
