"""
Shared methods of Series and DataFrames
"""

import numpy as np
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"])
print(nba.head(2))
#              Name                Team Position   Birthday   Salary
# 0    Shake Milton  Philadelphia 76ers       SG 1996-09-26  1445697
# 1  Christian Wood     Detroit Pistons       PF 1995-09-27  1645357

print(nba.tail(n=3))
#               Name                 Team Position   Birthday    Salary
# 447    Robin Lopez      Milwaukee Bucks        C 1988-04-01   4767000
# 448  Collin Sexton  Cleveland Cavaliers       PG 1999-01-04   4764960
# 449    Ricky Rubio         Phoenix Suns       PG 1990-10-21  16200000

print(nba.tail())
#               Name                 Team Position   Birthday    Salary
# 445  Austin Rivers      Houston Rockets       PG 1992-08-01   2174310
# 446    Harry Giles     Sacramento Kings       PF 1998-04-22   2578800
# 447    Robin Lopez      Milwaukee Bucks        C 1988-04-01   4767000
# 448  Collin Sexton  Cleveland Cavaliers       PG 1999-01-04   4764960
# 449    Ricky Rubio         Phoenix Suns       PG 1990-10-21  16200000

print(nba.sample(3))
#                Name               Team Position   Birthday    Salary
# 233  Ersan Ilyasova    Milwaukee Bucks       PF 1987-05-15   7000000
# 275    Trevor Ariza   Sacramento Kings       SF 1985-06-30  12200000
# 415  Andre Iguodala  Memphis Grizzlies       SF 1984-01-28  17185185

print(nba.sample(3))
#                  Name               Team Position   Birthday   Salary
# 270  Jarrell Brantley          Utah Jazz       PF 1996-06-07    79568
# 261    Garrett Temple      Brooklyn Nets       PG 1986-05-08  4767000
# 382       Jae Crowder  Memphis Grizzlies       SF 1990-07-06  7815533

s = nba.nunique()
print(s)
# Name        450
# Team         30
# Position      9
# Birthday    430
# Salary      269
# dtype: int64

# There are 30 unique teams, 269 unique salaries, and 9 unique positions in nba.

# The 'max' method returns a Series with the maximum value from each column.
print(nba.max())
# Name             Zylan Cheatham
# Team         Washington Wizards
# Position                     SG
# Birthday    2000-12-23 00:00:00
# Salary                 40231758
# dtype: object

# The min method returns a Series with the minimum value from each column.
print(nba.min())
# Name               Aaron Gordon
# Team              Atlanta Hawks
# Position                      C
# Birthday    1977-01-26 00:00:00
# Salary                    79568
# dtype: object

print(nba.nlargest(n=4, columns="Salary"))
#                   Name                   Team Position   Birthday    Salary
# 205      Stephen Curry  Golden State Warriors       PG 1988-03-14  40231758
# 38          Chris Paul  Oklahoma City Thunder       PG 1985-05-06  38506482
# 219  Russell Westbrook        Houston Rockets       PG 1988-11-12  38506482
# 251          John Wall     Washington Wizards       PG 1990-09-06  38199000

print(nba.nsmallest(n=3, columns=["Birthday"]))
#               Name             Team Position   Birthday   Salary
# 98    Vince Carter    Atlanta Hawks       PF 1977-01-26  2564753
# 196  Udonis Haslem       Miami Heat        C 1980-06-09  2564753
# 262    Kyle Korver  Milwaukee Bucks       PF 1981-03-17  6004753

# print(nba.nlargest(n=4, columns="Name"))
# # TypeError: Column 'Name' has dtype object, cannot use method 'nlargest' with this dtype

# print(nba.min(n=3, column="Name"))
# # TypeError: min() got an unexpected keyword argument 'n'

print(nba.sum(numeric_only=True))
# Salary    3444112694
# dtype: int64

print(nba.mean(numeric_only=True))
# Salary    7.653584e+06
# dtype: float64

print(nba.median(numeric_only=True))
# Salary    3303074.5
# dtype: float64

print(nba.mode(numeric_only=True))
#    Salary
# 0   79568

# The mode of a set of values is the value that appears most often. It can be multiple values.

df = pd.DataFrame([('bird', 2, 2),
                   ('mammal', 4, np.nan),
                   ('arthropod', 8, 0),
                   ('bird', 2, np.nan)],
                  index=('falcon', 'horse', 'spider', 'ostrich'),
                  columns=('species', 'legs', 'wings'))

print(df)
#            species  legs  wings
# falcon        bird     2    2.0
# horse       mammal     4    NaN
# spider   arthropod     8    0.0
# ostrich       bird     2    NaN

print(df.mode())
#   species  legs  wings
# 0    bird   2.0    0.0
# 1     NaN   NaN    2.0

# By default, missing values are not considered, and the mode of wings are both 0 and 2.
# Because the resulting DataFrame has two rows, the second row of species and legs contains NaN.

print(nba.std(numeric_only=True))
# Salary    9.288810e+06
# dtype: float64

# http://mng.bz/myDa