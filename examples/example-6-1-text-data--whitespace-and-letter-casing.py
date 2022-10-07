"""
-- Applied pandas
---- Working with Text Data
------ Whitespace and Letter Casing
"""
import pandas as pd
inspections = pd.read_csv("../datasets/chicago_food_inspections.csv")
print(inspections)
#                                       Name             Risk
# 0               MARRIOT MARQUIS CHICAGO       Risk 1 (High)
# 1                              JETS PIZZA   Risk 2 (Medium)
# 2                               ROOM 1520      Risk 3 (Low)
# 3                MARRIOT MARQUIS CHICAGO      Risk 1 (High)
# 4                            CHARTWELLS       Risk 1 (High)
# ...                                    ...              ...
# 153805                         WOLCOTT'S      Risk 1 (High)
# 153806     DUNKIN DONUTS/BASKIN-ROBBINS     Risk 2 (Medium)
# 153807                           Cafe 608     Risk 1 (High)
# 153808                        mr.daniel's     Risk 1 (High)
# 153809                         TEMPO CAFE     Risk 1 (High)
#
# [153810 rows x 2 columns]

print(inspections["Name"].head())
# [153810 rows x 2 columns]
# 0     MARRIOT MARQUIS CHICAGO
# 1                    JETS PIZZA
# 2                     ROOM 1520
# 3      MARRIOT MARQUIS CHICAGO
# 4                  CHARTWELLS
# Name: Name, dtype: object

print(repr(inspections["Name"].head().values))
# array([' MARRIOT MARQUIS CHICAGO   ', ' JETS PIZZA ', '   ROOM 1520 ',
#        '  MARRIOT MARQUIS CHICAGO  ', ' CHARTWELLS   '], dtype=object)

print(inspections["Name"].str)  # <pandas.core.strings.accessor.StringMethods object at 0x000002404D4797C0>

print(repr(inspections["Name"].str.lstrip().values))
# array(['MARRIOT MARQUIS CHICAGO   ', 'JETS PIZZA ', 'ROOM 1520 ', ...,
#        'Cafe 608 ', "mr.daniel's ", 'TEMPO CAFE '], dtype=object)

print(repr(inspections["Name"].str.rstrip().values))
# array([' MARRIOT MARQUIS CHICAGO', ' JETS PIZZA', '   ROOM 1520', ...,
#        ' Cafe 608', "  mr.daniel's", '   TEMPO CAFE'], dtype=object)

print(repr(inspections["Name"].str.strip().values))
# array(['MARRIOT MARQUIS CHICAGO', 'JETS PIZZA', 'ROOM 1520', ...,
#        'Cafe 608', "mr.daniel's", 'TEMPO CAFE'], dtype=object)

# No extra whitespace
inspections["Name"] = inspections["Name"].str.strip()

print(inspections.columns)  # Index(['Name', 'Risk'], dtype='object')
for column in inspections.columns:
    inspections[column] = inspections[column].str.strip()

print(inspections["Name"].str.lower().head())
# 0    marriot marquis chicago
# 1                 jets pizza
# 2                  room 1520
# 3    marriot marquis chicago
# 4                 chartwells
# Name: Name, dtype: object

steaks = pd.Series(["porterhouse", "filet mignon", "ribeye"])
print(steaks)
# 0     porterhouse
# 1    filet mignon
# 2          ribeye
# dtype: object

print(steaks.str.upper())
# 0     PORTERHOUSE
# 1    FILET MIGNON
# 2          RIBEYE
# dtype: object

print(inspections["Name"].str.capitalize())
# 0              Marriot marquis chicago
# 1                           Jets pizza
# 2                            Room 1520
# 3              Marriot marquis chicago
# 4                           Chartwells
#                       ...
# 153805                       Wolcott's
# 153806    Dunkin donuts/baskin-robbins
# 153807                        Cafe 608
# 153808                     Mr.daniel's
# 153809                      Tempo cafe
# Name: Name, Length: 153810, dtype: object

print(inspections["Name"].str.title())
# 0              Marriot Marquis Chicago
# 1                           Jets Pizza
# 2                            Room 1520
# 3              Marriot Marquis Chicago
# 4                           Chartwells
#                       ...
# 153805                       Wolcott'S
# 153806    Dunkin Donuts/Baskin-Robbins
# 153807                        Cafe 608
# 153808                     Mr.Daniel'S
# 153809                      Tempo Cafe
# Name: Name, Length: 153810, dtype: object

