# -*- coding: utf-8 -*-
# Page ID: 0
# This is where everything started, should be treated as the top level.
# Even if the map/district selection page is added, it shall start render from here.
# Further discussion on what to do is needed!
import dash
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import pathlib
import base64
import flask

import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

# TO-DO:
# Function ID: F-0-01
# In this section, we can make decision on what pages to be rendered for this project.
# This can be useful in the future, but as for now, we only select, and list the files here.
# Later on we can just sweep the sub-folder if desires.
from pages import (
    overview,
    Demographic,
    DemographicSlave,
    LanguageFamily,
    ChildCare,
    ChildCareSlave,
    Race,
    About,
)

# Control+Option+I to indent the code

# TO-DO:
# Function ID: F-0-02
# So, at this moment, the district name is hard-coded here rather than user selection.
# Top-level soon to come!
# But also, consider a place for library or such for a quick table-lookup rather than
# the SQL table matching.
# Current solution is to use a quick lookup table.

# get relative data folder
PATH = pathlib.Path(__file__)
DATA_PATH = PATH.joinpath("../prefetched").resolve()
df_RegionLib = pd.read_csv(DATA_PATH.joinpath("RegionLib.csv"))
df_CountyLib = pd.read_csv(DATA_PATH.joinpath("CountyLib.csv"))
df_ROELib = pd.read_csv(DATA_PATH.joinpath("ROELib.csv"))

# get rid of the nan values
county_df = df_CountyLib.dropna()
region_df = df_RegionLib.dropna()
roe_df = df_ROELib.dropna()
#selection_options = ['County', 'Region', 'ROE']
selection_options = ['County', 'ROE']
county_options = []
for index, row in county_df.iterrows():
    county_options.append({'label' : row['CountyName'], 'value' : row['CountyID']})

#region_options = []
#for index, row in region_df.iterrows():
#    region_options.append({'label' : row['RegionName'], 'value' : row['RegionID']})
    
roe_options = []
for index, row in roe_df.iterrows():
    roe_options.append({'label' : row['ROEAreaName'], 'value' : row['RegionID']})

# TO-DO:
# Function ID: F-0-04
# This is a value/flag designed to toggle the menu and header items.
# By doing so, we can save space, and have custom footnote and such
# in the future as well.
view_style = 0
view_style_full = 1

server = flask.Flask(__name__)
#app.config.requests_pathname_prefix = '/SD_U-46/'
app = dash.Dash(
   name="app1", meta_tags=[{"name": "viewport", "content": "width=device-width"}], suppress_callback_exceptions=True, server=server, serve_locally=False, requests_pathname_prefix = '/dash-snapshot-report/'
)
# Now we change the name of the site as well
#app.title = region + " Community Report"
# server = app.server
# app.config.requests_pathname_prefix = '/SD_U-46/'

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content"), dcc.Store(id='selected-region')]
)

landing_layout = html.Div([
    
    html.Img(src=app.get_asset_url('IECAM_Logo.png'), height = 150),
    html.Hr(),
    html.H3('Please select the type of region first from the radio buttons, then select the particular area within the dropdown list. You can type the name in the drop down list.', style={'font-size': '20px'}),
    
    html.Hr(),

    dcc.RadioItems(
        id='selection-type-radio',
        options=[{'label': k, 'value': k} for k in selection_options],
        value=selection_options[0]
    ),

    html.Hr(),

    dcc.Dropdown(id='selection-options'),

    html.Hr(),

    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Hr(),
    
    html.Strong("Area I-A, Area I-B-C, and Area I-B-D for ROE are not available at the moment."),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P('The project was developed by IECAM at University of Illinois at Urbana-Champaign.')
])

# To get rid of the callbac lacking initial state message.
app.config['suppress_callback_exceptions'] = True

@app.callback(
    Output('selection-options', 'options'),
    [Input('selection-type-radio', 'value')])
def set_selection_options(selected_type):
    if selected_type == 'County':
        return county_options
#    elif selected_type == 'Region':
#        return region_options
    else:
        return roe_options

@app.callback([Output('url', 'pathname'),
              Output('selected-region', 'data')],
              [Input('submit-button-state', 'n_clicks')],
              [State('selection-type-radio', 'value'),
              State('selection-options', 'value')])
