import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

external_stylesheets = [ dbc.themes.BOOTSTRAP, 'https://codepen.io/almostburtmacklin/pen/QWWKEJb.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets )
server = app.server
app.config.suppress_callback_exceptions = True
