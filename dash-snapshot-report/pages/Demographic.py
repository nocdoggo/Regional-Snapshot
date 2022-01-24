# Page ID: B
# The 2nd tab. That's it.

from dash_table import DataTable, FormatTemplate
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import plotly.express as px     # Only need when you toggle to use the external plotting, see below.
import numpy as np  # Fuck it, you do need it since Python doesn't work like C and Matlab.
import base64

###################################################################################
# Plot the population
# df = pd.DataFrame({
#     "x": fiscal_year,
#     "y": [1,2,3,4],
#     "customdata": [1,2,3,4],
#     "fruit": ["apple", "apple", "orange", "orange"]
# })
#
# fig = px.scatter(df, x="x", y="y", color="fruit", custom_data=["customdata"])
#
# LAYOUT = {'width': 250,
#           'plot_bgcolor': 'white',
#           'paper_bgcolor': 'white'}
#
# fig['layout'].update(LAYOUT)
#
# fig.update_layout(clickmode='event+select')
#
# fig.update_traces(marker_size=20)
#######################################################################################
# The script above is just another way to generate the plot separately without the    #
# weird, annoying HTML tags. It gives more power as well.                             #
# However, we do lose the way, the direct figure scaling from the web page.           #
# Why? since you scale the figure when you create it, but when you put into the web   #
# page, it got rescaled again. Any tiny resolution ratio difference will just stretch #
# the final image on the web page to something really weird.                          #
# As for now, the plotly has a open request for the feature, but it has been 2 years. #
# Sooooo, I guess we should take it as a no?                                          #
#######################################################################################


def dropdownFPLTableTrigger(app):
    @app.callback(
        Output('FPL-table', 'columns'),
        [Input('FPL-dropdown', 'value')],
        [State('FPL-table', 'columns')]
    )
    def update_columns(value, columns):
        #print("AAAAAAAAAAAAAAAAAAAAAAAAA")
        if value is None or columns is None:
            raise PreventUpdate

        inColumns = any(c.get('id') == value for c in columns)

        if inColumns == True:
            raise PreventUpdate
        
        # print(inColumns, "\n\t",value, "\n\t", columns)
        if value != []:
            for x in value:
                doNotAdd = False
                for y in columns:
                    if y['name'] == x:
                        doNotAdd = True
                # print(x, doNotAdd)
                if doNotAdd == False:
                    columns.append({'id' : x, 'name' : x, 'selectable' : True})
        else:
            tempCol = []
            for i in columns:
                if i['name'] == 'Fiscal Year':
                    tempCol.append(i)
            columns = tempCol
        # columns.append({
        #     'label': value,
        #     'id': value
        # })

        # remove non-selected
        if columns != []:
            for x in columns:
                exist = False
                for y in value:
                    if x['name'] == y:
                        exist = True
                if exist == False:
                   columns.remove(x)
                        
        return columns

