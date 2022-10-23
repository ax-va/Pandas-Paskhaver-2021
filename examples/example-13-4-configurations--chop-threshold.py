"""
-- Applied pandas
---- Configuring pandas
------ Chop threshold
"""

import pandas as pd

happiness = pd.read_csv("../datasets/happiness.csv")

pd.describe_option("display.chop_threshold")
# display.chop_threshold : float or None
#     if set to a float value, all float values smaller then the given threshold
#     will be displayed as exactly 0 by repr and friends.
#     [default: None] [currently: None]

print(happiness.tail())
#                       Country  Score  ...  Life expectancy  Generosity
# 151                    Rwanda  3.334  ...            0.614       0.217
# 152                  Tanzania  3.231  ...            0.499       0.276
# 153               Afghanistan  3.203  ...            0.361       0.158
# 154  Central African Republic  3.083  ...            0.105       0.235
# 155               South Sudan  2.853  ...            0.295       0.202
#
# [5 rows x 6 columns]

pd.set_option("display.chop_threshold", 0.25)

# Affects the representation only, but not data
print(happiness.tail())
#                       Country  Score  ...  Life expectancy  Generosity
# 151                    Rwanda  3.334  ...            0.614       0.000
# 152                  Tanzania  3.231  ...            0.499       0.276
# 153               Afghanistan  3.203  ...            0.361       0.000
# 154  Central African Republic  3.083  ...            0.000       0.000
# 155               South Sudan  2.853  ...            0.295       0.000
#
# [5 rows x 6 columns]
