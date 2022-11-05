"""
-- Applied pandas
---- Visualization
------ Bar graphs
"""

import pandas as pd
import matplotlib.pyplot as plt

space = pd.read_csv("../datasets/space_missions.csv", parse_dates=["Date"], index_col="Date")
print(space["Company Name"].value_counts())
# CASC            35
# SpaceX          25
# Roscosmos       12
# Arianespace     10
# Rocket Lab       9
# VKS RF           6
# ULA              6
# ISRO             5
# Northrop         5
# MHI              3
# ILS              1
# Virgin Orbit     1
# ExPace           1
# JAXA             1
# Name: Company Name, dtype: int64

space["Company Name"].value_counts().plot(kind="bar")
plt.savefig('../figures/figure-14-3-1.svg', bbox_inches='tight')

plt.clf()

space["Company Name"].value_counts().plot(kind="barh")
plt.savefig('../figures/figure-14-3-2.svg', bbox_inches='tight')
