"""
-- Core pandas
---- The DataFrame Object
------ Renaming Columns or Rows
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"], index_col="Name")

print(nba.columns)
# Index(['Team', 'Position', 'Birthday', 'Salary'], dtype='object')

nba.columns = ["Team", "Position", "Date of Birth", "Pay"]
print(nba.head(1))
#                             Team Position Date of Birth      Pay
# Name
# Shake Milton  Philadelphia 76ers       SG    1996-09-26  1445697

nba.rename(columns={"Date of Birth": "Birthday"})
print(nba.head(1))
#                             Team Position Date of Birth      Pay
# Name
# Shake Milton  Philadelphia 76ers       SG    1996-09-26  1445697

print(nba.rename(columns={"Date of Birth": "Birthday"}).head(1))
#                             Team Position   Birthday      Pay
# Name
# Shake Milton  Philadelphia 76ers       SG 1996-09-26  1445697

print(nba.loc["Giannis Antetokounmpo"])
# Team                 Milwaukee Bucks
# Position                          PF
# Date of Birth    1994-12-06 00:00:00
# Pay                         25842697
# Name: Giannis Antetokounmpo, dtype: object

print(nba.rename(index={"Giannis Antetokounmpo": "Greek Player"}).loc["Greek Player"])
# Team                 Milwaukee Bucks
# Position                          PF
# Date of Birth    1994-12-06 00:00:00
# Pay                         25842697
# Name: Greek Player, dtype: object