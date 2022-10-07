"""
-- Applied pandas
---- MultiIndex DataFrames
------ Coding Challenge
"""
import pandas as pd

investments = pd.read_csv("../datasets/investments.csv")
print(investments.head())
#                  Name    Market     Status State  Funding Rounds
# 0            #waywire      News   Acquired    NY               1
# 1  &TV Communications     Games  Operating    CA               2
# 2  -R- Ranch and Mine   Tourism  Operating    TX               2
# 3    004 Technologies  Software  Operating    IL               1
# 4             1-4 All  Software  Operating    NC               1

print(investments.nunique())
# Name              27763
# Market              693
# Status                3
# State                61
# Funding Rounds       16
# dtype: int64

investments = investments.set_index(keys=["Status", "Funding Rounds", "State"]).sort_index()
print(investments.head())
#                                                    Name               Market
# Status   Funding Rounds State
# Acquired 1              AB               Hallpass Media                Games
#                         AL                    EnteGreat  Enterprise Software
#                         AL     Onward Behavioral Health        Biotechnology
#                         AL                      Proxsys        Biotechnology
#                         AZ                  Envox Group     Public Relations

# Extract all rows with a Status of "Closed"
print(investments.loc[("Closed", )].head())
#                                              Name                Market
# Funding Rounds State
# 1              AB     Cardinal Media Technologies  Social Network Media
#                AB                Easy Bill Online              Tracking
#                AB                   Globel Direct      Public Relations
#                AB               Ph03nix New Media                 Games
#                AL                           Naubo                  News

# Extract all rows with a Status of "Acquired" and 10 funding rounds
print(investments.loc[("Acquired", 10)])
#                    Name       Market
# State
# NY     Genesis Networks  Web Hosting
# TX       ACTIVE Network     Software

# Extract all rows with a Status of "Operating", six funding rounds, and a State of "NJ"
print(investments.loc[("Operating", 6, "NJ")])
#                                               Name             Market
# Status    Funding Rounds State
# Operating 6              NJ     Agile Therapeutics      Biotechnology
#                          NJ               Agilence  Retail Technology
#                          NJ      Edge Therapeutics      Biotechnology
#                          NJ                Nistica        Web Hosting

# Extract all rows with a Status of "Closed" and eight funding rounds.
# Pull out only the Name column.
print(investments.loc[("Closed", 8), ("Name",)])
#                       Name
# State
# CA               CipherMax
# CA      Dilithium Networks
# CA                 Moblyng
# CA                SolFocus
# CA                Solyndra
# FL     Extreme Enterprises
# GA                MedShape
# NC     Biolex Therapeutics
# WA              Cozi Group

# Extract all rows with a State of "NJ", irrespective of the values in the Status and Funding Rounds levels.
# The two lines below are equivalent:
investments.xs(key="NJ", level=2).head()
investments.xs(key="NJ", level="State").head()
print(investments.xs(key="NJ", level=2).head())
#                                     Name               Market
# Status   Funding Rounds
# Acquired 1                         AkaRx        Biotechnology
#          1                Aptalis Pharma        Biotechnology
#          1                        Cadent             Software
#          1               Cancer Genetics  Health And Wellness
#          1                     Clacendix           E-Commerce

# Reincorporate the MultiIndex levels back into the DataFrame as columns
investments = investments.reset_index()
print(investments.head())
#      Status  Funding Rounds  ...                      Name               Market
# 0  Acquired               1  ...            Hallpass Media                Games
# 1  Acquired               1  ...                 EnteGreat  Enterprise Software
# 2  Acquired               1  ...  Onward Behavioral Health        Biotechnology
# 3  Acquired               1  ...                   Proxsys        Biotechnology
# 4  Acquired               1  ...               Envox Group     Public Relations
#
# [5 rows x 5 columns]
