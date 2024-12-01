#!/usr/bin/python3
"""
-- Appendix D
---- Generating fake data with Faker
------ Populating a DataFrame with fake values
"""

import pandas as pd
import numpy as np
import faker

fake = faker.Faker()

data = [
    {
        "Name": fake.name(),
        "Company": fake.company(),
        "Email": fake.email(),
        "Salary": np.random.randint(50000, 200000)
    } for i in range(1000)
]

df = pd.DataFrame(data=data)
print(df)
#                     Name  ...  Salary
# 0           Randall Ford  ...  140652
# 1             Wayne Ware  ...  126481
# 2           Angel Obrien  ...   77045
# 3        Catherine Lopez  ...  145368
# 4    Mr. James Olsen DVM  ...   59523
# ..                   ...  ...     ...
# 995    Kimberly Phillips  ...   62779
# 996   Timothy Richardson  ...   73534
# 997         Colleen Ruiz  ...  113739
# 998         Tonya Taylor  ...   83759
# 999      Amanda Jacobson  ...   63430
#
# [1000 rows x 4 columns]
