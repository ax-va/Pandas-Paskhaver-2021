"""
Creating a DataFrame from a NumPy ndarray
"""

import numpy as np
import pandas as pd

random_data = np.random.randint(1, 101, [3, 5])
print(random_data)

# [[91 35 80  9 15]
#  [94 12 41 70 12]
#  [49 41 96  6 77]]

print(pd.DataFrame(data=random_data))
#     0   1   2   3   4
# 0  91  35  80   9  15
# 1  94  12  41  70  12
# 2  49  41  96   6  77

row_labels = ["Morning", "Afternoon", "Evening"]
column_labels = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
)

print(
    pd.DataFrame(
        data=random_data,
        index=row_labels,
        columns=column_labels,
    )
)
#            Monday  Tuesday  Wednesday  Thursday  Friday
# Morning        91       35         80         9      15
# Afternoon      94       12         41        70      12
# Evening        49       41         96         6      77

row_labels = ["Morning", "Afternoon", "Morning"]
column_labels = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Tuesday",
    "Friday",
]

print(
    pd.DataFrame(
        data=random_data,
        index=row_labels,
        columns=column_labels,
    )
)
#            Monday  Tuesday  Wednesday  Tuesday  Friday
# Morning        66       56         72       50      86
# Afternoon      79       27         64       88      77
# Morning        26       16         14       71      15
