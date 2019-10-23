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
        dbc.DropdownMenuItem("New York Yankees", href = "/apps/yankees"),
        dbc.DropdownMenuItem("Tampa Bay Rays", href = "/apps/rays"),
        dbc.DropdownMenuItem("Boston Red Sox", href = "/apps/redsox"),
        dbc.DropdownMenuItem("Toronto Blue Jays", href = "/apps/jays"),
        dbc.DropdownMenuItem("Baltimore Orioles", href = "/apps/os")
    ]
    alc = [
        dbc.DropdownMenuItem("Minnesota Twins", href = "/apps/twins"),
        dbc.DropdownMenuItem("Cleveland Indians", href = "/apps/indians"),
        dbc.DropdownMenuItem("Chicago White Sox", href = "/apps/whitesoxs"),
        dbc.DropdownMenuItem("Kansas City Royals", href = "/apps/royals"),
        dbc.DropdownMenuItem("Detroit Tigers", href = "/apps/tigers")
    ]
    alw = [
        dbc.DropdownMenuItem("Minnesota Twins", href = "/apps/twins"),
        dbc.DropdownMenuItem("Cleveland Indians", href = "/apps/indians"),
        dbc.DropdownMenuItem("Chicago White Sox", href = "/apps/whitesoxs"),
        dbc.DropdownMenuItem("Kansas City Royals", href = "/apps/royals"),
        dbc.DropdownMenuItem("Detroit Tigers", href = "/apps/tigers")
    ]
    nle = [
        dbc.DropdownMenuItem("Atlanta Braves", href = "/apps/twins"),
        dbc.DropdownMenuItem("Cleveland Indians", href = "/apps/indians"),
        dbc.DropdownMenuItem("Chicago White Sox", href = "/apps/whitesoxs"),
        dbc.DropdownMenuItem("Kansas City Royals", href = "/apps/royals"),
        dbc.DropdownMenuItem("Detroit Tigers", href = "/apps/tigers")
    ]
    nlc = [
        dbc.DropdownMenuItem("St. Louis Cardinals", href = "/apps/twins"),
        dbc.DropdownMenuItem("Cleveland Indians", href = "/apps/indians"),
        dbc.DropdownMenuItem("Chicago White Sox", href = "/apps/whitesoxs"),
        dbc.DropdownMenuItem("Kansas City Royals", href = "/apps/royals"),
        dbc.DropdownMenuItem("Detroit Tigers", href = "/apps/tigers")
    ]
    nlw = [
        dbc.DropdownMenuItem("Los Angeles Dodgers", href = "/apps/twins"),
        dbc.DropdownMenuItem("Cleveland Indians", href = "/apps/indians"),
        dbc.DropdownMenuItem("Chicago White Sox", href = "/apps/whitesoxs"),
        dbc.DropdownMenuItem("Kansas City Royals", href = "/apps/royals"),
        dbc.DropdownMenuItem("Detroit Tigers", href = "/apps/tigers")
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
