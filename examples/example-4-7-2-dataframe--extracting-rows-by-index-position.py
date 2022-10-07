"""
-- Core pandas
---- The DataFrame Object
------ Selecting Rows from a DataFrame
-------- Extracting Rows by Index Position
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"], index_col="Name")
print(nba.iloc[300])
# Team             Denver Nuggets
# Position                     PF
# Birthday    1999-04-03 00:00:00
# Salary                  1416852
# Name: Jarred Vanderbilt, dtype: object

print(nba.iloc[[100, 200, 300, 400]])
# Name
# Brian Bowen           Indiana Pacers       SG 1998-10-02    79568
# Marco Belinelli    San Antonio Spurs       SF 1986-03-25  5846154
# Jarred Vanderbilt     Denver Nuggets       PF 1999-04-03  1416852
# Louis King           Detroit Pistons        F 1999-04-06    79568

# The row at index 404 is not included
print(nba.iloc[400:404])
# Name
# Louis King               Detroit Pistons        F 1999-04-06     79568
# Kostas Antetokounmpo  Los Angeles Lakers       PF 1997-11-20     79568
# Rodions Kurucs             Brooklyn Nets       PF 1998-02-05   1699236
# Spencer Dinwiddie          Brooklyn Nets       PG 1993-04-06  10605600

# The row at index 2 is not included
print(nba.iloc[:2])
# Name
# Shake Milton    Philadelphia 76ers       SG 1996-09-26  1445697
# Christian Wood     Detroit Pistons       PF 1995-09-27  1645357

print(nba.iloc[447:])
# Name
# Robin Lopez        Milwaukee Bucks        C 1988-04-01   4767000
# Collin Sexton  Cleveland Cavaliers       PG 1999-01-04   4764960
# Ricky Rubio           Phoenix Suns       PG 1990-10-21  16200000

# Extract rows from the 10th-to-last row up to (but not including) the 6th-to-last row
print(nba.iloc[-10:-6])
# Name
# Jared Dudley          Los Angeles Lakers       PF 1985-07-10  2564753
# Max Strus                  Chicago Bulls       SG 1996-03-28    79568
# Kevon Looney       Golden State Warriors        C 1996-02-06  4464286
# Willy Hernangomez      Charlotte Hornets        C 1994-05-27  1557250

print(nba.iloc[0:10:2])
# Name
# Shake Milton   Philadelphia 76ers       SG 1996-09-26   1445697
# PJ Washington   Charlotte Hornets       PF 1998-08-23   3831840
# Marial Shayok  Philadelphia 76ers        G 1995-07-26     79568
# Kendrick Nunn          Miami Heat       SG 1995-08-03   1416852
# Brook Lopez       Milwaukee Bucks        C 1988-04-01  12093024
