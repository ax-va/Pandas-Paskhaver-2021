#!/usr/bin/python3
"""
-- Applied pandas
---- Working with text data
------ Coding challenge
"""
import pandas as pd
customers = pd.read_csv("../datasets/customers.csv")
customers[["First Name", "Last Name"]] = customers["Name"].str.split(pat=" ", n=1, expand=True)
customers = customers.drop(labels="Name", axis="columns")

print(customers["Address"].str.split(",").head())
# 0    [6461 Quinn Groves,  East Matthew,  New Hampsh...
# 1    [1360 Tracey Ports Apt. 419,  Kyleport,  Vermo...
# 2    [19120 Fleming Manors,  Prestonstad,  Montana,...
# 3    [441 Olivia Creek,  Jimmymouth,  Georgia,  82991]
# 4    [4246 Chelsey Ford Apt. 310,  Karamouth,  Utah...
# Name: Address, dtype: object

print(customers["Address"].str.split(", ").head())
# 0    [6461 Quinn Groves, East Matthew, New Hampshir...
# 1    [1360 Tracey Ports Apt. 419, Kyleport, Vermont...
# 2    [19120 Fleming Manors, Prestonstad, Montana, 2...
# 3       [441 Olivia Creek, Jimmymouth, Georgia, 82991]
# 4    [4246 Chelsey Ford Apt. 310, Karamouth, Utah, ...
# Name: Address, dtype: object

print(customers["Address"].str.split(", ", expand=True).head())
#                             0             1              2      3
# 0           6461 Quinn Groves  East Matthew  New Hampshire  16656
# 1  1360 Tracey Ports Apt. 419      Kyleport        Vermont  31924
# 2        19120 Fleming Manors   Prestonstad        Montana  23495
# 3            441 Olivia Creek    Jimmymouth        Georgia  82991
# 4  4246 Chelsey Ford Apt. 310     Karamouth           Utah  76252

new_cols = ["Street", "City", "State", "Zip"]
customers[new_cols] = customers["Address"].str.split(pat=", ", expand=True)

print(customers.drop(labels="Address", axis="columns").head())
#   First Name    Last Name  ...          State    Zip
# 0      Frank      Manning  ...  New Hampshire  16656
# 1  Elizabeth      Johnson  ...        Vermont  31924
# 2     Donald     Stephens  ...        Montana  23495
# 3    Michael  Vincent III  ...        Georgia  82991
# 4    Jasmine       Zamora  ...           Utah  76252
#
# [5 rows x 6 columns]

del customers["Address"]
print(customers.tail())
#      First Name  Last Name  ...          State    Zip
# 9956       Dana   Browning  ...     New Mexico  28889
# 9957     Amanda   Anderson  ...          Maine  37378
# 9958       Eric      Davis  ...  West Virginia  03933
# 9959     Taylor  Hernandez  ...       Oklahoma  98916
# 9960     Sherry  Nicholson  ...     New Mexico  17581
#
# [5 rows x 6 columns]
