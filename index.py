import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app
from apps import pitch, first


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
    else:
        return first.layout


if __name__ == '__main__':
    app.run_server(debug=True)
