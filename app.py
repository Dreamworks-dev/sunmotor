import dash
import flask
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

external_stylesheets = [ dbc.themes.BOOTSTRAP, 'https://codepen.io/almostburtmacklin/pen/QWWKEJb.css']
server = flask.Flask(__name__)
@server.route('/apps')
def index():
    return 'Hello Flask app'

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                server = server)

app.config.suppress_callback_exceptions = True
