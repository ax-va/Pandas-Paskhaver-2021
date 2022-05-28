"""
Manipulate a DataFrame
"""
import pandas as pd

movies = pd.read_csv("../datasets/movies.csv", index_col="Title")
print(movies.head(4))
#                               Rank       Studio       Gross  Year
# Title
# Avengers: Endgame                1  Buena Vista  $2,796.30   2019
# Avatar                           2          Fox  $2,789.70   2009
# Titanic                          3    Paramount  $2,187.50   1997
# Star Wars: The Force Awakens     4  Buena Vista  $2,068.20   2015

print(movies.tail(6))
#                           Rank           Studio     Gross  Year
# Title
# 21 Jump Street             777             Sony  $201.60   2012
# Yogi Bear                  778  Warner Brothers  $201.60   2010
# Garfield: The Movie        779              Fox  $200.80   2004
# Cats & Dogs                780  Warner Brothers  $200.70   2001
# The Hunt for Red October   781        Paramount  $200.50   1990
# Valkyrie                   782              MGM  $200.30   2008

print(len(movies))  # 782
print(movies.shape)  # (782, 4)
print(movies.size)  # 3128
print(movies.dtypes)
# Rank       int64
# Studio    object
# Gross     object
# Year       int64
# dtype: object

print(movies.iloc[499])
# Rank           500
# Studio         Fox
# Gross     $288.30
# Year          2018
# Name: Maze Runner: The Death Cure, dtype: object

print(movies.loc["Forrest Gump"])
# Rank            119
# Studio    Paramount
# Gross      $677.90
# Year           1994
# Name: Forrest Gump, dtype: object

print(movies.loc["101 Dalmatians"])
# Title
# 101 Dalmatians   425  Buena Vista  $320.70   1996
# 101 Dalmatians   708  Buena Vista  $215.90   1961

print(movies.sort_values(by="Year", ascending=False).head())
#                                             Rank  ...  Year
# Title                                             ...
# Avengers: Endgame                              1  ...  2019
# John Wick: Chapter 3 - Parabellum            458  ...  2019
# The Wandering Earth                          114  ...  2019
# Toy Story 4                                  198  ...  2019
# How to Train Your Dragon: The Hidden World   199  ...  2019
#
# [5 rows x 4 columns]

print(movies.sort_values(by=["Studio", "Year"]).head())
#                          Rank       Studio     Gross  Year
# Title
# The Blair Witch Project   588      Artisan  $248.60   1999
# 101 Dalmatians            708  Buena Vista  $215.90   1961
# The Jungle Book           755  Buena Vista  $205.80   1967
# Who Framed Roger Rabbit   410  Buena Vista  $329.80   1988
# Dead Poets Society        636  Buena Vista  $235.90   1989

print(movies.sort_index().head())
#                   Rank           Studio     Gross  Year
# Title
# 10,000 B.C.        536  Warner Brothers  $269.80   2008
# 101 Dalmatians     708      Buena Vista  $215.90   1961
# 101 Dalmatians     425      Buena Vista  $320.70   1996
# 2 Fast 2 Furious   632        Universal  $236.40   2003
# 2012                93             Sony  $769.70   2009