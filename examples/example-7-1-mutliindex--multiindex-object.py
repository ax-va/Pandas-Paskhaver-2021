"""
-- Applied pandas
---- MultiIndex DataFrames
------ The MultiIndex object
"""
import pandas as pd

address = ("8809 Flair Square", "Toddside", "IL", "37206")
addresses = [
    ("8809 Flair Square", "Toddside", "IL", "37206"),
    ("9901 Austin Street", "Toddside", "IL", "37206"),
    ("905 Hogan Quarter", "Franklin", "IL", "37206"),
]

# The two lines below are equivalent
multiindex1 = pd.MultiIndex.from_tuples(addresses)
multiindex2 = pd.MultiIndex.from_tuples(tuples=addresses)
print(multiindex1)
# MultiIndex([( '8809 Flair Square', 'Toddside', 'IL', '37206'),
#             ('9901 Austin Street', 'Toddside', 'IL', '37206'),
#             ( '905 Hogan Quarter', 'Franklin', 'IL', '37206')],
#            )

row_multiindex = pd.MultiIndex.from_tuples(
    tuples=addresses,
    names=["Street", "City", "State", "Zip"]
)
print(row_multiindex)
# MultiIndex([( '8809 Flair Square', 'Toddside', 'IL', '37206'),
#             ('9901 Austin Street', 'Toddside', 'IL', '37206'),
#             ( '905 Hogan Quarter', 'Franklin', 'IL', '37206')],
#            names=['Street', 'City', 'State', 'Zip'])

data = [
    ["A", "B+"],
    ["C+", "C"],
    ["D-", "A"],
]
columns = ["Schools", "Cost of Living"]
area_grades = pd.DataFrame(data=data, index=row_multiindex, columns=columns)
print(area_grades)
#                                         Schools Cost of Living
# Street             City     State Zip
# 8809 Flair Square  Toddside IL    37206       A             B+
# 9901 Austin Street Toddside IL    37206      C+              C
# 905 Hogan Quarter  Franklin IL    37206      D-              A

print(area_grades.columns)
# Index(['Schools', 'Cost of Living'], dtype='object')

column_multiindex = pd.MultiIndex.from_tuples(
    [
        ("Culture", "Restaurants"),
        ("Culture", "Museums"),
        ("Services", "Police"),
        ("Services", "Schools"),
    ]
)
print(column_multiindex)
# MultiIndex([( 'Culture', 'Restaurants'),
#             ( 'Culture',     'Museums'),
#             ('Services',      'Police'),
#             ('Services',     'Schools')],
#            )

data = [
    ["C-", "B+", "B-", "A"],
    ["D+", "C", "A", "C+"],
    ["A-", "A", "D+", "F"],
]
print(pd.DataFrame(data=data, index=row_multiindex, columns=column_multiindex))
#                                             Culture         Services
#                                         Restaurants Museums   Police Schools
# Street             City     State Zip
# 8809 Flair Square  Toddside IL    37206          C-      B+       B-       A
# 9901 Austin Street Toddside IL    37206          D+       C        A      C+
# 905 Hogan Quarter  Franklin IL    37206          A-       A       D+       F
