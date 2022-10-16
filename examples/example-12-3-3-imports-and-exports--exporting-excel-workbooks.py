"""
-- Applied pandas
---- Imports and exports
------ Reading from and writing to CSV files
-------- Exporting Excel workbooks
"""

import pandas as pd

baby_names = pd.read_csv("../datasets/new_york_city_baby_names.csv")

girls = baby_names[baby_names["Gender"] == "FEMALE"]
boys = baby_names[baby_names["Gender"] == "MALE"]

# Creating an ExcelWriter object also creates a file
excel_file = pd.ExcelWriter("../datasets/Baby_Names.xlsx")
print(excel_file)  #<pandas.io.excel._openpyxl.OpenpyxlWriter object at 0x000001A333EC09A0>

girls.to_excel(excel_writer=excel_file, sheet_name="Girls", index=False)
# The worksheet is not added yet to the file

boys.to_excel(
    excel_file,
    sheet_name="Boys",
    index=False,
    columns=["Child's First Name", "Count", "Rank"]
)
# The worksheet is not added yet to the file

# Now save to the file
excel_file.save()
