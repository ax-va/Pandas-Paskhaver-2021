"""
-- Applied pandas
---- Reshaping and Pivoting
------ Coding Challenge
"""

import pandas as pd
cars = pd.read_csv("../datasets/used-cars.csv")
print(cars)
#        Manufacturer  Year   Fuel Transmission  Price
# 0             Acura  2012    Gas    Automatic  10299
# 1            Jaguar  2011    Gas    Automatic   9500
# 2             Honda  2004    Gas    Automatic   3995
# 3         Chevrolet  2016    Gas    Automatic  41988
# 4               Kia  2015    Gas    Automatic  12995
# ...             ...   ...    ...          ...    ...
# 460461        Rover  2008    Gas    Automatic   7950
# 460462       Nissan  2016    Gas    Automatic  13995
# 460463          BMW  2010    Gas    Automatic  10995
# 460464        Dodge  2015  Other       Manual   6495
# 460465          GMC  2008    Gas    Automatic   8990
#
# [460466 rows x 5 columns]

min_wage = pd.read_csv("../datasets/minimum-wage.csv")
print(min_wage)
#                    State  2010  2011  2012  2013   2014   2015   2016   2017
# 0                Alabama  0.00  0.00  0.00  0.00   0.00   0.00   0.00   0.00
# 1                 Alaska  8.90  8.63  8.45  8.33   8.20   9.24  10.17  10.01
# 2                Arizona  8.33  8.18  8.34  8.38   8.36   8.50   8.40  10.22
# 3               Arkansas  7.18  6.96  6.82  6.72   6.61   7.92   8.35   8.68
# 4             California  9.19  8.91  8.72  8.60   9.52   9.51  10.43  10.22
# 5               Colorado  8.31  8.19  8.33  8.36   8.46   8.69   8.67   9.50
# 6            Connecticut  9.47  9.18  9.00  8.87   9.20   9.67  10.02  10.32
# 7               Delaware  8.33  8.07  7.91  7.79   8.20   8.72   8.61   8.43
# 8   District of Columbia  9.47  9.18  9.00  8.87  10.05  11.09  12.00  11.75
# 9         Federal (FLSA)  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 10               Florida  8.33  8.07  8.37  8.37   8.39   8.50   8.40   8.27
# 11               Georgia  5.91  5.73  5.62  5.54   5.45   5.44   5.37   5.26
# 12                  Guam  8.33  8.07  7.91  7.79   7.67   8.72   8.61   8.43
# 13                Hawaii  8.33  8.07  7.91  7.79   7.67   8.19   8.87   9.45
# 14                 Idaho  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 15              Illinois  9.19  9.18  9.00  8.87   8.73   8.72   8.61   8.43
# 16               Indiana  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 17                  Iowa  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 18                Kansas  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 19              Kentucky  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 20             Louisiana  0.00  0.00  0.00  0.00   0.00   0.00   0.00   0.00
# 21                 Maine  8.61  8.35  8.18  8.06   7.93   7.92   7.82   9.19
# 22              Maryland  8.33  8.07  7.91  7.79   7.67   8.72   9.13   8.94
# 23         Massachusetts  9.19  8.91  8.72  8.60   8.46   9.51  10.43  11.24
# 24              Michigan  8.50  8.24  8.07  7.95   8.62   8.61   8.87   9.09
# 25             Minnesota  7.06  6.85  6.71  6.61   8.46   9.51   9.91   9.70
# 26           Mississippi  0.00  0.00  0.00  0.00   0.00   0.00   0.00   0.00
# 27              Missouri  8.33  8.07  7.91  7.90   7.93   8.08   7.98   7.87
# 28               Montana  8.33  8.18  8.34  8.38   8.36   8.50   8.40   8.33
# 29              Nebraska  8.33  8.07  7.91  7.79   7.67   8.45   9.39   9.19
# 30                Nevada  8.67  9.18  9.00  8.87   8.73   8.72   8.61   8.43
# 31         New Hampshire  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 32            New Jersey  8.33  8.07  7.91  7.79   8.73   8.85   8.74   8.62
# 33            New Mexico  8.61  8.35  8.18  8.06   7.93   7.92   7.82   7.66
# 34              New York  8.33  8.07  7.91  7.79   8.46   9.24   9.39   9.91
# 35        North Carolina  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 36          North Dakota  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 37                  Ohio  8.38  8.24  8.40  8.44   8.41   8.56   8.45   8.33
# 38              Oklahoma  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 39                Oregon  9.65  9.46  9.60  9.62   9.63   9.77  10.17   9.96
# 40          Pennsylvania  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 41           Puerto Rico  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 42          Rhode Island  8.50  8.24  8.07  8.33   8.46   9.51  10.02   9.81
# 43        South Carolina  0.00  0.00  0.00  0.00   0.00   0.00   0.00   0.00
# 44          South Dakota  8.33  8.07  7.91  7.79   7.67   8.98   8.92   8.84
# 45             Tennessee  0.00  0.00  0.00  0.00   0.00   0.00   0.00   0.00
# 46                 Texas  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 47   U.S. Virgin Islands  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 48                  Utah  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 49               Vermont  9.26  9.07  9.23  9.24   9.23   9.67  10.02  10.22
# 50              Virginia  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 51            Washington  9.82  9.65  9.86  9.88   9.86  10.00   9.88  11.24
# 52         West Virginia  8.33  8.07  7.91  7.79   7.67   8.45   9.13   8.94
# 53             Wisconsin  8.33  8.07  7.91  7.79   7.67   7.66   7.56   7.41
# 54               Wyoming  5.91  5.73  5.62  5.54   5.45   5.44   5.37   5.26

