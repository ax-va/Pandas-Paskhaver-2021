"""
-- Core pandas
---- The DataFrame Object
------ Dealing with Duplicates
-------- The drop_duplicates Method
"""
import pandas as pd
employees = pd.read_csv("../datasets/employees.csv", parse_dates=["Start Date"])

# All the six column values must be same to be then dropped
print(employees.drop_duplicates())
#      First Name  Gender Start Date    Salary   Mgmt          Team
# 0       Douglas    Male 1993-08-06       NaN   True     Marketing
# 1        Thomas    Male 1996-03-31   61933.0   True           NaN
# 2         Maria  Female        NaT  130590.0  False       Finance
# 3         Jerry     NaN 2005-03-04  138705.0   True       Finance
# 4         Larry    Male 1998-01-24  101004.0   True            IT
# ...         ...     ...        ...       ...    ...           ...
# 996     Phillip    Male 1984-01-31   42392.0  False       Finance
# 997     Russell    Male 2013-05-20   96914.0  False       Product
# 998       Larry    Male 2013-04-20   60500.0  False  Business Dev
# 999      Albert    Male 2012-05-15  129949.0   True         Sales
# 1000        NaN     NaN        NaT       NaN    NaN           NaN
#
# [1001 rows x 6 columns]

print(employees.drop_duplicates(subset=["Team"]))
#    First Name  Gender Start Date    Salary   Mgmt          Team
# 0     Douglas    Male 1993-08-06       NaN   True     Marketing
# 1      Thomas    Male 1996-03-31   61933.0   True           NaN
# 2       Maria  Female        NaT  130590.0  False       Finance
# 4       Larry    Male 1998-01-24  101004.0   True            IT
# 5      Dennis    Male 1987-04-18  115163.0  False         Legal
# 6        Ruby  Female 1987-08-17   65476.0   True       Product
# 8      Angela  Female 2005-11-22   95570.0   True   Engineering
# 9     Frances  Female 2002-08-08  139852.0   True  Business Dev
# 12    Brandon    Male 1980-12-01  112807.0   True            HR
# 13       Gary    Male 2008-01-27  109831.0  False         Sales
# 40    Michael    Male 2008-10-10   99283.0   True  Distribution

print(employees.drop_duplicates(subset=["Team"], keep="last"))
#      First Name  Gender Start Date    Salary   Mgmt          Team
# 988       Alice  Female 2004-10-05   47638.0  False            HR
# 989      Justin     NaN 1991-02-10   38344.0  False         Legal
# 990       Robin  Female 1987-07-24  100765.0   True            IT
# 993        Tina  Female 1997-05-15   56450.0   True   Engineering
# 994      George    Male 2013-06-21   98874.0   True     Marketing
# 995       Henry     NaN 2014-11-23  132483.0  False  Distribution
# 996     Phillip    Male 1984-01-31   42392.0  False       Finance
# 997     Russell    Male 2013-05-20   96914.0  False       Product
# 998       Larry    Male 2013-04-20   60500.0  False  Business Dev
# 999      Albert    Male 2012-05-15  129949.0   True         Sales
# 1000        NaN     NaN        NaT       NaN    NaN           NaN

# Pandas will reject a row if there are any other rows with the same value.
# In other words, these first names occur only once in the DataFrame.
print(employees.drop_duplicates(subset=["First Name"], keep=False))  # Keep nothing
#     First Name  Gender Start Date    Salary   Mgmt          Team
# 5       Dennis    Male 1987-04-18  115163.0  False         Legal
# 8       Angela  Female 2005-11-22   95570.0   True   Engineering
# 33        Jean  Female 1993-12-18  119082.0  False  Business Dev
# 190      Carol  Female 1996-03-19   57783.0  False       Finance
# 291      Tammy  Female 1984-11-11  132839.0   True            IT
# 495     Eugene    Male 1984-05-24   81077.0  False         Sales
# 688      Brian    Male 2007-04-07   93901.0   True         Legal
# 832      Keith    Male 2003-02-12  120672.0  False         Legal
# 887      David    Male 2009-12-05   92242.0  False         Legal

name_is_douglas = employees["First Name"] == "Douglas"
is_male = employees["Gender"] == "Male"
print(employees[name_is_douglas & is_male])
#     First Name Gender Start Date    Salary   Mgmt         Team
# 0      Douglas   Male 1993-08-06       NaN   True    Marketing
# 217    Douglas   Male 1999-09-03   83341.0   True           IT
# 322    Douglas   Male 2002-01-08   41428.0  False      Product
# 835    Douglas   Male 2007-08-04  132175.0  False  Engineering

# Pandas will exclude any other rows with the same two values from the results set
print(employees.drop_duplicates(subset=["Gender", "Team"]))
#     First Name  Gender Start Date    Salary   Mgmt          Team
# 0      Douglas    Male 1993-08-06       NaN   True     Marketing
# 1       Thomas    Male 1996-03-31   61933.0   True           NaN
# 2        Maria  Female        NaT  130590.0  False       Finance
# 3        Jerry     NaN 2005-03-04  138705.0   True       Finance
# 4        Larry    Male 1998-01-24  101004.0   True            IT
# 5       Dennis    Male 1987-04-18  115163.0  False         Legal
# 6         Ruby  Female 1987-08-17   65476.0   True       Product
# 8       Angela  Female 2005-11-22   95570.0   True   Engineering
# 9      Frances  Female 2002-08-08  139852.0   True  Business Dev
# 10      Louise  Female 1980-08-12   63241.0   True           NaN
# 11       Julie  Female 1997-10-26  102508.0   True         Legal
# 12     Brandon    Male 1980-12-01  112807.0   True            HR
# 13        Gary    Male 2008-01-27  109831.0  False         Sales
# 17       Shawn    Male 1986-12-07  111737.0  False       Product
# 18       Diana  Female 1981-10-23  132940.0  False            IT
# 20        Lois     NaN 1995-04-22   64714.0   True         Legal
# 22      Joshua     NaN 2012-03-08   90816.0   True            IT
# 31       Joyce     NaN 2005-02-20   88657.0  False       Product
# 35     Theresa  Female 2006-10-10   85182.0  False         Sales
# 40     Michael    Male 2008-10-10   99283.0   True  Distribution
# 41   Christine     NaN 2015-06-28   66582.0   True  Business Dev
# 43     Marilyn  Female 1980-12-07   73524.0   True     Marketing
# 46       Bruce    Male 2009-11-28  114796.0  False       Finance
# 48    Clarence    Male 1996-03-26   93581.0   True  Business Dev
# 49       Chris     NaN 1980-01-24  113590.0  False         Sales
# 60       Paula     NaN 2005-11-23   48866.0  False  Distribution
# 75      Bonnie  Female 1991-07-02  104897.0   True            HR
# 76    Margaret  Female 1988-09-10  131604.0   True  Distribution
# 91       James     NaN 2005-01-26  128771.0  False           NaN
# 97       Laura     NaN 2014-07-19  140371.0   True     Marketing
# 143     Teresa     NaN 2016-01-28  140013.0   True   Engineering
# 171    Patrick    Male 2007-08-17  143499.0   True   Engineering
# 239    Lillian     NaN 2016-05-12   64164.0  False            HR

