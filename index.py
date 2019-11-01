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
#from apps import nyy
#from apps import tbr
#from apps import bos
#from apps import tor
#from apps import mins
#from apps import cle
#from apps import chw
#from apps import kcr
#from apps import det
#from apps import hou
#from apps import oak
#from apps import tex
#from apps import laa
#from apps import sea
#from apps import atl
#from apps import wsn
#from apps import phi
#from apps import nym
#from apps import mia
#from apps import stl
from apps import mil
#from apps import chc
#from apps import cin
#from apps import pit
#from apps import lad
#from apps import sdp
#from apps import sfg
#from apps import ari
#from apps import col

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
    elif pathname == '/bal':
        return bal.layout
    elif pathname == '/nyy':
        from apps import nyy
        return nyy.layout
    elif pathname == '/tbr':
        from apps import tbr
        return tbr.layout
    elif pathname == '/bos':
        from apps import bos
        return bos.layout
    elif pathname == '/tor':
        from apps import tor
        return tor.layout
    elif pathname == '/mins':
        from apps import mins
        return mins.layout
    elif pathname == '/cle':
        from apps import cle
        return cle.layout
    elif pathname == '/chw':
        from apps import chw
        return chw.layout
    elif pathname == '/kcr':
        from apps import kcr
        return kcr.layout
    elif pathname == '/det':
        return det.layout
    elif pathname == '/hou':
        return hou.layout
    elif pathname == '/oak':
        return oak.layout
    elif pathname == '/tex':
        return tex.layout
    elif pathname == '/laa':
        return laa.layout
    elif pathname == '/sea':
        return sea.layout
    elif pathname == '/atl':
        return atl.layout
    elif pathname == '/wsn':
        return wsn.layout
    elif pathname == '/phi':
        return phi.layout
    elif pathname == '/nym':
        return nym.layout
    elif pathname == '/mia':
        return mia.layout
    elif pathname == '/stl':
        return stl.layout
    elif pathname == '/mil':
        return mil.layout
    elif pathname == '/chc':
        return chc.layout
    elif pathname == '/cin':
        return cin.layout
    elif pathname == '/pit':
        return pit.layout
    elif pathname == '/lad':
        return lad.layout
    elif pathname == '/sdp':
        return sdp.layout
    elif pathname == '/sfg':
        return sfg.layout
    elif pathname == '/ari':
        return ari.layout
    elif pathname == '/col':
        return col.layout
    else:
        return first.layout


if __name__ == '__main__':
    app.run_server(debug=True)
