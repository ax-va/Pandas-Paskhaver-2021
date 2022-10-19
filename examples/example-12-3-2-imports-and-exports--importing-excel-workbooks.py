"""
-- Applied pandas
---- Imports and exports
------ Reading from and writing to Excel workbooks
-------- Importing Excel workbooks
"""

import pandas as pd

print(pd.read_excel("../datasets/Single Worksheet.xlsx"))
#   First Name Last Name           City Gender
# 0    Brandon     James          Miami      M
# 1       Sean   Hawkins         Denver      M
# 2       Judy       Day    Los Angeles      F
# 3     Ashley      Ruiz  San Francisco      F
# 4  Stephanie     Gomez       Portland      F

print(
    pd.read_excel(
        io="../datasets/Single Worksheet.xlsx",
        usecols=["City", "First Name", "Last Name"],
        index_col="City"
    )
)
#               First Name Last Name
# City
# Miami            Brandon     James
# Denver              Sean   Hawkins
# Los Angeles         Judy       Day
# San Francisco     Ashley      Ruiz
# Portland       Stephanie     Gomez

# The two lines below are equivalent
pd.read_excel("../datasets/Multiple Worksheets.xlsx", sheet_name=0)
pd.read_excel("../datasets/Multiple Worksheets.xlsx", sheet_name="Data 1")

print(pd.read_excel("../datasets/Multiple Worksheets.xlsx", sheet_name="Data 1"))
#   First Name Last Name           City Gender
# 0    Brandon     James          Miami      M
# 1       Sean   Hawkins         Denver      M
# 2       Judy       Day    Los Angeles      F
# 3     Ashley      Ruiz  San Francisco      F
# 4  Stephanie     Gomez       Portland      F

workbook = pd.read_excel("../datasets/Multiple Worksheets.xlsx", sheet_name=None)
print(type(workbook))  # <class 'dict'>
print(workbook)
# {'Data 1':   First Name Last Name           City Gender
# 0    Brandon     James          Miami      M
# 1       Sean   Hawkins         Denver      M
# 2       Judy       Day    Los Angeles      F
# 3     Ashley      Ruiz  San Francisco      F
# 4  Stephanie     Gomez       Portland      F,
# 'Data 2':   First Name Last Name           City Gender
# 0     Parker     Power        Raleigh      F
# 1    Preston  Prescott   Philadelphia      F
# 2    Ronaldo   Donaldo         Bangor      M
# 3      Megan   Stiller  San Francisco      M
# 4     Bustin    Jieber         Austin      F,
# 'Data 3':   First Name  Last Name     City Gender
# 0     Robert     Miller  Seattle      M
# 1       Tara     Garcia  Phoenix      F
# 2    Raphael  Rodriguez  Orlando      M}

print(workbook["Data 2"])
#   First Name Last Name           City Gender
# 0     Parker     Power        Raleigh      F
# 1    Preston  Prescott   Philadelphia      F
# 2    Ronaldo   Donaldo         Bangor      M
# 3      Megan   Stiller  San Francisco      M
# 4     Bustin    Jieber         Austin      F

print(pd.read_excel("../datasets/Multiple Worksheets.xlsx", sheet_name=["Data 1", "Data 3"]))
# {'Data 1':   First Name Last Name           City Gender
# 0    Brandon     James          Miami      M
# 1       Sean   Hawkins         Denver      M
# 2       Judy       Day    Los Angeles      F
# 3     Ashley      Ruiz  San Francisco      F
# 4  Stephanie     Gomez       Portland      F, 'Data 3':   First Name  Last Name     City Gender
# 0     Robert     Miller  Seattle      M
# 1       Tara     Garcia  Phoenix      F
# 2    Raphael  Rodriguez  Orlando      M}

print(pd.read_excel("../datasets/Multiple Worksheets.xlsx", sheet_name=[1, 2]))
# {1:   First Name Last Name           City Gender
# 0     Parker     Power        Raleigh      F
# 1    Preston  Prescott   Philadelphia      F
# 2    Ronaldo   Donaldo         Bangor      M
# 3      Megan   Stiller  San Francisco      M
# 4     Bustin    Jieber         Austin      F, 2:   First Name  Last Name     City Gender
# 0     Robert     Miller  Seattle      M
# 1       Tara     Garcia  Phoenix      F
# 2    Raphael  Rodriguez  Orlando      M}
