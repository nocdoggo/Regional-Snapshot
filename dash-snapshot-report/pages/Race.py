# Page ID: E
# This page we focus on the centers and such, there is a map created soon!
# Layout of the page subjects to changes.

import dash
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# Import some libraries just for the plot. Can be turned off in other pages to reduce
# render time.
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Add @App.CallBack support
def TabGraphTrigger(app):
    @app.callback(Output('Main-Sub-Graph', 'children'),
                  [Input('Main-Sub-Toggle', 'value')],
                  [State("selected-region", "data")])
    def render_content(tab, data):
        if data == None:
            raise PreventUpdate
        else:
            region_code = data['code']
            
        PATH = pathlib.Path(__file__).parent
        DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()
        df_race_data = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Race.csv"))  # I am keeping the columns names

        df_race_state = pd.read_csv(
            PATH.joinpath("../prefetched/" + "Race_Ethnicity_IL_2015-2018.csv"))  # What is this for?

        df_race_data.rename(columns={'White Alone, Non Hispanic or Latino': 'White',
                                     'Hispanic or Latino (of any race)': 'Hispanic',
                                     'Black or African American, Non-Hispanic or Latino': 'Black',
                                     'American Indian and Alaska Native, Non-Hispanic or Latino': 'American Indian',
                                     'Asian, Non-Hispanic or Latino': 'Asian',
                                     'Two or More Races, Non-Hispanic or Latino': 'Multiracial',
                                     'Other, Non-Hispanic or Latino': 'Other',
                                     }, inplace=True)

        # This is indeed a better way to do this, I feel like I am idiot...
        fiscal_year = df_race_data['Fiscal Year'].tolist()
        max_length = len(fiscal_year)  # the max out index for the column

        if tab == 'tab-1':
            return html.Div(
                [
                    html.Br([]),
                    dcc.Graph(
                        id="graph-6",
                        figure={
                            "data": [go.Bar(
                                x=fiscal_year,
                                # This shit is hard coded to hell
                                y=df_race_data['White'].div(
                                    df_race_data['Total number of children'].values, axis=0),
                                # line={"color": "#97151c"},
                                # mode="markers+lines",
                                marker=dict(color='#1f77b4'),  # set color bar to Gold
                                name="White",
                            ),
                                go.Bar(
                                    x=fiscal_year,
                                    y=df_race_data['Black'].div(
                                        df_race_data['Total number of children'].values, axis=0),
                                    marker={"color": "#ff7f0e"},
                                    name="Black",
                                ),
                                go.Bar(
                                    x=fiscal_year,
                                    y=df_race_data['Hispanic'].div(
                                        df_race_data['Total number of children'].values, axis=0),
                                    marker={"color": "#7f7f7f"},
                                    name="Hispanic",
                                ),
                                go.Bar(
                                    x=fiscal_year,
                                    y=df_race_data['Asian'].div(
                                        df_race_data['Total number of children'].values, axis=0),
                                    marker={"color": "#bcbd22"},
                                    name="Asian"
                                ),
                                go.Bar(
                                    x=fiscal_year,
                                    y=df_race_data['Multiracial'].div(
                                        df_race_data['Total number of children'].values, axis=0),
                                    marker={"color": "#8c564b"},
                                    name="Multiracial"
                                )],

                            # layout = [go.Layout(
                            #                    title = 'Race Ethnicity',

                            #        )]
                            "layout": go.Layout(
                                autosize=True,
                                title='<b>Distribution of Race/Ethnicity per Year</b>',
                                font={"family": "Arial", "size": 10},
                                height=300,
                                width=540,
                                bargap=0.4,
                                barmode="stack",
                                hovermode="closest",
                                legend={
                                    "x": 0.2377108433735,
                                    "y": -0.142606516291,
                                    "orientation": "h",
                                },
                                margin={
                                    "r": 20,
                                    "t": 20,
                                    "b": 20,
                                    "l": 50,
                                },
                                showlegend=True,
                                xaxis={
                                    "autorange": True,
                                    "linecolor": "rgb(0, 0, 0)",
                                    "linewidth": 1,
                                    # It is -2 here cuz there is a stupid header row
                                    # Otherwise it should be -1 since the index starts with 0
                                    # Therefore, don't waste 10 minutes like me trying to figure
                                    # this shit out...
                                    "range": [df_race_state['Fiscal Year'].min(),
                                              df_race_state['Fiscal Year'].max()],
                                    "showgrid": False,
                                    "showline": True,
                                    # I mean. Everyone knows it is year.
                                    # "title": "Fiscal Year",
                                    "type": "linear",
                                },
                                yaxis={
                                    "autorange": True,
                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                    "mirror": False,
                                    # The following controls how many side legends you want.
                                    "nticks": 5,

                                    # TO-DO:
                                    # Function ID: F-E-02
                                    # As for now, the range is hard coded since I can't be fucked.
                                    # So, sorry, let's just use this thing for now!
                                    # In the future, the range should be calculated accordingly.
                                    # Lower bound =  min_val -500
                                    # Upper bound = max_val + 500
                                    #"range": [0, 1],
                                    "showgrid": True,
                                    "showline": True,
                                    "ticklen": 10,

                                    "ticks": "outside",
                                    "tickformat": ".0%",
                                    "title": "Children",
                                    "type": "linear",
                                    "zeroline": False,
                                    "zerolinewidth": 4
                                },
                            ),
                        },
                        className=" twelve columns",
                        config=dict({"displayModeBar": False, 'scrollZoom': True}),

                    ),
                ],style = {'margin':'auto','width': 'auto'},
            ),
        elif tab == 'tab-2':
            return html.Div(
                [
                    html.Br([]),
                    dcc.Graph(
                        id="graph-7",
                        # colors for Ethnicity were taken from the following link:
                        # https://blog.datawrapper.de/ethnicitycolors/

                        figure={
                            # bar plot for raw data
                            "data": [
                                go.Bar(
                                    x=fiscal_year,
                                    y=df_race_data['Multiracial'],
                                    marker={"color": '#3AFF11'},  # set color to green
                                    name="Two or More Races, non-Hispanic"
                                ),
                                go.Bar(
                                    x=fiscal_year,
                                    y=df_race_data['American Indian'],
                                    marker={"color": '#C0C3C0'},  # set color to grey
                                    name="Other, non-Hispanic"
                                ),
                                go.Bar(
                                    x=fiscal_year,
                                    y=df_race_data['Other'],
                                    marker={"color": '#9E3ECE'},  # set color to purple
                                    name="American Indian and Alaska Native"
                                ),
                            ],

                            # layout = [go.Layout(
                            #                    title = 'Race Ethnicity',

                            #        )]
                            "layout": go.Layout(
                                autosize=True,
                                title="Distribution of Race/Ethnicity per Year",
                                font={"family": "Raleway", "size": 10},
                                height=300,
                                width=540,
                                bargap=0.2,
                                barmode="group",
                                hovermode="closest",
                                legend={

                                    #    "x": 0.2377108433735,
                                    #    "y": -0.142606516291,
                                    "orientation": "h",
                                },
                                margin={
                                    "r": 20,
                                    "t": 20,
                                    "b": 20,
                                    "l": 50,
                                },
                                showlegend=True,
                                xaxis={
                                    "autorange": True,
                                    "linecolor": "rgb(0, 0, 0)",
                                    "linewidth": 1,
                                    # It is -2 here cuz there is a stupid header row
                                    # Otherwise it should be -1 since the index starts with 0
                                    # Therefore, don't waste 10 minutes like me trying to figure
                                    # this shit out...
                                    "range": [df_race_data['Fiscal Year'].min(),
                                              df_race_data['Fiscal Year'].max()],
                                    "showgrid": False,
                                    "showline": True,
                                    # I mean. Everyone knows it is year.
                                    # "title": "Fiscal Year",
                                    "type": "linear",
                                },
                                yaxis={
                                    "autorange": True,
                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                    "mirror": False,
                                    # The following controls how many side legends you want.
                                    "nticks": 5,

                                    # TO-DO:
                                    # Function ID: F-E-02
                                    # As for now, the range is hard coded since I can't be fucked.
                                    # So, sorry, let's just use this thing for now!
                                    # In the future, the range should be calculated accordingly.
                                    # Lower bound =  min_val -500
                                    # Upper bound = max_val + 500
                                    # "range": [0, df_race_data['White'].max()],
                                    "showgrid": True,
                                    "showline": True,
                                    "ticklen": 10,

                                    "ticks": "outside",
                                    # "tickformat":".0%",
                                    "title": "Number of Children",
                                    "type": "linear",
                                    "zeroline": False,
                                    "zerolinewidth": 4
                                },
                            ),
                        },

                        # figure = df_race_plot(df_race_data, race_type='all'),

                        className=" twelve columns",
                        config=dict({"displayModeBar": False, 'scrollZoom': True}),

                    ),
                ],style = {'margin':'auto','width': "85%"},
            ),




