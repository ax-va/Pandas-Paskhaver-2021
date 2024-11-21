#!/usr/bin/python3
"""
-- Applied pandas
---- The GroupBy object
------ Aggregate operations
"""

import pandas as pd
fortune = pd.read_csv("../datasets/fortune1000.csv")
sectors = fortune.groupby("Sector")
print(sectors.head(10))
#                  Company  ...                                  Industry
# 0                Walmart  ...                     General Merchandisers
# 1            Exxon Mobil  ...                        Petroleum Refining
# 2     Berkshire Hathaway  ...  Insurance: Property and Casualty (Stock)
# 3                  Apple  ...               Computers, Office Equipment
# 4     UnitedHealth Group  ...   Health Care: Insurance and Managed Care
# ..                   ...  ...                                       ...
# 587      Skechers U.S.A.  ...                                   Apparel
# 600       Ingles Markets  ...                      Food and Drug Stores
# 667         Weis Markets  ...                      Food and Drug Stores
# 678              Carters  ...                                   Apparel
# 907  Zayo Group Holdings  ...                        Telecommunications
#
# [210 rows x 6 columns]

print(sectors.sum().head(10))
#                              Revenues   Profits  Employees
# Sector
# Aerospace & Defense          383835.0   26733.5    1010124
# Apparel                      101157.3    6350.7     355699
# Business Services            316090.0   37179.2    1593999
# Chemicals                    251151.0   20475.0     474020
# Energy                      1543507.2   85369.6     981207
# Engineering & Construction   172782.0    7121.0     420745
# Financials                  2442480.0  264253.5    3500119
# Food &  Drug Stores          405468.0    8440.3    1398074
# Food, Beverages & Tobacco    510232.0   54902.5    1079316
# Health Care                 1507991.4   92791.1    2971189

print(sectors.get_group("Aerospace & Defense").head())
#                  Company  Revenues  ...               Sector               Industry
# 26                Boeing   93392.0  ...  Aerospace & Defense  Aerospace and Defense
# 50   United Technologies   59837.0  ...  Aerospace & Defense  Aerospace and Defense
# 58       Lockheed Martin   51048.0  ...  Aerospace & Defense  Aerospace and Defense
# 98      General Dynamics   30973.0  ...  Aerospace & Defense  Aerospace and Defense
# 117     Northrop Grumman   25803.0  ...  Aerospace & Defense  Aerospace and Defense
#
# [5 rows x 6 columns]

print(sectors.get_group("Aerospace & Defense").loc[:, "Revenues"].head())
# 26     93392.0
# 50     59837.0
# 58     51048.0
# 98     30973.0
# 117    25803.0
# Name: Revenues, dtype: float64

print(sectors.get_group("Aerospace & Defense").loc[:, "Revenues"].sum())  # 383835.0

print(sectors.mean().head())
#                          Revenues      Profits     Employees
# Sector
# Aerospace & Defense  15353.400000  1069.340000  40404.960000
# Apparel               7225.521429   453.621429  25407.071429
# Business Services     5963.962264   701.494340  30075.452830
# Chemicals             7610.636364   620.454545  14364.242424
# Energy               14425.300935   805.373585   9170.158879

print(sectors["Revenues"])
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x0000028442142910>

print(sectors["Revenues"].sum().head())
# Sector
# Aerospace & Defense     383835.0
# Apparel                 101157.3
# Business Services       316090.0
# Chemicals               251151.0
# Energy                 1543507.2
# Name: Revenues, dtype: float64

print(sectors["Employees"].mean().head())
# Sector
# Aerospace & Defense    40404.960000
# Apparel                25407.071429
# Business Services      30075.452830
# Chemicals              14364.242424
# Energy                  9170.158879
# Name: Employees, dtype: float64

print(sectors["Profits"].max().head())
# Sector
# Aerospace & Defense     8197.0
# Apparel                 4240.0
# Business Services       6699.0
# Chemicals               3000.4
# Energy                 19710.0
# Name: Profits, dtype: float64

print(sectors["Employees"].min().head())
# Sector
# Aerospace & Defense    5157
# Apparel                3700
# Business Services      2338
# Chemicals              1931
# Energy                  593
# Name: Employees, dtype: int64

aggregations = {"Revenues": "min", "Profits": "max", "Employees": "mean"}
print(sectors.agg(aggregations).head())
#                      Revenues  Profits     Employees
# Sector
# Aerospace & Defense    1877.0   8197.0  40404.960000
# Apparel                2350.0   4240.0  25407.071429
# Business Services      1851.0   6699.0  30075.452830
# Chemicals              1925.0   3000.4  14364.242424
# Energy                 1874.0  19710.0   9170.158879
