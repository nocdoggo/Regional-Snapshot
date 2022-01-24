# Page ID: F
# This is the final page for data description and about us info.

import dash_html_components as html
from utils import Header


def create_layout(app, region, region_code, view_style):
    pageID = 6

    return html.Div(
        [
            Header(app, region, view_style, pageID),
            # page 6
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(html.Strong("Data Resource and Description"), className="subtitle padded"),
                                    # html.Br([]),
                                    html.Div(
                                        [
                                            html.H6(
                                                html.Strong("Demographic Data",),
                                                style={
                                                    "color": "#852458",
                                                }
                                            ),
                                            html.Br([]),
                                            html.P(
                                                'Following the practice of the U.S. Census Bureau, each year IECAM \
                                                demographers prepare a “data release” that includes the new data for \
                                                the most recently available year plus updated data for the previous \
                                                several years. Each year’s release is slightly more accurate than the \
                                                revious year. The five-year span is based on IECAM’s use of the 5-year \
                                                ACS (American Community Survey) as one of its principal demographic \
                                                data sources.'
                                            ),
                                            html.P(
                                                "For more information, please visit: https://iecam.illinois.edu/data-releases/data-by-geo-region/"
                                            ),

                                            html.H6(
                                                html.Strong("Publicly Funded Preschool",),
                                                style={
                                                    "color": "#852458",
                                                }
                                            ),
                                            html.Br([]),
                                            html.P(
                                                'Preschool for All (PFA), Preschool for All Expansion (PFAE), and \
                                                Head Start are publicly funded preschool programs in Illinois. PFA \
                                                and PFAE are funded by the Illinois State Board of Education (ISBE), \
                                                while Head Start is federally funded by the Department of Health and \
                                                Human Services (HHS). Each of these programs serve young children, \
                                                age 3 through age 5, either in center-based or home-based service \
                                                delivery.'
                                            ),
                                            # html.P(
                                            #     "In 1998, Head Start was reauthorized for fiscal years 1999-2003. In subsequent years, Head Start was funded through the annual appropriations process. In 2007, Head Start was again reauthorized for FY2008."
                                            # ),
                                            html.P(
                                                "For more information, please visit: https://iecam.illinois.edu/data-definitions/isbe-pfa/"
                                            ),

                                            html.H6(
                                                html.Strong("Infant Toddler Programs",),
                                                style={
                                                    "color": "#852458",
                                                }
                                            ),
                                            html.Br([]),
                                            html.P(
                                                'Programs serving our youngest children, birth through age 2, \
                                                    include Prevention Initiative (PI; funded by ISBE), Early \
                                                        Head Start (EHS; funded by HHS), and Maternal, Infant, \
                                                            and Early Childhood Home Visiting (MIECHV; funded \
                                                                by Illinois Department of Human Services). PI \
                                                                    and EHS programs offer center-based and/or \
                                                                        home-based services.'
                                            ),
                                            html.P(
                                                "For more information, please visit: https://iecam.illinois.edu/data-search/topic-search/"
                                            ),
                                            html.H6(
                                                html.Strong("Child Care",),
                                                style={
                                                    "color": "#852458",
                                                }
                                            ),
                                            html.Br([]),
                                            html.P(
                                                'The Illinois Department of Human Services (IDHS) partners with \
                                                childcare providers throughout Illinois to provide working families of \
                                                low income means with access to affordable, quality childcare. IDHS \
                                                also supports services for families looking for care including free \
                                                referrals to childcare providers and consumer education information. \
                                                Child Care is delivered in centers and homes across the state and \
                                                includes licensed and licensed-exempt.'
                                            ),
                                            html.P(
                                                'For additional information on Illinois programs serving young \
                                                children, please see our infographic: \
                                                https://iecam.illinois.edu/blog/21206/ '
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),

                            html.Div(
                                [
                                    html.H6(html.Strong("Need Something Else?"), className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                "Couldn't find the information or data which you are looking for? We also provide the following services:"
                                            ),
                                            html.Li("IECAM Database Search: https://search.iecam.illinois.edu/cgi-bin/iecam/search.asp"),
                                            html.Li(
                                                "IECAM Data Request: https://iecam.illinois.edu/contact/data-request/"
                                            ),
                                            html.Li(
                                                "IECAM Newsletter: https://iecam.illinois.edu/newsletter/"
                                            ),
                                            html.Li(
                                                "More general queries: iecam@illinois.edu"
                                            ),
                                        ],
                                        id="reviews-bullet-pts",
                                    ),
                                    # html.Div(
                                    #     [
                                    #         html.P(
                                    #             "Developed in 2006, IECAM is currently funded by the Illinois State Board of Education (ISBE) and the Illinois Department of Human Services (IDHS)."
                                    #         ),
                                    #         html.Br([]),
                                    #         html.P(
                                    #             "* The performance of an index is not an exact representation of any particular investment, as you cannot invest directly in an index."
                                    #         ),
                                    #         html.Br([]),
                                    #         html.P(
                                    #             "Past performance is no guarantee of future returns. See performance data current to the most recent month-end."
                                    #         ),
                                    #     ],
                                    #     style={"color": "#7a7a7a"},
                                    # ),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.H6(html.Strong("About This Project"), className="subtitle padded"),
                                    html.Br([]),
                                    # html.Div(
                                    #     [
                                    #         html.Li("Launched in 1976."),
                                    #         html.Li(
                                    #             "On average, has historically produced returns that have far outpaced the rate of inflation.*"
                                    #         ),
                                    #         html.Li(
                                    #             "Quantitative Equity Group, the fund's advisor, is among the world's largest equity index managers."
                                    #         ),
                                    #     ],
                                    #     id="reviews-bullet-pts",
                                    # ),
                                    html.Div(
                                        [
                                            html.P(
                                                "This project was made possible by grant number 90TP0057-01. \
                                                Its contents are solely the responsibility of the authors and do not \
                                                necessarily represent the official view of the United States \
                                                Department of Health and Human Services, Administration for Children \
                                                and Families."
                                            ),
                                            html.Br([]),
                                            # html.P(
                                            #     "IECAM’s mission is to provide comprehensive early childhood data and maps to local and state agencies and other stakeholders in order to improve outcomes for Illinois children. Data on our website can be used to:"
                                            # ),
                                            # html.Li("make state resource allocation transparent"),
                                            # html.Li("help communities plan for early childhood services"),
                                            # html.Li("support early childhood research"),
                                            # html.Li("assist grant writers"),
                                            # html.Li("support data guided policy making"),
                                            # html.Li("provide a snapshot of the early childhood landscape in Illinois"),
                                            # html.Br([]),
                                            html.P(
                                                "Visit us at: https://iecamiafc.web.illinois.edu/"
                                            ),
                                        ],
                                        style={"color": "#000000"},
                                    ),
                                ],
                                className="row",
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
