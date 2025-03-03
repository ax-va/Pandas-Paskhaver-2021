#!/usr/bin/python3
"""
-- Core pandas
---- The Series object
------ Coding challenge
"""
import pandas as pd

superheroes = [
    "Batman",
    "Superman",
    "Spider-Man",
    "Iron Man",
    "Captain America",
    "Wonder Woman",
]

strength_levels = (100, 120, 90, 95, 110, 120)

# Populate a new Series object by the superheroes list
print(pd.Series(superheroes))
# 0             Batman
# 1           Superman
# 2         Spider-Man
# 3           Iron Man
# 4    Captain America
# 5       Wonder Woman
# dtype: object

# Populate a new Series object by the strength_levels tuple
print(pd.Series(data=strength_levels))
# 0    100
# 1    120
# 2     90
# 3     95
# 4    110
# 5    120
# dtype: int64

# Create a Series populating index nad values by superheroes and strength_levels, respectively
heroes = pd.Series(data=strength_levels, index=superheroes)
print(heroes)
# Batman             100
# Superman           120
# Spider-Man          90
# Iron Man            95
# Captain America    110
# Wonder Woman       120
# dtype: int64

# Extract the first two rows
print(heroes.head(2))
# Batman      100
# Superman    120
# dtype: int64

# Extract the last four rows
print(heroes.tail(4))
# Spider-Man          90
# Iron Man            95
# Captain America    110
# Wonder Woman       120
# dtype: int64

# Determine the number of unique values
print(heroes.nunique())  # 5
# Calculate the average strength
print(heroes.mean())  # 105.83333333333333
# Calculate the maximum and minimum strengths
print(heroes.max())  # 120
print(heroes.min())  # 90

# Doubled the strength level
print(heroes * 2)
# Batman             200
# Superman           240
# Spider-Man         180
# Iron Man           190
# Captain America    220
# Wonder Woman       240
# dtype: int64

# Convert to a dictionary
print(dict(heroes))
# {'Batman': 100, 'Superman': 120, 'Spider-Man': 90, 'Iron Man': 95, 'Captain America': 110, 'Wonder Woman': 120}


class A:
    pass


class B:
    pass


print(pd.Series([A(), A()]))
# 0    <__main__.A object at 0x00000293F6E39BB0>
# 1    <__main__.A object at 0x00000293F6E394F0>
# dtype: object

print(pd.Series([A(), A()]) + pd.Series([B(), B()]))
# TypeError: unsupported operand type(s) for +: 'A' and 'B'

