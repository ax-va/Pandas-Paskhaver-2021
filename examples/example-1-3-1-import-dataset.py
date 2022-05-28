"""
Importe a data set
"""

import pandas as pd

print(pd.read_csv("../datasets/movies.csv"))
#      Rank                         Title           Studio       Gross  Year
# 0       1             Avengers: Endgame      Buena Vista  $2,796.30   2019
# 1       2                        Avatar              Fox  $2,789.70   2009
# 2       3                       Titanic        Paramount  $2,187.50   1997
# 3       4  Star Wars: The Force Awakens      Buena Vista  $2,068.20   2015
# 4       5        Avengers: Infinity War      Buena Vista  $2,048.40   2018
# ..    ...                           ...              ...         ...   ...
# 777   778                     Yogi Bear  Warner Brothers    $201.60   2010
# 778   779           Garfield: The Movie              Fox    $200.80   2004
# 779   780                   Cats & Dogs  Warner Brothers    $200.70   2001
# 780   781      The Hunt for Red October        Paramount    $200.50   1990
# 781   782                      Valkyrie              MGM    $200.30   2008
#
# [782 rows x 5 columns]

print(pd.read_csv("../datasets/movies.csv", index_col="Title"))
#                               Rank           Studio       Gross  Year
# Title
# Avengers: Endgame                1      Buena Vista  $2,796.30   2019
# Avatar                           2              Fox  $2,789.70   2009
# Titanic                          3        Paramount  $2,187.50   1997
# Star Wars: The Force Awakens     4      Buena Vista  $2,068.20   2015
# Avengers: Infinity War           5      Buena Vista  $2,048.40   2018
# ...                            ...              ...         ...   ...
# Yogi Bear                      778  Warner Brothers    $201.60   2010
# Garfield: The Movie            779              Fox    $200.80   2004
# Cats & Dogs                    780  Warner Brothers    $200.70   2001
# The Hunt for Red October       781        Paramount    $200.50   1990
# Valkyrie                       782              MGM    $200.30   2008
#
# [782 rows x 4 columns]

movies = pd.read_csv("../datasets/movies.csv", index_col="Title")
print(movies)
#                               Rank           Studio       Gross  Year
# Title
# Avengers: Endgame                1      Buena Vista  $2,796.30   2019
# Avatar                           2              Fox  $2,789.70   2009
# Titanic                          3        Paramount  $2,187.50   1997
# Star Wars: The Force Awakens     4      Buena Vista  $2,068.20   2015
# Avengers: Infinity War           5      Buena Vista  $2,048.40   2018
# ...                            ...              ...         ...   ...
# Yogi Bear                      778  Warner Brothers    $201.60   2010
# Garfield: The Movie            779              Fox    $200.80   2004
# Cats & Dogs                    780  Warner Brothers    $200.70   2001
# The Hunt for Red October       781        Paramount    $200.50   1990
# Valkyrie                       782              MGM    $200.30   2008
#
# [782 rows x 4 columns]