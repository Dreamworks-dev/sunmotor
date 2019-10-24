import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

def get_header():
    header = html.Div([

        html.Div([
            html.H1(
                'Dash Boiler Plate')
        ], className="twelve columns padded"),       

    ], className="row gs-header gs-text-header")
    return header

def get_menu():

    ale = [
        dbc.DropdownMenuItem("New York Yankees", href = "/apps/nyy"),
        dbc.DropdownMenuItem("Tampa Bay Rays", href = "/apps/tbr"),
        dbc.DropdownMenuItem("Boston Red Sox", href = "/apps/bos"),
        dbc.DropdownMenuItem("Toronto Blue Jays", href = "/apps/tor"),
        dbc.DropdownMenuItem("Baltimore Orioles", href = "/apps/bal")
    ]
    alc = [
        dbc.DropdownMenuItem("Minnesota Twins", href = "/apps/min"),
        dbc.DropdownMenuItem("Cleveland Indians", href = "/apps/cle"),
        dbc.DropdownMenuItem("Chicago White Sox", href = "/apps/chw"),
        dbc.DropdownMenuItem("Kansas City Royals", href = "/apps/kcr"),
        dbc.DropdownMenuItem("Detroit Tigers", href = "/apps/det")
    ]
    alw = [
        dbc.DropdownMenuItem("Houston Astros", href = "/apps/hou"),
        dbc.DropdownMenuItem("Oakland A's", href = "/apps/oak"),
        dbc.DropdownMenuItem("Texas Rangers", href = "/apps/tex"),
        dbc.DropdownMenuItem("Los Angeles Angels", href = "/apps/laa"),
        dbc.DropdownMenuItem("Seattle Mariners", href = "/apps/sea")
    ]
    nle = [
        dbc.DropdownMenuItem("Atlanta Braves", href = "/apps/atl"),
        dbc.DropdownMenuItem("Washington Nationals", href = "/apps/wsn"),
        dbc.DropdownMenuItem("Philadelphia Phillies", href = "/apps/phi"),
        dbc.DropdownMenuItem("New York Mets", href = "/apps/nym"),
        dbc.DropdownMenuItem("Miami Marlins", href = "/apps/mia")
    ]
    nlc = [
        dbc.DropdownMenuItem("St. Louis Cardinals", href = "/apps/stl"),
        dbc.DropdownMenuItem("Milwakee Brewers", href = "/apps/mil"),
        dbc.DropdownMenuItem("Chicago Cubs", href = "/apps/chc"),
        dbc.DropdownMenuItem("Cincinatti Reds", href = "/apps/cin"),
        dbc.DropdownMenuItem("Pittsburg Pirates", href = "/apps/pit")
    ]
    nlw = [
        dbc.DropdownMenuItem("Los Angeles Dodgers", href = "/apps/lad"),
        dbc.DropdownMenuItem("San Diego Padres", href = "/apps/sdp"),
        dbc.DropdownMenuItem("San Fransico Giants", href = "/apps/sfg"),
        dbc.DropdownMenuItem("Arizona Diamondbacks", href = "/apps/ari"),
        dbc.DropdownMenuItem("Colorado Rockies", href = "/apps/col")
    ]

    dropdowns = html.Div(
        [
            dbc.Nav([
            dbc.NavItem(dbc.NavLink("Home", active=True, href="/apps/home", className = "m-1")),],pills=True,),
            
            dbc.DropdownMenu(
                ale, label="AL East", color="secondary", className="m-1"
            ),
            dbc.DropdownMenu(
                alc, label="AL Central", color="secondary", className="m-1"
            ),
            dbc.DropdownMenu(
                alw, label="AL West", color="secondary", className="m-1"
            ),
            dbc.DropdownMenu(
                nle, label="NL East", color="secondary", className="m-1"
            ),
            dbc.DropdownMenu(
                nlc, label="NL Central", color="secondary", className="m-1"
            ),
            dbc.DropdownMenu(nlw, label="NL West", color="secondary", className="m-1"),
        ],
        style={"display": "flex", "flexWrap": "wrap"},
    )
    return dropdowns
