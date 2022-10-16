"""
-- Applied pandas
---- Imports and exports
------ Reading from and writing to CSV files
"""

import pandas as pd

# url = "https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv"
# baby_names = pd.read_csv(url)

# Pandas raises an HTTPError exception if the link is invalid

baby_names = pd.read_csv("../datasets/new_york_city_baby_names.csv")
print(baby_names.head())

# Convert to a string including index
print(baby_names.head(10).to_csv())
# ,Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
# 0,2011,FEMALE,HISPANIC,GERALDINE,13,75
# 1,2011,FEMALE,HISPANIC,GIA,21,67
# 2,2011,FEMALE,HISPANIC,GIANNA,49,42
# 3,2011,FEMALE,HISPANIC,GISELLE,38,51
# 4,2011,FEMALE,HISPANIC,GRACE,36,53
# 5,2011,FEMALE,HISPANIC,GUADALUPE,26,62
# 6,2011,FEMALE,HISPANIC,HAILEY,126,8
# 7,2011,FEMALE,HISPANIC,HALEY,14,74
# 8,2011,FEMALE,HISPANIC,HANNAH,17,71
# 9,2011,FEMALE,HISPANIC,HAYLEE,17,71

# Convert to a string excluding index
print(baby_names.head(10).to_csv(index=False))
# Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
# 2011,FEMALE,HISPANIC,GERALDINE,13,75
# 2011,FEMALE,HISPANIC,GIA,21,67
# 2011,FEMALE,HISPANIC,GIANNA,49,42
# 2011,FEMALE,HISPANIC,GISELLE,38,51
# 2011,FEMALE,HISPANIC,GRACE,36,53
# 2011,FEMALE,HISPANIC,GUADALUPE,26,62
# 2011,FEMALE,HISPANIC,HAILEY,126,8
# 2011,FEMALE,HISPANIC,HALEY,14,74
# 2011,FEMALE,HISPANIC,HANNAH,17,71
# 2011,FEMALE,HISPANIC,HAYLEE,17,71

baby_names.to_csv("../datasets/NYC_Baby_Names.csv", index=False)

baby_names.to_csv(
    "../datasets/NYC_Baby_Names.csv",
    index=False,
    columns=["Gender", "Child's First Name", "Count"]
)


