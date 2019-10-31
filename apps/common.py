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
        dbc.DropdownMenuItem("New York Yankees", href = "/nyy"),
        dbc.DropdownMenuItem("Tampa Bay Rays", href = "/tbr"),
        dbc.DropdownMenuItem("Boston Red Sox", href = "/bos"),
        dbc.DropdownMenuItem("Toronto Blue Jays", href = "/tor"),
        dbc.DropdownMenuItem("Baltimore Orioles", href = "/bal")
    ]
    alc = [
        dbc.DropdownMenuItem("Minnesota Twins", href = "/mins"),
        dbc.DropdownMenuItem("Cleveland Indians", href = "/cle"),
        dbc.DropdownMenuItem("Chicago White Sox", href = "/chw"),
        dbc.DropdownMenuItem("Kansas City Royals", href = "/kcr"),
        dbc.DropdownMenuItem("Detroit Tigers", href = "/det")
    ]
    alw = [
        dbc.DropdownMenuItem("Houston Astros", href = "/hou"),
        dbc.DropdownMenuItem("Oakland A's", href = "/oak"),
        dbc.DropdownMenuItem("Texas Rangers", href = "/tex"),
        dbc.DropdownMenuItem("Los Angeles Angels", href = "/laa"),
        dbc.DropdownMenuItem("Seattle Mariners", href = "/sea")
    ]
    nle = [
        dbc.DropdownMenuItem("Atlanta Braves", href = "/atl"),
        dbc.DropdownMenuItem("Washington Nationals", href = "/wsn"),
        dbc.DropdownMenuItem("Philadelphia Phillies", href = "/phi"),
        dbc.DropdownMenuItem("New York Mets", href = "/nym"),
        dbc.DropdownMenuItem("Miami Marlins", href = "/mia")
    ]
    nlc = [
        dbc.DropdownMenuItem("St. Louis Cardinals", href = "/stl"),
        dbc.DropdownMenuItem("Milwakee Brewers", href = "/mil"),
        dbc.DropdownMenuItem("Chicago Cubs", href = "/chc"),
        dbc.DropdownMenuItem("Cincinatti Reds", href = "/cin"),
        dbc.DropdownMenuItem("Pittsburg Pirates", href = "/pit")
    ]
    nlw = [
        dbc.DropdownMenuItem("Los Angeles Dodgers", href = "/lad"),
        dbc.DropdownMenuItem("San Diego Padres", href = "/sdp"),
        dbc.DropdownMenuItem("San Fransico Giants", href = "/sfg"),
        dbc.DropdownMenuItem("Arizona Diamondbacks", href = "/ari"),
        dbc.DropdownMenuItem("Colorado Rockies", href = "/col")
    ]

    dropdowns = html.Div(
        [
            dbc.Nav([
            dbc.NavItem(dbc.NavLink("Home", active=True, href="/home", className = "m-1")),],pills=True,),
            
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
