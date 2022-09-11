"""
-- Core pandas
---- Series methods
------ Sorting a Series
-------- Retrieve the smallest and largest values with the nsmallest and nlargest methods
"""

import pandas as pd

google = pd.read_csv("../datasets/google_stocks.csv", parse_dates=["Date"], index_col="Date").squeeze("columns")

print(google.sort_values(ascending=False).head())
# Date
# 2019-04-29    1287.58
# 2019-04-26    1272.18
# 2018-07-26    1268.33
# 2019-10-25    1265.13
# 2019-04-23    1264.55
# Name: Close, dtype: float64

# The two lines below are equivalent
s1 = google.nlargest(n=5)
s2 = google.nlargest()

print(s1)
# Date
# 2019-04-29    1287.58
# 2019-04-26    1272.18
# 2018-07-26    1268.33
# 2019-10-25    1265.13
# 2019-04-23    1264.55
# Name: Close, dtype: float64

print(s2)
# Date
# 2019-04-29    1287.58
# 2019-04-26    1272.18
# 2018-07-26    1268.33
# 2019-10-25    1265.13
# 2019-04-23    1264.55
# Name: Close, dtype: float64

# The two lines below are equivalent
s3 = google.nsmallest(n=5)
s4 = google.nsmallest()

print(s3)
# Date
# 2004-09-03    49.82
# 2004-09-01    49.94
# 2004-08-19    49.98
# 2004-09-02    50.57
# 2004-09-07    50.60
# Name: Close, dtype: float64

print(s4)
# Date
# 2004-09-03    49.82
# 2004-09-01    49.94
# 2004-08-19    49.98
# 2004-09-02    50.57
# 2004-09-07    50.60
# Name: Close, dtype: float64
