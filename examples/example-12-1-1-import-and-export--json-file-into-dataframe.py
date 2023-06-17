#!/usr/bin/python3
"""
-- Applied pandas
---- Imports and exports
------ Reading from and writing to JSON files
-------- Loading a JSON file into a DataFrame
"""

import pandas as pd

nobel = pd.read_json("../datasets/nobel.json")
print(nobel)
#                                                 prizes
# 0    {'year': '2019', 'category': 'chemistry', 'lau...
# 1    {'year': '2019', 'category': 'economics', 'lau...
# 2    {'year': '2019', 'category': 'literature', 'la...
# 3    {'year': '2019', 'category': 'peace', 'laureat...
# 4    {'year': '2019', 'category': 'physics', 'overa...
# ..                                                 ...
# 641  {'year': '1901', 'category': 'chemistry', 'lau...
# 642  {'year': '1901', 'category': 'literature', 'la...
# 643  {'year': '1901', 'category': 'peace', 'laureat...
# 644  {'year': '1901', 'category': 'physics', 'laure...
# 645  {'year': '1901', 'category': 'medicine', 'laur...
#
# [646 rows x 1 columns]

nobel.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 646 entries, 0 to 645
# Data columns (total 1 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   prizes  646 non-null    object
# dtypes: object(1)
# memory usage: 5.2+ KB

print(nobel.loc[2, "prizes"])
# {
#     'year': '2019',
#     'category': 'literature',
#     'laureates': [
#         {
#             'id': '980',
#             'firstname': 'Peter',
#             'surname': 'Handke',
#             'motivation': '"for an influential work that with linguistic ingenuity has explored the periphery and the specificity of human experience"',
#             'share': '1'
#         }
#     ]
# }

print(type(nobel.loc[2, "prizes"]))  # <class 'dict'>

# Moving nested records of data into a single, one-dimensional list is called flattening or normalizing

chemistry_2019 = nobel.loc[0, "prizes"]
print(chemistry_2019)
# {
#     'year': '2019',
#     'category': 'chemistry',
#     'laureates': [
#         {
#             'id': '976',
#             'firstname': 'John',
#             'surname': 'Goodenough',
#             'motivation': '"for the development of lithium-ion batteries"',
#             'share': '3'
#         },
#         {
#             'id': '977',
#             'firstname': 'M. Stanley',
#             'surname': 'Whittingham',
#             'motivation': '"for the development of lithium-ion batteries"',
#             'share': '3'
#         },
#         {
#             'id': '978',
#             'firstname': 'Akira',
#             'surname': 'Yoshino',
#             'motivation': '"for the development of lithium-ion batteries"',
#             'share': '3'
#         }
#     ]
# }

print(pd.json_normalize(data=chemistry_2019))
#    year   category                                          laureates
# 0  2019  chemistry  [{'id': '976', 'firstname': 'John', 'surname':...

print(pd.json_normalize(data=chemistry_2019, record_path="laureates"))
#     id   firstname  ...                                      motivation share
# 0  976        John  ...  "for the development of lithium-ion batteries"     3
# 1  977  M. Stanley  ...  "for the development of lithium-ion batteries"     3
# 2  978       Akira  ...  "for the development of lithium-ion batteries"     3
#
# [3 rows x 5 columns]

print(pd.json_normalize(data=chemistry_2019, record_path="laureates", meta=["year", "category"]))
#     id   firstname      surname  ... share  year   category
# 0  976        John   Goodenough  ...     3  2019  chemistry
# 1  977  M. Stanley  Whittingham  ...     3  2019  chemistry
# 2  978       Akira      Yoshino  ...     3  2019  chemistry
#
# [3 rows x 7 columns]

# print(pd.json_normalize(data=nobel["prizes"], record_path="laureates", meta=["year", "category"]))
# # KeyError: "Key 'laureates' not found. If specifying a record_path, all elements of data should have the path."

# Some dictionaries in the prizes Series do not have a "laureates" key.

cheese_consumption = {"France": 57.9, "Germany": 53.2, "Luxembourg": 53.2}
cheese_consumption.setdefault("France", 0)
print(cheese_consumption)
# {'France': 57.9, 'Germany': 53.2, 'Luxembourg': 53.2}
cheese_consumption.setdefault("Italy", 48)
print(cheese_consumption)
# {'France': 57.9, 'Germany': 53.2, 'Luxembourg': 53.2, 'Italy': 48}

# Change the Series entries adding the new key-value pair if needed
nobel["prizes"].apply(lambda dict_entry: dict_entry.setdefault("laureates", []))

winners = pd.json_normalize(data=nobel["prizes"], record_path="laureates", meta=["year", "category"])
print(winners)
#       id       firstname      surname  ... share  year    category
# 0    976            John   Goodenough  ...     3  2019   chemistry
# 1    977      M. Stanley  Whittingham  ...     3  2019   chemistry
# 2    978           Akira      Yoshino  ...     3  2019   chemistry
# 3    982         Abhijit     Banerjee  ...     3  2019   economics
# 4    983          Esther        Duflo  ...     3  2019   economics
# ..   ...             ...          ...  ...   ...   ...         ...
# 945  569           Sully    Prudhomme  ...     1  1901  literature
# 946  462           Henry       Dunant  ...     2  1901       peace
# 947  463        Frédéric        Passy  ...     2  1901       peace
# 948    1  Wilhelm Conrad      Röntgen  ...     1  1901     physics
# 949  293            Emil  von Behring  ...     1  1901    medicine
#
# [950 rows x 7 columns]