def TabTableTrigger(app):
    @app.callback(Output('Num-Percent-Table', 'children'),
                  [Input('Num-Percent-Toggle', 'value')],
                  [State("selected-region", "data")])
    def render_content(tab, data):
        if data == None:
            raise PreventUpdate
        else:
            region_code = data['code']
            
        PATH = pathlib.Path(__file__).parent
        DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()

        # TO-DO:
        # Function ID: F-E-01
        # So, basically data is pre-cached to add proper column names and such.
        # A separated package needs to add on top of this to pull data from the
        # database. This also gives the ground for us if the database is broken
        # for whatever reason?
        # df_Language = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0, 23, 24])
        # df_Family = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0, 25, 26, 27, 28])
        # df_Race = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Race.csv"), usecols = [0, 2, 3, 4, 5, 6, 7, 8, 9])    # Skipping the total number for now

        df_race_data = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Race.csv"))  # I am keeping the columns names
        df_race_data_percent = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Race.csv"))

        df_race_state = pd.read_csv(
            PATH.joinpath("../prefetched/" + "Race_Ethnicity_IL_2015-2018.csv"))  # What is this for?

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

        df_race_data_percent.rename(columns={'Total number of children': 'Total',
                                     'White Alone, Non Hispanic or Latino': 'White',
                                     'Hispanic or Latino (of any race)': 'Hispanic',
                                     'Black or African American, Non-Hispanic or Latino': 'Black',
                                     'American Indian and Alaska Native, Non-Hispanic or Latino': 'American Indian',
                                     'Asian, Non-Hispanic or Latino': 'Asian',
                                     'Native Hawaiian and Other Pacific Islander, Non-Hispanic or Latino': 'Native Hawaiian',
                                     'Other, Non-Hispanic or Latino': 'Other',
                                     'Two or More Races, Non-Hispanic or Latino': 'Multiracial'
                                     }, inplace=True)

        # Pass the data in at first
        # df_race_data_percent['Total'] = round(df_race_data_percent['Total'] * 100 / df_race_data_percent['Total'], 2)
        df_race_data_percent['White'] = round(df_race_data_percent['White'] * 100 / df_race_data_percent['Total'], 2)
        df_race_data_percent['Hispanic'] = round(df_race_data_percent['Hispanic'] * 100 / df_race_data_percent['Total'],
                                                 2)
        df_race_data_percent['Black'] = round(df_race_data_percent['Black'] * 100 / df_race_data_percent['Total'], 2)
        df_race_data_percent['American Indian'] = round(
            df_race_data_percent['American Indian'] * 100 / df_race_data_percent['Total'], 2)
        df_race_data_percent['Asian'] = round(df_race_data_percent['Asian'] * 100 / df_race_data_percent['Total'], 2)
        df_race_data_percent['Native Hawaiian'] = round(
            df_race_data_percent['Native Hawaiian'] * 100 / df_race_data_percent['Total'], 2)
        df_race_data_percent['Other'] = round(df_race_data_percent['Other'] * 100 / df_race_data_percent['Total'], 2)
        df_race_data_percent['Multiracial'] = round(
            df_race_data_percent['Multiracial'] * 100 / df_race_data_percent['Total'], 2)
        # df_race_data_percent['Total'] = round(df_race_data_percent['Total'] * 100 / df_race_data_percent['Total'], 2)

        # Extract the fiscal year
        # This block of code is re-usable. But can't be fucked to .... Umm, what you call it, make into a module
        # df_fiscal_year = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0])

        # This is indeed a better way to do this, I feel like I am idiot...
        fiscal_year = df_race_data['Fiscal Year'].tolist()
        max_length = len(fiscal_year)  # the max out index for the column
        # Starting index set to 1 instead of 0, since we want to remove the header name of the column.
        # fiscal_year = [int(item[0]) for item in df_fiscal_year.values[1:max_length]]

        ##########################################################################################################

        if tab == 'tab-1':
            return html.Div(
                [
                    html.Table(
                                    [
                                        html.Tr([html.Th("Fiscal Year"), html.Th("Total number of children"),
                                                 html.Th("White, Non-Hispanic"), html.Th("Hispanic or Latino"),
                                                 html.Th("Black, Non Hispanic"),
                                                 html.Th("American Indian and Alaska Native, Non-Hispanic"),
                                                 html.Th("Asian, Non-Hispanic"),
                                                 html.Th("Native Hawaiian and Other Pacific Islander, Non-Hispanic"),
                                                 html.Th("Other, Non-Hispanic"), html.Th("Two or More Races, Non-Hispanic")
                                                 ])
                                    ] +
                                    make_dash_table(df_race_data),
                                    # So for the fuck sake, text align and filled color doesn't work.
                                    # Guess we can only change .css?

                                    # style={
                                    # # "background-color": "#ffffff",
                                    # }
                                ),
                    html.Div(
                        [

                                       dcc.Graph(
                                           id="graph-6",
                                           figure={
                                               "data": [go.Bar(
                                                   x=fiscal_year,
                                                   # This shit is hard coded to hell
                                                   y=df_race_data['White'],
                                                   # line={"color": "#97151c"},
                                                   # mode="markers+lines",
                                                   marker=dict(color='#1f77b4'),  # set color bar to Gold
                                                   name="White",
                                               ),
                                                   go.Bar(
                                                       x=fiscal_year,
                                                       y=df_race_data['Black'],
                                                       marker={"color": "#ff7f0e"},
                                                       name="Black",
                                                   ),
                                                   go.Bar(
                                                       x=fiscal_year,
                                                       y=df_race_data['Hispanic'],
                                                       marker={"color": "#7f7f7f"},
                                                       name="Hispanic",
                                                   ),
                                                   go.Bar(
                                                       x=fiscal_year,
                                                       y=df_race_data['Asian'],
                                                       marker={"color": "#bcbd22"},
                                                       name="Asian"
                                                   ),
                                                   go.Bar(
                                                       x=fiscal_year,
                                                       y=df_race_data['Multiracial'],
                                                       marker={"color": "#8c564b"},
                                                       name="Multiracial"
                                                   )],

                                               "layout": go.Layout(
                                                   autosize=True,
                                                   title="Distribution of Race/Ethnicity per Year",
                                                   font={"family": "Raleway", "size": 10},
                                                   height=300,
                                                   width=540,
                                                   bargap=0.4,
                                                   barmode="stack",
                                                   hovermode="closest",
                                                   legend={
                                                       "y": -0.142606516291,
                                                       "orientation": "h",
                                                   },
                                                   margin={
                                                       "r": 20,
                                                       "t": 20,
                                                       "b": 20,
                                                       "l": 50,
                                                   },
                                                   showlegend=True,
                                                   xaxis={
                                                       "autorange": True,
                                                       "linecolor": "rgb(0, 0, 0)",
                                                       "linewidth": 1,
                                                       # It is -2 here cuz there is a stupid header row
                                                       # Otherwise it should be -1 since the index starts with 0
                                                       # Therefore, don't waste 10 minutes like me trying to figure
                                                       # this shit out...
                                                       "range": [df_race_state['Fiscal Year'].min(),
                                                                 df_race_state['Fiscal Year'].max()],
                                                       "showgrid": False,
                                                       "showline": True,
                                                       # I mean. Everyone knows it is year.
                                                       # "title": "Fiscal Year",
                                                       "type": "linear",
                                                   },
                                                   yaxis={
                                                       "autorange": True,
                                                       "gridcolor": "rgba(127, 127, 127, 0.2)",
                                                       "mirror": False,
                                                       # The following controls how many side legends you want.
                                                       "nticks": 5,

                                                       # TO-DO:
                                                       # Function ID: F-E-02
                                                       # As for now, the range is hard coded since I can't be fucked.
                                                       # So, sorry, let's just use this thing for now!
                                                       # In the future, the range should be calculated accordingly.
                                                       # Lower bound =  min_val -500
                                                       # Upper bound = max_val + 500
                                                       #"range": [0, 6250],
                                                       "showgrid": True,
                                                       "showline": True,
                                                       "ticklen": 10,

                                                       "ticks": "outside",
                                                       "title": "Children",
                                                       "type": "linear",
                                                       "zeroline": False,
                                                       "zerolinewidth": 4
                                                   },
                                               ),
                                           },style = {'margin': 'auto', 'width': "75%"},
                                           className=" twelve columns",
                                           config=dict({"displayModeBar": False, 'scrollZoom': True}),


                                       ),
                            ],style = {'margin': 'auto', 'width': "75%"},
                    ),
                    ],
            ),
        elif tab == 'tab-2':
            return html.Div(
                [
                    html.Table(
                    [
                        html.Tr([html.Th("Fiscal Year"), html.Th("Total number of children"),
                                 html.Th("White, Non-Hispanic (%)"), html.Th("Hispanic or Latino (%)"),
                                 html.Th("Black, Non Hispanic (%)"),
                                 html.Th("American Indian and Alaska Native, Non-Hispanic (%)"),
                                 html.Th("Asian, Non-Hispanic (%)"),
                                 html.Th("Native Hawaiian and Other Pacific Islander, Non-Hispanic (%)"),
                                 html.Th("Other, Non-Hispanic (%)"), html.Th("Two or More Races, Non-Hispanic (%)")
                                 ]),
                    ] +
                    make_dash_table(df_race_data_percent),
                    # So for the fuck sake, text align and filled color doesn't work.
                    # Guess we can only change .css?

                    # style={
                    # # "background-color": "#ffffff",
                    # }
                ),
                    html.Div(
                        [

                            dcc.Graph(
                                id="graph-6",
                                figure={
                                    "data": [go.Bar(
                                        x=fiscal_year,
                                        # This shit is hard coded to hell
                                        y=df_race_data['White'].div(
                                            df_race_data['Total'].values, axis=0),
                                        # line={"color": "#97151c"},
                                        # mode="markers+lines",
                                        marker=dict(color='#1f77b4'),  # set color bar to Gold
                                        name="White",
                                    ),
                                        go.Bar(
                                            x=fiscal_year,
                                            y=df_race_data['Black'].div(
                                                df_race_data['Total'].values, axis=0),
                                            marker={"color": "#ff7f0e"},
                                            name="Black",
                                        ),
                                        go.Bar(
                                            x=fiscal_year,
                                            y=df_race_data['Hispanic'].div(
                                                df_race_data['Total'].values, axis=0),
                                            marker={"color": "#7f7f7f"},
                                            name="Hispanic",
                                        ),
                                        go.Bar(
                                            x=fiscal_year,
                                            y=df_race_data['Asian'].div(
                                                df_race_data['Total'].values, axis=0),
                                            marker={"color": "#bcbd22"},
                                            name="Asian"
                                        ),
                                        go.Bar(
                                            x=fiscal_year,
                                            y=df_race_data['Multiracial'].div(
                                                df_race_data['Total'].values, axis=0),
                                            marker={"color": "#8c564b"},
                                            name="Multiracial"
                                        )],

                                    "layout": go.Layout(
                                        autosize=True,
                                        title="Distribution of Race/Ethnicity per Year",
                                        font={"family": "Raleway", "size": 10},
                                        height=300,
                                        width=540,
                                        bargap=0.4,
                                        barmode="stack",
                                        hovermode="closest",
                                        legend={
                                            "y": -0.142606516291,
                                            "orientation": "h",
                                        },
                                        margin={
                                            "r": 20,
                                            "t": 20,
                                            "b": 20,
                                            "l": 50,
                                        },
                                        showlegend=True,
                                        xaxis={
                                            "autorange": True,
                                            "linecolor": "rgb(0, 0, 0)",
                                            "linewidth": 1,
                                            # It is -2 here cuz there is a stupid header row
                                            # Otherwise it should be -1 since the index starts with 0
                                            # Therefore, don't waste 10 minutes like me trying to figure
                                            # this shit out...
                                            "range": [df_race_state['Fiscal Year'].min(),
                                                      df_race_state['Fiscal Year'].max()],
                                            "showgrid": False,
                                            "showline": True,
                                            # I mean. Everyone knows it is year.
                                            # "title": "Fiscal Year",
                                            "type": "linear",
                                        },
                                        yaxis={
                                            "autorange": True,
                                            "gridcolor": "rgba(127, 127, 127, 0.2)",
                                            "mirror": False,
                                            # The following controls how many side legends you want.
                                            "nticks": 5,

                                            # TO-DO:
                                            # Function ID: F-E-02
                                            # As for now, the range is hard coded since I can't be fucked.
                                            # So, sorry, let's just use this thing for now!
                                            # In the future, the range should be calculated accordingly.
                                            # Lower bound =  min_val -500
                                            # Upper bound = max_val + 500
                                            #"range": [0, 1],
                                            "showgrid": True,
                                            "showline": True,
                                            "ticklen": 10,

                                            "ticks": "outside",
                                            "tickformat": ".0%",
                                            "title": "Children",
                                            "type": "linear",
                                            "zeroline": False,
                                            "zerolinewidth": 4
                                        },
                                    ),
                                }, style={'margin': 'auto', 'width': "75%"},
                                className=" twelve columns",
                                config=dict({"displayModeBar": False, 'scrollZoom': True}),

                            ),
                        ], style={'margin': 'auto', 'width': "75%"},
                    ),
                ],
            ),




