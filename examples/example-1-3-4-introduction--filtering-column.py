"""
-- Core pandas
---- Introducing pandas
------ A Tour of pandas
-------- Filter a Column by One or More Criteria
"""
import pandas as pd

movies = pd.read_csv("../datasets/movies.csv", index_col="Title")
print(movies[movies["Studio"] == "Universal"])
#                                 Rank     Studio       Gross  Year
# Title
# Jurassic World                     6  Universal  $1,671.70   2015
# Furious 7                          8  Universal  $1,516.00   2015
# Jurassic World: Fallen Kingdom    13  Universal  $1,309.50   2018
# The Fate of the Furious           17  Universal  $1,236.00   2017
# Minions                           19  Universal  $1,159.40   2015
# ...                              ...        ...         ...   ...
# The Break-Up                     763  Universal    $205.00   2006
# Everest                          766  Universal    $203.40   2015
# Patch Adams                      772  Universal    $202.30   1998
# Kindergarten Cop                 775  Universal    $202.00   1990
# Straight Outta Compton           776  Universal    $201.60   2015
#
# [109 rows x 4 columns]

released_by_universal = (movies["Studio"] == "Universal")
print(movies[released_by_universal].head())
#                                 Rank     Studio       Gross  Year
# Title
# Jurassic World                     6  Universal  $1,671.70   2015
# Furious 7                          8  Universal  $1,516.00   2015
# Jurassic World: Fallen Kingdom    13  Universal  $1,309.50   2018
# The Fate of the Furious           17  Universal  $1,236.00   2017
# Minions                           19  Universal  $1,159.40   2015

released_by_universal = movies["Studio"] == "Universal"
released_in_2015 = movies["Year"] == 2015
print(movies[released_by_universal & released_in_2015])
#                         Rank     Studio       Gross  Year
# Title
# Jurassic World             6  Universal  $1,671.70   2015
# Furious 7                  8  Universal  $1,516.00   2015
# Minions                   19  Universal  $1,159.40   2015
# Fifty Shades of Grey     165  Universal    $571.00   2015
# Pitch Perfect 2          504  Universal    $287.50   2015
# Ted 2                    702  Universal    $216.70   2015
# Everest                  766  Universal    $203.40   2015
# Straight Outta Compton   776  Universal    $201.60   2015

print(movies[released_by_universal | released_in_2015])
#                                 Rank       Studio       Gross  Year
# Title
# Star Wars: The Force Awakens       4  Buena Vista  $2,068.20   2015
# Jurassic World                     6    Universal  $1,671.70   2015
# Furious 7                          8    Universal  $1,516.00   2015
# Avengers: Age of Ultron            9  Buena Vista  $1,405.40   2015
# Jurassic World: Fallen Kingdom    13    Universal  $1,309.50   2018
# ...                              ...          ...         ...   ...
# The Break-Up                     763    Universal    $205.00   2006
# Everest                          766    Universal    $203.40   2015
# Patch Adams                      772    Universal    $202.30   1998
# Kindergarten Cop                 775    Universal    $202.00   1990
# Straight Outta Compton           776    Universal    $201.60   2015
#
# [140 rows x 4 columns]

before_1975 = movies["Year"] < 1975
print(movies[before_1975])
#                     Rank           Studio     Gross  Year
# Title
# The Exorcist         252  Warner Brothers  $441.30   1973
# Gone with the Wind   288              MGM  $402.40   1939
# Bambi                540              RKO  $267.40   1942
# The Godfather        604        Paramount  $245.10   1972
# 101 Dalmatians       708      Buena Vista  $215.90   1961
# The Jungle Book      755      Buena Vista  $205.80   1967

mid_80s = movies["Year"].between(1983, 1986)
print(movies[mid_80s])
#                                       Rank     Studio     Gross  Year
# Title
# Return of the Jedi                     222        Fox  $475.10   1983
# Back to the Future                     311  Universal  $381.10   1985
# Top Gun                                357  Paramount  $356.80   1986
# Indiana Jones and the Temple of Doom   403  Paramount  $333.10   1984
# Crocodile Dundee                       413  Paramount  $328.20   1986
# Beverly Hills Cop                      432  Paramount  $316.40   1984
# Rocky IV                               467        MGM  $300.50   1985
# Rambo: First Blood Part II             469    TriStar  $300.40   1985
# Ghostbusters                           485   Columbia  $295.20   1984
# Out of Africa                          662  Universal  $227.50   1985

has_dark_in_title = movies.index.str.lower().str.contains("dark")
print(movies[has_dark_in_title])
#                                 Rank           Studio       Gross  Year
# Title
# Transformers: Dark of the Moon    23        Paramount  $1,123.80   2011
# The Dark Knight Rises             27  Warner Brothers  $1,084.90   2012
# The Dark Knight                   39  Warner Brothers  $1,004.90   2008
# Thor: The Dark World             132      Buena Vista    $644.60   2013
# Star Trek Into Darkness          232        Paramount    $467.40   2013
# Fifty Shades Darker              309        Universal    $381.50   2017
# Dark Shadows                     600  Warner Brothers    $245.50   2012
# Dark Phoenix                     603              Fox    $245.10   2019
