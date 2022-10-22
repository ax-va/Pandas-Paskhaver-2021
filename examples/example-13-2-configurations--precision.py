"""
-- Applied pandas
---- Configuring pandas
------ Precision
"""

import pandas as pd

happiness = pd.read_csv("../datasets/happiness.csv")

pd.describe_option("display.precision")
# display.precision : int
#     Floating point output precision in terms of number of places after the
#     decimal, for regular formatting as well as scientific notation. Similar
#     to ``precision`` in :meth:`numpy.set_printoptions`.
#     [default: 6] [currently: 6]

# The two lines below are equivalent
pd.set_option("display.precision", 2)
pd.options.display.precision = 2
print(happiness.head())
#        Country  Score  ...  Life expectancy  Generosity
# 0      Finland   7.77  ...             0.99        0.15
# 1      Denmark   7.60  ...             1.00        0.25
# 2       Norway   7.55  ...             1.03        0.27
# 3      Iceland   7.49  ...             1.03        0.35
# 4  Netherlands   7.49  ...             1.00        0.32
#
# [5 rows x 6 columns]

# Affects only the representation, no data
print(happiness.loc[0, "Score"])  # 7.769
