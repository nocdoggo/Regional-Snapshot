# Page ID: D
# This page we focus on the centers and such, there is a map created soon!
# Layout of the page subjects to changes.

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd     # The source of cancer in a small package :)
import pathlib
import base64

def create_layout(app, region, region_code, view_style):


    ##########################################################################################################
    pageID = 2

    # get relative data folder
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()

    MAP_PATH = PATH.joinpath("../maps/" + str(region_code)).resolve()

    site_image = MAP_PATH.joinpath("site_map.png")
    site_base64 = base64.b64encode(open(site_image, 'rb').read()).decode('ascii')

    # Load data

    # TO-DO:
    # Function ID: F-D-01
    # So, basically data is pre-cached to add proper column names and such.
    # A separated package needs to add on top of this to pull data from the
    # database. This also gives the ground for us if the database is broken
    # for whatever reason?

    df_PFA = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Prog.csv"), usecols=[0, 1, 2, 3, 4])  # This includes PFA and PFA-E
    df_HS = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Prog.csv"),
                        usecols=[0, 5, 6, 7, 8])  # This includes Head Start and Early Head Start
    df_PI = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Prog.csv"), usecols=[0, 9, 10])  # This includes PI only
    df_CC = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Prog.csv"), usecols=[0, 11, 12, 13, 14, 15, 16])  # This includes PI only

    # Extract the fiscal year
    df_fiscal_year = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Prog.csv"), usecols=[0])
    max_length = len(df_fiscal_year)  # the max out index for the column

    # TO-DO:
    # Function ID: F-D-02
    # So for this part, I think it is the best if later on we need to append "FY" string in front
    # of the integer. Why? Well, cuz I am lazy, wanna just directly dump the data from the database
    # to the pre-cached files. Hence, in order to void the breakage of the SQL saved procedures, I
    # decide to let it do it over here. So in the future, rather than casting to (int), we will just
    # keep them as (str). Any drawback for the plot? No, actually. Since dcc.Graph can do string as
    # x-axis, which is farly interesting, since our data honestly is discrete. So no continuous
    # numeric property needs to be worried about. Good right? I know.
    # Starting index set to 1 instead of 0, since we want to remove the header name of the column.
    fiscal_year = [int(item[0]) for item in df_fiscal_year.values[1:max_length]]

    ##########################################################################################################


    return html.Div(
        [
            Header(app, region, view_style, pageID),
            # page 4
            html.Div(
                [
                    # # Row 1
                    # html.Div(
                    #     [
                    #         # TO-DO:
                    #         html.H6(["Introduction"], className="subtitle padded"),
                    #         html.P(
                    #
                    #             # TO-DO:
                    #             # Box ID: T-D-01
                    #             # I am not sure what is the best way to describe the data here.
                    #             # The description on the quick data report page doesn't make
                    #             # too much sense to me.
                    #
                    #             "\
                    #             Placeholder for some text.",
                    #             style={"color": "#000000"},
                    #             className="row",
                    #         ),
                    #     ],
                    #
                    #
                    #     className="row ",
                    # ),

                    # Row 5
                    html.Div(
                        [
                            html.P(
                                "Early care and education can take many forms,\
                                 may be associated with various local entities, \
                                 and be in schools, centers, or homes. Programs \
                                 may be state funded through the Illinois State \
                                 Board of Education, the Illinois Department of \
                                 Human Services, or the Illinois Department of \
                                 Children and Family Services, or federally \
                                 funded through Head Start. Programs may also \
                                 be privately funded through corporate sponsors \
                                 or parent tuition and fees. The three primary \
                                 early care and education programs for preschoolers \
                                 in Illinois are Preschool for All, Head Start, \
                                 and childcare. The primary infant and toddler \
                                 programs are Prevention Initiative, Early Head \
                                 Start, childcare, and various home-visiting \
                                 programs.")
                        ],
                        className='row ',
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Strong(),
                                    # html.Table(make_dash_table(df_expenses)),
                                    html.H6(html.Strong(["Preschool for All"]), className="subtitle padded"),
                                    html.Table(make_dash_table(df_PFA)),
                                ],
                                className="six columns",
                            ),

                            # html.Div(
                            #     [
                            #         html.Strong(),
                            #         # html.Table(make_dash_table(df_expenses)),
                            #         html.H6(html.Strong(["Prevention Initiative at ", region]), className="subtitle padded"),
                            #         html.Table(make_dash_table(df_PI)),
                            #     ],
                            #     className="three columns",
                            # ),

                            html.Div(
                                [
                                    html.Strong(),
                                    # html.Table(make_dash_table(df_expenses)),
                                    html.H6(html.Strong(["Head Start & Early Head Start"]), className="subtitle padded"),
                                    html.Table(make_dash_table(df_HS)),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [

                            html.Div(
                                [
                                    html.Strong(),
                                    # html.Table(make_dash_table(df_expenses)),
                                    html.H6(html.Strong(["Prevention Initiative"]),
                                            className="subtitle padded"),
                                    html.Table(make_dash_table(df_PI)),
                                ],
                                className=" four columns",
                            ),
                            html.Div(
                                [
                                    html.H6(html.Strong(["Licensed Child Care, Licensed Family Care Centers, and Licensed-Exempt Child Care Centers"]), className="subtitle padded"),
                                    html.Table(make_dash_table(df_CC)),
                                    
                                    # html.Strong("* : The selected fiscal year data does not exist or has not been delivered."),


                                ],
                                className=" eight columns",
                            ),
                        ],
                        className="row",
                    ),

                    # # Row 4
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.Center(html.Strong("Child Care Site Map", style={'justify':"center", 'align':"center",})),
                    #                 html.Img(src='data:image/png;base64,{}'.format(site_base64), width=408,
                    #                          height=250, style={'max-width': '100%',
                    #                                         'max-height': '100%',
                    #                                         'margin': 'auto',
                    #                                         'display': 'block'}),
                    #                 # html.Img(src='data:image/png;base64,{}'.format(site_base64), width=435,
                    #                 #          height=341, style={"display": "block",
                    #                 #                             "margin-left": "auto",
                    #                 #                             "margin-right": "auto"}),
                    #             ],
                    #             className="row ",
                    #         ),
                    #     ],
                    #     className="row ",
                    # ),


                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
