#!/usr/bin/python3
"""
-- Applied pandas
---- Configuring pandas
------ Maximum column width
"""

import pandas as pd

happiness = pd.read_csv("../datasets/happiness.csv")

pd.describe_option("display.max_colwidth")
# display.max_colwidth : int or None
#     The maximum width in characters of a column in the repr of
#     a pandas data structure. When the column overflows, a "..."
#     placeholder is embedded in the output. A 'None' value means unlimited.
#     [default: 50] [currently: 50]

# The two lines below are equivalent
pd.set_option("display.max_colwidth", 9)
pd.options.display.max_colwidth = 9
print(happiness.tail())
#       Country  Score  ...  Life expectancy  Generosity
# 151    Rwanda  3.334  ...     0.614            0.217
# 152  Tanzania  3.231  ...     0.499            0.276
# 153  Afgha...  3.203  ...     0.361            0.158
# 154  Centr...  3.083  ...     0.105            0.235
# 155  South...  2.853  ...     0.295            0.202
