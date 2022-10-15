"""
-- Applied pandas
---- Working with dates and times
------ Using the DatetimeProperties object
"""

import pandas as pd

disney = pd.read_csv("../datasets/disney.csv", parse_dates=["Date"])
# # Alternatively
# disney = pd.read_csv("../datasets/disney.csv")
# disney["Date"] = pd.to_datetime(disney["Date"])

print(disney["Date"].dt)
# <pandas.core.indexes.accessors.DatetimeProperties object at 0x0000022CCBDD9C10>

print(disney["Date"].head(3))
# 0   1962-01-02
# 1   1962-01-03
# 2   1962-01-04
# Name: Date, dtype: datetime64[ns]

print(disney["Date"].dt.day.head(3))
# 0    2
# 1    3
# 2    4
# Name: Date, dtype: int64

print(disney["Date"].dt.month.head(3))
# 0    1
# 1    1
# 2    1
# Name: Date, dtype: int64

print(disney["Date"].dt.year.head(3))
# 0    1962
# 1    1962
# 2    1962
# Name: Date, dtype: int64

print(disney["Date"].dt.dayofweek.head(7))
# 0    1
# 1    2
# 2    3
# 3    4
# 4    0
# 5    1
# 6    2
# Name: Date, dtype: int64

# 0 denotes Monday, 1 denotes Tuesday, and so on up to 6 for Sunday

print(disney["Date"].dt.day_name().head(7))
# 0      Tuesday
# 1    Wednesday
# 2     Thursday
# 3       Friday
# 4       Monday
# 5      Tuesday
# 6    Wednesday
# Name: Date, dtype: object

disney["Day of Week"] = disney["Date"].dt.day_name()
print(disney.head(7))
#         Date      High       Low      Open     Close Day of Week
# 0 1962-01-02  0.096026  0.092908  0.092908  0.092908     Tuesday
# 1 1962-01-03  0.094467  0.092908  0.092908  0.094155   Wednesday
# 2 1962-01-04  0.094467  0.093532  0.094155  0.094155    Thursday
# 3 1962-01-05  0.094779  0.093844  0.094155  0.094467      Friday
# 4 1962-01-08  0.095714  0.092285  0.094467  0.094155      Monday
# 5 1962-01-09  0.096026  0.093532  0.094155  0.096026     Tuesday
# 6 1962-01-10  0.097585  0.096026  0.096026  0.096961   Wednesday

print(disney.groupby("Day of Week").mean())
#                   High        Low       Open      Close
# Day of Week
# Friday       23.767304  23.318898  23.552872  23.554498
# Monday       23.377271  22.930606  23.161392  23.162543
# Thursday     23.770234  23.288687  23.534561  23.540359
# Tuesday      23.791234  23.335267  23.571755  23.562907
# Wednesday    23.842743  23.355419  23.605618  23.609873

print(disney["Date"].dt.month_name().head())
# 0    January
# 1    January
# 2    January
# 3    January
# 4    January
# Name: Date, dtype: object

# is_quarter_start and is_quarter_end
print(disney["Date"].dt.is_quarter_start.tail())
# 14722    False
# 14723    False
# 14724    False
# 14725     True
# 14726    False
# Name: Date, dtype: bool

# The four quarters of a business year start on January 1, April 1, July 1, and October 1

print(disney[disney["Date"].dt.is_quarter_start].head())
#           Date      High       Low      Open     Close Day of Week
# 189 1962-10-01  0.064849  0.062355  0.063913  0.062355      Monday
# 314 1963-04-01  0.087989  0.086704  0.087025  0.086704      Monday
# 377 1963-07-01  0.096338  0.095053  0.096338  0.095696      Monday
# 441 1963-10-01  0.110467  0.107898  0.107898  0.110467     Tuesday
# 565 1964-04-01  0.116248  0.112394  0.112394  0.116248   Wednesday

print(disney[disney["Date"].dt.is_quarter_end].head())
#           Date      High       Low      Open     Close Day of Week
# 251 1962-12-31  0.074501  0.071290  0.074501  0.072253      Monday
# 440 1963-09-30  0.109825  0.105972  0.108541  0.107577      Monday
# 502 1963-12-31  0.101476  0.096980  0.097622  0.101476     Tuesday
# 564 1964-03-31  0.115605  0.112394  0.114963  0.112394     Tuesday
# 628 1964-06-30  0.101476  0.100191  0.101476  0.100834     Tuesday

# is_month_start and is_month_end
print(disney[disney["Date"].dt.is_month_start].head())
#           Date      High       Low      Open     Close Day of Week
# 22  1962-02-01  0.096338  0.093532  0.093532  0.094779    Thursday
# 41  1962-03-01  0.095714  0.093532  0.093532  0.095714    Thursday
# 83  1962-05-01  0.087296  0.085426  0.085738  0.086673     Tuesday
# 105 1962-06-01  0.079814  0.077943  0.079814  0.079814      Friday
# 147 1962-08-01  0.068590  0.068278  0.068590  0.068590   Wednesday

print(disney[disney["Date"].dt.is_month_end].head())
#           Date      High       Low      Open     Close Day of Week
# 21  1962-01-31  0.093844  0.092908  0.093532  0.093532   Wednesday
# 40  1962-02-28  0.094779  0.093220  0.094155  0.093220   Wednesday
# 82  1962-04-30  0.087608  0.085738  0.087608  0.085738      Monday
# 104 1962-05-31  0.082308  0.079814  0.079814  0.079814    Thursday
# 146 1962-07-31  0.069214  0.068278  0.068278  0.068590     Tuesday

# Also is_year_start and is_year_end
print(disney[disney["Date"].dt.is_year_start].head())
# Empty DataFrame
# Columns: [Date, High, Low, Open, Close, Day of Week]
# Index: []

# The stock market is closed on New Year's Day

print(disney[disney["Date"].dt.is_year_end].head())
#            Date      High       Low      Open     Close Day of Week
# 251  1962-12-31  0.074501  0.071290  0.074501  0.072253      Monday
# 502  1963-12-31  0.101476  0.096980  0.097622  0.101476     Tuesday
# 755  1964-12-31  0.117853  0.116890  0.116890  0.116890    Thursday
# 1007 1965-12-31  0.154141  0.150929  0.153498  0.152214      Friday
# 1736 1968-12-31  0.439301  0.431594  0.434163  0.436732     Tuesday
