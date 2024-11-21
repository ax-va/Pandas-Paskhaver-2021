#!/usr/bin/python3
"""
-- Applied pandas
---- Visualization
------ Pie charts
"""

import pandas as pd
import matplotlib.pyplot as plt

space = pd.read_csv("../datasets/space_missions.csv", parse_dates=["Date"], index_col="Date")
print(space["Status"].value_counts())
# Success    114
# Failure      6
# Name: Status, dtype: int64

space["Status"].value_counts().plot(kind="pie")
plt.savefig('../figures/figure-14-4-1.svg')
plt.close()

space["Status"].value_counts().plot(kind="pie", legend=True)
plt.savefig('../figures/figure-14-4-2.svg')
plt.close()
