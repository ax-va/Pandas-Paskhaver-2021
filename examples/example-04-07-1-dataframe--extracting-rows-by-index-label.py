"""
-- Core pandas
---- The DataFrame object
------ Selecting rows from a DataFrame
-------- Extracting rows by index label
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"], index_col="Name")

# The next example extracts the nba row with an index label of "LeBron James"
s = nba.loc["LeBron James"]
print(s)
# Team         Los Angeles Lakers
# Position                     PF
# Birthday    1984-12-30 00:00:00
# Salary                 37436858
# Name: LeBron James, dtype: object
print(type(s))  # <class 'pandas.core.series.Series'>

print(nba.loc[["Kawhi Leonard", "Paul George"]])
#                                Team Position   Birthday    Salary
# Name
# Kawhi Leonard  Los Angeles Clippers       SF 1991-06-29  32742000
# Paul George    Los Angeles Clippers       SF 1990-05-02  33005556
print(type(nba.loc[["Kawhi Leonard", "Paul George"]]))  # <class 'pandas.core.frame.DataFrame'>

print(nba.loc[["Paul George", "Kawhi Leonard"]])
#                                Team Position   Birthday    Salary
# Name
# Paul George    Los Angeles Clippers       SF 1990-05-02  33005556
# Kawhi Leonard  Los Angeles Clippers       SF 1991-06-29  32742000

print(nba.sort_index().loc["Otto Porter":"Patrick Beverley"])
# Name
# Otto Porter              Chicago Bulls       SF 1993-06-03  27250576
# PJ Dozier               Denver Nuggets       PG 1996-10-25     79568
# PJ Washington        Charlotte Hornets       PF 1998-08-23   3831840
# Pascal Siakam          Toronto Raptors       PF 1994-04-02   2351838
# Pat Connaughton        Milwaukee Bucks       SG 1993-01-06   1723050
# Patrick Beverley  Los Angeles Clippers       PG 1988-07-12  12345680

print(nba.loc["Robert Franks":"Darius Bazley"])
# Empty DataFrame
# Columns: [Team, Position, Birthday, Salary]
# Index: []

players = ["Otto Porter", "PJ Dozier", "PJ Washington"]
print(players[0:2])  # ['Otto Porter', 'PJ Dozier']

print(nba.sort_index().loc["Zach Collins":])
# Name
# Zach Collins     Portland Trail Blazers        C 1997-11-19   4240200
# Zach LaVine               Chicago Bulls       PG 1995-03-10  19500000
# Zach Norvell         Los Angeles Lakers       SG 1997-12-09     79568
# Zhaire Smith         Philadelphia 76ers       SG 1999-06-04   3058800
# Zion Williamson    New Orleans Pelicans        F 2000-07-06   9757440
# Zylan Cheatham     New Orleans Pelicans       SF 1995-11-17     79568

print(nba.loc["Zach Collins":])
# Name
# Zach Collins      Portland Trail Blazers        C 1997-11-19   4240200
# Stanley Johnson          Toronto Raptors       PF 1996-05-29   3623000
# Boban Marjanovic        Dallas Mavericks        C 1988-08-15   3500000
# Josh Magette               Orlando Magic       PG 1989-11-28     79568
# Kyle Lowry               Toronto Raptors       PG 1986-03-25  33296296
# ...                                  ...      ...        ...       ...
# Austin Rivers            Houston Rockets       PG 1992-08-01   2174310
# Harry Giles             Sacramento Kings       PF 1998-04-22   2578800
# Robin Lopez              Milwaukee Bucks        C 1988-04-01   4767000
# Collin Sexton        Cleveland Cavaliers       PG 1999-01-04   4764960
# Ricky Rubio                 Phoenix Suns       PG 1990-10-21  16200000
#
# [131 rows x 4 columns]

print(nba.sort_index().loc[:"Al Horford"])
# Name
# Aaron Gordon               Orlando Magic       PF 1995-09-16  19863636
# Aaron Holiday             Indiana Pacers       PG 1996-09-30   2239200
# Abdel Nader        Oklahoma City Thunder       SF 1993-09-25   1618520
# Adam Mokoka                Chicago Bulls        G 1998-07-18     79568
# Admiral Schofield     Washington Wizards       SF 1997-03-30   1000000
# Al Horford            Philadelphia 76ers        C 1986-06-03  28000000

# print(nba.loc["Bugs Bunny"])  # KeyError: 'Bugs Bunny'



