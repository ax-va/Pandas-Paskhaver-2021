"""
Group data
"""
import pandas as pd

movies = pd.read_csv("../datasets/movies.csv", index_col="Title")
print(movies["Gross"].str.replace("$", "", regex=False).str.replace(",", "", regex=False))
# Title
# Avengers: Endgame               2796.30
# Avatar                          2789.70
# Titanic                         2187.50
# Star Wars: The Force Awakens    2068.20
# Avengers: Infinity War          2048.40
#                                   ...
# Yogi Bear                        201.60
# Garfield: The Movie              200.80
# Cats & Dogs                      200.70
# The Hunt for Red October         200.50
# Valkyrie                         200.30
# Name: Gross, Length: 782, dtype: object
print(movies["Gross"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float))
# Title
# Avengers: Endgame               2796.3
# Avatar                          2789.7
# Titanic                         2187.5
# Star Wars: The Force Awakens    2068.2
# Avengers: Infinity War          2048.4
#                                  ...
# Yogi Bear                        201.6
# Garfield: The Movie              200.8
# Cats & Dogs                      200.7
# The Hunt for Red October         200.5
# Valkyrie                         200.3
# Name: Gross, Length: 782, dtype: float64
movies["Gross"] = movies["Gross"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)
print(movies["Gross"].mean())  # 439.0308184143222

studios = movies.groupby("Studio")
print(studios["Gross"].count().head())
# Studio
# Artisan                     1
# Buena Vista               125
# CL                          1
# China Film Corporation      1
# Columbia                    5
# Name: Gross, dtype: int64
print(studios["Gross"].count().sort_values(ascending=False).head())
# Studio
# Warner Brothers    132
# Buena Vista        125
# Fox                117
# Universal          109
# Sony                86
# Name: Gross, dtype: int64
print(studios["Gross"].sum().head())
# Studio
# Artisan                     248.6
# Buena Vista               73585.0
# CL                          228.1
# China Film Corporation      699.8
# Columbia                   1276.6
# Name: Gross, dtype: float64
print(studios["Gross"].sum().sort_values(ascending=False).head())
# Studio
# Buena Vista        73585.0
# Warner Brothers    58643.8
# Fox                50420.8
# Universal          44302.3
# Sony               32822.5
# Name: Gross, dtype: float64
