#!/usr/bin/python3
"""
-- Core pandas
---- The DataFrame object
------ Sorting a DataFrame
-------- Sorting by a single column
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"])

# The two lines below are equivalent
sorted1 = nba.sort_values("Name")
sorted2 = nba.sort_values(by="Name")
print(sorted1)
#                   Name                   Team Position   Birthday    Salary
# 52        Aaron Gordon          Orlando Magic       PF 1995-09-16  19863636
# 101      Aaron Holiday         Indiana Pacers       PG 1996-09-30   2239200
# 437        Abdel Nader  Oklahoma City Thunder       SF 1993-09-25   1618520
# 81         Adam Mokoka          Chicago Bulls        G 1998-07-18     79568
# 399  Admiral Schofield     Washington Wizards       SF 1997-03-30   1000000
# ..                 ...                    ...      ...        ...       ...
# 159        Zach LaVine          Chicago Bulls       PG 1995-03-10  19500000
# 302       Zach Norvell     Los Angeles Lakers       SG 1997-12-09     79568
# 312       Zhaire Smith     Philadelphia 76ers       SG 1999-06-04   3058800
# 137    Zion Williamson   New Orleans Pelicans        F 2000-07-06   9757440
# 248     Zylan Cheatham   New Orleans Pelicans       SF 1995-11-17     79568
#
# [450 rows x 5 columns]
print(sorted2)
#                   Name                   Team Position   Birthday    Salary
# 52        Aaron Gordon          Orlando Magic       PF 1995-09-16  19863636
# 101      Aaron Holiday         Indiana Pacers       PG 1996-09-30   2239200
# 437        Abdel Nader  Oklahoma City Thunder       SF 1993-09-25   1618520
# 81         Adam Mokoka          Chicago Bulls        G 1998-07-18     79568
# 399  Admiral Schofield     Washington Wizards       SF 1997-03-30   1000000
# ..                 ...                    ...      ...        ...       ...
# 159        Zach LaVine          Chicago Bulls       PG 1995-03-10  19500000
# 302       Zach Norvell     Los Angeles Lakers       SG 1997-12-09     79568
# 312       Zhaire Smith     Philadelphia 76ers       SG 1999-06-04   3058800
# 137    Zion Williamson   New Orleans Pelicans        F 2000-07-06   9757440
# 248     Zylan Cheatham   New Orleans Pelicans       SF 1995-11-17     79568
#
# [450 rows x 5 columns]

sorted3 = nba.sort_values("Name", ascending=False).head()
print(sorted3)
#                 Name                  Team Position   Birthday    Salary
# 248   Zylan Cheatham  New Orleans Pelicans       SF 1995-11-17     79568
# 137  Zion Williamson  New Orleans Pelicans        F 2000-07-06   9757440
# 312     Zhaire Smith    Philadelphia 76ers       SG 1999-06-04   3058800
# 302     Zach Norvell    Los Angeles Lakers       SG 1997-12-09     79568
# 159      Zach LaVine         Chicago Bulls       PG 1995-03-10  19500000

print(type(sorted1))  # <class 'pandas.core.frame.DataFrame'>
print(type(sorted3))  # <class 'pandas.core.frame.DataFrame'>

# Find the five youngest players in nba without using the nsmallest method
print(nba.sort_values("Birthday", ascending=False).head())
#                     Name                  Team Position   Birthday   Salary
# 136      Sekou Doumbouya       Detroit Pistons       SF 2000-12-23  3285120
# 432  Talen Horton-Tucker    Los Angeles Lakers       GF 2000-11-25   898310
# 137      Zion Williamson  New Orleans Pelicans        F 2000-07-06  9757440
# 313           RJ Barrett       New York Knicks       SG 2000-06-14  7839960
# 392         Jalen Lecque          Phoenix Suns        G 2000-06-13   898310