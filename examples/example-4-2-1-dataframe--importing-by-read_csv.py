"""
-- Core pandas
---- The DataFrame Object
------ Similarities Between Series and DataFrames
-------- Importing a DataFrame with the read_csv Function
"""
import pandas as pd

print(pd.read_csv("../datasets/nba.csv"))
#                Name                 Team Position  Birthday    Salary
# 0      Shake Milton   Philadelphia 76ers       SG   9/26/96   1445697
# 1    Christian Wood      Detroit Pistons       PF   9/27/95   1645357
# 2     PJ Washington    Charlotte Hornets       PF   8/23/98   3831840
# 3      Derrick Rose      Detroit Pistons       PG   10/4/88   7317074
# 4     Marial Shayok   Philadelphia 76ers        G   7/26/95     79568
# ..              ...                  ...      ...       ...       ...
# 445   Austin Rivers      Houston Rockets       PG    8/1/92   2174310
# 446     Harry Giles     Sacramento Kings       PF   4/22/98   2578800
# 447     Robin Lopez      Milwaukee Bucks        C    4/1/88   4767000
# 448   Collin Sexton  Cleveland Cavaliers       PG    1/4/99   4764960
# 449     Ricky Rubio         Phoenix Suns       PG  10/21/90  16200000
#
# [450 rows x 5 columns]

print(pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"]))  # in YYYY-MM-DD
#                Name                 Team Position   Birthday    Salary
# 0      Shake Milton   Philadelphia 76ers       SG 1996-09-26   1445697
# 1    Christian Wood      Detroit Pistons       PF 1995-09-27   1645357
# 2     PJ Washington    Charlotte Hornets       PF 1998-08-23   3831840
# 3      Derrick Rose      Detroit Pistons       PG 1988-10-04   7317074
# 4     Marial Shayok   Philadelphia 76ers        G 1995-07-26     79568
# ..              ...                  ...      ...        ...       ...
# 445   Austin Rivers      Houston Rockets       PG 1992-08-01   2174310
# 446     Harry Giles     Sacramento Kings       PF 1998-04-22   2578800
# 447     Robin Lopez      Milwaukee Bucks        C 1988-04-01   4767000
# 448   Collin Sexton  Cleveland Cavaliers       PG 1999-01-04   4764960
# 449     Ricky Rubio         Phoenix Suns       PG 1990-10-21  16200000
#
# [450 rows x 5 columns]

print(pd.read_csv("../datasets/nba-short.csv"))
#              Name                Team Position  Birthday   Salary
# 0    Shake Milton  Philadelphia 76ers       SG  26/09/96  1445697
# 1  Christian Wood     Detroit Pistons       PF  27/12/95  1645357
# 2   PJ Washington   Charlotte Hornets       PF  28/01/00  3831840

print(pd.read_csv("../datasets/nba-short.csv", parse_dates=["Birthday"]))  # in YYYY-MM-DD
#              Name                Team Position   Birthday   Salary
# 0    Shake Milton  Philadelphia 76ers       SG 1996-09-26  1445697
# 1  Christian Wood     Detroit Pistons       PF 1995-12-27  1645357
# 2   PJ Washington   Charlotte Hornets       PF 2000-01-28  3831840

print(pd.read_csv("../datasets/nba-very-short.csv"))
#            Name                Team Position  Birthday   Salary
# 0  Shake Milton  Philadelphia 76ers       SG  01/02/03  1445697

print(pd.read_csv("../datasets/nba-very-short.csv", parse_dates=["Birthday"]))  # in YYYY-MM-DD
#            Name                Team Position   Birthday   Salary
# 0  Shake Milton  Philadelphia 76ers       SG 2003-01-02  1445697