# Aggregate the sum of car prices in cars.
# Group the results by fuel type on the row axis.
print(cars.pivot_table(values="Price", index="Fuel", aggfunc="sum"))
#                 Price
# Fuel
# Diesel      986177143
# Electric     18502957
# Gas       86203853926
# Hybrid       44926064
# Other       242096286

# Aggregate the count of cars in cars.
# Group the results by manufacturer on the index axis and transmission type on the column axis.
# Show the subtotals for both the rows and columns.
print(
    cars.pivot_table(
        values="Price",
        index="Manufacturer",
        columns="Transmission",
        aggfunc="count",
        margins=True
    )
)
# Transmission     Automatic   Manual    Other     All
# Manufacturer
# Acura               3443.0    141.0     48.0    3632
# Alfa-Romeo            50.0      NaN     11.0      61
# Aston-Martin          20.0      5.0      NaN      25
# Audi                4974.0    375.0     69.0    5418
# BMW                11641.0    774.0    627.0   13042
# Buick               6187.0     17.0    265.0    6469
# Cadillac            6357.0     74.0    406.0    6837
# Chevrolet          61006.0   1820.0   4255.0   67081
# Chrysler            7553.0    133.0    212.0    7898
# Dodge              14338.0    626.0    991.0   15955
# Ferrari               29.0      4.0      9.0      42
# Fiat                 435.0    220.0    187.0     842
# Ford               75980.0   2979.0   3505.0   82464
# GMC                19504.0    137.0    939.0   20580
# Harley-Davidson      115.0     61.0     10.0     186
# Hennessey              NaN      1.0      NaN       1
# Honda              20666.0   1502.0    921.0   23089
# Hyundai            10350.0    544.0    334.0   11228
# Infiniti            3555.0    185.0     76.0    3816
# Jaguar               882.0     29.0     50.0     961
# Jeep               17687.0   2316.0   1385.0   21388
# Kia                 7615.0    466.0    587.0    8668
# Land Rover            23.0      NaN      NaN      23
# Lexus               5573.0     30.0    226.0    5829
# Lincoln             3001.0     10.0     51.0    3062
# Mazda               4127.0    746.0    649.0    5522
# Mercedes-Benz       9599.0     74.0     98.0    9771
# Mercury             1437.0     15.0      2.0    1454
# Mini                1411.0    712.0    138.0    2261
# Mitsubishi          2064.0    247.0     52.0    2363
# Nissan             22262.0    858.0   1429.0   24549
# Pontiac             2710.0    213.0     28.0    2951
# Porche                 9.0      1.0      NaN      10
# Ram                19996.0    837.0   1243.0   22076
# Rover               1752.0      9.0     24.0    1785
# Saturn              1451.0    152.0     12.0    1615
# Subaru              8317.0   1884.0    420.0   10621
# Tesla                179.0      NaN     59.0     238
# Toyota             31480.0   1367.0   2134.0   34981
# Volkswagen          7985.0   1286.0    236.0    9507
# Volvo               2665.0    155.0     50.0    2870
# All               398428.0  21005.0  21738.0  441171

