"""
-- Core pandas
---- The DataFrame object
------ Coding challenge
"""
import pandas as pd
netflix = pd.read_csv("../datasets/netflix.csv")
print(netflix)
#                       title        director date_added     type
# 0               Alias Grace             NaN   3-Nov-17  TV Show
# 1            A Patch of Fog  Michael Lennox  15-Apr-17    Movie
# 2                  Lunatics             NaN  19-Apr-19  TV Show
# 3                 Uriyadi 2     Vijay Kumar   2-Aug-19    Movie
# 4         Shrek the Musical     Jason Moore  29-Dec-13    Movie
# ...                     ...             ...        ...      ...
# 5832            The Pursuit     John Papola   7-Aug-19    Movie
# 5833       Hurricane Bianca   Matt Kugelman   1-Jan-17    Movie
# 5834           Amar's Hands  Khaled Youssef  26-Apr-19    Movie
# 5835  Bill Nye: Science Guy  Jason Sussberg  25-Apr-18    Movie
# 5836           Age of Glory             NaN        NaN  TV Show
#
# [5837 rows x 4 columns]

# Optimize the data set for limited memory use and maximum utility
netflix = pd.read_csv("../datasets/netflix.csv", parse_dates=["date_added"])
netflix.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5837 entries, 0 to 5836
# Data columns (total 4 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   title       5837 non-null   object
#  1   director    3936 non-null   object
#  2   date_added  5195 non-null   datetime64[ns]
#  3   type        5837 non-null   object
# dtypes: datetime64[ns](1), object(3)
# memory usage: 182.5+ KB

print(netflix.nunique())
# title         5780
# director      3024
# date_added    1092
# type             2
# dtype: int64

netflix["type"] = netflix["type"].astype("category")
netflix.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5837 entries, 0 to 5836
# Data columns (total 4 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   title       5837 non-null   object
#  1   director    3936 non-null   object
#  2   date_added  5195 non-null   datetime64[ns]
#  3   type        5837 non-null   category
# dtypes: category(1), datetime64[ns](1), object(2)
# memory usage: 142.8+ KB

# Find all rows with a title of "Limitless"
print(netflix[netflix["title"] == "Limitless"])
#           title         director date_added     type
# 1559  Limitless      Neil Burger 2019-05-16    Movie
# 2564  Limitless              NaN 2016-07-01  TV Show
# 4579  Limitless  Vrinda Samartha 2019-10-01    Movie

# Find all rows with a director of "Robert Rodriguez" and a type of "Movie"
directed_by_robert_rodriguez = netflix["director"] == "Robert Rodriguez"
is_movie = netflix["type"] == "Movie"
print(netflix[directed_by_robert_rodriguez & is_movie])
# 1384    Spy Kids: All the Time in the World  Robert Rodriguez 2019-02-19  Movie
# 1416                  Spy Kids 3: Game Over  Robert Rodriguez 2019-04-01  Movie
# 1460  Spy Kids 2: The Island of Lost Dreams  Robert Rodriguez 2019-03-08  Movie
# 2890                               Sin City  Robert Rodriguez 2019-10-01  Movie
# 3836                                 Shorts  Robert Rodriguez 2019-07-01  Movie
# 3883                               Spy Kids  Robert Rodriguez 2019-04-01  Movie

# Find all rows with either a date_added of "2019-07-31" or a director of "Robert Altman"
added_on_july_31 = netflix["date_added"] == "2019-07-31"
directed_by_altman = netflix["director"] == "Robert Altman"
print(netflix[added_on_july_31 | directed_by_altman])
#                                 title       director date_added     type
# 611                            Popeye  Robert Altman 2019-11-24    Movie
# 1028        The Red Sea Diving Resort    Gideon Raff 2019-07-31    Movie
# 1092                     Gosford Park  Robert Altman 2019-11-01    Movie
# 3473  Bangkok Love Stories: Innocence            NaN 2019-07-31  TV Show
# 5117                       Ramen Shop      Eric Khoo 2019-07-31    Movie