def update_output(n_clicks, type, selected_code):
    if n_clicks is None:
        raise PreventUpdate
    if selected_code == None or selected_code == 0:
        data = {'code':0, 'region':"none"}
        return '/dash-snapshot-report/landing', data

    if type == 'County':
        region = df_CountyLib.loc[df_CountyLib['CountyID'] == selected_code].iloc[0]['CountyName']
    #elif type == 'Region':
    #    region = df_RegionLib.loc[df_RegionLib['RegionID'] == selected_code].iloc[0]['RegionName']
    elif type == 'ROE':
        region = df_ROELib.loc[df_ROELib['RegionID'] == selected_code].iloc[0]['ROEAreaName']
    
    #encode the region code and region and store it
    data = {'code':selected_code, 'region':region}
    return '/dash-snapshot-report/overview', data
 
# Update page
@app.callback(Output("page-content", "children"), 
            [Input("url", "pathname")],
            [State("selected-region", "data")])
def display_page(pathname, data):
    if data == None:
        region_code = 0
        region = "None"
    else:
        region_code = data['code']
        region = data['region']

    if pathname == "/dash-snapshot-report/demographic":
        return (
            Demographic.create_layout(app, region, region_code, view_style),
            DemographicSlave.create_layout(app, region, region_code, view_style),
        )
    elif pathname == "/dash-snapshot-report/language-family":
        return LanguageFamily.create_layout(app, region, region_code, view_style)
    elif pathname == "/dash-snapshot-report/child-care":
        return (
            ChildCare.create_layout(app, region, region_code, view_style),
            ChildCareSlave.create_layout(app, region, region_code, view_style),
        )
    elif pathname == "/dash-snapshot-report/race":
        return Race.create_layout(app, region, region_code, view_style)
    elif pathname == "/dash-snapshot-report/about":
        return About.create_layout(app, region, region_code, view_style)
    elif pathname == "/dash-snapshot-report/full-view":
        return (
            # This is where you create all the rendering for the page.
            # Also, when generating the full view, it controls the order of which
            overview.create_layout(app, region, region_code, view_style_full),
            ChildCare.create_layout(app, region, region_code, view_style_full),
            ChildCareSlave.create_layout(app, region, region_code, view_style_full),
            Demographic.create_layout(app, region, region_code, view_style_full),
            DemographicSlave.create_layout(app, region, region_code, view_style_full),
            LanguageFamily.create_layout(app, region, region_code, view_style_full),
            Race.create_layout(app, region, region_code, view_style_full),
            About.create_layout(app, region, region_code, view_style_full),
        )
    elif pathname == "/dash-snapshot-report/overview":
        return overview.create_layout(app, region, region_code, view_style)
    else:
        # TO-DO:
        # Function ID: F-0-05
        # Change the top level applet page in order to grant users with the abilities to
        # select the district/regions which they desire.
        # Currently, it is directed to the front page of the report.
        return landing_layout


Demographic.dropdownFPLTableTrigger(app)
DemographicSlave.dropdownImageTrigger(app)

Race.TabTableTrigger(app)
Race.TabGraphTrigger(app)
# dcc.Store(id='localTest', storage_type='session')
# overview.buttonTest(app)
#Demographic.dropdownFPLTableTrigger(app)
#DemographicSlave.dropdownImageTrigger(app)
#Race.TabTableTrigger(app, region_code)
#Race.TabGraphTrigger(app, region_code)
#
# # output the stored clicks in the table cell.
# @app.callback(Output('testP', 'children'),
#             # Since we use the data prop in an output,
#             # we cannot get the initial data on load with the data prop.
#             # To counter this, you can use the modified_timestamp
#             # as Input and the data as State.
#             # This limitation is due to the initial None callbacks
#             # https://github.com/plotly/dash-renderer/pull/81
#             [Input("url", "pathname")]
#             )
# def on_data(pathname):
#     global testG
#     print("HIIIIIIIIIIIIIIIIIIIIIIIIIIII", testG)
#     return "ddd" # data['value']

# if __name__ == "__main__":
#     app.run_server(debug=True)

# def application(environ, start_response):
#     app.run_server(debug=True)
#     return



