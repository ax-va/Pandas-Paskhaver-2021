"""
-- Core pandas
---- The DataFrame object
------ Sorting by index
-------- Sorting by row index
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"])
nba = nba.sort_values(by=["Team", "Salary"], ascending=[True, False])
print(nba)
#                   Name                Team Position   Birthday    Salary
# 111   Chandler Parsons       Atlanta Hawks       SF 1988-10-25  25102512
# 28         Evan Turner       Atlanta Hawks       PG 1988-10-27  18606556
# 167       Allen Crabbe       Atlanta Hawks       SG 1992-04-09  18500000
# 213    De'Andre Hunter       Atlanta Hawks       SF 1997-12-02   7068360
# 339      Jabari Parker       Atlanta Hawks       PF 1995-03-15   6500000
# ..                 ...                 ...      ...        ...       ...
# 80         Isaac Bonga  Washington Wizards       PG 1999-11-08   1416852
# 399  Admiral Schofield  Washington Wizards       SF 1997-03-30   1000000
# 273    Justin Robinson  Washington Wizards       PG 1997-10-12    898310
# 283   Garrison Mathews  Washington Wizards       SG 1996-10-24     79568
# 353      Chris Chiozza  Washington Wizards       PG 1995-11-21     79568
#
# [450 rows x 5 columns]

nba = nba.sort_index()
print(nba)
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

print(nba.sort_index(ascending=False))
#                Name                 Team Position   Birthday    Salary
# 449     Ricky Rubio         Phoenix Suns       PG 1990-10-21  16200000
# 448   Collin Sexton  Cleveland Cavaliers       PG 1999-01-04   4764960
# 447     Robin Lopez      Milwaukee Bucks        C 1988-04-01   4767000
# 446     Harry Giles     Sacramento Kings       PF 1998-04-22   2578800
# 445   Austin Rivers      Houston Rockets       PG 1992-08-01   2174310
# ..              ...                  ...      ...        ...       ...
# 4     Marial Shayok   Philadelphia 76ers        G 1995-07-26     79568
# 3      Derrick Rose      Detroit Pistons       PG 1988-10-04   7317074
# 2     PJ Washington    Charlotte Hornets       PF 1998-08-23   3831840
# 1    Christian Wood      Detroit Pistons       PF 1995-09-27   1645357
# 0      Shake Milton   Philadelphia 76ers       SG 1996-09-26   1445697
#
# [450 rows x 5 columns]