"""
-- Applied pandas
---- MultiIndex DataFrames
------ Sorting a MultiIndex
"""
import pandas as pd

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv", index_col=[0, 1, 2], header=[0, 1])
neighborhoods.columns.names = ["Category", "Subcategory"]

print(neighborhoods.sort_index())
# Category                                      Culture         Services
# Subcategory                               Restaurants Museums   Police Schools
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove              C-      A-       A+       C
#       Scottstad      082 Leblanc Freeway            D      C-        D      B+
#                      114 Jones Garden              D-      D-        D       D
#       Stevenshire    238 Andrew Rue                D-       A       A-      A-
# AL    Clarkland      430 Douglas Mission            A       F       C+      B+
# ...                                               ...     ...      ...     ...
# WY    Lake Nicole    754 Weaver Turnpike            B      D-        B       D
#                      933 Jennifer Burg              C      A+       A-       C
#       Martintown     013 Bell Mills                C-       D       A-      B-
#       Port Jason     624 Faulkner Orchard          A-       F       C+      C+
#       Reneeshire     717 Patel Square               B      B+        D       A
#
# [251 rows x 4 columns]

print(neighborhoods.sort_index(ascending=False).head())
# Category                                   Culture         Services
# Subcategory                            Restaurants Museums   Police Schools
# State City        Street
# WY    Reneeshire  717 Patel Square               B      B+        D       A
#       Port Jason  624 Faulkner Orchard          A-       F       C+      C+
#       Martintown  013 Bell Mills                C-       D       A-      B-
#       Lake Nicole 933 Jennifer Burg              C      A+       A-       C
#                   754 Weaver Turnpike            B      D-        B       D

print(neighborhoods.sort_index(ascending=[True, False, True]).head())
# Category                                     Culture         Services
# Subcategory                              Restaurants Museums   Police Schools
# State City           Street
# AK    Stevenshire    238 Andrew Rue               D-       A       A-      A-
#       Scottstad      082 Leblanc Freeway           D      C-        D      B+
#                      114 Jones Garden             D-      D-        D       D
#       Rowlandchester 386 Rebecca Cove             C-      A-       A+       C
# AL    Vegaside       191 Mindy Meadows            B+      A-       A+      D+

# The two lines below are equivalent
neighborhoods.sort_index(level=1)
neighborhoods.sort_index(level="City")
print(neighborhoods.sort_index(level="City"))
# Category                                      Culture         Services
# Subcategory                               Restaurants Museums   Police Schools
# State City          Street
# AR    Allisonland   124 Diaz Brooks                C-      A+        F      C+
# GA    Amyburgh      941 Brian Expressway            B       B       D-      C+
# IA    Amyburgh      163 Heather Neck                F       D       A+      A-
# ID    Andrewshire   952 Ellis Drive                C+      A-       C+       A
# UT    Baileyfort    919 Stewart Hills              D+      C+        A       C
# ...                                               ...     ...      ...     ...
# NC    West Scott    348 Jack Branch                A-      D-       A-       A
# SD    West Scott    139 Hardy Vista                C+      A-       D+      B-
# IN    Wilsonborough 066 Carr Road                  A+      C-        B       F
# NC    Wilsonshire   871 Christopher Vista          B+       B       D+       F
# NV    Wilsonshire   542 Jessica Stream              A      A+       C-      C+
#
# [251 rows x 4 columns]

# The two lines below are equivalent
neighborhoods.sort_index(level=[1, 2]).head()
neighborhoods.sort_index(level=["City", "Street"]).head()

print(neighborhoods.sort_index(level=["City", "Street"]).head())
# Category                                   Culture         Services
# Subcategory                            Restaurants Museums   Police Schools
# State City        Street
# AR    Allisonland 124 Diaz Brooks               C-      A+        F      C+
# IA    Amyburgh    163 Heather Neck               F       D       A+      A-
# GA    Amyburgh    941 Brian Expressway           B       B       D-      C+
# ID    Andrewshire 952 Ellis Drive               C+      A-       C+       A
# VT    Baileyfort  831 Norma Cove                 B      D+       A+      D+

print(neighborhoods.sort_index(level=["City", "Street"], ascending=[True, False]).head())
# Category                                   Culture         Services
# Subcategory                            Restaurants Museums   Police Schools
# State City        Street
# AR    Allisonland 124 Diaz Brooks               C-      A+        F      C+
# GA    Amyburgh    941 Brian Expressway           B       B       D-      C+
# IA    Amyburgh    163 Heather Neck               F       D       A+      A-
# ID    Andrewshire 952 Ellis Drive               C+      A-       C+       A
# UT    Baileyfort  919 Stewart Hills             D+      C+        A       C

# The two lines below are equivalent
neighborhoods.sort_index(axis=1).head(3)
neighborhoods.sort_index(axis="columns").head(3)
print(neighborhoods.sort_index(axis="columns").head(3))
# Category                                 Culture             Services
# Subcategory                              Museums Restaurants   Police Schools
# State City             Street
# MO    Fisherborough    244 Tracy View          F          C+       D-      A+
# SD    Port Curtisville 446 Cynthia Inlet       B          C-        B      D+
# WV    Jimenezview      432 John Common        A+           A        F       B

print(neighborhoods.sort_index(axis=1, level="Subcategory", ascending=False).head(3))
# Category                                 Services     Culture Services Culture
# Subcategory                               Schools Restaurants   Police Museums
# State City             Street
# MO    Fisherborough    244 Tracy View          A+          C+       D-       F
# SD    Port Curtisville 446 Cynthia Inlet       D+          C-        B       B
# WV    Jimenezview      432 John Common          B           A        F      A+

neighborhoods = neighborhoods.sort_index(ascending=True)
print(neighborhoods)
# Category                                      Culture         Services
# Subcategory                               Restaurants Museums   Police Schools
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove              C-      A-       A+       C
#       Scottstad      082 Leblanc Freeway            D      C-        D      B+
#                      114 Jones Garden              D-      D-        D       D
#       Stevenshire    238 Andrew Rue                D-       A       A-      A-
# AL    Clarkland      430 Douglas Mission            A       F       C+      B+
# ...                                               ...     ...      ...     ...
# WY    Lake Nicole    754 Weaver Turnpike            B      D-        B       D
#                      933 Jennifer Burg              C      A+       A-       C
#       Martintown     013 Bell Mills                C-       D       A-      B-
#       Port Jason     624 Faulkner Orchard          A-       F       C+      C+
#       Reneeshire     717 Patel Square               B      B+        D       A
#
# [251 rows x 4 columns]
