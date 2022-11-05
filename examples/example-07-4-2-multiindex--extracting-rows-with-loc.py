#!/usr/bin/python3
"""
-- Applied pandas
---- MultiIndex DataFrames
------ Selecting with a MultiIndex
-------- Extracting one or more rows with loc
"""
import pandas as pd

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv", index_col=[0, 1, 2], header=[0, 1])
neighborhoods.columns.names = ["Category", "Subcategory"]
neighborhoods = neighborhoods.sort_index(ascending=True)

print(neighborhoods.loc[("TX", "Kingchester", "534 Gordon Falls")])
# Category  Subcategory
# Culture   Restaurants     C
#           Museums        D+
# Services  Police          B
#           Schools         B
# Name: (TX, Kingchester, 534 Gordon Falls), dtype: object

print(type(neighborhoods.loc[("TX", "Kingchester", "534 Gordon Falls")]))  # <class 'pandas.core.series.Series'>

# Looking for it only in the outermost multiindex level
print(neighborhoods.loc["CA"])
# Category                              Culture         Services
# Subcategory                       Restaurants Museums   Police Schools
# City           Street
# Dustinmouth    793 Cynthia Square          A-      A+       C-       A
# North Jennifer 303 Alisha Road             D-      C+       C+      A+
# Ryanfort       934 David Run                F      B+        F      D-

print(type(neighborhoods.loc["CA"]))  # <class 'pandas.core.frame.DataFrame'>

# Not recommended:
print(neighborhoods.loc["CA", "Dustinmouth"])
# Category               Culture         Services
# Subcategory        Restaurants Museums   Police Schools
# Street
# 793 Cynthia Square          A-      A+       C-       A

# Not recommended:
print(neighborhoods.loc["CA", "Culture"])
# Subcategory                       Restaurants Museums
# City           Street
# Dustinmouth    793 Cynthia Square          A-      A+
# North Jennifer 303 Alisha Road             D-      C+
# Ryanfort       934 David Run                F      B+

# Recommended:
print(neighborhoods.loc[("CA", "Dustinmouth")])
# Category               Culture         Services
# Subcategory        Restaurants Museums   Police Schools
# Street
# 793 Cynthia Square          A-      A+       C-       A

# Recommended:
print(neighborhoods.loc[("CA", "Dustinmouth"), ("Culture",)])
# Subcategory        Restaurants Museums
# Street
# 793 Cynthia Square          A-      A+

print(neighborhoods.loc[("CA", "Dustinmouth"), ("Services", "Schools")])
# Street
# 793 Cynthia Square    A
# Name: (Services, Schools), dtype: object

# In pandas slicing, the endpoint (the value after the colon) is inclusive
print(neighborhoods["NE":"NH"])
# Category                                          Culture  ... Services
# Subcategory                                   Restaurants  ...  Schools
# State City               Street                            ...
# NE    Barryborough       460 Anna Tunnel               A+  ...        A
#       Shawnchester       802 Cook Cliff                D-  ...        A
#       South Kennethmouth 346 Wallace Pass              C-  ...       A-
#       South Nathan       821 Jake Fork                 C+  ...        A
# NH    Courtneyfort       697 Spencer Isle              A+  ...       A+
#       East Deborahberg   271 Ryan Mount                 B  ...       B-
#       Ingramton          430 Calvin Underpass          C+  ...       C-
#       North Latoya       603 Clark Mount               D-  ...       B-
#       South Tara         559 Michael Glens             C-  ...        B
#
# [9 rows x 4 columns]

print(neighborhoods.loc[("NE", "Shawnchester"):("NH", "North Latoya")])
# NE    Shawnchester       802 Cook Cliff                D-  ...        A
#       South Kennethmouth 346 Wallace Pass              C-  ...       A-
#       South Nathan       821 Jake Fork                 C+  ...        A
# NH    Courtneyfort       697 Spencer Isle              A+  ...       A+
#       East Deborahberg   271 Ryan Mount                 B  ...       B-
#       Ingramton          430 Calvin Underpass          C+  ...       C-
#       North Latoya       603 Clark Mount               D-  ...       B-
#
# [7 rows x 4 columns]

start = ("NE", "Shawnchester")
end = ("NH", "North Latoya")
print(neighborhoods.loc[start:end])
# Category                                          Culture  ... Services
# Subcategory                                   Restaurants  ...  Schools
# State City               Street                            ...
# NE    Shawnchester       802 Cook Cliff                D-  ...        A
#       South Kennethmouth 346 Wallace Pass              C-  ...       A-
#       South Nathan       821 Jake Fork                 C+  ...        A
# NH    Courtneyfort       697 Spencer Isle              A+  ...       A+
#       East Deborahberg   271 Ryan Mount                 B  ...       B-
#       Ingramton          430 Calvin Underpass          C+  ...       C-
#       North Latoya       603 Clark Mount               D-  ...       B-
#
# [7 rows x 4 columns]

print(neighborhoods.loc[("NE", "Shawnchester"):("NH", )])
# Category                                          Culture  ... Services
# Subcategory                                   Restaurants  ...  Schools
# State City               Street                            ...
# NE    Shawnchester       802 Cook Cliff                D-  ...        A
#       South Kennethmouth 346 Wallace Pass              C-  ...       A-
#       South Nathan       821 Jake Fork                 C+  ...        A
# NH    Courtneyfort       697 Spencer Isle              A+  ...       A+
#       East Deborahberg   271 Ryan Mount                 B  ...       B-
#       Ingramton          430 Calvin Underpass          C+  ...       C-
#       North Latoya       603 Clark Mount               D-  ...       B-
#       South Tara         559 Michael Glens             C-  ...        B
#
# [8 rows x 4 columns]

# Use a list to store multiple keys.
# Use a tuple to store the components of one multilevel key.
# But it does not work with multiple multilevel keys.
print(neighborhoods.loc[["NE", "NH"]])
# Category                                          Culture  ... Services
# Subcategory                                   Restaurants  ...  Schools
# State City               Street                            ...
# NE    Barryborough       460 Anna Tunnel               A+  ...        A
#       Shawnchester       802 Cook Cliff                D-  ...        A
#       South Kennethmouth 346 Wallace Pass              C-  ...       A-
#       South Nathan       821 Jake Fork                 C+  ...        A
# NH    Courtneyfort       697 Spencer Isle              A+  ...       A+
#       East Deborahberg   271 Ryan Mount                 B  ...       B-
#       Ingramton          430 Calvin Underpass          C+  ...       C-
#       North Latoya       603 Clark Mount               D-  ...       B-
#       South Tara         559 Michael Glens             C-  ...        B
#
# [9 rows x 4 columns]

# Does not work with multiple multilevel keys
# print(neighborhoods.loc[[("NE", "Barryborough"), ("NH", "Courtneyfort")]])
# # ValueError: operands could not be broadcast together with shapes (2,2) (3,) (2,2)

# Does not work with multiple multilevel keys
# print(neighborhoods.loc[[("NE", "Barryborough, 460 Anna Tunnel"), ("NH", "Courtneyfort", "697 Spencer Isle")]])
# # ValueError: operands could not be broadcast together with shapes (2,2) (3,) (2,2)


