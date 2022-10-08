"""
-- Core pandas
---- The DataFrame object
------ Sorting a DataFrame
-------- Sorting by multiple columns
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"])
print(nba.sort_values(by=["Team", "Name"]))
#                 Name                Team Position   Birthday    Salary
# 359         Alex Len       Atlanta Hawks        C 1993-06-16   4160000
# 167     Allen Crabbe       Atlanta Hawks       SG 1992-04-09  18500000
# 276  Brandon Goodwin       Atlanta Hawks       PG 1995-10-02     79568
# 438   Bruno Fernando       Atlanta Hawks        C 1998-08-15   1400000
# 194      Cam Reddish       Atlanta Hawks       SF 1999-09-01   4245720
# ..               ...                 ...      ...        ...       ...
# 418     Jordan McRae  Washington Wizards       PG 1991-03-28   1645357
# 273  Justin Robinson  Washington Wizards       PG 1997-10-12    898310
# 428    Moritz Wagner  Washington Wizards        C 1997-04-26   2063520
# 21     Rui Hachimura  Washington Wizards       PF 1998-02-08   4469160
# 36     Thomas Bryant  Washington Wizards        C 1997-07-31   8000000
#
# [450 rows x 5 columns]

print(nba.sort_values(["Team", "Name"], ascending=False))
#                 Name                Team Position   Birthday    Salary
# 36     Thomas Bryant  Washington Wizards        C 1997-07-31   8000000
# 21     Rui Hachimura  Washington Wizards       PF 1998-02-08   4469160
# 428    Moritz Wagner  Washington Wizards        C 1997-04-26   2063520
# 273  Justin Robinson  Washington Wizards       PG 1997-10-12    898310
# 418     Jordan McRae  Washington Wizards       PG 1991-03-28   1645357
# ..               ...                 ...      ...        ...       ...
# 194      Cam Reddish       Atlanta Hawks       SF 1999-09-01   4245720
# 438   Bruno Fernando       Atlanta Hawks        C 1998-08-15   1400000
# 276  Brandon Goodwin       Atlanta Hawks       PG 1995-10-02     79568
# 167     Allen Crabbe       Atlanta Hawks       SG 1992-04-09  18500000
# 359         Alex Len       Atlanta Hawks        C 1993-06-16   4160000
#
# [450 rows x 5 columns]

print(nba.sort_values(by=["Team", "Salary"], ascending=[True, False]))
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
