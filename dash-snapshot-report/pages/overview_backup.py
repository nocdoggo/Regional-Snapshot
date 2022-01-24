# Page ID: A
# The overview landing page post region selection.

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib
import base64   # This is for displaying the image, since we need the directory to be correctly imported



def create_layout(app, region, region_code, view_style):

    ##########################################################################################################

    # Playground for all the code for data processing.
    # I had a brain fart when I was creating the app, and let the things went onto the
    # top. So, please kindly leave the code here under 'def create_layout(......)'.

    # get relative data folder
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()
    MAP_PATH = PATH.joinpath("../maps/"+str(region_code)).resolve()

    df_population = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 1, 2, 3])
    new_population = df_population.values[-1].tolist()

    df_PFA = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Prog.csv"), usecols=[0, 1, 2, 3, 4])  # This includes PFA and PFA-E
    df_HS = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Prog.csv"),
                        usecols=[0, 5, 6, 7, 8])  # This includes Head Start and Early Head Start
    df_PI = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Prog.csv"), usecols=[0, 9, 10])  # This includes PI only

    new_HS = df_HS.values[-1].tolist()

    # TO-DO:
    # Function ID: F-A-01
    # Fetch map image, in the future, the name has to be encoded as in format of:
    # <region_code>.png
    map_image = MAP_PATH.joinpath("geo_map.png")
    map_base64 = base64.b64encode(open(map_image, 'rb').read()).decode('ascii')

    ##########################################################################################################



    # Page layouts
    return html.Div(
        [
            html.Div([Header(app, region, view_style)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(

                                # TO-DO:
                                # Box ID: T-A-01
                                # This intro paragraph is subject to change based on the feedback from the team.
                                # Mark as To-Do till altered.

                                [
                                    html.H5("Report Summary"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    The Illinois Early Childhood Asset Map (IECAM) Child Care Quick Data Report\
                                         provides a snap shot of the capacity of center-based and licensed family home\
                                          care in a given geographic area. This report provides information on the\
                                           capacity and/or enrollment of child care centers and licensed family child \
                                           care homes. This report shows the total capacity of centers and licensed\
                                            homes, but does not specify the capacity during specific sessions. Some \
                                            programs have part and full-day sessions. More detail about capacity of \
                                            different sessions is available on the IECAM data collection.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            # TO-DO:
                                            # Box ID: T-A-02
                                            # Not sure what we want here, maybe we need some more detailed stuff?
                                            # Maybe some disclaimer stuff?

                                            html.H6([html.Strong("Introduction")], className="subtitle padded"),
                                            html.Br([]),
                                            html.P(
                                                "\
                                                IECAM data does not reveal the specific child care needs of local families. \
                                                Some communities may need more child care for infants and toddlers or care \
                                                provided during second shift, overnights or weekends. Other communities may \
                                                need a higher proportion of care for children who are ready for preschool \
                                                programs. Discussions at the community level are needed to understand these \
                                                nuances and factors.",
                                                style={"color": "#000000"},

                                            ),
                                            html.P(
                                                "\
                                                It is important to recognize the complexity of early care and education in \
                                                Illinois. Programs may serve young children with blended funding streams, \
                                                with funding from Preschool for All (PFA), Head Start, and child care. As \
                                                such, the numbers reported on IECAM help to form a one-dimensional picture, \
                                                which, by necessity, requires ongoing conversations between community \
                                                partners to complete the picture. To facilitate non-duplication of numbers, \
                                                children in Head Start- and PFA-only programs are NOT included in this Child \
                                                Care Quick Data Report. A report on the capacity of these programs is on the \
                                                IECAM Web site.",
                                                style={"color": "#000000"},

                                            ),
                                            html.Br([]),

                                            html.H6([html.Strong("Geo-location")], className="subtitle padded"),
                                            # html.Br([]),

                                            # TO-DO:
                                            # Function ID: F-A-02
                                            # This is from Wikipedia, in the future, it is preferable to build a web
                                            # scraping utility to scrape out the first paragraph of the web page. And
                                            # the reference links can be saved in a database or somewhere, and can be
                                            # combined with the DeadURL checker tool which I developed earlier.
                                            html.P(
                                                "\
                                                Aurora is a city in DuPage, Kane, Kendall, and Will counties in the U.S.\
                                                 state of Illinois. Located primarily in DuPage and Kane counties, it is\
                                                  an outer suburb of Chicago and the second most populous city in the \
                                                  state, and the 115th most populous city in the country. The population \
                                                  was 197,899 at the 2010 census, and was estimated to have decreased to 197,757 by 2019.",
                                                style={"color": "#000000"},

                                            ),
                                            html.Br([]),
                                            html.Br([]),
                                        ],
                                        className=" eight columns",
                                    ),

                                    html.Div(

                                        # TO-DO:
                                        # Box ID: I-A-01
                                        # This intro paragraph is subject to change based on the feedback from the team.
                                        # Mark as To-Do till altered.

                                        [
                                            html.Br([]),
                                            html.Br([]),
                                            html.Img(src='data:image/png;base64,{}'.format(map_base64), width=245,
                                                     height=365)
                                        ],
                                        className="four columns",
                                    ),

                                ],

                            )
                        ],
                        className="row",
                    ),
                    # # Row 4
                    # html.Div(
                    #     [
                    #
                    #         # I am dumb, can use a + sign instead...
                    #
                    #         html.H6([html.Strong("Data Highlights in 2019 at "), html.Strong(region)], className="subtitle padded"),
                    #         html.Br([]),
                    #
                    #         html.Div(
                    #             [
                    #                 html.Div(
                    #                     [
                    #                         html.Strong(["Number of Children", html.Br(), "Under Age 5"]),
                    #                         html.H5(18744),
                    #                     ],
                    #                     className="product",
                    #                     style={"background-color": "#f0236a"}
                    #                 ),
                    #
                    #             ],
                    #             className=" four columns",
                    #         ),
                    #         html.Div(
                    #             [
                    #                 html.Div(
                    #                     [
                    #                         html.Strong(["Number of Children", html.Br(), "Ages 0 - 2"]),
                    #                         html.H5(8901),
                    #                     ],
                    #                     className="product",
                    #                     style={"background-color": "#518623"}
                    #                 ),
                    #
                    #             ],
                    #             className=" four columns",
                    #         ),
                    #         html.Div(
                    #             [
                    #                 html.Div(
                    #                     [
                    #                         html.Strong(["Number of Children", html.Br(), "Ages 3 - 5"]),
                    #                         html.H5(9843),
                    #                     ],
                    #                     className="product",
                    #                     style={"background-color": "#123456"}
                    #                 ),
                    #
                    #             ],
                    #             className=" four columns",
                    #         ),
                    #     ],
                    #     className="row",
                    # ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6([html.Strong("Demographic (FY2018)")], className="subtitle padded"),
                                ],
                                className=' six columns',
                            ),

                            html.Div(
                                [
                                    html.H6([html.Strong("Head Start & Early Head Start (FY2019)")], className="subtitle padded"),
                                ],
                                className=' six columns',
                            ),

                        ],
                        className=' row',
                    ),

                    html.Div(
                        [
                            # TO-DO:
                            # Graph ID: G-A-01
                            # This is the part of new design of hybrid data cards.
                            # For the following chunk, it does a 1+2 style card.

                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Br([]),
                                        ],
                                        className=" one columns",
                                    ),

                                    html.Div(
                                        [
                                            html.Br([]),
                                            html.Br([]),

                                            # html.Strong(
                                            #     [
                                            #         # Pulls the actual FY year for the data.
                                            #         "In FY" + new_population[0]
                                            #     ],
                                            #     style={
                                            #         "color": "#000000",
                                            #     },
                                            # ),

                                            # html.Br([]),
                                            html.Br([]),
                                            html.H6(
                                                [
                                                    html.Strong("# of Children Under 5"),
                                                ], style={"justify":"center","text-align": "center"}
                                            ),

                                            # html.H4(
                                            #     [9843],
                                            #     style={"text-align": "center"},
                                            # ),
                                            html.Div(
                                                [
                                                    html.H4(int(new_population[3]), style={"justify":"center","text-align": "center"}),
                                                ],


                                            ),


                                            html.Br([]),
                                        ],
                                        # justify="center", align="center",
                                        className=" six columns",
                                        style={  # "background-color": "#123456",
                                            "color": "#ffffff",
                                        },
                                    ),
                                    html.Div(
                                        [
                                            html.Br([]),
                                        ],
                                        className=" one columns",
                                    ),

                                    html.Div(
                                        [

                                            html.Br([]),
                                            html.Div(
                                                [

                                                    html.H6([
                                                        html.Strong("# of Children 0-2"),
                                                    ], style={"justify":"center","text-align": "center"}),

                                                    html.H5(int(new_population[1]), style={"justify":"center","text-align": "center"}),
                                                ],
                                                className=" row"
                                            ),
                                            html.Br([]),
                                            html.Div(
                                                [
                                                    html.H6([
                                                        html.Strong("# of Children 3-5"),
                                                    ], style={"justify":"center","text-align": "center"}),

                                                    html.H5(int(new_population[2]), style={"justify":"center","text-align": "center"}),

                                                ],
                                                className=" row"
                                            ),
                                            # html.Br([]),

                                        ],
                                        className=" five columns",
                                        style={  # "background-color": "#123456",
                                            "color": "#ffffff"}
                                    ),

                                ],
                                style={"background-color": "#123456"},
                                className=" six columns",
                            ),

                            html.Div(
                                [
                                    html.Div(
                                        [
                                            # html.Div(
                                            #     [
                                            #         html.Br([]),
                                            #     ],
                                            #     className=" one columns",
                                            # ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [

                                                            html.Br([]),
                                                            html.H6([
                                                                html.Strong("Number of Sites"),
                                                            ], style={"justify":"center","text-align": "center"}),
                                                            html.H5(int(new_HS[1]), style={"justify":"center","text-align": "center"}),
                                                        ],
                                                        className=" row"
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.Br([]),
                                                            html.H6(html.Strong("Funded Enrollment"), style={"justify":"center","text-align": "center"}),
                                                            # html.Br([]),
                                                            html.H5(int(new_HS[2]), style={"justify":"center","text-align": "center"}),
                                                            # html.Br([]),

                                                        ],
                                                        className=" row"
                                                    ),
                                                ],
                                                className=" row",
                                            ),
                                        ],
                                        style={"background-color": "#518623",
                                               "color": "#ffffff"},
                                        className=" twelve columns",
                                    ),
                                ],
                                # style={"background-color": "#659485"},
                                className=" three columns",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            # html.Div(
                                            #     [
                                            #         html.Br([]),
                                            #     ],
                                            #     className=" one columns",
                                            # ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [

                                                            html.Br([]),
                                                            html.H6([
                                                                html.Strong("Number of Sites"),
                                                            ], style={"justify":"center","text-align": "center"}),
                                                            html.H5(int(new_HS[3]), style={"justify":"center","text-align": "center"}),
                                                        ],
                                                        className=" row"
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.Br([]),
                                                            html.H6(html.Strong("Funded Enrollment"), style={"justify":"center","text-align": "center"}),
                                                            # html.Br([]),
                                                            html.H5(int(new_HS[4]), style={"justify":"center","text-align": "center"}),
                                                            # html.Br([]),

                                                        ],
                                                        className=" row"
                                                    ),
                                                ],
                                                className=" row",
                                            ),
                                        ],
                                        style={"background-color": "#c34a82",
                                               "color": "#ffffff"},
                                        className=" twelve columns",
                                    ),
                                ],
                                # style={"background-color": "#659485"},
                                className=" three columns",
                            ),
                        ],
                        className="row",
                    ),


                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
