# Page ID: C
# The 3rd tab on the menu

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib


def create_layout(app, region, region_code, view_style):

    ##########################################################################################################
    pageID = 5

    # get relative data folder
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()

    # TO-DO:
    # Function ID: F-C-01
    # So, basically data is pre-cached to add proper column names and such.
    # A separated package needs to add on top of this to pull data from the
    # database. This also gives the ground for us if the database is broken
    # for whatever reason?
    df_Language = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0, 52, 53, 54])
    df_Family = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0, 57, 58, 59, 60])

    # Extract the fiscal year
    # This block of code is re-usable. But can't be fucked to .... Umm, what you call it, make into a module
    df_fiscal_year = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0])
    max_length = len(df_fiscal_year)  # the max out index for the column
    # Starting index set to 1 instead of 0, since we want to remove the header name of the column.
    fiscal_year = [int(item[0]) for item in df_fiscal_year.values[1:max_length]]

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
                            # Box ID: T-C-01
                            # Not sure what we want here, maybe we need some more detailed stuff?
                            # Maybe some disclaimer stuff? Since it is a part of the demographic
                            # data, so I am not sure in this case.

                            # html.H6([html.Strong("Introduction")], className="subtitle padded"),
                            html.Strong(

                                # TO-DO:
                                # Box ID: T-C-02
                                # I am not sure what is the best way to describe the data here.
                                # The description on the quick data report page doesn't make
                                # too much sense to me.

                                "\
                                This report recognizes that there may be special needs in populations where English \
                                is not the first language and includes information about households that are limited \
                                English speaking. It is important to note that low income and linguistic isolation \
                                are only two factors for families that may put children at risk of academic failure, \
                                and this report does not provide data about other factors.",
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
                                        [html.Strong("Household Language at "+ region)], className="subtitle padded"
                                    ),

                                    # TO-DO:
                                    # Table ID: B-C-01
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

                                    html.Table(
                                        make_dash_table(df_Language),
                                        # So for the fuck sake, text align and filled color doesn't work.
                                        # Guess we can only change .css?

                                        # style={
                                        # # "background-color": "#ffffff",
                                        # }
                                    ),
                                    # html.P("**** refers to the variable wasn't sampled at the given time."),

                                ],
                                # Currently still using 6 columns, even though it can be less. :/
                                className="six columns",
                            ),

                            # Plot ID: P-C-01
                            # This one is for the language, well, more like for Spanish.
                            # Now, let's add a graph to it!
                            html.Div(
                                [
                                    html.Br([]),
                                    html.Strong(
                                        "Number of Household Speaking Spanish",
                                        style={"color": "#3a3a3a",
                                               # For the padding, you can have reference from:
                                               # https://community.plotly.com/t/center-alignment-for-html-div-dcc-slider/12337/5
                                               # The percentage requires some serious maneuvering. :)
                                               "padding-left": "25%"},
                                    ),
                                    html.Br([]),
                                    html.Strong(
                                        "and Other Languages",
                                        style={"color": "#3a3a3a",
                                               # For the padding, you can have reference from:
                                               # https://community.plotly.com/t/center-alignment-for-html-div-dcc-slider/12337/5
                                               # The percentage requires some serious maneuvering. :)
                                               "padding-left": "41%"},
                                    ),



                                    dcc.Graph(
                                        # The title of the plot is in the block above, scroll back up!
                                        id="graph-B1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=fiscal_year,
                                                    # This shit is hard coded to hell
                                                    y=[int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols=[53]).values[1:max_length]],
                                                    #line={"color": "#97151c"},
                                                    #mode="markers+lines",
                                                    marker=dict(color='#03fcba'), #set color bar to Gold
                                                    name="Spanish",
                                                ),
                                                go.Bar(
                                                    x=fiscal_year,
                                                    y=[int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols=[54]).values[1:max_length]],
                                                    #line={"color": "#30151c"},
                                                    marker=dict(color='#8732db'), #Set colobar to silver
                                                    #mode="markers+lines",
                                                    name="Other Languages",
                                                )


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
                                                    # Modified the x value so that it can be shifted to the center.
                                                    # Default is to "xanchor" to the left. Which gives the best position.
                                                    # However, it is yet to be the center of the plot.
                                                    # Plotly's legend system is pretty fucked as we speak today.
                                                    # The official documentation is rubbish, go see here:
                                                    # https://stackoverflow.com/questions/60123611/how-to-position-legends-inside-a-plot-in-plotly
                                                    # and also:
                                                    # https://github.com/plotly/plotly.js/issues/53
                                                    # https://stackoverflow.com/questions/41599166/python-plotly-legend-positioning-and-formatting

                                                    "x": 0.2377108433735,
                                                    "y": -0.142606516291,
                                                    "orientation": "h",
                                                    # "xanchor": "left",    # Can be center and right
                                                    # "yanchor": "top",     # Can be bottom and center if you fancy
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
                                                    "nticks": 10,

                                                    # TO-DO:
                                                    # Function ID: F-C-02
                                                    # As for now, the range is hard coded since I can't be fucked.
                                                    # So, sorry, let's just use this thing for now!
                                                    # In the future, the range should be calculated accordingly.
                                                    #"range": [500, 3000],
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
                                # Currently still using 6 columns, even though it can be less. :/
                                className="six columns",
                            ),
                            #     html.Div(
                            #         [
                            #             html.P(
                            #                 "Calibre Index Fund seeks to track the performance of\
                            # a benchmark index that measures the investment return of large-capitalization stocks."
                            #             ),
                            #             html.P(
                            #                 "Learn more about this portfolio's investment strategy and policy."
                            #             ),
                            #         ],
                            #         className="eight columns middle-aligned",
                            #         style={"color": "#696969"},
                            #     ),

                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Br([]),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                    
                                        [html.Strong("Working Families at "+ region)],
                                        className="subtitle padded",
                                    ),
                    
                                    html.Table(
                    
                                        # TO-DO:
                                        # Table ID: B-C-02
                                        # So right now, as in B-C-01, we are sill doing the base html table drawing.
                                        # Therefore, in the future, make it better!
                    
                                        make_dash_table(df_Family),
                                        className="tiny-header",
                                    ),
                                ],
                                className="six columns",
                            ),
                    
                            # TO-DO:
                            # Plot ID: P-C-02
                            # This one is for the working family thing. But to be honest, I don't think either line or
                            # bar plots are the correct thing to do. Honestly, what I have in mind is something like
                            # for circles, aka, using the plotly.shape thing. For more information, go visit here :
                            # https://plotly.com/python/shapes/
                            # Since I am an imbecile, I don't wanna crash the existing layout. So after the first
                            # stable release, I'd go figure this out again in later on?
                    
                            html.Div(
                                [
                                    html.Br([]),
                                    html.Strong(
                                        "Children by Working Family Condition",
                                        style={"color": "#3a3a3a",
                                               # For the padding, you can have reference from:
                                               # https://community.plotly.com/t/center-alignment-for-html-div-dcc-slider/12337/5
                                               # The percentage requires some serious maneuvering. :)
                                               "padding-left": "25%"},
                                    ),
                    
                                    dcc.Graph(
                                        # The title of the plot is in the block above, scroll back up!
                                        id="graph-B1",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=fiscal_year,
                                                    # This shit is hard coded to hell
                                                    y=[int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols=[57]).values[1:max_length]],
                                                    line={"color": "#97151c"},
                                                    mode="markers+lines",
                                                    name="2 Parents",
                                                ),
                                                go.Scatter(
                                                    x=fiscal_year,
                                                    y=[int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols=[58]).values[1:max_length]],
                                                    line={"color": "#30151c"},
                                                    mode="markers+lines",
                                                    name="2 Working Parents",
                                                ),
                                                go.Scatter(
                                                    x=fiscal_year,
                                                    y=[int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols=[59]).values[1:max_length]],
                                                    line={"color": "#2972b1"},
                                                    mode="markers+lines",
                                                    name="1 Parent",
                                                ),
                                                go.Scatter(
                                                    x=fiscal_year,
                                                    y=[int(item[0]) for item in
                                                       pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"),
                                                                   usecols=[60]).values[1:max_length]],
                                                    line={"color": "#617749"},      # The color codes are coming out of my ass.
                                                    # Go figure out some newer/better ones if needed.
                                                    mode="markers+lines",
                                                    name="1 Working Parent",
                                                ),
                    
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
                                                    # Modified the x value so that it can be shifted to the center.
                                                    # Default is to "xanchor" to the left. Which gives the best position.
                                                    # However, it is yet to be the center of the plot.
                                                    # Plotly's legend system is pretty fucked as we speak today.
                                                    # The official documentation is rubbish, go see here:
                                                    # https://stackoverflow.com/questions/60123611/how-to-position-legends-inside-a-plot-in-plotly
                                                    # and also:
                                                    # https://github.com/plotly/plotly.js/issues/53
                                                    # https://stackoverflow.com/questions/41599166/python-plotly-legend-positioning-and-formatting
                    
                                                    # But I *REALLY* hate this thing lol
                                                    "x": 0.0877108433735,
                                                    "y": -0.142606516291,
                                                    "orientation": "h",
                                                    # "xanchor": "left",    # Can be center and right
                                                    # "yanchor": "top",     # Can be bottom and center if you fancy
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
                                                    "nticks": 10,
                    
                                                    # TO-DO:
                                                    # Function ID: F-C-03
                                                    # As for now, the range is hard coded since I can't be fucked.
                                                    # So, sorry, let's just use this thing for now!
                                                    # In the future, the range should be calculated accordingly.
                    
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "ticklen": 5,
                                                    "ticks": "outside",
                                                    "title": "Children",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                    "zerolinewidth": 4,
                                                },
                                            ),
                                        },
                                    ),
                    
                                ],
                                className="six columns",
                    
                            ),
                        ],
                        className="row "
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [

                    
                                ],
                    
                                # TO-DO:
                                # Function ID: F-C-04
                                # It has to be more than 9 columns due to the shear amount of, not data,
                                # but the text in the header of each column. I don't know if the naming
                                # can be reduced or not, since to me, the "non-hispanic or latino" at
                                # the end of some of the column names is just redundant. But, What do I
                                # know about census and kids data you might wonder? So I just leave it
                                # to you guys. Man! Have fun!
                                className=" twelve columns",
                            ),
                        ],
                        className="row ",
                    ),

                    html.Div(
                        [
                            html.Br([]),
                            html.Br([]),
                            html.Br([]),
                        ]
                    ),

                    # Row 5
                    html.Div(
                        [

                            html.Div(
                                [
                                    html.H6(
                                        html.Strong(["Footnote"]),
                                        className="subtitle padded",
                                    ),

                                    #html.Br([]),
                                    # html.P("My brain doesn't work well when sun is about to come up... Noctis @ 5am."),



                                ],
                                className=" twelve columns",


                            ),

                            html.Div(
                                [
                                    html.P(
                                        "Language numbers are provided for:",
                                    ),

                                    html.Li(
                                        "Number of households speaking Spanish at home that are limited English-speaking households",
                                    ),

                                    html.Li(
                                        "Number of households speaking other non-English languages at home that are limited English-speaking households",
                                    ),
                                    
                                    # html.P(
                                    #     "Working family numbers are provided for:",
                                    #     ),
                                        
                                    # html.Li(
                                    #     "Children living with one or two working parents may be more likely to need early care and education services.",
                                    #     ),
                                        
                                    # html.Li(
                                    #     "This report provides data on the number of children living in one and two parent families and the number of children who have working parents.",
                                    #     ),

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
                    ),

                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    # html.H6(
                                    #     ["Maybe we also need footnotes for all these data."],
                                    #     className="subtitle padded",
                                    # ),

                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
