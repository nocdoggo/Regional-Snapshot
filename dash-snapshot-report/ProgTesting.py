# Testing the files

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import plotly.express as px
import numpy as np  # Fuck it

import plotly.offline as pyo
"""
# Now get prefetched data folder
PATH = pathlib.Path(__file__).parent    # Perform cd..
DATA_PATH = PATH.joinpath("./prefetched").resolve()


df_race_state = pd.read_csv(DATA_PATH.joinpath("Race_Ethnicity_IL_2015-2018.csv"))
df_race_data = pd.read_csv(DATA_PATH.joinpath("SD_U-46_Race.csv"))

#rename all the columns. Both files have the same columns for race/ethnicity.
#I will just use a shorter name
df_race_state.rename(columns = {'White Alone, Non Hispanic or Latino':'White',
                    'Hispanic or Latino (of any race)':'Hispanic',
                    'Black or African American, Non-Hispanic or Latino':'Black',
                    'American Indian and Alaska Native, Non-Hispanic or Latino':'American Indian',
                    'Asian, Non-Hispanic or Latino':'Asian'
                    }, inplace = True)

df_race_data.rename(columns = {'White Alone, Non Hispanic or Latino':'White',
                    'Hispanic or Latino (of any race)':'Hispanic',
                    'Black or African American, Non-Hispanic or Latino':'Black',
                    'American Indian and Alaska Native, Non-Hispanic or Latino':'American Indian',
                    'Asian, Non-Hispanic or Latino':'Asian',
                    'Two or More Races, Non-Hispanic or Latino':'Multiracial'
                    }, inplace = True)
#df_population.rename(columns = {'Num of Sites (PFA)':'NumSites(PFA)'})
#print(df_race_state)

fiscal_year = (df_race_data['Fiscal Year'].tolist())
print(fiscal_year)

#race and Ethnicity without Chicago population
df_wo_chicago = df_race_state.loc[df_race_state['State'] == 'IL State w/o Chicago']

#race and ethnicity including Chicago population
df_state = df_race_state.loc[df_race_state['State'] == 'IL State']
print(df_wo_chicago.head())
print(df_race_data.columns)
print(df_state.columns)
df_percents_race = df_race_data.copy()
df_percents_race[['White %', 'Hispanic %', 'Black %', 'Asian %']] = df_race_data[['White', 'Hispanic', 'Black', 'Asian']].div(df_state['Total number of children'].values,axis=0)

#print((df_race_data['White'].astype(float)/df_state['White'].astype(float))*100)
print(df_race_data['White'])
print(df_state['Total number of children'])
print(df_percents_race)

data = [go.Bar(
                x=fiscal_year,
                # This shit is hard coded to hell
                y=df_race_data['White'].div(df_race_data['Total number of children'].values, axis = 0),
                #line={"color": "#97151c"},
                #mode="markers+lines",
                marker=dict(color='#1f77b4'), #set color bar to Gold
                name="White",
                ),
        go.Bar(
                x=fiscal_year,
                y=df_race_data['Black'].div(df_race_data['Total number of children'].values, axis = 0),
                marker={"color": "#ff7f0e"},
                name="Black",
                ),
        go.Bar(
                x=fiscal_year,
                y=df_race_data['Hispanic'].div(df_race_data['Total number of children'].values, axis = 0),
                marker={"color": "#7f7f7f"},
                name="Hispanic",
                ),
        go.Bar(
                x=fiscal_year,
                y=df_race_data['Asian'].div(df_race_data['Total number of children'].values, axis = 0),
                marker={"color": "#bcbd22"},
                name="Asian"
                ),
        go.Bar(
                x=fiscal_year,
                y=df_race_data['Multiracial'].div(df_race_data['Total number of children'].values, axis = 0),
                marker={"color": "#8c564b"},
                name="Multiracial"
        )]

#layout = [go.Layout(
#                    title = 'Race Ethnicity',

#        )]
layout = go.Layout(
                    autosize=True,
                    title="",
                    font={"family": "Raleway", "size": 10},
                    height=400,
                    width=720,
                    bargap = 0.4,
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
                        "range": [df_race_state['Fiscal Year'].min(), df_race_state['Fiscal Year'].max()],
                        "showgrid": False,
                        "showline": True,
                        # I mean. Everyone knows it is year.
                        # "title": "Fiscal Year",
                        "type": "linear",
                    },
                    yaxis={
                        "autorange": False,
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
                        "range": [0, 1],
                        "showgrid": True,
                        "showline": True,
                        "ticklen": 10,

                        "ticks": "outside",
                        "tickformat":".0%",
                        "title": "Students",
                        "type": "linear",
                        "zeroline": False,
                        "zerolinewidth": 4
                        }
                    )


fig = go.Figure(data = data, layout = layout)

fig.show()
"""

