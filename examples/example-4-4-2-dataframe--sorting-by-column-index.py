"""
-- Core pandas
---- The DataFrame Object
------ Sorting by Index
-------- Sorting by Column Index
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"])

# The two lines below are equivalent
print(nba.sort_index(axis="columns").head())
#     Birthday            Name Position   Salary                Team
# 0 1996-09-26    Shake Milton       SG  1445697  Philadelphia 76ers
# 1 1995-09-27  Christian Wood       PF  1645357     Detroit Pistons
# 2 1998-08-23   PJ Washington       PF  3831840   Charlotte Hornets
# 3 1988-10-04    Derrick Rose       PG  7317074     Detroit Pistons
# 4 1995-07-26   Marial Shayok        G    79568  Philadelphia 76ers
print(nba.sort_index(axis=1).head())
#     Birthday            Name Position   Salary                Team
# 0 1996-09-26    Shake Milton       SG  1445697  Philadelphia 76ers
# 1 1995-09-27  Christian Wood       PF  1645357     Detroit Pistons
# 2 1998-08-23   PJ Washington       PF  3831840   Charlotte Hornets
# 3 1988-10-04    Derrick Rose       PG  7317074     Detroit Pistons
# 4 1995-07-26   Marial Shayok        G    79568  Philadelphia 76ers

print(nba.sort_index(axis="columns", ascending=False).head())
#                  Team   Salary Position            Name   Birthday
# 0  Philadelphia 76ers  1445697       SG    Shake Milton 1996-09-26
# 1     Detroit Pistons  1645357       PF  Christian Wood 1995-09-27
# 2   Charlotte Hornets  3831840       PF   PJ Washington 1998-08-23
# 3     Detroit Pistons  7317074       PG    Derrick Rose 1988-10-04
# 4  Philadelphia 76ers    79568        G   Marial Shayok 1995-07-26
