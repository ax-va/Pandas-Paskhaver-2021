#!/usr/bin/python3
"""
-- Applied pandas
---- Imports and exports
------ Coding challenge
"""

import pandas as pd

tv_shows_series = pd.read_json("../datasets/tv_shows.json")
print(tv_shows_series)
#                                                shows
# 0  {'show': 'The X-Files', 'runtime': 60, 'networ...
# 1  {'show': 'Lost', 'runtime': 60, 'network': 'AB...
# 2  {'show': 'Buffy the Vampire Slayer', 'runtime'...

print(tv_shows_series.loc[0, "shows"])
# {
# 	'show': 'The X-Files',
# 	'runtime': 60,
# 	'network': 'FOX',
# 	'episodes': [{
# 		'season': 1,
# 		'episode': 1,
# 		'name': 'Pilot',
# 		'air_date': '1993-09-11 01:00:00'
# 	}, ...

# Normalize the nested episode data for each dictionary in the shows column
tv_shows = pd.json_normalize(
    data=tv_shows_series["shows"],
    record_path="episodes",
    meta=["show", "runtime", "network"]
)
print(tv_shows.head())
#   season  episode              name  ...         show runtime network
# 0       1        1             Pilot  ...  The X-Files      60     FOX
# 1       1        2       Deep Throat  ...  The X-Files      60     FOX
# 2       1        3           Squeeze  ...  The X-Files      60     FOX
# 3       1        4           Conduit  ...  The X-Files      60     FOX
# 4       1        5  The Jersey Devil  ...  The X-Files      60     FOX
#
# [5 rows x 7 columns]

# Filter the normalized data set into three separate DataFrames
x_files = tv_shows[tv_shows["show"] == "The X-Files"]
lost = tv_shows[tv_shows["show"] == "Lost"]
buffy = tv_shows[tv_shows["show"] == "Buffy the Vampire Slayer"]

# Write the three DataFrames to an episodes.xlsx Excel workbook,
# and save each TV show’s episode data to a separate worksheet
episodes = pd.ExcelWriter("../datasets/episodes.xlsx")

for dataframe, name in [(x_files, "X-Files"), (lost, "Lost"), (buffy, "Buffy the Vampire Slayer")]:
    dataframe.to_excel(excel_writer=episodes, sheet_name=name, index=False)
episodes.save()