"""

import platform
trace0 = go.Scatter(
    x=[1.5, 4.5],
    y=[0.75, 0.75],
    text='',
    mode='text'
)
data = [trace0]
layout = {'width':700,
          'height':350,
          'xaxis': {'range': [2, 7],
                    'showgrid': False,
                    'zeroline':False,
                    'visible':False},
          'yaxis': {'range': [0.5, 2.5],
          'showgrid': False,
          'zeroline':False,
          'visible':False},
          #'paper_bgcolor':'rgba(0,0,0,0)',
          'plot_bgcolor':'rgba(0,0,0,0)',
          'shapes': [
                    # filled Rectangle
                    {
                    'type': 'rect',
                    'x0': 3,
                    'y0': 1,
                    'x1': 6,
                    'y1': 2,
                    'line': {
                    'color': 'rgba(128, 0, 128, 1)',
                    'width': 2,
                    },
                    'fillcolor': 'rgba(128, 0, 128, 0.7)'
                    }]}
#fw = go.FigureWidget(data=data, layout=layout)

x0 = 3
y0 = 1
x1 = 6
y1 = 2
h = 0.2
rounded_bottom_left = f' M {x0+h}, {y0} Q {x0}, {y0} {x0}, {y0+h}'
rounded_top_left = f' L {x0}, {y1-h} Q {x0}, {y1} {x0+h}, {y1}'
rounded_top_right = f' L {x1-h}, {y1} Q {x1}, {y1} {x1}, {y1-h}'
rounded_bottom_right = f' L {x1}, {y0+h} Q {x1}, {y0} {x1-h}, {y0}Z'
path = rounded_bottom_left + rounded_top_left+\
         rounded_top_right+rounded_bottom_right


fig = go.Figure(data = data, layout = layout)

fig2 = go.Figure(data=fig.data, layout=fig.layout)

fig2.layout.shapes = [dict(type='path',
                          path=path,
                          fillcolor='rgba(128, 0, 128, 0.7)',
                          layer='above',
                          line=dict(color='rgba(128, 0, 128, 0.7)', width=0.5))]


fig2.show()

"""

#Let's try using matplotlib
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch

# Bbox object around which the fancy box will be drawn.
bb = mtransforms.Bbox([[0.3, 0.4], [0.7, 0.6]])


def draw_bbox(ax, bb):
    # boxstyle=square with pad=0, i.e. bbox itself.
    p_bbox = FancyBboxPatch((bb.xmin, bb.ymin),
                            abs(bb.width), abs(bb.height),
                            boxstyle="square,pad=0.",
                            ec="k", fc="none", zorder=10.,
                            )
    ax.add_patch(p_bbox)


def test1(ax):

    # a fancy box with round corners. pad=0.1
    p_fancy = FancyBboxPatch((bb.xmin, bb.ymin),
                             abs(bb.width), abs(bb.height),
                             boxstyle="round,pad=0.1",
                             fc=(1., .8, 1.),
                             ec=(1., 0.5, 1.))

    ax.add_patch(p_fancy)

    ax.text(0.1, 0.8,
            r' boxstyle="round,pad=0.1"',
            size=10, transform=ax.transAxes)

    # draws control points for the fancy box.
    # l = p_fancy.get_path().vertices
    # ax.plot(l[:,0], l[:,1], ".")

    # draw the original bbox in black
    draw_bbox(ax, bb)

"""
plt.clf()
fig, ax = plt.subplots(figsize=(5,3))

test1(ax)
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)
ax.set_title("test1")
ax.set_aspect(1.)

plt.show()
"""

import pandas as pd
import numpy as np
# make up some example data
np.random.seed(0)
df = pd.DataFrame(np.random.uniform(0,20, size=(2,4)))
df = df.div(df.sum(1), axis=0)
# plot a stacked horizontal bar chart
ax = df.plot.barh(stacked=True, width=1, legend=False)
ax.figure.set_size_inches(6,6)


new_patches = []
for patch in reversed(ax.patches):
    bb = patch.get_bbox()
    color=patch.get_facecolor()
    p_bbox = FancyBboxPatch((bb.xmin, bb.ymin),
                        abs(bb.width), abs(bb.height),
                        boxstyle="round,pad=-0.0040,rounding_size=0.015",
                        ec="none", fc=color,
                        mutation_aspect=4
                        )
    patch.remove()
    new_patches.append(p_bbox)
for patch in new_patches:
    ax.add_patch(patch)

plt.show()
print(df.head())
print(df)


'''
fig = px.scatter(df_population, x='Fiscal Year', y = 'Proposed Capacity(PFA)',
                size = 'Proposed Capacity(PFA)', size_max = 60, color = 'Num of Sites (PFA)')

fig.show()

fig2 = px.bar(df_population, x='Fiscal Year', y='Proposed Capacity(PFA)',
                color='Num of Sites (PFA)', barmode='group', hover_data=['Num of Sites (PFA)', 'Proposed Capacity(PFA)'])
fig2.show()
'''