"""
#I like the idea of creating this procedure.
#I'll work on it whan I get back.

def race_plot(df_Race, region):

    # Create the default labels, since the csv is comma-separated, so it is hard to retain its original format.
    # Hence, this part is hard coded.
    labels = ["White, Non-Hispanic", "Hispanic or Latino", "Black, Non Hispanic", "American Indian and Alaska Native, Non-Hispanic", "Asian, Non-Hispanic", "Native Hawaiian and Other Pacific Islander, Non-Hispanic", "Other, Non-Hispanic", "Two or More Races, Non-Hispanic"]
    #labels = [1, 2, 3, 4, 5, 6, 7, 8]

    # Extract the latest 2 years' data out
    FY_A = df_Race.values[-2].tolist()
    FY_B = df_Race.values[-1].tolist()

    # Extract out the year number first
    fiscal_year_A = FY_A[0]
    fiscal_year_B = FY_B[0]

    # Create subplots: use 'domain' type for Pie subplot
    #fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=labels, values=FY_B[2:], name = "Percentage"))

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.35, hoverinfo="label+percent+name")

    fig.update_layout(
        autosize = True,
        height = 650,
        #title_text="Race at "+region,
    legend = dict( orientation = "v", font=dict(size = 10)),
    )

        # Add annotations in the center of the donut pies.
        #annotations=[dict(text=str(fis), x=0.82, y=0.5, font_size=20, showarrow=False)])


    return fig
"""

