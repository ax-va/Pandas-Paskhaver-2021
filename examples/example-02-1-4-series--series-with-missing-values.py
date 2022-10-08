"""
-- Core pandas
---- The Series object
------ Overview of a Series
-------- Create Series with missing values
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

