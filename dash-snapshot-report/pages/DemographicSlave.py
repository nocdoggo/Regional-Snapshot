# Page ID: B
# The 2nd tab. That's it.

import dash
import dash_core_components as dcc
import dash_html_components as html
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


def dropdownImageTrigger(app):
    @app.callback(
    dash.dependencies.Output('image', 'src'),
    [dash.dependencies.Input('image-dropdown', 'value')])
    def update_image_src(image_path):
        # print the image_path to confirm the selection is as expected
        # print('current image_path = {}'.format(image_path))
        encoded_image = base64.b64encode(open(image_path, 'rb').read())
        return 'data:image/png;base64,{}'.format(encoded_image.decode())


def create_layout(app, region, region_code, view_style):


    ##########################################################################################################
    pageID = 3

    # Now get prefetched data folder
    PATH = pathlib.Path(__file__).parent  # Perform cd..
    DATA_PATH = PATH.joinpath("../prefetched/" + str(region_code)).resolve()
    MAP_PATH = PATH.joinpath("../maps/" + str(region_code)).resolve()

    FPL_50_img = MAP_PATH.joinpath("FPL @ 50%.png")
    FPL_100_img = MAP_PATH.joinpath("FPL @ 100%.png")
    FPL_185_img = MAP_PATH.joinpath("FPL @ 185%.png")
    FPL_200_img = MAP_PATH.joinpath("FPL @ 200%.png")
    # FPL_base64 = base64.b64encode(open(FPL_50_img, 'rb').read()).decode('ascii')
    # TODO: fix list of images
    list_of_images = [str(FPL_50_img), str(FPL_100_img), str(FPL_185_img), str(FPL_200_img)]
    name_of_images = ["50% Federal Poverty Level", "100% Federal Poverty Level", "185% Federal Poverty Level", "200% Federal Poverty Level"]
    # Load data

    # TO-DO:
    # Function ID: F-B-01
    # So, basically data is pre-cached to add proper column names and such.
    # A separated package needs to add on top of this to pull data from the
    # database. This also gives the ground for us if the database is broken
    # for whatever reason?

    # df_population = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 1, 2, 3])
    # df_FPL_50 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 5, 6, 7])
    # df_FPL_100 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 8, 9, 10])
    # df_FPL_130 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 11, 12, 13])
    # df_FPL_185 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 14, 15, 16])
    # df_FPL_200 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 17, 18, 19])
    # df_FPL_400 = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_Demo.csv"), usecols=[0, 20, 21, 22])

    FPL_level = [24300, 24600, 25100, 25750]

    # Extract the fiscal year
    df_fiscal_year = pd.read_csv(DATA_PATH.joinpath(str(region_code) + "_DemoLib.csv"), usecols=[0])
    max_length = len(df_fiscal_year)  # the max out index for the column
    # Starting index set to 1 instead of 0, since we want to remove the header name of the column.
    fiscal_year = [int(item[0]) for item in df_fiscal_year.values[1:max_length]]

    ##########################################################################################################

    return html.Div(
        [
            # Don't remove this if you wanna lose the menu!
            Header(app, region, view_style, pageID),
            # page 2
            html.Div(
                [
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            html.Strong("Federal Poverty Guidelines for a Family of Four"),
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            # html.Table(
                                            #     #make_dash_table(df_after_tax),
                                            #     #className="tiny-header",
                                            # )

                                            # # TO-DO:
                                            # # Text ID: T-B-03
                                            # # Right now this section is being hard-phrased in the page.
                                            # # However, if space is allowed after re-arranging the blocks,
                                            # # we might just fit a real table underneath for better readability.
                                            # # And you don't really need to store in file. Since as long as we
                                            # # have the 100% level, saved somewhere, just a simple math, man.
                                            #

                                            html.Table(
                                                [
                                                    html.Tr([html.Th("Fiscal Year"), html.Th("100%"),
                                                             html.Th("185%"), html.Th("200%")])
                                                ] +
                                                [
                                                    # TO-DO:
                                                    # Table ID: B-B-03
                                                    # The way how we display groups of data being offered, and the
                                                    # fiscal year(s) being covered, should be re-discussed in the
                                                    # group. Not only the possible alignment issue, but also the
                                                    # way to be concisely described.
                                                    # Say, for example, the CCAP data was generated in October 2017
                                                    # for data for FY2018. This data might be too far in front of
                                                    # other data. Some data can be collected at the end of the
                                                    # fiscal year. Hence, how we put the data together in a more
                                                    # meaningful way is important.

                                                    html.Tr([html.Td("2016"), html.Td('${:,.2f}'.format(FPL_level[0])),
                                                             html.Td('${:,.2f}'.format(FPL_level[0]*1.85)), html.Td('${:,.2f}'.format(FPL_level[0]*2))]),
                                                    html.Tr([html.Td("2017"), html.Td('${:,.2f}'.format(FPL_level[1])),
                                                             html.Td('${:,.2f}'.format(FPL_level[1]*1.85)), html.Td('${:,.2f}'.format(FPL_level[1]*2))]),
                                                    html.Tr([html.Td("2018"), html.Td('${:,.2f}'.format(FPL_level[2])),
                                                             html.Td('${:,.2f}'.format(FPL_level[2]*1.85)), html.Td('${:,.2f}'.format(FPL_level[2]*2))]),
                                                    html.Tr([html.Td("2019"), html.Td('${:,.2f}'.format(FPL_level[3])),
                                                             html.Td('${:,.2f}'.format(FPL_level[3]*1.85)), html.Td('${:,.2f}'.format(FPL_level[3]*2))]),
                                                ],
                                            ),
                                            # html.P(
                                            #     "For more information, please visit: \
                                            #     https://aspe.hhs.gov/poverty-guidelines"
                                            # ),
                                            #html.Br([]),
                                            # html.P(
                                            #     "https://aspe.hhs.gov/poverty-guidelines"
                                            # ),

                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="six columns ",
                            ),

                            # TO-DO:
                            # Graph ID: I-B-01
                            # In the future, this need to have a size template per sey. Now it is hard
                            # coded rather than dynamically scaled.

                            html.Div(
                                [
                                    #html.Br([]),
                                    html.Div(
                                        [

                                            html.Br([]),
                                            html.Br([]),
                                            html.Br([]),
                                            html.Br([]),

                                            html.Strong('Income thresholds that vary by family size and \
                                            composition are used to determine who is in poverty. If a \
                                            family’s income is less than a particular threshold, then \
                                            that family and everyone in it is considered to be living in \
                                            poverty.'),

                                            html.Br([]),


                                            html.P('For more information, please visit: '),
                                            html.Br([]),
                                            html.P('https://aspe.hhs.gov/poverty-guidelines')

                                        ],
                                        className="row ",
                                    ),


                                ],
                                className="six columns ",
                            ),

                        ],
                        className="row ",
                    ),

                    html.Div(
                        [
                            # html.Img(src='data:image/png;base64,{}'.format(FPL_base64), width=306,
                            #          height=204),
                            html.H6 (
                                [
                                    "Use dropdown menu to select from ",
                                    html.Strong("Federal Poverty Percentage Level (FPL) at 50%, 100%, 185%, or 200%:"),
                                ],
                            ),

                            dcc.Dropdown(
                                id='image-dropdown',
                                options=[{'label': j, 'value': i} for i, j in zip(list_of_images, name_of_images)],
                                # initially display the first entry in the list
                                value=list_of_images[1]
                            ),
                            html.Div(
                                html.Img(id='image', style={'max-width': '100%',
                                                            'max-height': '100%',
                                                            'margin': 'auto',
                                                            'display': 'inline-block'},
                                ),
                            ),


                            # html.Img(id='image', width="100%", height="100%")
                        ],
                        className="row ",
                    ),

                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
