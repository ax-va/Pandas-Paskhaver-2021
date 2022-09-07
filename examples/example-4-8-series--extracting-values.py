"""
Extracting values from Series
"""
import pandas as pd

nba = pd.read_csv("../datasets/nba.csv", parse_dates=["Birthday"], index_col="Name")

print(nba["Salary"].loc["Damian Lillard"])  # 29802321
print(nba["Salary"].at["Damian Lillard"])  # 29802321
print(nba["Salary"].iloc[234])  # 2033160
print(nba["Salary"].iat[234])  # 2033160