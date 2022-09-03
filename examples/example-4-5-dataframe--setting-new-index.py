"""
Setting a new index
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"])

# The two lines below are equivalent
nba.set_index(keys="Name")
nba.set_index("Name")
print(nba.set_index("Name"))
#                                Team Position   Birthday    Salary
# Name
# Shake Milton     Philadelphia 76ers       SG 1996-09-26   1445697
# Christian Wood      Detroit Pistons       PF 1995-09-27   1645357
# PJ Washington     Charlotte Hornets       PF 1998-08-23   3831840
# Derrick Rose        Detroit Pistons       PG 1988-10-04   7317074
# Marial Shayok    Philadelphia 76ers        G 1995-07-26     79568
# ...                             ...      ...        ...       ...
# Austin Rivers       Houston Rockets       PG 1992-08-01   2174310
# Harry Giles        Sacramento Kings       PF 1998-04-22   2578800
# Robin Lopez         Milwaukee Bucks        C 1988-04-01   4767000
# Collin Sexton   Cleveland Cavaliers       PG 1999-01-04   4764960
# Ricky Rubio            Phoenix Suns       PG 1990-10-21  16200000
#
# [450 rows x 4 columns]

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"], index_col="Name")
print(nba)
#                                Team Position   Birthday    Salary
# Name
# Shake Milton     Philadelphia 76ers       SG 1996-09-26   1445697
# Christian Wood      Detroit Pistons       PF 1995-09-27   1645357
# PJ Washington     Charlotte Hornets       PF 1998-08-23   3831840
# Derrick Rose        Detroit Pistons       PG 1988-10-04   7317074
# Marial Shayok    Philadelphia 76ers        G 1995-07-26     79568
# ...                             ...      ...        ...       ...
# Austin Rivers       Houston Rockets       PG 1992-08-01   2174310
# Harry Giles        Sacramento Kings       PF 1998-04-22   2578800
# Robin Lopez         Milwaukee Bucks        C 1988-04-01   4767000
# Collin Sexton   Cleveland Cavaliers       PG 1999-01-04   4764960
# Ricky Rubio            Phoenix Suns       PG 1990-10-21  16200000
#
# [450 rows x 4 columns]