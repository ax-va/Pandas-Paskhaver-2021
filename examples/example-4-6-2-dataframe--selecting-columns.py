"""
-- Core pandas
---- The DataFrame object
------ Selecting columns and rows from a DataFrame
-------- Selecting multiple columns from a DataFrame
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"], index_col="Name")

print(nba[["Salary", "Birthday"]])
#                   Salary   Birthday
# Name
# Shake Milton     1445697 1996-09-26
# Christian Wood   1645357 1995-09-27
# PJ Washington    3831840 1998-08-23
# Derrick Rose     7317074 1988-10-04
# Marial Shayok      79568 1995-07-26
# ...                  ...        ...
# Austin Rivers    2174310 1992-08-01
# Harry Giles      2578800 1998-04-22
# Robin Lopez      4767000 1988-04-01
# Collin Sexton    4764960 1999-01-04
# Ricky Rubio     16200000 1990-10-21
#
# [450 rows x 2 columns]

print(type(nba[["Salary", "Birthday"]]))  # <class 'pandas.core.frame.DataFrame'>

# The next example selects only string columns from nba:
print(nba.select_dtypes(include="object"))
# Name
# Shake Milton     Philadelphia 76ers       SG
# Christian Wood      Detroit Pistons       PF
# PJ Washington     Charlotte Hornets       PF
# Derrick Rose        Detroit Pistons       PG
# Marial Shayok    Philadelphia 76ers        G
# ...                             ...      ...
# Austin Rivers       Houston Rockets       PG
# Harry Giles        Sacramento Kings       PF
# Robin Lopez         Milwaukee Bucks        C
# Collin Sexton   Cleveland Cavaliers       PG
# Ricky Rubio            Phoenix Suns       PG
#
# [450 rows x 2 columns]

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"])
print(nba.select_dtypes(include="object"))
#                Name                 Team Position
# 0      Shake Milton   Philadelphia 76ers       SG
# 1    Christian Wood      Detroit Pistons       PF
# 2     PJ Washington    Charlotte Hornets       PF
# 3      Derrick Rose      Detroit Pistons       PG
# 4     Marial Shayok   Philadelphia 76ers        G
# ..              ...                  ...      ...
# 445   Austin Rivers      Houston Rockets       PG
# 446     Harry Giles     Sacramento Kings       PF
# 447     Robin Lopez      Milwaukee Bucks        C
# 448   Collin Sexton  Cleveland Cavaliers       PG
# 449     Ricky Rubio         Phoenix Suns       PG
#
# [450 rows x 3 columns]

nba = nba.set_index("Name")

# The next example selects all columns except string and integer columns:
print(nba.select_dtypes(exclude=["object", "int"]))
#                  Birthday
# Name
# Shake Milton   1996-09-26
# Christian Wood 1995-09-27
# PJ Washington  1998-08-23
# Derrick Rose   1988-10-04
# Marial Shayok  1995-07-26
# ...                   ...
# Austin Rivers  1992-08-01
# Harry Giles    1998-04-22
# Robin Lopez    1988-04-01
# Collin Sexton  1999-01-04
# Ricky Rubio    1990-10-21
#
# [450 rows x 1 columns]