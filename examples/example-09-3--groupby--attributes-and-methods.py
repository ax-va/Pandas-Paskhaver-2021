#!/usr/bin/python3
"""
-- Applied pandas
---- The GroupBy object
------ Attributes and methods of a GroupBy object
"""

import pandas as pd
fortune = pd.read_csv("../datasets/fortune1000.csv")
sectors = fortune.groupby("Sector")

print(sectors.groups)
# {'Aerospace & Defense': [26, 50, 58, 98, 117, 118, 207, 224, 275, 380, 404, 406, 414, 540, 660, 661, 806, 829, 884,
# 930, 954, 955, 959, 975, 988], 'Apparel': [88, 241, 331, 420, 432, 526, 529, 554, 587, 678, 766, 774, 835, 861],
# 'Business Services': [142, 160, 187, 199, 201, 221, 235, 242, 253, 295, 325, 358, 364, 423, 462, 465, 486, 493, 497,
# ...

print(fortune.loc[26, "Sector"])  # Aerospace & Defense

# The GroupBy object’s first method extracts
# the first row listed for each sector in fortune
print(sectors.first())
#                                               Company  ...                                  Industry
# Sector                                                 ...
# Aerospace & Defense                            Boeing  ...                     Aerospace and Defense
# Apparel                                          Nike  ...                                   Apparel
# Business Services                       ManpowerGroup  ...                            Temporary Help
# Chemicals                                   DowDuPont  ...                                 Chemicals
# Energy                                    Exxon Mobil  ...                        Petroleum Refining
# Engineering & Construction                      Fluor  ...                 Engineering, Construction
# Financials                         Berkshire Hathaway  ...  Insurance: Property and Casualty (Stock)
# Food &  Drug Stores                            Kroger  ...                      Food and Drug Stores
# Food, Beverages & Tobacco                     PepsiCo  ...                    Food Consumer Products
# Health Care                        UnitedHealth Group  ...   Health Care: Insurance and Managed Care
# Hotels, Restaurants & Leisure  Marriott International  ...                  Hotels, Casinos, Resorts
# Household Products                   Procter & Gamble  ...           Household and Personal Products
# Industrials                          General Electric  ...                      Industrial Machinery
# Materials                         International Paper  ...                     Packaging, Containers
# Media                                          Disney  ...                             Entertainment
# Motor Vehicles & Parts                 General Motors  ...                  Motor Vehicles and Parts
# Retailing                                     Walmart  ...                     General Merchandisers
# Technology                                      Apple  ...               Computers, Office Equipment
# Telecommunications                               AT&T  ...                        Telecommunications
# Transportation                                    UPS  ...       Mail, Package, and Freight Delivery
# Wholesalers                                  McKesson  ...                  Wholesalers: Health Care
#
# [21 rows x 5 columns]

print(sectors.last())
#                                                    Company  ...                         Industry
# Sector                                                      ...
# Aerospace & Defense            Aerojet Rocketdyne Holdings  ...            Aerospace and Defense
# Apparel                               Wolverine World Wide  ...                          Apparel
# Business Services                                CoreLogic  ...          Financial Data Services
# Chemicals                                           Stepan  ...                        Chemicals
# Energy                            Superior Energy Services  ...  Oil and Gas Equipment, Services
# Engineering & Construction                        TopBuild  ...        Engineering, Construction
# Financials                                             HCP  ...                      Real estate
# Food &  Drug Stores                                  Freds  ...             Food and Drug Stores
# Food, Beverages & Tobacco                        Universal  ...                          Tobacco
# Health Care                                   Ensign Group  ...  Health Care: Medical Facilities
# Hotels, Restaurants & Leisure                 Vail Resorts  ...         Hotels, Casinos, Resorts
# Household Products                             ACCO Brands  ...      Home Equipment, Furnishings
# Industrials                                        Rexnord  ...             Industrial Machinery
# Materials                                 Summit Materials  ...        Building Materials, Glass
# Media                                        Tribune Media  ...                    Entertainment
# Motor Vehicles & Parts                 Tower International  ...         Motor Vehicles and Parts
# Retailing                                  Childrens Place  ...     Specialty Retailers: Apparel
# Technology                                VeriFone Systems  ...          Financial Data Services
# Telecommunications                     Zayo Group Holdings  ...               Telecommunications
# Transportation                       Echo Global Logistics  ...     Transportation and Logistics
# Wholesalers                       SiteOne Landscape Supply  ...         Wholesalers: Diversified
#
# [21 rows x 5 columns]

