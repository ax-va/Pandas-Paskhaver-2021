"""
-- Core pandas
---- Introducing pandas
------ A Tour of pandas
-------- Count Values in a Series
"""
import pandas as pd

movies = pd.read_csv("../datasets/movies.csv", index_col="Title")
print(movies["Studio"])
# Title
# Avengers: Endgame                   Buena Vista
# Avatar                                      Fox
# Titanic                               Paramount
# Star Wars: The Force Awakens        Buena Vista
# Avengers: Infinity War              Buena Vista
#                                      ...
# Yogi Bear                       Warner Brothers
# Garfield: The Movie                         Fox
# Cats & Dogs                     Warner Brothers
# The Hunt for Red October              Paramount
# Valkyrie                                    MGM
# Name: Studio, Length: 782, dtype: object

print(movies["Studio"].value_counts().head(10))
# Warner Brothers    132
# Buena Vista        125
# Fox                117
# Universal          109
# Sony                86
# Paramount           76
# Dreamworks          27
# Lionsgate           21
# New Line            16
# MGM                 11
# Name: Studio, dtype: int64
