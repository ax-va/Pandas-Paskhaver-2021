#!/usr/bin/python3
"""
-- Applied pandas
---- Working with text data
------ Boolean methods
"""
import pandas as pd
inspections = pd.read_csv("../datasets/chicago_food_inspections.csv")

print(inspections["Name"].str.lower().str.contains("pizza").head())
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False
# Name: Name, dtype: bool

has_pizza = inspections["Name"].str.lower().str.contains("pizza")
print(inspections[has_pizza])
#                                         Name             Risk
# 1                                JETS PIZZA   Risk 2 (Medium)
# 19           NANCY'S HOME OF STUFFED PIZZA      Risk 1 (High)
# 27             NARY'S GRILL & PIZZA ,INC.       Risk 1 (High)
# 29                     NARYS GRILL & PIZZA      Risk 1 (High)
# 68                          COLUTAS PIZZA       Risk 1 (High)
# ...                                      ...              ...
# 153756          ANGELO'S STUFFED PIZZA CORP     Risk 1 (High)
# 153764                 COCHIAROS PIZZA #2       Risk 1 (High)
# 153772     FERNANDO'S MEXICAN GRILL & PIZZA     Risk 1 (High)
# 153788               REGGIO'S PIZZA EXPRESS     Risk 1 (High)
# 153801          State Street Pizza Company      Risk 1 (High)
#
# [3993 rows x 2 columns]

print(inspections["Name"].str.lower().str.startswith("tacos").head())
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# Name: Name, dtype: bool

inspections["Name"] = inspections["Name"].str.strip()
starts_with_tacos = (inspections["Name"].str.lower().str.startswith("tacos"))
print(inspections[starts_with_tacos])
#                          Name           Risk
# 69               TACOS NIETOS  Risk 1 (High)
# 556       TACOS EL TIO 2 INC.  Risk 1 (High)
# 675          TACOS DON GABINO  Risk 1 (High)
# 958       TACOS EL TIO 2 INC.  Risk 1 (High)
# 1036      TACOS EL TIO 2 INC.  Risk 1 (High)
# ...                       ...            ...
# 143587          TACOS DE LUNA  Risk 1 (High)
# 144026           TACOS GARCIA  Risk 1 (High)
# 146174        Tacos Place's 1  Risk 1 (High)
# 147810  TACOS MARIO'S LIMITED  Risk 1 (High)
# 151191            TACOS REYNA  Risk 1 (High)
#
# [105 rows x 2 columns]

ends_with_tacos = (inspections["Name"].str.lower().str.endswith("tacos"))
print(inspections[ends_with_tacos])
#                    Name           Risk
# 382        LAZO'S TACOS  Risk 1 (High)
# 569        LAZO'S TACOS  Risk 1 (High)
# 2652       FLYING TACOS   Risk 3 (Low)
# 3250       JONY'S TACOS  Risk 1 (High)
# 3812       PACO'S TACOS  Risk 1 (High)
# ...                 ...            ...
# 151121      REYES TACOS  Risk 1 (High)
# 151318   EL MACHO TACOS  Risk 1 (High)
# 151801   EL MACHO TACOS  Risk 1 (High)
# 153087  RAYMOND'S TACOS  Risk 1 (High)
# 153504        MIS TACOS  Risk 1 (High)
#
# [304 rows x 2 columns]
