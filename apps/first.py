import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import datetime
import numpy as np
from dash.dependencies import Input, Output
from apps import common
from app import app

df = pd.read_csv('data/finalInfo.csv')

features = df.pitcher_id.unique()
features.sort()
opts = [{'label' : i, 'value' : i} for i in features]

trace_1 = go.Histogram2dContour(x = df.px, y = df.pz, colorscale = 'Jet', zmin = 1, zauto = False)
                    

layouts = go.Layout(title = 'Pitch Location',
                   hovermode = False,
                   height = 700,
                   width = 700)
fig = go.Figure(data = [trace_1], layout = layouts)

layout = html.Div([
                #common.get_header(),
                #common.get_menu(),
                html.Div([
                    html.H1("This is my first dashboard"),
                    html.P("Dash is so interesting!!")
                         ],
                     style = {'padding' : '50px' ,
                              'backgroundColor' : '#3aaab2'}),
                
                html.Div(id='app-2-display-value'),
                dcc.Link('Go to Pitch', href='/pitch'),
                

    
                dcc.Graph(id='plot-app2',figure = fig),
    
                html.P([
                    dcc.Dropdown(id = 'opt', options = opts, value = opts[0]['value'])]
                   )])

@app.callback(
    Output('plot-app2', 'figure'),
    [Input('opt', 'value')]
    )
def update_figure(input1):
    df1 = df[df.pitcher_id == input1]                  
    trace_2 = go.Histogram2dContour(x = df1.px, y = df1.pz, colorscale = 'Jet', zmin = 1, zauto = False)
    fig = go.Figure(data = [trace_2], layout = layouts)
    fig.layout.update(
    shapes=[
        # unfilled Rectangle
        go.layout.Shape(
            type="rect",
            x0=-.7083,
            y0=1.56,
            x1=.7083,
            y1=3.435,
            line=dict(
                color="Black",
            ))])
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
