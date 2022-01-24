import dash_html_components as html
import dash_core_components as dcc

def Header(app, region, view_style, pageID):

    # This is a really dumb way to do the tab selection highlighting.
    # Since it did not really add the html.Strong(). so, left something else for desire!
    HighLight = ["#000000", "#000000", "#000000", "#000000", "#000000", "#000000"]
    BGColor   = ["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff"]
    HighLight[pageID - 1] = "#97151c"
    BGColor[pageID - 1] = "#ffffff"
    # BGColor[pageID - 1] = "#fcfdc9"

    if (view_style == 0):
        return html.Div([get_header(app, region, view_style), html.Br([]), get_menu(HighLight, BGColor, pageID)])
    elif(view_style == 1):
        return html.Div([get_header(app, region, view_style)])
    else:
        return html.Div()

def get_header(app, region, view_style):
    if (view_style == 0):
        header = html.Div(
            [
                html.Div(
                    [
                        # TO-DO:
                        # Image ID: I-U-01
                        # The logo subject to change, the style and size.
                        # Not sure if this is the latest "graphical design",
                        # so I just screenshot the icon from the front
                        # page, not even finding the source file. :)
                        # Sorry!

                        html.Img(
                            src=app.get_asset_url("IECAM_long_logo.png"),
                            className="logo",
                        ),
                        html.A(
                            html.Button("Back To Landing", id="learn-more-button"),
                            href="/dash-snapshot-report/landing",
                        ),
                        html.A(
                            html.Button("Learn More", id="learn-more-button"),
                            href="https://iecam.illinois.edu/",
                        ),
                    ],
                    className="row",
                ),
                html.Div(
                    [
                        html.Div(

                            # TO-DO:
                            # Text ID: T-U-01
                            # This title is ass-long for a report.
                            # There should be a more elegant way to have it
                            # described.

                            [html.H5(region + " Regional Report")],

                            # Note that 7 is the magical number for the layout
                            className="seven columns main-title",
                        ),
                        html.Div(
                            [
                                dcc.Link(
                                    "Full View",
                                    href="/dash-snapshot-report/full-view",
                                    className="full-view-link",
                                )
                            ],
                            className="five columns",
                        ),
                    ],
                    className="twelve columns",
                    style={"padding-left": "0"},
                ),
            ],
            className="row",
        )
    else:
        header = html.Div(
            [
                html.Div(
                    [
                        # TO-DO:
                        # Image ID: I-U-01
                        # The logo subject to change, the style and size.
                        # Not sure if this is the latest "graphical design",
                        # so I just screenshot the icon from the front
                        # page, not even finding the source file. :)
                        # Sorry!

                        html.Img(
                            src=app.get_asset_url("IECAM_long_logo.png"),
                            className="logo",
                        ),
                        html.A(
                            html.Button("Back To Landing", id="learn-more-button"),
                            href="/dash-snapshot-report/landing",
                        ),
                        html.A(
                            html.Button("Learn More", id="learn-more-button"),
                            href="https://iecam.illinois.edu/",
                        ),
                    ],
                    className="row",
                ),
                html.Div(
                    [
                        html.Div(

                            # TO-DO:
                            # Text ID: T-U-01
                            # This title is ass-long for a report.
                            # There should be a more elegant way to have it
                            # described.

                            [html.H5(region + " Community Report")],

                            # Note that 7 is the magical number for the layout
                            className="seven columns main-title",
                        ),
                        html.Div(
                            [

                            ],
                            className="five columns",
                        ),
                    ],
                    className="twelve columns",
                    style={"padding-left": "0"},
                ),
            ],
            className="row",
        )


    return header


# TO-DO:
# Function ID: F-U-01
# The order of the menu, and the text of the tab require further attention.