# Aggregate the average of car prices in cars.
# Group the results by year and fuel type on the index axis and transmission type on the column axis.
print(
    cars.pivot_table(
        values="Price",
        index=["Year", "Fuel"],
        columns=["Transmission"],
        aggfunc="mean"
    )
)
# Transmission      Automatic        Manual         Other
# Year Fuel
# 2000 Diesel    11326.176962  14010.164021  11075.000000
#      Electric   1500.000000           NaN           NaN
#      Gas        4314.675996   6226.140327   3203.538462
#      Hybrid     2600.000000   2400.000000           NaN
#      Other     16014.918919  11361.952381  12984.642857
# ...                     ...           ...           ...
# 2020 Diesel    63272.595930      1.000000   1234.000000
#      Electric   8015.166667   2200.000000  20247.500000
#      Gas       34925.857933  36007.270833  20971.045455
#      Hybrid    35753.200000           NaN   1234.000000
#      Other     22210.306452           NaN   2725.925926
#
# [102 rows x 3 columns]

# Move the transmission level from the column axis to the row axis
report = cars.pivot_table(
    values="Price",
    index=["Year", "Fuel"],
    columns=["Transmission"],
    aggfunc="mean"
)
print(report.stack())
# Year  Fuel      Transmission
# 2000  Diesel    Automatic       11326.176962
#                 Manual          14010.164021
#                 Other           11075.000000
#       Electric  Automatic        1500.000000
#       Gas       Automatic        4314.675996
#                                     ...
# 2020  Gas       Other           20971.045455
#       Hybrid    Automatic       35753.200000
#                 Other            1234.000000
#       Other     Automatic       22210.306452
#                 Other            2725.925926
# Length: 274, dtype: float64

print(report.stack().unstack())
# Transmission      Automatic        Manual         Other
# Year Fuel
# 2000 Diesel    11326.176962  14010.164021  11075.000000
#      Electric   1500.000000           NaN           NaN
#      Gas        4314.675996   6226.140327   3203.538462
#      Hybrid     2600.000000   2400.000000           NaN
#      Other     16014.918919  11361.952381  12984.642857
# ...                     ...           ...           ...
# 2020 Diesel    63272.595930      1.000000   1234.000000
#      Electric   8015.166667   2200.000000  20247.500000
#      Gas       34925.857933  36007.270833  20971.045455
#      Hybrid    35753.200000           NaN   1234.000000
#      Other     22210.306452           NaN   2725.925926

# Convert the min_wage from wide format to narrow format
year_columns = [str(year) for year in range(2010, 2018)]
print(year_columns)
# ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
print(min_wage.melt(id_vars="State", value_vars=year_columns))
#              State variable  value
# 0          Alabama     2010   0.00
# 1           Alaska     2010   8.90
# 2          Arizona     2010   8.33
# 3         Arkansas     2010   7.18
# 4       California     2010   9.19
# ..             ...      ...    ...
# 435       Virginia     2017   7.41
# 436     Washington     2017  11.24
# 437  West Virginia     2017   8.94
# 438      Wisconsin     2017   7.41
# 439        Wyoming     2017   5.26
#
# [440 rows x 3 columns]

# By default, pandas melts data from all columns
# except the one we pass to the id_vars parameter
print(min_wage.melt(id_vars="State"))
#              State variable  value
# 0          Alabama     2010   0.00
# 1           Alaska     2010   8.90
# 2          Arizona     2010   8.33
# 3         Arkansas     2010   7.18
# 4       California     2010   9.19
# ..             ...      ...    ...
# 435       Virginia     2017   7.41
# 436     Washington     2017  11.24
# 437  West Virginia     2017   8.94
# 438      Wisconsin     2017   7.41
# 439        Wyoming     2017   5.26
#
# [440 rows x 3 columns]

print(min_wage.melt(id_vars="State", var_name="Year", value_name="Wage"))
#              State  Year   Wage
# 0          Alabama  2010   0.00
# 1           Alaska  2010   8.90
# 2          Arizona  2010   8.33
# 3         Arkansas  2010   7.18
# 4       California  2010   9.19
# ..             ...   ...    ...
# 435       Virginia  2017   7.41
# 436     Washington  2017  11.24
# 437  West Virginia  2017   8.94
# 438      Wisconsin  2017   7.41
# 439        Wyoming  2017   5.26
#
# [440 rows x 3 columns]