# sectors.nth(0) is equivalent to sectors.first()
print(sectors.nth(0))
#                                               Company  ...                                  Industry
# Sector                                                 ...
# Aerospace & Defense                            Boeing  ...                     Aerospace and Defense
# Apparel                                          Nike  ...                                   Apparel
# Business Services                       ManpowerGroup  ...                            Temporary Help
# Chemicals                                   DowDuPont  ...                                 Chemicals
# Energy                                    Exxon Mobil  ...                        Petroleum Refining
# Engineering & Construction                      Fluor  ...                 Engineering, Construction
# Financials                         Berkshire Hathaway  ...  Insurance: Property and Casualty (Stock)
# Food &  Drug Stores                            Kroger  ...                      Food and Drug Stores
# Food, Beverages & Tobacco                     PepsiCo  ...                    Food Consumer Products
# Health Care                        UnitedHealth Group  ...   Health Care: Insurance and Managed Care
# Hotels, Restaurants & Leisure  Marriott International  ...                  Hotels, Casinos, Resorts
# Household Products                   Procter & Gamble  ...           Household and Personal Products
# Industrials                          General Electric  ...                      Industrial Machinery
# Materials                         International Paper  ...                     Packaging, Containers
# Media                                          Disney  ...                             Entertainment
# Motor Vehicles & Parts                 General Motors  ...                  Motor Vehicles and Parts
# Retailing                                     Walmart  ...                     General Merchandisers
# Technology                                      Apple  ...               Computers, Office Equipment
# Telecommunications                               AT&T  ...                        Telecommunications
# Transportation                                    UPS  ...       Mail, Package, and Freight Delivery
# Wholesalers                                  McKesson  ...                  Wholesalers: Health Care
#
# [21 rows x 5 columns]

# Pull out the fourth row from each sector
print(sectors.nth(3))
#                                               Company  ...                                 Industry
# Sector                                                 ...
# Aerospace & Defense                  General Dynamics  ...                    Aerospace and Defense
# Apparel                                  Ralph Lauren  ...                                  Apparel
# Business Services                             Aramark  ...         Diversified Outsourcing Services
# Chemicals                                    Monsanto  ...                                Chemicals
# Energy                                  Valero Energy  ...                       Petroleum Refining
# Engineering & Construction                     Lennar  ...                             Homebuilders
# Financials                      Bank of America Corp.  ...                         Commercial Banks
# Food &  Drug Stores              Publix Super Markets  ...                     Food and Drug Stores
# Food, Beverages & Tobacco                   Coca-Cola  ...                                Beverages
# Health Care                                    Anthem  ...  Health Care: Insurance and Managed Care
# Hotels, Restaurants & Leisure         Las Vegas Sands  ...                 Hotels, Casinos, Resorts
# Household Products                      Newell Brands  ...              Home Equipment, Furnishings
# Industrials                                        3M  ...                            Miscellaneous
# Materials                         United States Steel  ...                                   Metals
# Media                                             CBS  ...                            Entertainment
# Motor Vehicles & Parts         Goodyear Tire & Rubber  ...                 Motor Vehicles and Parts
# Retailing                                  Home Depot  ...               Specialty Retailers: Other
# Technology                                        IBM  ...          Information Technology Services
# Telecommunications             Charter Communications  ...                       Telecommunications
# Transportation                        Delta Air Lines  ...                                 Airlines
# Wholesalers                                     Sysco  ...            Wholesalers: Food and Grocery
#
# [21 rows x 5 columns]

