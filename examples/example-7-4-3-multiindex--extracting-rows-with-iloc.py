"""
-- Applied pandas
---- MultiIndex DataFrames
------ Selecting with a MultiIndex
-------- Extracting One or More Rows with iloc
"""
import pandas as pd

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv", index_col=[0, 1, 2], header=[0, 1])
neighborhoods.columns.names = ["Category", "Subcategory"]
neighborhoods = neighborhoods.sort_index(ascending=True)

print(neighborhoods.iloc[0])
# Category  Subcategory
# Culture   Restaurants    C-
#           Museums        A-
# Services  Police         A+
#           Schools         C
# Name: (AK, Rowlandchester, 386 Rebecca Cove), dtype: object

print(neighborhoods.iloc[0, 0])
# Name: (CT, East Jessicaland, 208 Todd Knolls), dtype: object
# C-

print(neighborhoods.iloc[0, 1])
# A-

print(neighborhoods.iloc[1])
# Category  Subcategory
# Culture   Restaurants     D
#           Museums        C-
# Services  Police          D
#           Schools        B+
# Name: (AK, Scottstad, 082 Leblanc Freeway), dtype: object

# Pull out multiple rows the State indices of 0 and 1
print(neighborhoods.iloc[[0, 1]])
# Category                                     Culture         Services
# Subcategory                              Restaurants Museums   Police Schools
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove             C-      A-       A+       C
#       Scottstad      082 Leblanc Freeway           D      C-        D      B+

# When slicing the endpoint is exclusive
print(neighborhoods.iloc[0:2])
# Category                                     Culture         Services
# Subcategory                              Restaurants Museums   Police Schools
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove             C-      A-       A+       C
#       Scottstad      082 Leblanc Freeway           D      C-        D      B+

print(neighborhoods.iloc[0:2, 1:3])
# Category                                 Culture Services
# Subcategory                              Museums   Police
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove         A-       A+
#       Scottstad      082 Leblanc Freeway      C-        D

print(neighborhoods.iloc[-1:])
# Category                              Culture         Services
# Subcategory                       Restaurants Museums   Police Schools
# State City       Street
# WY    Reneeshire 717 Patel Square           B      B+        D       A

print(neighborhoods.iloc[-4:])
# Category                                   Culture         Services
# Subcategory                            Restaurants Museums   Police Schools
# State City        Street
# WY    Lake Nicole 933 Jennifer Burg              C      A+       A-       C
#       Martintown  013 Bell Mills                C-       D       A-      B-
#       Port Jason  624 Faulkner Orchard          A-       F       C+      C+
#       Reneeshire  717 Patel Square               B      B+        D       A

print(neighborhoods.iloc[-4:, -2:])
# Category                               Services
# Subcategory                              Police Schools
# State City        Street
# WY    Lake Nicole 933 Jennifer Burg          A-       C
#       Martintown  013 Bell Mills             A-      B-
#       Port Jason  624 Faulkner Orchard       C+      C+
#       Reneeshire  717 Patel Square            D       A

# Using the multiindex with iloc is not possible