def create_layout(app, region, region_code, view_style):


    ##########################################################################################################
    pageID = 4

    # Now get prefetched data folder
    PATH = pathlib.Path(__file__).parent  # Perform cd..
    DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()
    MAP_PATH = PATH.joinpath("../maps/" + str(region_code)).resolve()


    # Load data

    # TO-DO:
    # Function ID: F-B-01
    # So, basically data is pre-cached to add proper column names and such.
    # A separated package needs to add on top of this to pull data from the
    # database. This also gives the ground for us if the database is broken
    # for whatever reason?

    df_population = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    df_FPL_50 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0, 10, 11, 12, 13, 14, 15, 16])
    df_FPL_100 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0, 17, 18, 19, 20, 21, 22, 23])
    df_FPL_130 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0, 24, 25, 26, 27, 28, 29, 30])
    df_FPL_185 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0, 31, 32, 33, 34, 35, 36, 37])
    df_FPL_200 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0, 38, 39, 40, 41, 42, 43, 44])
    df_FPL_400 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0, 45, 46, 47, 48, 49, 50, 51])

    # df_FPL_50 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 5, 6, 7])
    # df_FPL_100 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 8, 9, 10])
    # df_FPL_130 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 11, 12, 13])
    # df_FPL_185 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 14, 15, 16])
    # df_FPL_200 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 17, 18, 19])
    # df_FPL_400 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 20, 21, 22])

    FPL_level = [24250, 24300, 24600, 25100]



    # Extract the fiscal year
    df_fiscal_year = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0])
    max_length = len(df_fiscal_year)   # the max out index for the column
    # Starting index set to 1 instead of 0, since we want to remove the header name of the column.
    fiscal_year = [int(item[0]) for item in df_fiscal_year.values[1:max_length]]

    pop0 = [int(item[0]) for item in
           pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                       usecols = [2]).values[1:max_length]]
    pop1 = [int(item[0]) for item in
           pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                       usecols = [3]).values[1:max_length]]
    pop2 = [int(item[0]) for item in
           pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                       usecols = [4]).values[1:max_length]]
    pop3 = [int(item[0]) for item in
           pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                       usecols = [5]).values[1:max_length]]
    pop4 = [int(item[0]) for item in
           pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                       usecols = [6]).values[1:max_length]]
    pop5 = [int(item[0]) for item in
           pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                       usecols = [7]).values[1:max_length]]
    pop0_5 = [int(item[0]) for item in
           pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                       usecols = [8]).values[1:max_length]]
                       
    #pop_min = min(pop0+pop1+pop2-250, pop3+pop4+pop5-250)
    #pop_max = max(pop0+pop1+pop2+250, pop3+pop4+pop5+250)

    ##########################################################################################################


    # dt_id_list = ['year', '0' '1', '2', '3', '4', '5', '0-2', '3-5', '0-5']
    dt_id_list_off = ['0-2', '3-5', '0-5']
    return html.Div(
        [
            # Don't remove this if you wanna lose the menu!
            Header(app, region, view_style, pageID),
            # page 2
            html.Div(
                [
                    # html.Div(
                    #     [
                    #         html.P(id='testP')
                    #     ],
                    #     className="row ",
                    # ),

                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [html.Strong("Population at "+ region)], className="subtitle padded"
                                    ),

                                    # TO-DO:
                                    # Table ID: B-B-01
                                    # So the thing here is that, since I cheap out on using css based HTML-based
                                    # table maker, so there is no styling or whatsoever. Later on, please consider
                                    # to change to plotly express based mechanism.

                                    #html.Table(make_dash_table(df_population)), # Temporarily not using tiny header

                                    # Just for clarity and style. Should have other ways to do so, like
                                    # changing the header row's color? Lazy as for now.
                                    DataTable(
                                        columns=[
                                            # {"name": "Fiscal Year", "id": "year"},
                                            # {"name": "# of Age 0", "id": "0", "hideable": True},
                                            # {"name": "# of Age 1", "id": "1", "hideable": True},
                                            # {"name": "# of Age 2", "id": "2", "hideable": True},
                                            # {"name": "# of Age 3", "id": "3", "hideable": True},
                                            # {"name": "# of Age 4", "id": "4", "hideable": True},
                                            # {"name": "# of Age 5", "id": "5", "hideable": True},
                                            # {"name": "# of Age 0 to 2", "id": "0-2", "hideable": True},
                                            # {"name": "# of Age 3 to 5", "id": "3-5", "hideable": True},
                                            # {"name": "# of Age Under 5", "id": "0-5", "hideable": True},
                                            {"name": "Fiscal Year", "id": "year"},
                                            {"name": "0", "id": "0", "hideable": True},
                                            {"name": "1", "id": "1", "hideable": True},
                                            {"name": "2", "id": "2", "hideable": True},
                                            {"name": "3", "id": "3", "hideable": True},
                                            {"name": "4", "id": "4", "hideable": True},
                                            {"name": "5", "id": "5", "hideable": True},
                                            {"name": "0 - 2", "id": "0-2", "hideable": True},
                                            {"name": "3 - 5", "id": "3-5", "hideable": True},
                                            {"name": "0 - 5", "id": "0-5", "hideable": True},
                                        ],
                                        data=[
                                            {
                                                "year": fiscal_year[i],
                                                "0": pop0[i],
                                                "1": pop1[i],
                                                "2": pop2[i],
                                                "3": pop3[i],
                                                "4": pop4[i],
                                                "5": pop5[i],
                                                "0-2": pop0[i] + pop1[i] + pop2[i],
                                                "3-5": pop3[i] + pop4[i] + pop5[i],
                                                "0-5": pop0_5[i],
                                            }
                                            for i in range(4)

                                        ],
                                        # style_table={
                                        #     'overflowX': 'scroll'
                                        # },
                                        # export_name = 'Test',
                                        export_format='xlsx',
                                        export_headers='display',
                                        merge_duplicate_headers=True,
                                        # row_selectable='multi',
                                        selected_rows=[],
                                        sort_action='native',
                                        sort_mode='multi',
                                        style_cell_conditional=[
                                            {
                                                'if': {'column_id': c},
                                                'display': 'none'
                                                } for c in dt_id_list_off
                                        ],
                                        hidden_columns=dt_id_list_off
                                    ),
                                ],
                                className="six columns",
                            ),

                            # We will need to create a plot for this population
                            html.Div(
                                [
                                    # Please check on the page to make sure we use just
                                    # enough new lines to align the graph with the table.
                                    html.Br([]),
                                    html.Br([]),
                                    html.Br([]),
                                    html.Br([]),

                                    html.Strong(
                                        "Children Ages Birth-2 and 3-5",
                                        style={"color": "#3a3a3a",
                                               # For the padding, you can have reference from:
                                               # https://community.plotly.com/t/center-alignment-for-html-div-dcc-slider/12337/5
                                               # The percentage requires some serious maneuvering. :)
                                               "padding-left": "30%"},
                                    ),

                                    # Okay, I was stupid, just glue the go.Scatter together,
                                    # then the shit will work... Why the hell I was looking
                                    # hard for the documentation...

                                    # TO-DO:
                                    # Function ID: G-B-01
                                    # The file loading part needs to be re-coded. Since right now is hard-coded
                                    # to read the certain file.
                                    dcc.Graph(
                                        # The title of the plot is in the block above, scroll back up!
                                        id="graph-B1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=fiscal_year,
                                                    # This shit is hard coded to hell
                                                    y=np.array([int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols = [2]).values[1:max_length]]) + np.array([int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols = [3]).values[1:max_length]]) + np.array([int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols = [4]).values[1:max_length]]),


                                                    #line={"color": "#97151c"},
                                                    #mode="markers+lines",
                                                    marker=dict(color='#03fcba'), #set color bar to Gold
                                                    name="Birth–2",
                                                ),
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=np.array([int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols = [5]).values[1:max_length]]) + np.array([int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols = [6]).values[1:max_length]]) + np.array([int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols = [7]).values[1:max_length]]),
                                                    #line={"color": "#30151c"},
                                                    #mode="markers+lines",
                                                    marker=dict(color='#8732db'), #Set colobar to silver
                                                    name="Ages 3–5",
                                                )

                                                # Note:
                                                # This is optional, since 0-5 is just 2 values added together.
                                                # I'd consider it is a waste of time to plot the sum value,
                                                # and it also makes the scales fucked, and hard to see.
                                                # If we were to toggle it back on, we will need to also change
                                                # the scale for the y axis.


                                                # go.Scatter(
                                                #     x=fiscal_year,
                                                #     y=[int(item[0]) for item in
                                                #        pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                                #                    usecols=[3]).values[1:max_length]],
                                                #     line={"color": "#ff0912"},
                                                #     mode="markers+lines",
                                                #     name="Age 3 - 5",
                                                # )
                                            ],
                                            # For the layout configuration, please see:
                                            # https://plotly.com/python/line-and-scatter/
                                            # Good luck?
                                            "layout": go.Layout(
                                                autosize=True,
                                                title="",
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=360,
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
                                                    "range": [fiscal_year[0], fiscal_year[max_length - 2]],
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
                                                    # Function ID: F-B-02
                                                    # As for now, the range is hard coded since I can't be fucked.
                                                    # So, sorry, let's just use this thing for now!
                                                    # In the future, the range should be calculated accordingly.
                                                    # Lower bound =  min_val -500
                                                    # Upper bound = max_val + 500
                                                    #"range": [500, 1500],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "ticklen": 10,
                                                    "ticks": "outside",
                                                    "title": "Children",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                    "zerolinewidth": 4,
                                                },
                                            ),
                                        },
                                        # Please leave it as disabled, otherwise when you export,
                                        # there will be an ugly-ass bar on top of the graph.
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",


                            ),
                        ],
                        className="row ",   # Remember the tag
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.H6(
                                [
                                    html.Strong("Federal Poverty Level at "+ region),
                                ],
                                className="subtitle padded",
                            ),
                            html.Div(
                                [
                                    # TO-DO:
                                    # Table ID: B-B-02
                                    # So the thing here is that, since I cheap out on using css based HTML-based
                                    # table maker, so there is no styling or whatsoever. Later on, please consider
                                    # to change to plotly express based mechanism.
                                    # html.Table(make_dash_table(pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                    #                                        usecols=[0, 5, 6, 8, 9, 14, 15, 17,
                                    #                                                 18]))),
                                    html.H6(
                                        [
                                            "Use the dropdown menu to select ",
                                            html.Strong("individual ages or age groups "),
                                            "at different Federal Poverty Levels:",
                                        ],
                                    ),
                                    dcc.Dropdown(
                                        id = 'FPL-dropdown',
                                        options=[{'label': 'Birth–2 (50% FPL)', 'value': 'Birth–2 (50% FPL)'},
                                                 {'label': '3–5 (50% FPL)', 'value': '3–5 (50% FPL)'},
                                                 {'label': '0–5 (50% FPL)', 'value': '0–5 (50% FPL)'},
                                                 {'label': 'Birth–2 (100% FPL)', 'value': 'Birth–2 (100% FPL)'},
                                                 {'label': '3–5 (100% FPL)', 'value': '3–5 (100% FPL)'},
                                                 {'label': '0–5 (100% FPL)', 'value': '0–5 (100% FPL)'},
                                                 {'label': 'Birth–2 (130% FPL)', 'value': 'Birth–2 (130% FPL)'},
                                                 {'label': '3–5 (130% FPL)', 'value': '3–5 (130% FPL)'},
                                                 {'label': '0–5 (130% FPL)', 'value': '0–5 (130% FPL)'},
                                                 {'label': 'Birth–2 (185% FPL)', 'value': 'Birth–2 (185% FPL)'},
                                                 {'label': '3–5 (185% FPL)', 'value': '3–5 (185% FPL)'},
                                                 {'label': '0–5 (185% FPL)', 'value': '0–5 (185% FPL)'},
                                                 {'label': 'Birth–2 (200% FPL)', 'value': 'Birth–2 (200% FPL)'},
                                                 {'label': '3–5 (200% FPL)', 'value': '3–5 (200% FPL)'},
                                                 {'label': '0–5 (200% FPL)', 'value': '0–5 (200% FPL)'},
                                                 {'label': 'Birth–2 (400% FPL)', 'value': 'Birth–2 (400% FPL)'},
                                                 {'label': '3–5 (400% FPL)', 'value': '3–5 (400% FPL)'},
                                                 {'label': '0–5 (400% FPL)', 'value': '0–5 (400% FPL)'}
                                                 ],
                                        # value=['100-0-2', '100-3-5', '100-0-5','185-0-2', '185-3-5', '185-0-5','200-0-2', '200-3-5', '200-0-5'],
                                        value=['Birth–2 (100% FPL)', '3–5 (100% FPL)', '0–5 (100% FPL)'],
                                        multi=True
                                    ),
                                    DataTable(
                                        id='FPL-table',
                                        columns=[{
                                            'name':x,
                                            'id':x,
                                            'selectable':True
                                        } for x in ['Fiscal Year']
                                        # } for x in ['Fiscal Year', '100-0-2', '100-3-5', '100-0-5']
                                        ],
                                        column_selectable="multi",
                                        data=[{
                                            'Fiscal Year':fiscal_year[x],
                                            'Birth–2 (50% FPL)': df_FPL_50.iloc[x + 1][1]+df_FPL_50.iloc[x + 1][2]+df_FPL_50.iloc[x + 1][3],
                                            '3–5 (50% FPL)': df_FPL_50.iloc[x + 1][4]+df_FPL_50.iloc[x + 1][5]+df_FPL_50.iloc[x + 1][6],
                                            '0–5 (50% FPL)': df_FPL_50.iloc[x + 1][7],
                                            'Birth–2 (100% FPL)': df_FPL_100.iloc[x + 1][1]+df_FPL_100.iloc[x + 1][2]+df_FPL_100.iloc[x + 1][3],
                                            '3–5 (100% FPL)': df_FPL_100.iloc[x + 1][4]+df_FPL_100.iloc[x + 1][5]+df_FPL_100.iloc[x + 1][6],
                                            '0–5 (100% FPL)': df_FPL_100.iloc[x + 1][7],
                                            'Birth–2 (130% FPL)': df_FPL_130.iloc[x + 1][1] + df_FPL_130.iloc[x + 1][2] +
                                                                df_FPL_130.iloc[x + 1][3],
                                            '3–5 (130% FPL)': df_FPL_130.iloc[x + 1][4] + df_FPL_130.iloc[x + 1][5] +
                                                                df_FPL_130.iloc[x + 1][6],
                                            '0–5 (130% FPL)': df_FPL_130.iloc[x + 1][7],
                                            'Birth–2 (185% FPL)': df_FPL_185.iloc[x + 1][1]+df_FPL_185.iloc[x + 1][2]+df_FPL_185.iloc[x + 1][3],
                                            '3–5 (185% FPL)': df_FPL_185.iloc[x + 1][4]+df_FPL_185.iloc[x + 1][5]+df_FPL_185.iloc[x + 1][6],
                                            '0–5 (185% FPL)': df_FPL_185.iloc[x + 1][7],
                                            'Birth–2 (200% FPL)': df_FPL_200.iloc[x + 1][1]+df_FPL_200.iloc[x + 1][2]+df_FPL_200.iloc[x + 1][3],
                                            '3–5 (200% FPL)': df_FPL_200.iloc[x + 1][4]+df_FPL_200.iloc[x + 1][5]+df_FPL_200.iloc[x + 1][6],
                                            '0–5 (200% FPL)': df_FPL_200.iloc[x + 1][7],
                                            'Birth–2 (400% FPL)': df_FPL_400.iloc[x + 1][1] + df_FPL_400.iloc[x + 1][2] +
                                                                df_FPL_400.iloc[x + 1][3],
                                            '3–5 (400% FPL)': df_FPL_400.iloc[x + 1][4] + df_FPL_400.iloc[x + 1][5] +
                                                                df_FPL_400.iloc[x + 1][6],
                                            '0–5 (400% FPL)': df_FPL_400.iloc[x + 1][7],
                                        }for x in range(4)],
                                        export_format='xlsx',
                                        export_headers='display',
                                        merge_duplicate_headers=True,
                                        # row_selectable='multi',
                                        selected_rows=[],
                                        sort_action='native',
                                        sort_mode='multi',
                                    )

                                ],
                                className="twelve-columns ",  # Remember the tag
                            ),
                        ],
                        className="row "
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    # TO-DO:
                                    # Function ID: G-B-02
                                    # For this graph, the auto-range is disabled, and hard-coded to read from
                                    # certain file. Need to fix it later.
                                    html.Strong(
                                        "FPL Ages Birth–2",
                                        style={"color": "#3a3a3a",
                                               "padding-left": "40%"},
                                    ),
                                    dcc.Graph(
                                        id="graph-B2",
                                        figure={
                                            "data": [
                                                # First, we stack the 50%
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[10]).values[1:max_length]]) + np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[11]).values[1:max_length]]) + np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[12]).values[1:max_length]]),
                                                    marker={"color": "#97151c"},
                                                    name="50%",
                                                ),
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=(np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(
                                                                    str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[17]).values[
                                                                1:max_length]]) + np.array([int(item[0]) for item in
                                                                                            pd.read_csv(
                                                                                                DATA_PATH.joinpath(str(
                                                                                                    region_code) + "_DemoLib.csv"),
                                                                                                usecols=[18]).values[
                                                                                            1:max_length]]) + np.array(
                                                        [int(item[0]) for item in
                                                         pd.read_csv(
                                                             DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                             usecols=[19]).values[1:max_length]]))
                                                      -
                                                      (np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(
                                                                    str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[10]).values[
                                                                1:max_length]]) + np.array([int(item[0]) for item in
                                                                                            pd.read_csv(
                                                                                                DATA_PATH.joinpath(str(
                                                                                                    region_code) + "_DemoLib.csv"),
                                                                                                usecols=[11]).values[
                                                                                            1:max_length]]) + np.array(
                                                        [int(item[0]) for item in
                                                         pd.read_csv(
                                                             DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                             usecols=[12]).values[1:max_length]])),
                                                    marker={"color": "#fcba03"},
                                                    name="100%",
                                                ),
                                                #go.Bar(
                                                #    x=fiscal_year,
                                                #    y=np.array([int(item[0]) for item in
                                                #                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                                #                            usecols=[11]).values[1:max_length]])
                                                #      -
                                                #      np.array([int(item[0]) for item in
                                                #                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                                #                            usecols=[8]).values[1:max_length]]),
                                                #    marker={"color": "#03fcba"},
                                                #    name="130%",
                                                #),
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=(np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(
                                                                    str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[31]).values[
                                                                1:max_length]]) + np.array([int(item[0]) for item in
                                                                                            pd.read_csv(
                                                                                                DATA_PATH.joinpath(str(
                                                                                                    region_code) + "_DemoLib.csv"),
                                                                                                usecols=[32]).values[
                                                                                            1:max_length]]) + np.array(
                                                        [int(item[0]) for item in
                                                         pd.read_csv(
                                                             DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                             usecols=[33]).values[1:max_length]]))
                                                      -
                                                      (np.array([int(item[0]) for item in
                                                                 pd.read_csv(DATA_PATH.joinpath(
                                                                     str(region_code) + "_DemoLib.csv"),
                                                                     usecols=[17]).values[
                                                                 1:max_length]]) + np.array([int(item[0]) for item in
                                                                                             pd.read_csv(
                                                                                                 DATA_PATH.joinpath(str(
                                                                                                     region_code) + "_DemoLib.csv"),
                                                                                                 usecols=[18]).values[
                                                                                             1:max_length]]) + np.array(
                                                          [int(item[0]) for item in
                                                           pd.read_csv(
                                                               DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                               usecols=[19]).values[1:max_length]])),
                                                    marker={"color": "#8732db"},
                                                    name="185%",
                                                ),
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=(np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(
                                                                    str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[38]).values[
                                                                1:max_length]]) + np.array([int(item[0]) for item in
                                                                                            pd.read_csv(
                                                                                                DATA_PATH.joinpath(str(
                                                                                                    region_code) + "_DemoLib.csv"),
                                                                                                usecols=[39]).values[
                                                                                            1:max_length]]) + np.array(
                                                        [int(item[0]) for item in
                                                         pd.read_csv(
                                                             DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                             usecols=[40]).values[1:max_length]]))
                                                      -
                                                      (np.array([int(item[0]) for item in
                                                                 pd.read_csv(DATA_PATH.joinpath(
                                                                     str(region_code) + "_DemoLib.csv"),
                                                                     usecols=[31]).values[
                                                                 1:max_length]]) + np.array([int(item[0]) for item in
                                                                                             pd.read_csv(
                                                                                                 DATA_PATH.joinpath(str(
                                                                                                     region_code) + "_DemoLib.csv"),
                                                                                                 usecols=[32]).values[
                                                                                             1:max_length]]) + np.array(
                                                          [int(item[0]) for item in
                                                           pd.read_csv(
                                                               DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                               usecols=[33]).values[1:max_length]])),
                                                    marker={"color": "#f5f525"},
                                                    name="200%",
                                                ),
                                                #go.Bar(
                                                #    x=fiscal_year,
                                                #    y=np.array([int(item[0]) for item in
                                                #                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                                #                            usecols=[20]).values[1:max_length]])
                                                #      -
                                                #      np.array([int(item[0]) for item in
                                                #                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                                #                            usecols=[17]).values[1:max_length]]),
                                                #    marker={"color": "#f22248"},
                                                #    name="400%",
                                                #    ),

                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                height=225,
                                                width=375,
                                                bargap=0.4,
                                                barmode="stack",
                                                hovermode="closest",
                                                margin={
                                                    "r": 40,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 40,
                                                },
                                                showlegend=True,
                                                legend={
                                                    "y": 0.142606516291,
                                                },
                                                title="",
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 1.5],
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 11,
                                                    },
                                                    "title": "",
                                                    "type": "category",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "mirror": False,
                                                    "nticks": 10,
                                                    #"range": [0, 3000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 11,
                                                    },
                                                    # Cuz this thing is not money
                                                    # "tickprefix": "$",
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",  # Remember the tag
                            ),
                            html.Div(
                                [
                                    # TO-DO:
                                    # Function ID: G-B-03
                                    # For this graph, the auto-range is disabled, and hard-coded to read from
                                    # certain file. Need to fix it later.
                                    html.Strong(
                                        "FPL Ages 3–5",
                                        style={"color": "#3a3a3a",
                                               "padding-left": "40%"},
                                    ),
                                    dcc.Graph(
                                        id="graph-B3",
                                        figure={
                                            "data": [
                                                # First, we stack the 50%
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[13]).values[1:max_length]]) + np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[14]).values[1:max_length]]) + np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[15]).values[1:max_length]]),
                                                    marker={"color": "#97151c"},
                                                    name="50%",
                                                ),
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=(np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(
                                                                    str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[20]).values[
                                                                1:max_length]]) + np.array([int(item[0]) for item in
                                                                                            pd.read_csv(
                                                                                                DATA_PATH.joinpath(str(
                                                                                                    region_code) + "_DemoLib.csv"),
                                                                                                usecols=[21]).values[
                                                                                            1:max_length]]) + np.array(
                                                        [int(item[0]) for item in
                                                         pd.read_csv(
                                                             DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                             usecols=[22]).values[1:max_length]]))
                                                      -
                                                      (np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(
                                                                    str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[13]).values[
                                                                1:max_length]]) + np.array([int(item[0]) for item in
                                                                                            pd.read_csv(
                                                                                                DATA_PATH.joinpath(str(
                                                                                                    region_code) + "_DemoLib.csv"),
                                                                                                usecols=[14]).values[
                                                                                            1:max_length]]) + np.array(
                                                        [int(item[0]) for item in
                                                         pd.read_csv(
                                                             DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                             usecols=[15]).values[1:max_length]])),
                                                    marker={"color": "#fcba03"},
                                                    name="100%",
                                                ),
                                                #go.Bar(
                                                #    x=fiscal_year,
                                                #    y=np.array([int(item[0]) for item in
                                                #                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                                #                            usecols=[12]).values[1:max_length]])
                                                #      -
                                                #      np.array([int(item[0]) for item in
                                                #                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                                #                            usecols=[9]).values[1:max_length]]),
                                                #    marker={"color": "#03fcba"},
                                                #    name="130%",
                                                #),
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=(np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(
                                                                    str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[34]).values[
                                                                1:max_length]]) + np.array([int(item[0]) for item in
                                                                                            pd.read_csv(
                                                                                                DATA_PATH.joinpath(str(
                                                                                                    region_code) + "_DemoLib.csv"),
                                                                                                usecols=[35]).values[
                                                                                            1:max_length]]) + np.array(
                                                        [int(item[0]) for item in
                                                         pd.read_csv(
                                                             DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                             usecols=[36]).values[1:max_length]]))
                                                      -
                                                      (np.array([int(item[0]) for item in
                                                                 pd.read_csv(DATA_PATH.joinpath(
                                                                     str(region_code) + "_DemoLib.csv"),
                                                                     usecols=[20]).values[
                                                                 1:max_length]]) + np.array([int(item[0]) for item in
                                                                                             pd.read_csv(
                                                                                                 DATA_PATH.joinpath(str(
                                                                                                     region_code) + "_DemoLib.csv"),
                                                                                                 usecols=[21]).values[
                                                                                             1:max_length]]) + np.array(
                                                          [int(item[0]) for item in
                                                           pd.read_csv(
                                                               DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                               usecols=[22]).values[1:max_length]])),
                                                    marker={"color": "#8732db"},
                                                    name="185%",
                                                ),
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=(np.array([int(item[0]) for item in
                                                                pd.read_csv(DATA_PATH.joinpath(
                                                                    str(region_code) + "_DemoLib.csv"),
                                                                            usecols=[41]).values[
                                                                1:max_length]]) + np.array([int(item[0]) for item in
                                                                                            pd.read_csv(
                                                                                                DATA_PATH.joinpath(str(
                                                                                                    region_code) + "_DemoLib.csv"),
                                                                                                usecols=[42]).values[
                                                                                            1:max_length]]) + np.array(
                                                        [int(item[0]) for item in
                                                         pd.read_csv(
                                                             DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                             usecols=[43]).values[1:max_length]]))
                                                      -
                                                      (np.array([int(item[0]) for item in
                                                                 pd.read_csv(DATA_PATH.joinpath(
                                                                     str(region_code) + "_DemoLib.csv"),
                                                                     usecols=[34]).values[
                                                                 1:max_length]]) + np.array([int(item[0]) for item in
                                                                                             pd.read_csv(
                                                                                                 DATA_PATH.joinpath(str(
                                                                                                     region_code) + "_DemoLib.csv"),
                                                                                                 usecols=[35]).values[
                                                                                             1:max_length]]) + np.array(
                                                          [int(item[0]) for item in
                                                           pd.read_csv(
                                                               DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                               usecols=[36]).values[1:max_length]])),
                                                    marker={"color": "#f5f525"},
                                                    name="200%",
                                                ),
                                                #go.Bar(
                                                #    x=fiscal_year,
                                                #    y=np.array([int(item[0]) for item in
                                                #                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                                #                            usecols=[21]).values[1:max_length]])
                                                #      -
                                                #      np.array([int(item[0]) for item in
                                                #                pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"),
                                                #                            usecols=[18]).values[1:max_length]]),
                                                #    marker={"color": "#f22248"},
                                                #    name="400%",
                                                #),

                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                height=225,
                                                width=375,
                                                bargap=0.4,
                                                barmode="stack",
                                                hovermode="closest",
                                                margin={
                                                    "r": 40,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 40,
                                                },
                                                showlegend=True,
                                                legend={
                                                    "y": 0.142606516291,
                                                },
                                                title="",
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 1.5],
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 11,
                                                    },
                                                    "title": "",
                                                    "type": "category",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "mirror": False,
                                                    "nticks": 10,
                                                    #"range": [0, 3000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 11,
                                                    },
                                                    # Cuz this thing is not money
                                                    # "tickprefix": "$",
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],

                                # FOR THE FUCK SAKE WHY 6 COLUMNS TAG IS "six columns"
                                # WHEREAS THE FUCKING 12 COLUMNS TAG IS "twelve-columns"
                                # PLOTLY ARE YOU FUCKING KIDDING ME?
                                # FOR THE SAKE OF 1 HOUR IN MY LIFE!
                                className="six columns",
                            ),
                        ],
                        className="row ",  # Remember the tag



                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