# head(2) extracts the first two rows for each sector
print(sectors.head(2))
#                       Company  ...                                  Industry
# 0                     Walmart  ...                     General Merchandisers
# 1                 Exxon Mobil  ...                        Petroleum Refining
# 2          Berkshire Hathaway  ...  Insurance: Property and Casualty (Stock)
# 3                       Apple  ...               Computers, Office Equipment
# 4          UnitedHealth Group  ...   Health Care: Insurance and Managed Care
# 5                    McKesson  ...                  Wholesalers: Health Care
# 6                  CVS Health  ...  Health Care: Pharmacy and Other Services
# 7                  Amazon.com  ...           Internet Services and Retailing
# 8                        AT&T  ...                        Telecommunications
# 9              General Motors  ...                  Motor Vehicles and Parts
# 10                 Ford Motor  ...                  Motor Vehicles and Parts
# 11          AmerisourceBergen  ...                  Wholesalers: Health Care
# 12                    Chevron  ...                        Petroleum Refining
# 15                    Verizon  ...                        Telecommunications
# 16                     Kroger  ...                      Food and Drug Stores
# 17           General Electric  ...                      Industrial Machinery
# 18   Walgreens Boots Alliance  ...                      Food and Drug Stores
# 19             JPMorgan Chase  ...                          Commercial Banks
# 21                   Alphabet  ...           Internet Services and Retailing
# 26                     Boeing  ...                     Aerospace and Defense
# 41           Procter & Gamble  ...           Household and Personal Products
# 43                        UPS  ...       Mail, Package, and Freight Delivery
# 44                    PepsiCo  ...                    Food Consumer Products
# 46                  DowDuPont  ...                                 Chemicals
# 47     Archer Daniels Midland  ...                           Food Production
# 49                      FedEx  ...       Mail, Package, and Freight Delivery
# 50        United Technologies  ...                     Aerospace and Defense
# 54                     Disney  ...                             Entertainment
# 64                Caterpillar  ...           Construction and Farm Machinery
# 88                       Nike  ...                                   Apparel
# 97                Time Warner  ...                             Entertainment
# 123       International Paper  ...                     Packaging, Containers
# 126    Marriott International  ...                  Hotels, Casinos, Resorts
# 130                 McDonalds  ...                             Food Services
# 142             ManpowerGroup  ...                            Temporary Help
# 150                     Nucor  ...                                    Metals
# 152                     Fluor  ...                 Engineering, Construction
# 160                      Visa  ...                   Financial Data Services
# 162            Kimberly-Clark  ...           Household and Personal Products
# 163                     AECOM  ...                 Engineering, Construction
# 189          Sherwin-Williams  ...                                 Chemicals
# 241                        VF  ...                                   Apparel
#
# [42 rows x 6 columns]

# tail(3) pulls the last three rows for each sector
print(sectors.tail(3))
#                              Company  ...                                  Industry
# 473              Windstream Holdings  ...                        Telecommunications
# 520         Telephone & Data Systems  ...                        Telecommunications
# 667                     Weis Markets  ...                      Food and Drug Stores
# 759             Hain Celestial Group  ...                    Food Consumer Products
# 774                     Fossil Group  ...                                   Apparel
# ..                               ...  ...                                       ...
# 995         SiteOne Landscape Supply  ...                  Wholesalers: Diversified
# 996  Charles River Laboratories Intl  ...  Health Care: Pharmacy and Other Services
# 997                        CoreLogic  ...                   Financial Data Services
# 998                     Ensign Group  ...           Health Care: Medical Facilities
# 999                              HCP  ...                               Real estate
#
# [63 rows x 6 columns]

print(sectors.get_group("Energy").head())
#                Company  Revenues  ...  Sector            Industry
# 1          Exxon Mobil  244363.0  ...  Energy  Petroleum Refining
# 12             Chevron  134533.0  ...  Energy  Petroleum Refining
# 27         Phillips 66   91568.0  ...  Energy  Petroleum Refining
# 30       Valero Energy   88407.0  ...  Energy  Petroleum Refining
# 40  Marathon Petroleum   67610.0  ...  Energy  Petroleum Refining
#
# [5 rows x 6 columns]
