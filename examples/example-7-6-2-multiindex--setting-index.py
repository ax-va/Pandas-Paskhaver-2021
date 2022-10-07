"""
-- Applied pandas
---- MultiIndex DataFrames
------ Manipulating the Index
-------- Setting the Index
"""
import pandas as pd

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv", index_col=[0, 1, 2], header=[0, 1])
neighborhoods.columns.names = ["Category", "Subcategory"]
neighborhoods = neighborhoods.sort_index(ascending=True)
neighborhoods = neighborhoods.reset_index()

print(neighborhoods.head(3))
# Category    State            City               Street  ... Culture Services
# Subcategory                                             ... Museums   Police Schools
# 0              AK  Rowlandchester     386 Rebecca Cove  ...      A-       A+       C
# 1              AK       Scottstad  082 Leblanc Freeway  ...      C-        D      B+
# 2              AK       Scottstad     114 Jones Garden  ...      D-        D       D
#
# [3 rows x 7 columns]

print(neighborhoods.set_index(keys="City").head())
# Category       State               Street     Culture         Services
# Subcategory                               Restaurants Museums   Police Schools
# City
# Rowlandchester    AK     386 Rebecca Cove          C-      A-       A+       C
# Scottstad         AK  082 Leblanc Freeway           D      C-        D      B+
# Scottstad         AK     114 Jones Garden          D-      D-        D       D
# Stevenshire       AK       238 Andrew Rue          D-       A       A-      A-
# Clarkland         AL  430 Douglas Mission           A       F       C+      B+

# Set an index from a MultiIndex (using a MultiIndex level) with a tuple
print(neighborhoods.set_index(keys=("Culture", "Museums")).head())
# Category           State            City  ... Services
# Subcategory                               ...   Police Schools
# (Culture, Museums)                        ...
# A-                    AK  Rowlandchester  ...       A+       C
# C-                    AK       Scottstad  ...        D      B+
# D-                    AK       Scottstad  ...        D       D
# A                     AK     Stevenshire  ...       A-      A-
# F                     AL       Clarkland  ...       C+      B+
#
# [5 rows x 6 columns]

# Set a MultiIndex with a list
print(neighborhoods.set_index(keys=["State", "City"]).head())
# Category                           Street     Culture         Services
# Subcategory                               Restaurants Museums   Police Schools
# State City
# AK    Rowlandchester     386 Rebecca Cove          C-      A-       A+       C
#       Scottstad       082 Leblanc Freeway           D      C-        D      B+
#       Scottstad          114 Jones Garden          D-      D-        D       D
#       Stevenshire          238 Andrew Rue          D-       A       A-      A-
# AL    Clarkland       430 Douglas Mission           A       F       C+      B+
