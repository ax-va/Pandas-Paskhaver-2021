#!/usr/bin/python3
"""
-- Applied pandas
---- Working with text data
------ Splitting strings
"""
import pandas as pd
customers = pd.read_csv("../datasets/customers.csv")
print(customers)
#                      Name                                            Address
# 0           Frank Manning  6461 Quinn Groves, East Matthew, New Hampshire...
# 1       Elizabeth Johnson  1360 Tracey Ports Apt. 419, Kyleport, Vermont,...
# 2         Donald Stephens  19120 Fleming Manors, Prestonstad, Montana, 23495
# 3     Michael Vincent III       441 Olivia Creek, Jimmymouth, Georgia, 82991
# 4          Jasmine Zamora  4246 Chelsey Ford Apt. 310, Karamouth, Utah, 7...
# ...                   ...                                                ...
# 9956        Dana Browning  762 Andrew Views Apt. 254, North Paul, New Mex...
# 9957      Amanda Anderson  44188 Day Crest Apt. 901, Lake Marcia, Maine, ...
# 9958           Eric Davis  73015 Michelle Squares, Watsonville, West Virg...
# 9959     Taylor Hernandez       129 Keith Greens, Haleyfurt, Oklahoma, 98916
# 9960     Sherry Nicholson   355 Griffin Valley, Davidtown, New Mexico, 17581
#
# [9961 rows x 2 columns]

print(customers["Name"].str.len().head())
# 0    13
# 1    17
# 2    15
# 3    19
# 4    14
# Name: Name, dtype: int64

# The two lines below are equivalent
customers["Name"].str.split(pat=" ").head()
customers["Name"].str.split(" ").head()
print(customers["Name"].str.split(" ").head())
# 0           [Frank, Manning]
# 1       [Elizabeth, Johnson]
# 2         [Donald, Stephens]
# 3    [Michael, Vincent, III]
# 4          [Jasmine, Zamora]
# Name: Name, dtype: object

print(customers["Name"].str.split(" ").str.len().head())
# 0    2
# 1    2
# 2    2
# 3    3
# 4    2
# Name: Name, dtype: int64

print(customers["Name"].str.split(pat=" ", n=1).head())
# 0          [Frank, Manning]
# 1      [Elizabeth, Johnson]
# 2        [Donald, Stephens]
# 3    [Michael, Vincent III]
# 4         [Jasmine, Zamora]
# Name: Name, dtype: object

print(customers["Name"].str.split(pat=" ", n=1).str.get(0).head())
# 0        Frank
# 1    Elizabeth
# 2       Donald
# 3      Michael
# 4      Jasmine
# Name: Name, dtype: object

print(customers["Name"].str.split(pat=" ", n=1).str.slice(0, 1).head())
# 0        [Frank]
# 1    [Elizabeth]
# 2       [Donald]
# 3      [Michael]
# 4      [Jasmine]
# Name: Name, dtype: object

print(customers["Name"].str.split(pat=" ", n=1).str[0:1].head())
# 0        [Frank]
# 1    [Elizabeth]
# 2       [Donald]
# 3      [Michael]
# 4      [Jasmine]
# Name: Name, dtype: object

print(customers["Name"].str.split(pat=" ", n=1).str.get(1).head())
# 0        Manning
# 1        Johnson
# 2       Stephens
# 3    Vincent III
# 4         Zamora
# Name: Name, dtype: object

print(customers["Name"].str.split(pat=" ", n=1).str.get(-1).head())
# 0        Manning
# 1        Johnson
# 2       Stephens
# 3    Vincent III
# 4         Zamora
# Name: Name, dtype: object

print(customers["Name"].str.split(pat=" ", n=1, expand=True).head())
#            0            1
# 0      Frank      Manning
# 1  Elizabeth      Johnson
# 2     Donald     Stephens
# 3    Michael  Vincent III
# 4    Jasmine       Zamora

print(customers["Name"].str.split(pat=" ", expand=True).head())
#            0         1     2
# 0      Frank   Manning  None
# 1  Elizabeth   Johnson  None
# 2     Donald  Stephens  None
# 3    Michael   Vincent   III
# 4    Jasmine    Zamora  None

customers[["First Name", "Last Name"]] = customers["Name"].str.split(pat=" ", n=1, expand=True)
print(customers.head())
#                   Name  ...    Last Name
# 0        Frank Manning  ...      Manning
# 1    Elizabeth Johnson  ...      Johnson
# 2      Donald Stephens  ...     Stephens
# 3  Michael Vincent III  ...  Vincent III
# 4       Jasmine Zamora  ...       Zamora
#
# [5 rows x 4 columns]

customers = customers.drop(labels="Name", axis="columns")
print(customers.head())
#                                              Address First Name    Last Name
# 0  6461 Quinn Groves, East Matthew, New Hampshire...      Frank      Manning
# 1  1360 Tracey Ports Apt. 419, Kyleport, Vermont,...  Elizabeth      Johnson
# 2  19120 Fleming Manors, Prestonstad, Montana, 23495     Donald     Stephens
# 3       441 Olivia Creek, Jimmymouth, Georgia, 82991    Michael  Vincent III
# 4  4246 Chelsey Ford Apt. 310, Karamouth, Utah, 7...    Jasmine       Zamora
