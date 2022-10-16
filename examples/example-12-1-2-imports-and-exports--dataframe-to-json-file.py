"""
-- Applied pandas
---- Imports and exports
------ Reading from and writing to JSON files
-------- Exporting a DataFrame to a JSON file
"""

import pandas as pd

nobel = pd.read_json("../datasets/nobel.json")
nobel["prizes"].apply(lambda dict_entry: dict_entry.setdefault("laureates", []))
winners = pd.json_normalize(data=nobel["prizes"], record_path="laureates", meta=["year", "category"])
print(winners.head(3))
#     id   firstname      surname  ... share  year   category
# 0  976        John   Goodenough  ...     3  2019  chemistry
# 1  977  M. Stanley  Whittingham  ...     3  2019  chemistry
# 2  978       Akira      Yoshino  ...     3  2019  chemistry
#
# [3 rows x 7 columns]

print(winners.head(3).to_json(orient="records"))
# (Used https://jsonlint.com/ to make the JSON string more readable)
# [{
# 	"id": "976",
# 	"firstname": "John",
# 	"surname": "Goodenough",
# 	"motivation": "\"for the development of lithium-ion batteries\"",
# 	"share": "3",
# 	"year": "2019",
# 	"category": "chemistry"
# }, {
# 	"id": "977",
# 	"firstname": "M. Stanley",
# 	"surname": "Whittingham",
# 	"motivation": "\"for the development of lithium-ion batteries\"",
# 	"share": "3",
# 	"year": "2019",
# 	"category": "chemistry"
# }, {
# 	"id": "978",
# 	"firstname": "Akira",
# 	"surname": "Yoshino",
# 	"motivation": "\"for the development of lithium-ion batteries\"",
# 	"share": "3",
# 	"year": "2019",
# 	"category": "chemistry"
# }]

# Prevent duplicates in column names
print(winners.head(3).to_json(orient="split"))
# (Used https://jsonlint.com/ to make the JSON string more readable)
# {
# 	"columns": ["id", "firstname", "surname", "motivation", "share", "year", "category"],
# 	"index": [0, 1, 2],
# 	"data": [
# 		["976", "John", "Goodenough", "\"for the development of lithium-ion batteries\"", "3", "2019", "chemistry"],
# 		["977", "M. Stanley", "Whittingham", "\"for the development of lithium-ion batteries\"", "3", "2019", "chemistry"],
# 		["978", "Akira", "Yoshino", "\"for the development of lithium-ion batteries\"", "3", "2019", "chemistry"]
# 	]
# }

print(winners.head(3).to_json(orient="index"))
# (Used https://jsonlint.com/ to make the JSON string more readable)
# {
# 	"0": {
# 		"id": "976",
# 		"firstname": "John",
# 		"surname": "Goodenough",
# 		"motivation": "\"for the development of lithium-ion batteries\"",
# 		"share": "3",
# 		"year": "2019",
# 		"category": "chemistry"
# 	},
# 	"1": {
# 		"id": "977",
# 		"firstname": "M. Stanley",
# 		"surname": "Whittingham",
# 		"motivation": "\"for the development of lithium-ion batteries\"",
# 		"share": "3",
# 		"year": "2019",
# 		"category": "chemistry"
# 	},
# 	"2": {
# 		"id": "978",
# 		"firstname": "Akira",
# 		"surname": "Yoshino",
# 		"motivation": "\"for the development of lithium-ion batteries\"",
# 		"share": "3",
# 		"year": "2019",
# 		"category": "chemistry"
# 	}
# }

print(winners.head(3).to_json(orient="columns"))
# {
# 	"id": {
# 		"0": "976",
# 		"1": "977",
# 		"2": "978"
# 	},
# 	"firstname": {
# 		"0": "John",
# 		"1": "M. Stanley",
# 		"2": "Akira"
# 	},
# 	"surname": {
# 		"0": "Goodenough",
# 		"1": "Whittingham",
# 		"2": "Yoshino"
# 	},
# 	"motivation": {
# 		"0": "\"for the development of lithium-ion batteries\"",
# 		"1": "\"for the development of lithium-ion batteries\"",
# 		"2": "\"for the development of lithium-ion batteries\""
# 	},
# 	"share": {
# 		"0": "3",
# 		"1": "3",
# 		"2": "3"
# 	},
# 	"year": {
# 		"0": "2019",
# 		"1": "2019",
# 		"2": "2019"
# 	},
# 	"category": {
# 		"0": "chemistry",
# 		"1": "chemistry",
# 		"2": "chemistry"
# 	}
# }

print(winners.head(3).to_json(orient="values"))
# [
# 	["976", "John", "Goodenough", "\"for the development of lithium-ion batteries\"", "3", "2019", "chemistry"],
# 	["977", "M. Stanley", "Whittingham", "\"for the development of lithium-ion batteries\"", "3", "2019", "chemistry"],
# 	["978", "Akira", "Yoshino", "\"for the development of lithium-ion batteries\"", "3", "2019", "chemistry"]
# ]

print(winners.head(3).to_json(orient="table"))
# {
# 	"schema": {
# 		"fields": [{
# 			"name": "index",
# 			"type": "integer"
# 		}, {
# 			"name": "id",
# 			"type": "string"
# 		}, {
# 			"name": "firstname",
# 			"type": "string"
# 		}, {
# 			"name": "surname",
# 			"type": "string"
# 		}, {
# 			"name": "motivation",
# 			"type": "string"
# 		}, {
# 			"name": "share",
# 			"type": "string"
# 		}, {
# 			"name": "year",
# 			"type": "string"
# 		}, {
# 			"name": "category",
# 			"type": "string"
# 		}],
# 		"primaryKey": ["index"],
# 		"pandas_version": "1.4.0"
# 	},
# 	"data": [{
# 		"index": 0,
# 		"id": "976",
# 		"firstname": "John",
# 		"surname": "Goodenough",
# 		"motivation": "\"for the development of lithium-ion batteries\"",
# 		"share": "3",
# 		"year": "2019",
# 		"category": "chemistry"
# 	}, {
# 		"index": 1,
# 		"id": "977",
# 		"firstname": "M. Stanley",
# 		"surname": "Whittingham",
# 		"motivation": "\"for the development of lithium-ion batteries\"",
# 		"share": "3",
# 		"year": "2019",
# 		"category": "chemistry"
# 	}, {
# 		"index": 2,
# 		"id": "978",
# 		"firstname": "Akira",
# 		"surname": "Yoshino",
# 		"motivation": "\"for the development of lithium-ion batteries\"",
# 		"share": "3",
# 		"year": "2019",
# 		"category": "chemistry"
# 	}]
# }

winners.to_json("../datasets/winners.json", orient="records")
