#!/usr/bin/python3
"""
-- Core pandas
---- The DataFrame object
------ Selecting rows from a dataFrame
-------- Extracting values from specific columns
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"], index_col="Name")

print(nba.loc["Giannis Antetokounmpo", "Team"])  # Milwaukee Bucks
print(nba.loc["James Harden", ["Position", "Birthday"]])
# Milwaukee Bucks
# Position                     PG
# Birthday    1989-08-26 00:00:00
# Name: James Harden, dtype: object
print(type(nba.loc["James Harden", ["Position", "Birthday"]]))  # <class 'pandas.core.series.Series'>

print(nba.loc[["Russell Westbrook", "Anthony Davis"], ["Team", "Salary"]])
#                                  Team    Salary
# Name
# Russell Westbrook     Houston Rockets  38506482
# Anthony Davis      Los Angeles Lakers  27093019
print(type(nba.loc[["Russell Westbrook", "Anthony Davis"], ["Team", "Salary"]]))  # <class 'pandas.core.frame.DataFrame'>

print(nba.loc["Joel Embiid", "Position":"Salary"])
# Position                      C
# Birthday    1994-03-16 00:00:00
# Salary                 27504630
# Name: Joel Embiid, dtype: object

print(nba.loc["Joel Embiid", "Salary":"Position"])
# Series([], Name: Joel Embiid, dtype: object)

# In nba, the Team column has an index of 0, Position has an index of 1,
# Birthday has an index of 2, Salary has an index of 3, and so on.

# The next example targets the value at the intersection of the row at index 57
# and the column at index 3 (Salary)
print(nba.iloc[57, 3])  # 796806

# not including index position 104, not including the column at index position 3 (Salary)
print(nba.iloc[100:104, :3])
#                              Team Position   Birthday
# Name
# Brian Bowen        Indiana Pacers       SG 1998-10-02
# Aaron Holiday      Indiana Pacers       PG 1996-09-30
# Troy Daniels   Los Angeles Lakers       SG 1991-07-15
# Buddy Hield      Sacramento Kings       SG 1992-12-17

# speedier
print(nba.at["Austin Rivers", "Birthday"])  # 1992-08-01 00:00:00
print(nba.iat[263, 1])  # PF