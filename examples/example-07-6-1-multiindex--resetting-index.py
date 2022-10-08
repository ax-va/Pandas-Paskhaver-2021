"""
-- Applied pandas
---- MultiIndex DataFrames
------ Manipulating the index
-------- Resetting the index
"""
import pandas as pd

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv", index_col=[0, 1, 2], header=[0, 1])
neighborhoods.columns.names = ["Category", "Subcategory"]
neighborhoods = neighborhoods.sort_index(ascending=True)

print(neighborhoods.head())
# Category                                     Culture         Services
# Subcategory                              Restaurants Museums   Police Schools
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove             C-      A-       A+       C
#       Scottstad      082 Leblanc Freeway           D      C-        D      B+
#                      114 Jones Garden             D-      D-        D       D
#       Stevenshire    238 Andrew Rue               D-       A       A-      A-
# AL    Clarkland      430 Douglas Mission           A       F       C+      B+

new_order = ["City", "State", "Street"]
print(neighborhoods.reorder_levels(order=new_order).head())
# Category                                     Culture         Services
# Subcategory                              Restaurants Museums   Police Schools
# City           State Street
# Rowlandchester AK    386 Rebecca Cove             C-      A-       A+       C
# Scottstad      AK    082 Leblanc Freeway           D      C-        D      B+
#                      114 Jones Garden             D-      D-        D       D
# Stevenshire    AK    238 Andrew Rue               D-       A       A-      A-
# Clarkland      AL    430 Douglas Mission           A       F       C+      B+

print(neighborhoods.reorder_levels(order=[1, 0, 2]).head())
# Category                                     Culture         Services
# Subcategory                              Restaurants Museums   Police Schools
# City           State Street
# Rowlandchester AK    386 Rebecca Cove             C-      A-       A+       C
# Scottstad      AK    082 Leblanc Freeway           D      C-        D      B+
#                      114 Jones Garden             D-      D-        D       D
# Stevenshire    AK    238 Andrew Rue               D-       A       A-      A-
# Clarkland      AL    430 Douglas Mission           A       F       C+      B+

print(neighborhoods.reset_index().tail())
# Category    State         City                Street  ... Culture Services
# Subcategory                                           ... Museums   Police Schools
# 246            WY  Lake Nicole   754 Weaver Turnpike  ...      D-        B       D
# 247            WY  Lake Nicole     933 Jennifer Burg  ...      A+       A-       C
# 248            WY   Martintown        013 Bell Mills  ...       D       A-      B-
# 249            WY   Port Jason  624 Faulkner Orchard  ...       F       C+      C+
# 250            WY   Reneeshire      717 Patel Square  ...      B+        D       A
#
# [5 rows x 7 columns]

# The two lines below are equivalent
neighborhoods.reset_index(col_level=1).tail()
neighborhoods.reset_index(col_level="Subcategory").tail()
print(neighborhoods.reset_index(col_level="Subcategory").tail())
# Category                                              ... Culture Services
# Subcategory State         City                Street  ... Museums   Police Schools
# 246            WY  Lake Nicole   754 Weaver Turnpike  ...      D-        B       D
# 247            WY  Lake Nicole     933 Jennifer Burg  ...      A+       A-       C
# 248            WY   Martintown        013 Bell Mills  ...       D       A-      B-
# 249            WY   Port Jason  624 Faulkner Orchard  ...       F       C+      C+
# 250            WY   Reneeshire      717 Patel Square  ...      B+        D       A
#
# [5 rows x 7 columns]

# Group the three new columns under an Address parent level
print(neighborhoods.reset_index(col_fill="Address", col_level="Subcategory").tail())
# Category    Address                                     ... Culture Services
# Subcategory   State         City                Street  ... Museums   Police Schools
# 246              WY  Lake Nicole   754 Weaver Turnpike  ...      D-        B       D
# 247              WY  Lake Nicole     933 Jennifer Burg  ...      A+       A-       C
# 248              WY   Martintown        013 Bell Mills  ...       D       A-      B-
# 249              WY   Port Jason  624 Faulkner Orchard  ...       F       C+      C+
# 250              WY   Reneeshire      717 Patel Square  ...      B+        D       A
#
# [5 rows x 7 columns]

print(neighborhoods.reset_index(level="Street").tail())
# Category                         Street     Culture         Services
# Subcategory                             Restaurants Museums   Police Schools
# State City
# WY    Lake Nicole   754 Weaver Turnpike           B      D-        B       D
#       Lake Nicole     933 Jennifer Burg           C      A+       A-       C
#       Martintown         013 Bell Mills          C-       D       A-      B-
#       Port Jason   624 Faulkner Orchard          A-       F       C+      C+
#       Reneeshire       717 Patel Square           B      B+        D       A

print(neighborhoods.reset_index(level=["Street", "City"]).tail())
# Category            City                Street  ... Services
# Subcategory                                     ...   Police Schools
# State                                           ...
# WY           Lake Nicole   754 Weaver Turnpike  ...        B       D
# WY           Lake Nicole     933 Jennifer Burg  ...       A-       C
# WY            Martintown        013 Bell Mills  ...       A-      B-
# WY            Port Jason  624 Faulkner Orchard  ...       C+      C+
# WY            Reneeshire      717 Patel Square  ...        D       A
#
# [5 rows x 6 columns]

print(neighborhoods.reset_index(level="Street", drop=True).tail())
# Category              Culture         Services
# Subcategory       Restaurants Museums   Police Schools
# State City
# WY    Lake Nicole           B      D-        B       D
#       Lake Nicole           C      A+       A-       C
#       Martintown           C-       D       A-      B-
#       Port Jason           A-       F       C+      C+
#       Reneeshire            B      B+        D       A

neighborhoods = neighborhoods.reset_index()
print(neighborhoods)
# Category    State            City  ... Services
# Subcategory                        ...   Police Schools
# 0              AK  Rowlandchester  ...       A+       C
# 1              AK       Scottstad  ...        D      B+
# 2              AK       Scottstad  ...        D       D
# 3              AK     Stevenshire  ...       A-      A-
# 4              AL       Clarkland  ...       C+      B+
# ..            ...             ...  ...      ...     ...
# 246            WY     Lake Nicole  ...        B       D
# 247            WY     Lake Nicole  ...       A-       C
# 248            WY      Martintown  ...       A-      B-
# 249            WY      Port Jason  ...       C+      C+
# 250            WY      Reneeshire  ...        D       A
#
# [251 rows x 7 columns]
