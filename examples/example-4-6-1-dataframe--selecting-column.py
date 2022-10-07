"""
-- Core pandas
---- The DataFrame object
------ Selecting Columns and Rows from a DataFrame
-------- Selecting a Single Column from a DataFrame
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"], index_col="Name")
print(nba.Salary)
# Name
# Shake Milton       1445697
# Christian Wood     1645357
# PJ Washington      3831840
# Derrick Rose       7317074
# Marial Shayok        79568
#                     ...
# Austin Rivers      2174310
# Harry Giles        2578800
# Robin Lopez        4767000
# Collin Sexton      4764960
# Ricky Rubio       16200000
# Name: Salary, Length: 450, dtype: int64

print(nba["Position"])
# Name
# Shake Milton      SG
# Christian Wood    PF
# PJ Washington     PF
# Derrick Rose      PG
# Marial Shayok      G
#                   ..
# Austin Rivers     PG
# Harry Giles       PF
# Robin Lopez        C
# Collin Sexton     PG
# Ricky Rubio       PG
# Name: Position, Length: 450, dtype: object

# The square-bracket syntax for extraction is recommended

