"""
-- Core pandas
---- The Series Object
------ Overview of a Series
-------- Create Series with Missing Values
"""
import numpy as np
import pandas as pd

temperatures = [94, 88, np.nan, 91]
print(pd.Series(data=temperatures))
# 0    94.0
# 1    88.0
# 2     NaN
# 3    91.0
# dtype: float64

