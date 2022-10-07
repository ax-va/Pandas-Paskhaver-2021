"""
-- Applied pandas
---- The GroupBy Object
------ Creating a GroupBy Object from a Data Set
"""

import pandas as pd

fortune = pd.read_csv("../datasets/fortune1000.csv")
print(fortune)
#                              Company  ...                                  Industry
# 0                            Walmart  ...                     General Merchandisers
# 1                        Exxon Mobil  ...                        Petroleum Refining
# 2                 Berkshire Hathaway  ...  Insurance: Property and Casualty (Stock)
# 3                              Apple  ...               Computers, Office Equipment
# 4                 UnitedHealth Group  ...   Health Care: Insurance and Managed Care
# ..                               ...  ...                                       ...
# 995         SiteOne Landscape Supply  ...                  Wholesalers: Diversified
# 996  Charles River Laboratories Intl  ...  Health Care: Pharmacy and Other Services
# 997                        CoreLogic  ...                   Financial Data Services
# 998                     Ensign Group  ...           Health Care: Medical Facilities
# 999                              HCP  ...                               Real estate
#
# [1000 rows x 6 columns]

fortune.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000 entries, 0 to 999
# Data columns (total 6 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Company    1000 non-null   object
#  1   Revenues   1000 non-null   float64
#  2   Profits    998 non-null    float64
#  3   Employees  1000 non-null   int64
#  4   Sector     1000 non-null   object
#  5   Industry   1000 non-null   object
# dtypes: float64(2), int64(1), object(3)
# memory usage: 47.0+ KB

# Without GroupBy
in_retailing = fortune["Sector"] == "Retailing"
retail_companies = fortune[in_retailing]
print(retail_companies)
#                       Company  ...                         Industry
# 0                     Walmart  ...            General Merchandisers
# 7                  Amazon.com  ...  Internet Services and Retailing
# 14                     Costco  ...            General Merchandisers
# 22                 Home Depot  ...       Specialty Retailers: Other
# 38                     Target  ...            General Merchandisers
# ..                        ...  ...                              ...
# 909      99 Cents Only Stores  ...       Specialty Retailers: Other
# 926                   Express  ...     Specialty Retailers: Apparel
# 971               Finish Line  ...     Specialty Retailers: Apparel
# 989  Barnes & Noble Education  ...       Specialty Retailers: Other
# 992           Childrens Place  ...     Specialty Retailers: Apparel
#
# [77 rows x 6 columns]

print(retail_companies["Revenues"].head())
# 0     500343.0
# 7     177866.0
# 14    129025.0
# 22    100904.0
# 38     71879.0
# Name: Revenues, dtype: float64

print(retail_companies["Revenues"].mean())  # 21874.714285714286

# With GroupBy
sectors = fortune.groupby("Sector")
print(sectors)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000247AF286970>
print(len(sectors))  # 21
print(fortune["Sector"].nunique())  # 21
print(sectors.size())
# Sector
# Aerospace & Defense               25
# Apparel                           14
# Business Services                 53
# Chemicals                         33
# Energy                           107
# Engineering & Construction        27
# Financials                       155
# Food &  Drug Stores               12
# Food, Beverages & Tobacco         37
# Health Care                       71
# Hotels, Restaurants & Leisure     26
# Household Products                28
# Industrials                       49
# Materials                         45
# Media                             25
# Motor Vehicles & Parts            19
# Retailing                         77
# Technology                       103
# Telecommunications                10
# Transportation                    40
# Wholesalers                       44
# dtype: int64