# Find all rows with a director of "Orson Welles", "Aditya Kripalani", or "Sam Raimi"
directors = ["Orson Welles", "Aditya Kripalani", "Sam Raimi"]
target_directors = netflix["director"].isin(directors)
print(netflix[target_directors])
#                            title          director date_added   type
# 946                 The Stranger      Orson Welles 2018-07-19  Movie
# 1870                    The Gift         Sam Raimi 2019-11-20  Movie
# 3706                Spider-Man 3         Sam Raimi 2019-11-01  Movie
# 4243        Tikli and Laxmi Bomb  Aditya Kripalani 2018-08-01  Movie
# 4475  The Other Side of the Wind      Orson Welles 2018-11-02  Movie
# 5115    Tottaa Pataaka Item Maal  Aditya Kripalani 2019-06-25  Movie

# Find all rows with a date_added value between May 1, 2019 and June 1, 2019
may_movies = netflix["date_added"].between("2019-05-01", "2019-06-01")
print(netflix[may_movies].head())
#                    title      director date_added     type
# 29            Chopsticks  Sachin Yardi 2019-05-31    Movie
# 60        Away From Home           NaN 2019-05-08  TV Show
# 82   III Smoking Barrels    Sanjib Dey 2019-06-01    Movie
# 108            Jailbirds           NaN 2019-05-10  TV Show
# 124              Pegasus       Han Han 2019-05-31    Movie

# Drop all rows with a NaN value in the director column
print(netflix.dropna(subset=["director"]))
#                                    title        director date_added   type
# 1                         A Patch of Fog  Michael Lennox 2017-04-15  Movie
# 3                              Uriyadi 2     Vijay Kumar 2019-08-02  Movie
# 4                      Shrek the Musical     Jason Moore 2013-12-29  Movie
# 5                       Schubert In Love     Lars Büchel 2018-03-01  Movie
# 6     We Have Always Lived in the Castle   Stacie Passon 2019-09-14  Movie
# ...                                  ...             ...        ...    ...
# 5830                         Bibi & Tina     Detlev Buck 2017-04-15  Movie
# 5832                         The Pursuit     John Papola 2019-08-07  Movie
# 5833                    Hurricane Bianca   Matt Kugelman 2017-01-01  Movie
# 5834                        Amar's Hands  Khaled Youssef 2019-04-26  Movie
# 5835               Bill Nye: Science Guy  Jason Sussberg 2018-04-25  Movie
#
# [3936 rows x 4 columns]

print(netflix.dropna())
#                                    title        director date_added   type
# 1                         A Patch of Fog  Michael Lennox 2017-04-15  Movie
# 3                              Uriyadi 2     Vijay Kumar 2019-08-02  Movie
# 4                      Shrek the Musical     Jason Moore 2013-12-29  Movie
# 5                       Schubert In Love     Lars Büchel 2018-03-01  Movie
# 6     We Have Always Lived in the Castle   Stacie Passon 2019-09-14  Movie
# ...                                  ...             ...        ...    ...
# 5830                         Bibi & Tina     Detlev Buck 2017-04-15  Movie
# 5832                         The Pursuit     John Papola 2019-08-07  Movie
# 5833                    Hurricane Bianca   Matt Kugelman 2017-01-01  Movie
# 5834                        Amar's Hands  Khaled Youssef 2019-04-26  Movie
# 5835               Bill Nye: Science Guy  Jason Sussberg 2018-04-25  Movie
#
# [3901 rows x 4 columns]

# Identify the days when Netflix added only one movie to its catalog
# Keep nothing if duplicates occurred
print(netflix.drop_duplicates(subset=["date_added"], keep=False))
#                                         title  ...   type
# 4                           Shrek the Musical  ...  Movie
# 12                              Without Gorky  ...  Movie
# 30                 Anjelah Johnson: Not Fancy  ...  Movie
# 38                             One Last Thing  ...  Movie
# 70    Marvel's Iron Man & Hulk: Heroes United  ...  Movie
# ...                                       ...  ...    ...
# 5748                                  Menorca  ...  Movie
# 5749                               Green Room  ...  Movie
# 5788          Chris Brown: Welcome to My Life  ...  Movie
# 5789                  A Very Murray Christmas  ...  Movie
# 5812                 Little Singham in London  ...  Movie
#
# [391 rows x 4 columns]
