import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app
from app import server
from apps import pitch
from apps import first
from apps import bal
from apps import nyy
from apps import tor
from apps import tbr
from apps import bos


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/first':
        return first.layout
    elif pathname == '/pitch':
        return pitch.layout
    elif pathname == '/apps/bal':
        return bal.layout
    elif pathname == '/apps/nyy':
        return nyy.layout
    elif pathname == '/apps/tbr':
        return tbr.layout
    elif pathname == '/apps/bos':
        return bos.layout
    elif pathname == '/apps/tor':
        return tor.layout
    else:
        return first.layout


if __name__ == '__main__':
    app.run_server(debug=True)
