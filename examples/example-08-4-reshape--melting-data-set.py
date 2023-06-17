#!/usr/bin/python3
"""
-- Applied pandas
---- Reshaping and pivoting
------ Melting a data set
"""
# Melting is the process of converting a wide data set to a narrow one.
# Narrow data is easier to aggregate and pivot than wide data.

import pandas as pd
sales = pd.read_csv("../datasets/sales_by_employee.csv", parse_dates=["Date"])

# Narrow format
print(sales.head(1))
#         Date   Name       Customer  Revenue  Expenses
# 0 2020-01-01  Oscar  Logistics XYZ     5250       531

video_game_sales = pd.read_csv("../datasets/video_game_sales.csv")
print(video_game_sales.head())
#                        Name     NA     EU     JP  Other
# 0                Wii Sports  41.49  29.02   3.77   8.46
# 1         Super Mario Bros.  29.08   3.58   6.81   0.77
# 2            Mario Kart Wii  15.85  12.88   3.79   3.31
# 3         Wii Sports Resort  15.75  11.01   3.28   2.96
# 4  Pokemon Red/Pokemon Blue  11.27   8.89  10.22   1.00

# Wide format
print(video_game_sales.head(1))
# 0  Wii Sports  41.49  29.02  3.77   8.46

# Problem: 41.49 is not a type of NA (North America) or a measurement of NA

# Melted data set
print(video_game_sales.melt(id_vars="Name", value_vars="NA").head())
#                        Name variable  value
# 0                Wii Sports       NA  41.49
# 1         Super Mario Bros.       NA  29.08
# 2            Mario Kart Wii       NA  15.85
# 3         Wii Sports Resort       NA  15.75
# 4  Pokemon Red/Pokemon Blue       NA  11.27

# Melted data set
regional_sales_columns = ["NA", "EU", "JP", "Other"]
print(video_game_sales.melt(id_vars="Name", value_vars=regional_sales_columns))
#                                                    Name variable  value
# 0                                            Wii Sports       NA  41.49
# 1                                     Super Mario Bros.       NA  29.08
# 2                                        Mario Kart Wii       NA  15.85
# 3                                     Wii Sports Resort       NA  15.75
# 4                              Pokemon Red/Pokemon Blue       NA  11.27
# ...                                                 ...      ...    ...
# 66259                Woody Woodpecker in Crazy Castle 5    Other   0.00
# 66260                     Men in Black II: Alien Escape    Other   0.00
# 66261  SCORE International Baja 1000: The Official Game    Other   0.00
# 66262                                        Know How 2    Other   0.00
# 66263                                  Spirits & Spells    Other   0.00
#
# [66264 rows x 3 columns]

# Melted data set
video_game_sales_by_region = video_game_sales.melt(
    id_vars="Name",
    value_vars=regional_sales_columns,
    var_name="Region",
    value_name="Sales"
)
print(video_game_sales_by_region.head())
#                        Name Region  Sales
# 0                Wii Sports     NA  41.49
# 1         Super Mario Bros.     NA  29.08
# 2            Mario Kart Wii     NA  15.85
# 3         Wii Sports Resort     NA  15.75
# 4  Pokemon Red/Pokemon Blue     NA  11.27

# Aggregate over all the regions
print(
    video_game_sales_by_region.pivot_table(
        index="Name",
        values="Sales",
        aggfunc="sum").head()
)
#                                Sales
# Name
# '98 Koshien                     0.40
# .hack//G.U. Vol.1//Rebirth      0.17
# .hack//G.U. Vol.2//Reminisce    0.23
# .hack//G.U. Vol.3//Redemption   0.17
# .hack//Infection Part 1         1.26
