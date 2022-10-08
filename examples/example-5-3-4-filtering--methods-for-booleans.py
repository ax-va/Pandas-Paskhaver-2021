"""
-- Core pandas
---- Filtering a DataFrame
------ Filtering by multiple conditions
-------- Methods for Booleans
"""
# Equality                  employees["Team"] == "Marketing"        employees["Team"].eq("Marketing")
# Inequality                employees["Team"] != "Marketing"        employees["Team"].ne("Marketing")
# Less than                 employees["Salary"] < 100000            employees["Salary"].lt(100000)
# Less than or equal to     employees["Salary"] <= 100000           employees["Salary"].le(100000)
# Greater than              employees["Salary"] > 100000            employees["Salary"].gt(100000)
# Greater than or equal to  employees["Salary"] >= 100000           employees["Salary"].ge(100000)
