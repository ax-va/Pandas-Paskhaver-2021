#!/usr/bin/python3
"""
-- Applied pandas
---- Working with text data
------ A note on regular expressions
"""
import pandas as pd
customers = pd.read_csv("../datasets/customers.csv")
customers[["First Name", "Last Name"]] = customers["Name"].str.split(pat=" ", n=1, expand=True)
customers = customers.drop(labels="Name", axis="columns")
new_cols = ["Street", "City", "State", "Zip"]
customers[new_cols] = customers["Address"].str.split(pat=", ", expand=True)
del customers["Address"]

print(customers["Street"].head())
# 0             6461 Quinn Groves
# 1    1360 Tracey Ports Apt. 419
# 2          19120 Fleming Manors
# 3              441 Olivia Creek
# 4    4246 Chelsey Ford Apt. 310
# Name: Street, dtype: object

print(customers["Street"].str.replace("\d{4,}", "*", regex=True).head())
# 0             * Quinn Groves
# 1    * Tracey Ports Apt. 419
# 2           * Fleming Manors
# 3           441 Olivia Creek
# 4    * Chelsey Ford Apt. 310
# Name: Street, dtype: object