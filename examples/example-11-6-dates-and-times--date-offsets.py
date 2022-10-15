"""
-- Applied pandas
---- Working with dates and times
------ Date offsets
"""

import pandas as pd

disney = pd.read_csv("../datasets/disney.csv", parse_dates=["Date"])

print(disney["Date"].tail())
# 14722   2020-06-26
# 14723   2020-06-29
# 14724   2020-06-30
# 14725   2020-07-01
# 14726   2020-07-02
# Name: Date, dtype: datetime64[ns]

# Round each date to the NEXT month-end
print((disney["Date"] + pd.offsets.MonthEnd()).tail())
# 14722   2020-06-30
# 14723   2020-06-30
# 14724   2020-07-31
# 14725   2020-07-31
# 14726   2020-07-31
# Name: Date, dtype: datetime64[ns]

# 14724 2020-06-30 is the end of month and the NEXT month-end is 2020-07-31

# Round each date to the PREVIOUS month-end
print((disney["Date"] - pd.offsets.MonthEnd()).tail())
# 14722   2020-05-31
# 14723   2020-05-31
# 14724   2020-05-31
# 14725   2020-06-30
# 14726   2020-06-30
# Name: Date, dtype: datetime64[ns]

# Rounds to the first date of a NEXT month
print((disney["Date"] + pd.offsets.MonthBegin()).tail())
# 14722   2020-07-01
# 14723   2020-07-01
# 14724   2020-07-01
# 14725   2020-08-01
# 14726   2020-08-01
# Name: Date, dtype: datetime64[ns]

# Rounds to the first date of a PREVIOUS or THIS month
print((disney["Date"] - pd.offsets.MonthBegin()).tail())
# 14722   2020-06-01
# 14723   2020-06-01
# 14724   2020-06-01
# 14725   2020-06-01
# 14726   2020-07-01
# Name: Date, dtype: datetime64[ns]

# 14725 2020-07-01 is the first day of month and pandas moves it to the first day of the previous month

# Compare MonthEnd and BMonthEnd (B for business).
# The five business days are Monday, Tuesday, Wednesday, Thursday, and Friday.
may_dates = ["2020-05-28", "2020-05-29", "2020-05-30", "2020-05-31"]
end_of_may = pd.Series(pd.to_datetime(may_dates))
print(end_of_may)
# 0   2020-05-28
# 1   2020-05-29
# 2   2020-05-30
# 3   2020-05-31
# dtype: datetime64[ns]]

print(end_of_may.dt.day_name())
# 0    Thursday
# 1      Friday
# 2    Saturday
# 3      Sunday
# dtype: object

print(end_of_may + pd.offsets.MonthEnd())
# 0   2020-05-31
# 1   2020-05-31
# 2   2020-05-31
# 3   2020-06-30
# dtype: datetime64[ns]

print(end_of_may + pd.offsets.BMonthEnd())
# 0   2020-05-29
# 1   2020-06-30
# 2   2020-06-30
# 3   2020-06-30
# dtype: datetime64[ns]