def get_menu(HighLight, BGColor, pageID):
    if pageID == 1:

        menu = html.Div(
            [
                dcc.Link(
                    html.Strong("Overview"),style={"color": HighLight[0]},
                    href="/dash-snapshot-report/overview",
                    className="tab first",
                ),
                dcc.Link(
                    ("Early Care and Education"),style={"color": HighLight[1],"background-color": BGColor[1]},
                    href="/dash-snapshot-report/child-care",
                    className="tab"
                ),
                dcc.Link(
                    ("Demographics"),style={"color": HighLight[2],"background-color": BGColor[2]},
                    href="/dash-snapshot-report/demographic",
                    className="tab",
                    id='demoButton'
                ),
                dcc.Link(
                    ("Language & Family"),style={"color": HighLight[3],"background-color": BGColor[3]},
                    href="/dash-snapshot-report/language-family",
                    className="tab",
                ),
                dcc.Link(
                    ("Race/Ethnicity"),style={"color": HighLight[4],"background-color": BGColor[4]},
                    href="/dash-snapshot-report/race",
                    className="tab",
                ),
                dcc.Link(
                    ("About"),style={"color": HighLight[5],"background-color": BGColor[5]},
                    href="/dash-snapshot-report/about",
                    className="tab",
                ),
            ],
            className="row all-tabs",
        )
    elif pageID == 2:
        menu = html.Div(
            [
                dcc.Link(
                    ("Overview"), style={"color": HighLight[0]},
                    href="/dash-snapshot-report/overview",
                    className="tab first",
                ),
                dcc.Link(
                    html.Strong("Early Care and Education"), style={"color": HighLight[1], "background-color": BGColor[1]},
                    href="/dash-snapshot-report/child-care",
                    className="tab"
                ),
                dcc.Link(
                    ("Demographics"), style={"color": HighLight[2], "background-color": BGColor[2]},
                    href="/dash-snapshot-report/demographic",
                    className="tab",
                    id='demoButton'
                ),
                dcc.Link(
                    ("Language & Family"), style={"color": HighLight[3], "background-color": BGColor[3]},
                    href="/dash-snapshot-report/language-family",
                    className="tab",
                ),
                dcc.Link(
                    ("Race/Ethnicity"), style={"color": HighLight[4], "background-color": BGColor[4]},
                    href="/dash-snapshot-report/race",
                    className="tab",
                ),
                dcc.Link(
                    ("About"), style={"color": HighLight[5], "background-color": BGColor[5]},
                    href="/dash-snapshot-report/about",
                    className="tab",
                ),
            ],
            className="row all-tabs",
        )
    elif pageID == 3:
        menu = html.Div(
            [
                dcc.Link(
                    ("Overview"), style={"color": HighLight[0]},
                    href="/dash-snapshot-report/overview",
                    className="tab first",
                ),
                dcc.Link(
                    ("Early Care and Education"), style={"color": HighLight[1], "background-color": BGColor[1]},
                    href="/dash-snapshot-report/child-care",
                    className="tab"
                ),
                dcc.Link(
                    html.Strong("Demographics"), style={"color": HighLight[2], "background-color": BGColor[2]},
                    href="/dash-snapshot-report/demographic",
                    className="tab",
                    id='demoButton'
                ),
                dcc.Link(
                    ("Language & Family"), style={"color": HighLight[3], "background-color": BGColor[3]},
                    href="/dash-snapshot-report/language-family",
                    className="tab",
                ),
                dcc.Link(
                    ("Race/Ethnicity"), style={"color": HighLight[4], "background-color": BGColor[4]},
                    href="/dash-snapshot-report/race",
                    className="tab",
                ),
                dcc.Link(
                    ("About"), style={"color": HighLight[5], "background-color": BGColor[5]},
                    href="/dash-snapshot-report/about",
                    className="tab",
                ),
            ],
            className="row all-tabs",
        )
    elif pageID == 4:
        menu = html.Div(
            [
                dcc.Link(
                    ("Overview"), style={"color": HighLight[0]},
                    href="/dash-snapshot-report/overview",
                    className="tab first",
                ),
                dcc.Link(
                    ("Early Care and Education"), style={"color": HighLight[1], "background-color": BGColor[1]},
                    href="/dash-snapshot-report/child-care",
                    className="tab"
                ),
                dcc.Link(
                    ("Demographics"), style={"color": HighLight[2], "background-color": BGColor[2]},
                    href="/dash-snapshot-report/demographic",
                    className="tab",
                    id='demoButton'
                ),
                dcc.Link(
                    html.Strong("Language & Family"), style={"color": HighLight[3], "background-color": BGColor[3]},
                    href="/dash-snapshot-report/language-family",
                    className="tab",
                ),
                dcc.Link(
                    ("Race/Ethnicity"), style={"color": HighLight[4], "background-color": BGColor[4]},
                    href="/dash-snapshot-report/race",
                    className="tab",
                ),
                dcc.Link(
                    ("About"), style={"color": HighLight[5], "background-color": BGColor[5]},
                    href="/dash-snapshot-report/about",
                    className="tab",
                ),
            ],
            className="row all-tabs",
        )
    elif pageID == 5:
        menu = html.Div(
            [
                dcc.Link(
                    ("Overview"), style={"color": HighLight[0]},
                    href="/dash-snapshot-report/overview",
                    className="tab first",
                ),
                dcc.Link(
                    ("Early Care and Education"), style={"color": HighLight[1], "background-color": BGColor[1]},
                    href="/dash-snapshot-report/child-care",
                    className="tab"
                ),
                dcc.Link(
                    ("Demographics"), style={"color": HighLight[2], "background-color": BGColor[2]},
                    href="/dash-snapshot-report/demographic",
                    className="tab",
                    id='demoButton'
                ),
                dcc.Link(
                    ("Language & Family"), style={"color": HighLight[3], "background-color": BGColor[3]},
                    href="/dash-snapshot-report/language-family",
                    className="tab",
                ),
                dcc.Link(
                    html.Strong("Race/Ethnicity"), style={"color": HighLight[4], "background-color": BGColor[4]},
                    href="/dash-snapshot-report/race",
                    className="tab",
                ),
                dcc.Link(
                    ("About"), style={"color": HighLight[5], "background-color": BGColor[5]},
                    href="/dash-snapshot-report/about",
                    className="tab",
                ),
            ],
            className="row all-tabs",
        )
    elif pageID == 6:
        menu = html.Div(
            [
                dcc.Link(
                    ("Overview"), style={"color": HighLight[0]},
                    href="/dash-snapshot-report/overview",
                    className="tab first",
                ),
                dcc.Link(
                    ("Early Care and Education"), style={"color": HighLight[1], "background-color": BGColor[1]},
                    href="/dash-snapshot-report/child-care",
                    className="tab"
                ),
                dcc.Link(
                    ("Demographics"), style={"color": HighLight[2], "background-color": BGColor[2]},
                    href="/dash-snapshot-report/demographic",
                    className="tab",
                    id='demoButton'
                ),
                dcc.Link(
                    ("Language & Family"), style={"color": HighLight[3], "background-color": BGColor[3]},
                    href="/dash-snapshot-report/language-family",
                    className="tab",
                ),
                dcc.Link(
                    ("Race/Ethnicity"), style={"color": HighLight[4], "background-color": BGColor[4]},
                    href="/dash-snapshot-report/race",
                    className="tab",
                ),
                dcc.Link(
                    html.Strong("About"), style={"color": HighLight[5], "background-color": BGColor[5]},
                    href="/dash-snapshot-report/about",
                    className="tab",
                ),
            ],
            className="row all-tabs",
        )
    return menu

# TO-DO:
# Function ID: F-U-02
# This is a rather lazy way to make a pre-defined function to direct load table
# from csv files. A lot of good functionality are missing. Such as sorting, and
# custom background color. Please consider to further develop it! Such as adding
# custom code input parameters and etc.
def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    #print(df.columns)
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]], style = {'padding':'7px', 'margin':'0'}))
        table.append(html.Tr(html_row))
        #print(table)
    return table

# I want to display the tables with the headers from the
# dataframe.
#def make_dash_table_ricardo(df):
# Maybe consider to develop from the function above?
