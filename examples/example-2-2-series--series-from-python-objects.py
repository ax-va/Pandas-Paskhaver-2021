"""
Create Series from Python objects
"""
import numpy as np
import pandas as pd

calorie_info = {
    "Cereal": 125,
    "Chocolate Bar": 406,
    "Ice Cream Sundae": 342,
}
diet = pd.Series(calorie_info)
print(diet)
# Cereal              125
# Chocolate Bar       406
# Ice Cream Sundae    342
# dtype: int64

print(pd.Series(data=("Red", "Green", "Blue")))
# 0      Red
# 1    Green
# 2     Blue
# dtype: object

rgb_colors = [(120, 41, 26), (196, 165, 45)]
print(pd.Series(data=rgb_colors))
# 0     (120, 41, 26)
# 1    (196, 165, 45)
# dtype: object

my_set = {"Ricky", "Bobby"}
print(pd.Series(list(my_set)))
# 0    Bobby
# 1    Ricky
# dtype: object

random_data = np.random.randint(1, 101, 10)
print(pd.Series(random_data))
# 0     5
# 1    31
# 2     7
# 3    75
# 4    51
# 5    44
# 6    88
# 7    71
# 8    48
# 9    52
# dtype: int32

