"""
-- Applied pandas
---- Reshaping and Pivoting
------ Exploding a list of values
"""

import pandas as pd
recipes = pd.read_csv("../datasets/recipes.csv")
print(recipes)
#                     Recipe                                        Ingredients
# 0   Cashew Crusted Chicken  Apricot preserves, Dijon mustard, curry powder...
# 1      Tomato Basil Salmon  Salmon filets, basil, tomato, olive oil, Parme...
# 2  Parmesan Cheese Chicken  Bread crumbs, Parmesan cheese, Italian seasoni...

print(recipes["Ingredients"].str.split(","))
# 0    [Apricot preserves,  Dijon mustard,  curry pow...
# 1    [Salmon filets,  basil,  tomato,  olive oil,  ...
# 2    [Bread crumbs,  Parmesan cheese,  Italian seas...
# Name: Ingredients, dtype: object

recipes["Ingredients"] = recipes["Ingredients"].str.split(",")
print(recipes)
#                     Recipe                                        Ingredients
# 0   Cashew Crusted Chicken  [Apricot preserves,  Dijon mustard,  curry pow...
# 1      Tomato Basil Salmon  [Salmon filets,  basil,  tomato,  olive oil,  ...
# 2  Parmesan Cheese Chicken  [Bread crumbs,  Parmesan cheese,  Italian seas...

recipes = recipes.explode("Ingredients")
print(recipes)
#                     Recipe         Ingredients
# 0   Cashew Crusted Chicken   Apricot preserves
# 0   Cashew Crusted Chicken       Dijon mustard
# 0   Cashew Crusted Chicken        curry powder
# 0   Cashew Crusted Chicken     chicken breasts
# 0   Cashew Crusted Chicken             cashews
# 1      Tomato Basil Salmon       Salmon filets
# 1      Tomato Basil Salmon               basil
# 1      Tomato Basil Salmon              tomato
# 1      Tomato Basil Salmon           olive oil
# 1      Tomato Basil Salmon     Parmesan cheese
# 2  Parmesan Cheese Chicken        Bread crumbs
# 2  Parmesan Cheese Chicken     Parmesan cheese
# 2  Parmesan Cheese Chicken   Italian seasoning
# 2  Parmesan Cheese Chicken                 egg
# 2  Parmesan Cheese Chicken     chicken breasts
