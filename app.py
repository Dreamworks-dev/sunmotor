import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from scout_apm.flask import ScoutApm

external_stylesheets = [ dbc.themes.BOOTSTRAP, 'https://codepen.io/almostburtmacklin/pen/QWWKEJb.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}])
server = app.server
app.config.suppress_callback_exceptions = True



ScoutApm(app)

app.config["SCOUT_MONITOR"] = True
app.config["SCOUT_KEY"] = "DLHussA7KhTv6t1G8CmG"
app.config["SCOUT_NAME"] = "Baseball Webb App"
