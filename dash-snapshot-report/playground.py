# This is a playground for testing random code.
# Cuz I am idiot, sometimes I forget about how shit works from time to time.

# Import test libraries
import pandas as pd
import pathlib
import numpy as np
import plotly.express as px
import sys

# See if pandas being imported properly
print(pd.__version__)   # 1.1.0

# get relative data folder

region_code = 5554
PATH = pathlib.Path(__file__)
DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()
print(DATA_PATH)

# print("Current directory is: ", PATH)     # Just to see if thing works
# print("Data directory is: ", DATA_PATH)     # Just to see if thing works
#
# # get the region library
# df_RegionLib = pd.read_csv(DATA_PATH.joinpath("RegionLib.csv"))
# print(df_RegionLib)
#
# row_1 = df_RegionLib.values[5554].tolist()
# print(row_1[1])
#


# df_fiscal_year = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0])
# max_length = len(df_fiscal_year)  # the max out index for the column
# # Starting index set to 1 instead of 0, since we want to remove the header name of the column.
# fiscal_year = [int(item[0]) for item in df_fiscal_year.values[1:max_length]]
#
# pop0 = [int(item[0]) for item in
#            pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
#                        usecols = [2]).values[1:max_length]]
#
# print(fiscal_year)
# print(pop0)

df_race_data = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Race.csv"))  # I am keeping the columns names


df_race_data.rename(columns={'Total number of children': 'Total',
                             'White Alone, Non Hispanic or Latino': 'White',
                             'Hispanic or Latino (of any race)': 'Hispanic',
                             'Black or African American, Non-Hispanic or Latino': 'Black',
                             'American Indian and Alaska Native, Non-Hispanic or Latino': 'American Indian',
                             'Asian, Non-Hispanic or Latino': 'Asian',
                             'Native Hawaiian and Other Pacific Islander, Non-Hispanic or Latino': 'Native Hawaiian',
                             'Other, Non-Hispanic or Latino': 'Other',
                             'Two or More Races, Non-Hispanic or Latino': 'Multiracial'
                             }, inplace=True)

# Extract the fiscal year
# This block of code is re-usable. But can't be fucked to .... Umm, what you call it, make into a module
# df_fiscal_year = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0])

# This is indeed a better way to do this, I feel like I am idiot...
fiscal_year = df_race_data['Fiscal Year'].tolist()
max_length = len(fiscal_year)  # the max out index for the column

# Pass the data in at first
df_race_data_percent = df_race_data
df_race_data_percent['White'] = round(df_race_data_percent['White']*100/df_race_data_percent['Total'], 2)
df_race_data_percent['Hispanic'] = round(df_race_data_percent['Hispanic']*100/df_race_data_percent['Total'], 2)
df_race_data_percent['Black'] = round(df_race_data_percent['Black']*100/df_race_data_percent['Total'], 2)
df_race_data_percent['American Indian'] = round(df_race_data_percent['American Indian']*100/df_race_data_percent['Total'], 2)
df_race_data_percent['Asian'] = round(df_race_data_percent['Asian']*100/df_race_data_percent['Total'], 2)
df_race_data_percent['Native Hawaiian'] = round(df_race_data_percent['Native Hawaiian']*100/df_race_data_percent['Total'], 2)
df_race_data_percent['Other'] = round(df_race_data_percent['Other']*100/df_race_data_percent['Total'], 2)
df_race_data_percent['Multiracial'] = round(df_race_data_percent['Multiracial']*100/df_race_data_percent['Total'], 2)
print(df_race_data_percent['White'])

# MAP_PATH = PATH.joinpath("../maps/"+str(region_code)).resolve()
# print("Map directory is: ", MAP_PATH)     # Just to see if thing works



# df_after_tax = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Race.csv"))
# print(df_after_tax)
# print("next")
# temp = df_after_tax.values[-1].tolist()[0:]
# print(temp)
# print(temp[2:])

# df_population = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0, 1, 2, 3])
# print(df_population)
# print("Try to fetch latest data")
# new_population = df_population.values[-1].tolist()
# print(int(new_population[2])+10000)

# df_PFA = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Prog.csv"), usecols = [0, 1, 2, 3, 4])     # This includes PFA and PFA-E
# df_HS = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Prog.csv"), usecols = [0, 5, 6, 7, 8])     # This includes Head Start and Early Head Start
# df_PI = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Prog.csv"), usecols = [0, 9, 10])     # This includes PI only
#
# new_HS = df_HS.values[-1].tolist()
# print(new_HS)


# print(df_after_tax)
# fiscal_year = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0])
# #print(fiscal_year.values[1:5])
# print(len(fiscal_year))
#
# fiscal_year_num = fiscal_year.values
#
# print(fiscal_year_num)
# df_fiscal_year = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0])
# max_length = len(df_fiscal_year)   # the max out index for the column
# fiscal_year = [int(item[0]) for item in df_fiscal_year.values[1:max_length]]
# [int(item[0]) for item in pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [1]).values[1:max_length]]
# print(max_length)
# print("what")
# # Ok, I am fucking stupid
# # x = np.array(fiscal_year_num.tolist())
# # x = x.astype(np.int)
# #x = [int(item[0]) for item in fiscal_year[1:max_length]]
# #print(x)
# #print(x[0], x[len(x)-1])
#
# print([int(item[0]) for item in pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [1]).values[1:max_length]])
#
# print("next")

# df = px.data.iris()
# print(len(df.sepal_width))
# print(len(df.sepal_length))
# print(df.species.shape)
# print(df.species)
# print(df.shape)
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
#                  size='petal_length', hover_data=['petal_width'])
# #fig.show()