def create_layout(app, region, region_code, view_style):


    ##########################################################################################################
    pageID = 6

    # get relative data folder
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()

    # TO-DO:
    # Function ID: F-E-01
    # So, basically data is pre-cached to add proper column names and such.
    # A separated package needs to add on top of this to pull data from the
    # database. This also gives the ground for us if the database is broken
    # for whatever reason?
    # df_Language = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0, 23, 24])
    # df_Family = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0, 25, 26, 27, 28])
    # df_Race = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Race.csv"), usecols = [0, 2, 3, 4, 5, 6, 7, 8, 9])    # Skipping the total number for now

    df_race_data = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Race.csv"))  # I am keeping the columns names

    df_race_state = pd.read_csv(PATH.joinpath("../prefetched/" + "Race_Ethnicity_IL_2015-2018.csv")) # What is this for?

    df_race_data.rename(columns={'White Alone, Non Hispanic or Latino': 'White',
                                 'Hispanic or Latino (of any race)': 'Hispanic',
                                 'Black or African American, Non-Hispanic or Latino': 'Black',
                                 'American Indian and Alaska Native, Non-Hispanic or Latino': 'American Indian',
                                 'Asian, Non-Hispanic or Latino': 'Asian',
                                 'Two or More Races, Non-Hispanic or Latino': 'Multiracial',
                                 'Other, Non-Hispanic or Latino': 'Other',
                                 }, inplace=True)

    # Extract the fiscal year
    # This block of code is re-usable. But can't be fucked to .... Umm, what you call it, make into a module
    # df_fiscal_year = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Demo.csv"), usecols = [0])

    # This is indeed a better way to do this, I feel like I am idiot...
    fiscal_year = df_race_data['Fiscal Year'].tolist()
    max_length = len(fiscal_year)  # the max out index for the column
    # Starting index set to 1 instead of 0, since we want to remove the header name of the column.
    # fiscal_year = [int(item[0]) for item in df_fiscal_year.values[1:max_length]]

    ##########################################################################################################



    return html.Div(
        [
            Header(app, region, view_style, pageID),
            # page 3
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            # TO-DO:
                            # Box ID: T-E-01
                            # Not sure what we want here, maybe we need some more detailed stuff?
                            # Maybe some disclaimer stuff? Since it is a part of the demographic
                            # data, so I am not sure in this case.

                            # html.H6(["Introduction"], className="subtitle padded"),
                            html.P(

                                # TO-DO:
                                # Box ID: T-E-02
                                # I am not sure what is the best way to describe the data here.
                                # The description on the quick data report page doesn't make
                                # too much sense to me.

                                "\
                                Population numbers are provided for the total number of children under age 5, \
                                and for the number of children under age 5 who are categorized as below.",
                                style={"color": "#000000"},
                                className="row",
                            ),
                        ],

                    ),

                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        html.Strong(["Race/Ethnicity at ", region]), className="subtitle padded"
                                    ),

                                    # TO-DO:
                                    # Table ID: B-E-01
                                    # Cuz I am a lazy fuck want something real fast to be done.
                                    # Sooooo, I didn't use the plotly's dash make table.
                                    # Instead, I use the html.Table.
                                    # Pros: 1. Shit is lightening ass fast to render, instant, period.
                                    #          This is way faster than needing the dash and plotly package
                                    #          to run in the background. There are a couple milliseconds'
                                    #          delay.
                                    #       2. Lazy, can't go wrong or trigger error.
                                    #          It is just pouring an Excel file there, what could go wrong?
                                    #          Maybe you forgot to import the file?
                                    # Cons: 1. No style, period.
                                    #          Well, plotly is funny, you'd assume that the html based style
                                    #          tags will work right? Hecc, no!
                                    #       2. No sorting and other fancy operations.
                                    #          You, just can't... It is as miserable as our life in 2020...
                                    #       3. Isn't that enough cons?

                                    dcc.Tabs(id='Num-Percent-Toggle', value='tab-1', children=[
                                        dcc.Tab(label='Number', value='tab-1'),
                                        dcc.Tab(label='Percent', value='tab-2'),
                                    ]),
                                    html.Div(id='Num-Percent-Table'),

                                    # html.Table(
                                    #     [
                                    #     html.Tr([html.Th("Fiscal Year"), html.Th("Total number of children"),
                                    #             html.Th("White, Non-Hispanic"), html.Th("Hispanic or Latino"),
                                    #             html.Th("Black, Non Hispanic"), html.Th("American Indian and Alaska Native, Non-Hispanic"),
                                    #             html.Th("Asian, Non-Hispanic"), html.Th("Native Hawaiian and Other Pacific Islander, Non-Hispanic"),
                                    #             html.Th("Other, Non-Hispanic"), html.Th("Two or More Races, Non-Hispanic")
                                    #             ])
                                    #     ] +
                                    #     make_dash_table(df_race_data),
                                    #     # So for the fuck sake, text align and filled color doesn't work.
                                    #     # Guess we can only change .css?
                                    #
                                    #     # style={
                                    #     # # "background-color": "#ffffff",
                                    #     # }
                                    # ),

                                ],
                                className=" twelve columns",
                            ),

                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Br([]),
                    html.Div(
                        [

                            # TO-DO:
                            # Graph ID: G-E-02
                            # This one is for the working family thing. But to be honest, I don't think either line or
                            # bar plots are the correct thing to do. Honestly, what I have in mind is something like
                            # for circles, aka, using the plotly.shape thing. For more information, go visit here :
                            # https://plotly.com/python/shapes/
                            # Since I am an imbecile, I don't wanna crash the existing layout. So after the first
                            # stable release, I'd go figure this out again in later on?

                            # dcc.Tabs(id='Main-Sub-Toggle', value='tab-1', children=[
                            #     dcc.Tab(label='Ethnicity Distribution Outlook', value='tab-1'),
                            #     dcc.Tab(label='Multiracial Distribution Outlook', value='tab-2'),
                            # ]),
                            # html.Div(id='Main-Sub-Graph'),

                        ],
                    ),
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        html.Strong(["Footnote"]),
                                        className="subtitle padded",
                                    ),

                                ],
                                className=" twelve columns",
                            ),

                            html.Div(
                                [

                                    html.P(
                                        "IECAM demographers prepared this data based on Census Bureau estimates from the Population Estimates Program and the American Community Survey (5 year).",
                                    ),

                                    # html.Li(
                                    #     "Population Estimates Program",
                                    # ),

                                    # html.Li(
                                    #     "American Community Survey, 5-year estimate",
                                    # )

                                ],
                                className=" twelve columns"
                            ),
                        ],
                        className="row ",
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
