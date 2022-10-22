"""
-- Applied pandas
---- Configuring pandas
------ Getting and setting pandas options
"""

import pandas as pd

happiness = pd.read_csv("../datasets/happiness.csv")
print(happiness.head())
#        Country  Score  ...  Life expectancy  Generosity
# 0      Finland  7.769  ...            0.986       0.153
# 1      Denmark  7.600  ...            0.996       0.252
# 2       Norway  7.554  ...            1.028       0.271
# 3      Iceland  7.494  ...            1.026       0.354
# 4  Netherlands  7.488  ...            0.999       0.322
#
# [5 rows x 6 columns]

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

pd.describe_option("display.max_rows")
# display.max_rows : int
#     If max_rows is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
#
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the height of the terminal and print a truncated object which fits
#     the screen height. The IPython notebook, IPython qtconsole, or
#     IDLE do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 60] [currently: 60]

pd.describe_option("max_col")
# display.max_columns : int
#     If max_cols is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
#
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the width of the terminal and print a truncated object which fits
#     the screen width. The IPython notebook, IPython qtconsole, or IDLE
#     do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 0] [currently: 0]
# display.max_colwidth : int or None
#     The maximum width in characters of a column in the repr of
#     a pandas data structure. When the column overflows, a "..."
#     placeholder is embedded in the output. A 'None' value means unlimited.
#     [default: 50] [currently: 50]
# styler.render.max_columns : int, optional
#     The maximum number of columns that will be rendered. May still be reduced to
#     satsify ``max_elements``, which takes precedence.
#     [default: None] [currently: None]

# The two lines below are equivalent
print(pd.get_option("display.max_rows"))  # 60
print(pd.options.display.max_rows)  # 60

# The two lines below are equivalent
pd.set_option("display.max_rows", 6)
pd.options.display.max_rows = 6
print(pd.options.display.max_rows)  # 6

print(happiness.head(6))
#        Country  Score  ...  Life expectancy  Generosity
# 0      Finland  7.769  ...            0.986       0.153
# 1      Denmark  7.600  ...            0.996       0.252
# 2       Norway  7.554  ...            1.028       0.271
# 3      Iceland  7.494  ...            1.026       0.354
# 4  Netherlands  7.488  ...            0.999       0.322
# 5  Switzerland  7.480  ...            1.052       0.263
#
# [6 rows x 6 columns]

print(happiness.head(7))
#         Country  Score  ...  Life expectancy  Generosity
# 0       Finland  7.769  ...            0.986       0.153
# 1       Denmark  7.600  ...            0.996       0.252
# 2        Norway  7.554  ...            1.028       0.271
# ..          ...    ...  ...              ...         ...
# 4   Netherlands  7.488  ...            0.999       0.322
# 5   Switzerland  7.480  ...            1.052       0.263
# 6        Sweden  7.343  ...            1.009       0.267
#
# [7 rows x 6 columns]

print(pd.options.display.max_columns)  # 0
# The two lines below are equivalent
pd.set_option("display.max_columns", 10)
pd.options.display.max_columns = 10
print(pd.options.display.max_columns)  # 10
print(happiness.head(6))
#        Country  Score  GDP per capita  Social support  Life expectancy  \
# 0      Finland  7.769           1.340           1.587            0.986
# 1      Denmark  7.600           1.383           1.573            0.996
# 2       Norway  7.554           1.488           1.582            1.028
# 3      Iceland  7.494           1.380           1.624            1.026
# 4  Netherlands  7.488           1.396           1.522            0.999
# 5  Switzerland  7.480           1.452           1.526            1.052
#
#    Generosity
# 0       0.153
# 1       0.252
# 2       0.271
# 3       0.354
# 4       0.322
# 5       0.263

pd.options.display.max_columns = 2
print(happiness.head(6))
#        Country  ...  Generosity
# 0      Finland  ...       0.153
# 1      Denmark  ...       0.252
# 2       Norway  ...       0.271
# 3      Iceland  ...       0.354
# 4  Netherlands  ...       0.322
# 5  Switzerland  ...       0.263
#
# [6 rows x 6 columns]

# The two lines below are equivalent
pd.set_option("display.max_columns", 5)
pd.options.display.max_columns = 5
print(happiness.head(6))
#        Country  Score  ...  Life expectancy  Generosity
# 0      Finland  7.769  ...            0.986       0.153
# 1      Denmark  7.600  ...            0.996       0.252
# 2       Norway  7.554  ...            1.028       0.271
# 3      Iceland  7.494  ...            1.026       0.354
# 4  Netherlands  7.488  ...            0.999       0.322
# 5  Switzerland  7.480  ...            1.052       0.263
#
# [6 rows x 6 columns]

pd.reset_option("display.max_rows")
print(pd.get_option("display.max_rows"))  # 60