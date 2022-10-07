"""
-- Core pandas
---- The DataFrame Object
------ Coding Challenge
"""
import pandas as pd

# Import the nfl.csv file
# Convert the values in its Birthday column to datetimes
# Set the DataFrame index to store the player names
nfl = pd.read_csv("../datasets/nfl.csv", parse_dates=["Birthday"], index_col="Name")
# nfl = pd.read_csv("../datasets/nfl.csv", parse_dates=["Birthday"])
# nfl = nfl.set_index("Name")

# Count the number of players per team
# The two lines below are equivalent
s1 = nfl.Team.value_counts().head()
s2 = nfl["Team"].value_counts().head()
print(s1)
# New York Jets          58
# Kansas City Chiefs     56
# Washington Redskins    56
# New Orleans Saints     55
# San Francisco 49Ers    55
# Name: Team, dtype: int64
print(s2)
# New York Jets          58
# Kansas City Chiefs     56
# Washington Redskins    56
# New Orleans Saints     55
# San Francisco 49Ers    55
# Name: Team, dtype: int64

# Get the five highest-paid players
print(nfl.sort_values("Salary", ascending=False).head())
#                                  Team Position   Birthday    Salary
# Name
# Kirk Cousins        Minnesota Vikings       QB 1988-08-19  27500000
# Jameis Winston   Tampa Bay Buccaneers       QB 1994-01-06  20922000
# Marcus Mariota       Tennessee Titans       QB 1993-10-30  20922000
# Derek Carr            Oakland Raiders       QB 1991-03-28  19900000
# Jimmy Garoppolo   San Francisco 49Ers       QB 1991-11-02  17200000

# Get the five highest-paid players
print(nfl.nlargest(n=5, columns="Salary"))
#                                  Team Position   Birthday    Salary
# Name
# Kirk Cousins        Minnesota Vikings       QB 1988-08-19  27500000
# Marcus Mariota       Tennessee Titans       QB 1993-10-30  20922000
# Jameis Winston   Tampa Bay Buccaneers       QB 1994-01-06  20922000
# Derek Carr            Oakland Raiders       QB 1991-03-28  19900000
# Jimmy Garoppolo   San Francisco 49Ers       QB 1991-11-02  17200000

# Sort the data set first by teams in alphabetical order and then by salary in descending order
print(nfl.sort_values(by=["Team", "Salary"], ascending=[True, False]))
#                                    Team Position   Birthday    Salary
# Name
# Chandler Jones        Arizona Cardinals      OLB 1990-02-27  16500000
# Patrick Peterson      Arizona Cardinals       CB 1990-07-11  11000000
# Larry Fitzgerald      Arizona Cardinals       WR 1983-08-31  11000000
# David Johnson         Arizona Cardinals       RB 1991-12-16   5700000
# Justin Pugh           Arizona Cardinals        G 1990-08-15   5000000
# ...                                 ...      ...        ...       ...
# Ross Pierschbacher  Washington Redskins        C 1995-05-05    495000
# Kelvin Harmon       Washington Redskins       WR 1996-12-15    495000
# Wes Martin          Washington Redskins        G 1996-05-09    495000
# Jimmy Moreland      Washington Redskins       CB 1995-08-26    495000
# Jeremy Reaves       Washington Redskins       SS 1996-08-29    495000
#
# [1655 rows x 4 columns]

# Get the oldest player on the New York Jets roster and his birthday
nfl = nfl.reset_index().set_index(keys="Team")
print(nfl.head(3))
#                                 Name Position   Birthday   Salary
# Team
# Philadelphia Eagles     Tremon Smith       RB 1996-07-20   570000
# Cincinnati Bengals    Shawn Williams       SS 1991-05-13  3500000
# New England Patriots     Adam Butler       DT 1994-04-12   645000

print(nfl.loc["New York Jets"].head())
#                            Name Position   Birthday   Salary
# Team
# New York Jets   Bronson Kaufusi       DE 1991-07-06   645000
# New York Jets    Darryl Roberts       CB 1990-11-26  1000000
# New York Jets     Jordan Willis       DE 1995-05-02   754750
# New York Jets  Quinnen Williams       DE 1997-12-21   495000
# New York Jets        Sam Ficken        K 1992-12-14   495000

print(nfl.loc["New York Jets"].sort_values("Birthday").head(1))
#                      Name Position   Birthday   Salary
# Team
# New York Jets  Ryan Kalil        C 1985-03-29  2400000
