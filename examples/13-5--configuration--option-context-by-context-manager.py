#!/usr/bin/python3
"""
-- Applied pandas
---- Configuring pandas
------ Option context by the context manager
"""

import pandas as pd

happiness = pd.read_csv("../datasets/happiness.csv")

with pd.option_context(
        "display.precision", 2,
        "display.chop_threshold", 0.25
        ):
    print(happiness)
    #                       Country  Score  ...  Life expectancy  Generosity
    # 0                     Finland   7.77  ...             0.99        0.00
    # 1                     Denmark   7.60  ...             1.00        0.25
    # 2                      Norway   7.55  ...             1.03        0.27
    # 3                     Iceland   7.49  ...             1.03        0.35
    # 4                 Netherlands   7.49  ...             1.00        0.32
    # ..                        ...    ...  ...              ...         ...
    # 151                    Rwanda   3.33  ...             0.61        0.00
    # 152                  Tanzania   3.23  ...             0.50        0.28
    # 153               Afghanistan   3.20  ...             0.36        0.00
    # 154  Central African Republic   3.08  ...             0.00        0.00
    # 155               South Sudan   2.85  ...             0.29        0.00
    #
    # [156 rows x 6 columns]

print(happiness)
#                       Country  Score  ...  Life expectancy  Generosity
# 0                     Finland  7.769  ...            0.986       0.153
# 1                     Denmark  7.600  ...            0.996       0.252
# 2                      Norway  7.554  ...            1.028       0.271
# 3                     Iceland  7.494  ...            1.026       0.354
# 4                 Netherlands  7.488  ...            0.999       0.322
# ..                        ...    ...  ...              ...         ...
# 151                    Rwanda  3.334  ...            0.614       0.217
# 152                  Tanzania  3.231  ...            0.499       0.276
# 153               Afghanistan  3.203  ...            0.361       0.158
# 154  Central African Republic  3.083  ...            0.105       0.235
# 155               South Sudan  2.853  ...            0.295       0.202
#
# [156 rows x 6 columns]
