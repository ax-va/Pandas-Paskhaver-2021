"""
-- Applied pandas
---- MultiIndex DataFrames
------ Selecting with a MultiIndex
-------- Extracting one or more columns
"""
import pandas as pd

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv", index_col=[0, 1, 2], header=[0, 1])
neighborhoods.columns.names = ["Category", "Subcategory"]
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

print(neighborhoods["Services"])
# Subcategory                               Police Schools
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove         A+       C
#       Scottstad      082 Leblanc Freeway       D      B+
#                      114 Jones Garden          D       D
#       Stevenshire    238 Andrew Rue           A-      A-
# AL    Clarkland      430 Douglas Mission      C+      B+
# ...                                          ...     ...
# WY    Lake Nicole    754 Weaver Turnpike       B       D
#                      933 Jennifer Burg        A-       C
#       Martintown     013 Bell Mills           A-      B-
#       Port Jason     624 Faulkner Orchard     C+      C+
#       Reneeshire     717 Patel Square          D       A
#
# [251 rows x 2 columns]

# Searching for the index can be only in the outermost multiindex level if only one index is given in [].
# "Schools" is not the outermost one.
# neighborhoods["Schools"]  # KeyError: 'Schools'

print(neighborhoods[("Services", "Schools")])
# State  City            Street
# AK     Rowlandchester  386 Rebecca Cove         C
#        Scottstad       082 Leblanc Freeway     B+
#                        114 Jones Garden         D
#        Stevenshire     238 Andrew Rue          A-
# AL     Clarkland       430 Douglas Mission     B+
#                                                ..
# WY     Lake Nicole     754 Weaver Turnpike      D
#                        933 Jennifer Burg        C
#        Martintown      013 Bell Mills          B-
#        Port Jason      624 Faulkner Orchard    C+
#        Reneeshire      717 Patel Square         A
# Name: (Services, Schools), Length: 251, dtype: object

print(type(neighborhoods[("Services", "Schools")]))  # <class 'pandas.core.series.Series'>

print(neighborhoods[[("Services", "Schools"), ("Culture", "Museums")]])
# Category                                  Services Culture
# Subcategory                                Schools Museums
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove            C      A-
#       Scottstad      082 Leblanc Freeway        B+      C-
#                      114 Jones Garden            D      D-
#       Stevenshire    238 Andrew Rue             A-       A
# AL    Clarkland      430 Douglas Mission        B+       F
# ...                                            ...     ...
# WY    Lake Nicole    754 Weaver Turnpike         D      D-
#                      933 Jennifer Burg           C      A+
#       Martintown     013 Bell Mills             B-       D
#       Port Jason     624 Faulkner Orchard       C+       F
#       Reneeshire     717 Patel Square            A      B+
#
# [251 rows x 2 columns]

columns = [
    ("Services", "Schools"),
    ("Culture", "Museums"),
]

print(neighborhoods[columns])
# Category                                  Services Culture
# Subcategory                                Schools Museums
# State City           Street
# AK    Rowlandchester 386 Rebecca Cove            C      A-
#       Scottstad      082 Leblanc Freeway        B+      C-
#                      114 Jones Garden            D      D-
#       Stevenshire    238 Andrew Rue             A-       A
# AL    Clarkland      430 Douglas Mission        B+       F
# ...                                            ...     ...
# WY    Lake Nicole    754 Weaver Turnpike         D      D-
#                      933 Jennifer Burg           C      A+
#       Martintown     013 Bell Mills             B-       D
#       Port Jason     624 Faulkner Orchard       C+       F
#       Reneeshire     717 Patel Square            A      B+
#
# [251 rows x 2 columns]

