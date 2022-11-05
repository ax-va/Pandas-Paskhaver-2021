#!/usr/bin/python3
"""
-- Applied pandas
---- Visualization
------ Line charts
"""

import pandas as pd
import matplotlib.pyplot as plt
# For Jupyter or Spyder, render in the output area
# %matplotlib inline

space = pd.read_csv("../datasets/space_missions.csv", parse_dates=["Date"], index_col="Date")
print(space.head())
#            Company Name Location    Cost   Status
# Date
# 2019-02-05  Arianespace   France  200.00  Success
# 2019-02-22       SpaceX      USA   50.00  Success
# 2019-03-02       SpaceX      USA   50.00  Success
# 2019-03-09         CASC    China   29.15  Success
# 2019-03-22  Arianespace   France   37.00  Success

print(space["Cost"].head())
# Date
# 2019-02-05    200.00
# 2019-02-22     50.00
# 2019-03-02     50.00
# 2019-03-09     29.15
# 2019-03-22     37.00
# Name: Cost, dtype: float64

print(repr(space["Cost"].plot()))
# <AxesSubplot: xlabel='Date'>

# Plot in a popup window taking the figure object from the memory
# plt.show()

plt.savefig('../figures/figure-14-2-1.svg')

data = [
    [2000, 3000000],
    [5000, 5000000]
]
df = pd.DataFrame(data=data, columns=["Small", "Large"])
print(df)
#    Small    Large
# 0   2000  3000000
# 1   5000  5000000
df.plot()
plt.savefig('../figures/figure-14-2-2.svg')

space.plot(y="Cost")
plt.savefig('../figures/figure-14-2-3.svg')

space.plot(y="Cost", colormap="gray")
plt.savefig('../figures/figure-14-2-4.svg')

print(plt.colormaps())
# ['magma', 'inferno', 'plasma', 'viridis', 'cividis', 'twilight', 'twilight_shifted',
# 'turbo', 'Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap', 'GnBu', 'Greens', 'Greys', 'OrRd',
# 'Oranges', 'PRGn', 'PiYG', 'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy',
# 'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr',
# 'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone', 'brg', 'bwr', 'cool', 'coolwarm',
# 'copper', 'cubehelix', 'flag', 'gist_earth', 'gist_gray', 'gist_heat', 'gist_ncar',
# 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 'gray', 'hot', 'hsv',
# 'jet', 'nipy_spectral', 'ocean', 'pink', 'prism', 'rainbow', 'seismic', 'spring', 'summer',
# 'terrain', 'winter', 'Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 'Set1', 'Set2',
# 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c', 'magma_r', 'inferno_r', 'plasma_r', 'viridis_r',
# 'cividis_r', 'twilight_r', 'twilight_shifted_r', 'turbo_r', 'Blues_r', 'BrBG_r', 'BuGn_r',
# 'BuPu_r', 'CMRmap_r', 'GnBu_r', 'Greens_r', 'Greys_r', 'OrRd_r', 'Oranges_r', 'PRGn_r',
# 'PiYG_r', 'PuBu_r', 'PuBuGn_r', 'PuOr_r', 'PuRd_r', 'Purples_r', 'RdBu_r', 'RdGy_r', 'RdPu_r',
# 'RdYlBu_r', 'RdYlGn_r', 'Reds_r', 'Spectral_r', 'Wistia_r', 'YlGn_r', 'YlGnBu_r', 'YlOrBr_r',
# 'YlOrRd_r', 'afmhot_r', 'autumn_r', 'binary_r', 'bone_r', 'brg_r', 'bwr_r', 'cool_r',
# 'coolwarm_r', 'copper_r', 'cubehelix_r', 'flag_r', 'gist_earth_r', 'gist_gray_r', 'gist_heat_r',
# 'gist_ncar_r', 'gist_rainbow_r', 'gist_stern_r', 'gist_yarg_r', 'gnuplot_r', 'gnuplot2_r',
# 'gray_r', 'hot_r', 'hsv_r', 'jet_r', 'nipy_spectral_r', 'ocean_r', 'pink_r', 'prism_r',
# 'rainbow_r', 'seismic_r', 'spring_r', 'summer_r', 'terrain_r', 'winter_r', 'Accent_r', 'Dark2_r',
# 'Paired_r', 'Pastel1_r', 'Pastel2_r', 'Set1_r', 'Set2_r', 'Set3_r', 'tab10_r', 'tab20_r',
# 'tab20b_r', 'tab20c_r']
