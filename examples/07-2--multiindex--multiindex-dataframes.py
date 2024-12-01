#!/usr/bin/python3
"""
-- Applied pandas
---- MultiIndex DataFrames
------ MultiIndex DataFrames
"""
import pandas as pd

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv")
# ,,,Culture,Culture,Services,Services
# ,,,Restaurants,Museums,Police,Schools
# State,City,Street,,,,
# MO,Fisherborough,244 Tracy View,C+,F,D-,A+
# SD,Port Curtisville,446 Cynthia Inlet,C-,B,B,D+
# WV,Jimenezview,432 John Common,A,A+,F,B
# AK,Stevenshire,238 Andrew Rue,D-,A,A-,A-

print(neighborhoods)
#     Unnamed: 0          Unnamed: 1  ... Services Services.1
# 0          NaN                 NaN  ...   Police    Schools
# 1        State                City  ...      NaN        NaN
# 2           MO       Fisherborough  ...       D-         A+
# 3           SD    Port Curtisville  ...        B         D+
# 4           WV         Jimenezview  ...        F          B
# ..         ...                 ...  ...      ...        ...
# 248         MI       North Matthew  ...        B         C+
# 249         MT             Chadton  ...       D+          D
# 250         SC           Diazmouth  ...       B-         D+
# 251         VA          Laurentown  ...        F         D-
# 252         NE  South Kennethmouth  ...        A         A-
#
# [253 rows x 7 columns]

print(neighborhoods.head())
#   Unnamed: 0        Unnamed: 1         Unnamed: 2  ... Culture.1 Services Services.1
# 0        NaN               NaN                NaN  ...   Museums   Police    Schools
# 1      State              City             Street  ...       NaN      NaN        NaN
# 2         MO     Fisherborough     244 Tracy View  ...         F       D-         A+
# 3         SD  Port Curtisville  446 Cynthia Inlet  ...         B        B         D+
# 4         WV       Jimenezview    432 John Common  ...        A+        F          B
#
# [5 rows x 7 columns]

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv", index_col=[0, 1, 2])
print(neighborhoods.head())
#                                               Culture  ... Services.1
# NaN   NaN              NaN                Restaurants  ...    Schools
# State City             Street                     NaN  ...        NaN
# MO    Fisherborough    244 Tracy View              C+  ...         A+
# SD    Port Curtisville 446 Cynthia Inlet           C-  ...         D+
# WV    Jimenezview      432 John Common              A  ...          B
#
# [5 rows x 4 columns]

neighborhoods = pd.read_csv("../datasets/neighborhoods.csv", index_col=[0, 1, 2], header=[0, 1])
print(neighborhoods.head())
#                                              Culture         Services
#                                          Restaurants Museums   Police Schools
# State City             Street
# MO    Fisherborough    244 Tracy View             C+       F       D-      A+
# SD    Port Curtisville 446 Cynthia Inlet          C-       B        B      D+
# WV    Jimenezview      432 John Common             A      A+        F       B
# AK    Stevenshire      238 Andrew Rue             D-       A       A-      A-
# ND    New Joshuaport   877 Walter Neck            D+      C-        B       B

neighborhoods.info()
# <class 'pandas.core.frame.DataFrame'>
# MultiIndex: 251 entries, ('MO', 'Fisherborough', '244 Tracy View') to ('NE', 'South Kennethmouth', '346 Wallace Pass')
# Data columns (total 4 columns):
#  #   Column                  Non-Null Count  Dtype
# ---  ------                  --------------  -----
#  0   (Culture, Restaurants)  251 non-null    object
#  1   (Culture, Museums)      251 non-null    object
#  2   (Services, Police)      251 non-null    object
#  3   (Services, Schools)     251 non-null    object
# dtypes: object(4)
# memory usage: 27.2+ KB

print(neighborhoods.index)
# MultiIndex([('MO',      'Fisherborough',        '244 Tracy View'),
#             ('SD',   'Port Curtisville',     '446 Cynthia Inlet'),
#             ('WV',        'Jimenezview',       '432 John Common'),
#             ('AK',        'Stevenshire',        '238 Andrew Rue'),
#             ('ND',     'New Joshuaport',       '877 Walter Neck'),
#             ('ID',         'Wellsville',   '696 Weber Stravenue'),
#             ('TN',          'Jodiburgh',    '285 Justin Corners'),
#             ('DC',   'Lake Christopher',   '607 Montoya Harbors'),
#             ('OH',          'Port Mike',      '041 Michael Neck'),
#             ('ND',         'Hardyburgh', '550 Gilmore Mountains'),
#             ...
#             ('AK',          'Scottstad',      '114 Jones Garden'),
#             ('IA',    'Port Willieport',  '320 Jennifer Mission'),
#             ('ME',         'Port Linda',        '692 Hill Glens'),
#             ('KS',         'Kaylamouth',       '483 Freeman Via'),
#             ('WA',     'Port Shawnfort',    '691 Winters Bridge'),
#             ('MI',      'North Matthew',      '055 Clayton Isle'),
#             ('MT',            'Chadton',     '601 Richards Road'),
#             ('SC',          'Diazmouth',     '385 Robin Harbors'),
#             ('VA',         'Laurentown',     '255 Gonzalez Land'),
#             ('NE', 'South Kennethmouth',      '346 Wallace Pass')],
#            names=['State', 'City', 'Street'], length=251)

print(neighborhoods.columns)
# MultiIndex([( 'Culture', 'Restaurants'),
#             ( 'Culture',     'Museums'),
#             ('Services',      'Police'),
#             ('Services',     'Schools')],
#            )

print(neighborhoods.index.names)  # ['State', 'City', 'Street']

# The two lines below are equivalent
neighborhoods.index.get_level_values(1)
neighborhoods.index.get_level_values("City")
print(neighborhoods.index.get_level_values(1))
# Index(['Fisherborough', 'Port Curtisville', 'Jimenezview', 'Stevenshire',
#        'New Joshuaport', 'Wellsville', 'Jodiburgh', 'Lake Christopher',
#        'Port Mike', 'Hardyburgh',
#        ...
#        'Scottstad', 'Port Willieport', 'Port Linda', 'Kaylamouth',
#        'Port Shawnfort', 'North Matthew', 'Chadton', 'Diazmouth', 'Laurentown',
#        'South Kennethmouth'],
#       dtype='object', name='City', length=251)

print(neighborhoods.columns.names)  # [None, None]

neighborhoods.columns.names = ["Category", "Subcategory"]
print(neighborhoods.columns.names)  # ['Category', 'Subcategory']
print(neighborhoods.head(3))
# Category                                     Culture         Services
# Subcategory                              Restaurants Museums   Police Schools
# State City             Street
# MO    Fisherborough    244 Tracy View             C+       F       D-      A+
# SD    Port Curtisville 446 Cynthia Inlet          C-       B        B      D+
# WV    Jimenezview      432 John Common             A      A+        F       B

# The two lines below are equivalent
neighborhoods.columns.get_level_values(0)
neighborhoods.columns.get_level_values("Category")
print(neighborhoods.columns.get_level_values(0))
# Index(['Culture', 'Culture', 'Services', 'Services'], dtype='object', name='Category')

# Count of unique values per column
print(neighborhoods.nunique())
# Category  Subcategory
# Culture   Restaurants    13
#           Museums        13
# Services  Police         13
#           Schools        13
# dtype: int64

# All four columns hold the 13 possible grades (A+ to F)

print(type(neighborhoods.nunique()))  # <class 'pandas.core.series.Series'>



