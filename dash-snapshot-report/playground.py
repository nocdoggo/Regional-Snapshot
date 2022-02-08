# This is a playground for testing random code.
# Cuz I am idiot, sometimes I forget about how shit works from time to time.

# Import test libraries
import pandas as pd
import pathlib
import numpy as np
import plotly.express as px
import sys


import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import base64

# See if pandas being imported properly
print(pd.__version__)   # 1.1.0
region_code = 17001
# get relative data folder
PATH = pathlib.Path(__file__)
DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()

MAP_PATH = PATH.joinpath("../maps/" + str(region_code)).resolve()

site_image = MAP_PATH.joinpath("site_map.png")
# site_base64 = base64.b64encode(open(site_image, 'rb').read()).decode('ascii')

# Load data

# TO-DO:
# Function ID: F-D-01
# So, basically data is pre-cached to add proper column names and such.
# A separated package needs to add on top of this to pull data from the
# database. This also gives the ground for us if the database is broken
# for whatever reason?

df_MIECHV = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_HV.csv"), usecols=[0, 4])  # This includes PFA and PFA-E
df_HSHV = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_HV.csv"),
                      usecols=[0, 2, 3])  # This includes Head Start and Early Head Start
df_PIHV = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_HV.csv"), usecols=[0, 1])  # This includes PI only
df_HFI = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_HV.csv"), usecols=[0, 5])  # This includes HFI only
df_PTS = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_HV.csv"),
                     usecols=[0, 6])  # This includes Parent too soon only
df_ALL = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_HV.csv"),
                     usecols=[0, 1, 2, 3, 4, 5, 6, 7])  # This includes all data

# Extract the fiscal year
df_fiscal_year = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Prog.csv"), usecols=[0])
max_length = len(df_fiscal_year)  # the max out index for the column
df_ALL.at[0, '1'] = 'ISBE Prevention Initiative (PI)'
df_ALL.at[0, '2'] = 'Head Start (HS)'
df_ALL.at[0, '3'] = 'Early Head Start (EHS)'
df_ALL.at[0, '4'] = 'IDHS Maternal Infant and Early Childhood Home Visiting (MIECHV)'
df_ALL.at[0, '5'] = 'IDHS Healthy Families Illinois (HFI)'
df_ALL.at[0, '6'] = 'IDHS Parents Too Soon (PTS)'

print(df_ALL)