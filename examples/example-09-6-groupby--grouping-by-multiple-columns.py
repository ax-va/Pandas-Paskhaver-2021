#!/usr/bin/python3
"""
-- Applied pandas
---- The GroupBy object
------ Grouping by multiple columns
"""

import pandas as pd
fortune = pd.read_csv("../datasets/fortune1000.csv")

sector_and_industry = fortune.groupby(by=["Sector", "Industry"])
print(sector_and_industry)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000026DC4A888B0>
print(sector_and_industry.size())
# Sector               Industry
# Aerospace & Defense  Aerospace and Defense                            25
# Apparel              Apparel                                          14
# Business Services    Advertising, marketing                            2
#                      Diversified Outsourcing Services                 14
#                      Education                                         2
#                                                                       ..
# Transportation       Trucking, Truck Leasing                          11
# Wholesalers          Wholesalers: Diversified                         24
#                      Wholesalers: Electronics and Office Equipment     8
#                      Wholesalers: Food and Grocery                     6
#                      Wholesalers: Health Care                          6
# Length: 82, dtype: int64

print(sector_and_industry.get_group(("Business Services", "Education")))
#                 Company  Revenues  ...             Sector   Industry
# 567  Laureate Education    4378.0  ...  Business Services  Education
# 810     Graham Holdings    2592.0  ...  Business Services  Education
#
# [2 rows x 6 columns]

print(sector_and_industry.sum())
#                                                                    Revenues  ...  Employees
# Sector              Industry                                                 ...
# Aerospace & Defense Aerospace and Defense                          383835.0  ...    1010124
# Apparel             Apparel                                        101157.3  ...     355699
# Business Services   Advertising, marketing                          23156.0  ...     127500
#                     Diversified Outsourcing Services                74175.0  ...     858600
#                     Education                                        6970.0  ...      70653
# ...                                                                     ...  ...        ...
# Transportation      Trucking, Truck Leasing                         43676.0  ...     208312
# Wholesalers         Wholesalers: Diversified                       130984.0  ...     262390
#                     Wholesalers: Electronics and Office Equipment  122231.0  ...     183518
#                     Wholesalers: Food and Grocery                  125908.0  ...     135767
#                     Wholesalers: Health Care                       509026.0  ...     162500
#
# [82 rows x 3 columns]

print(sector_and_industry["Revenues"].mean().head(5))
# Sector               Industry
# Aerospace & Defense  Aerospace and Defense               15353.400000
# Apparel              Apparel                              7225.521429
# Business Services    Advertising, marketing              11578.000000
#                      Diversified Outsourcing Services     5298.214286
#                      Education                            3485.000000
# Name: Revenues, dtype: float64