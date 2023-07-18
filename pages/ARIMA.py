from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML


def ARIMA(languages):
    return html.Div([
        html.H3("ARIMA model"),
        dcc.Dropdown(
            id='arima-language-dropdown',  # changed id
            options=[{'label': i, 'value': i} for i in languages],
            value='Hebrew'
        ),
        dcc.Loading(
            id="loading",
            type="cube",
            children=[
                dcc.Graph(id='arima-graph'),
                html.Br(),
                dbc.Card(id='arima-summary-card'),  # use this instead of html.Div
                dbc.Card(id='arima-summary-card')
            ],
            style={'height': '300px', 'width': '500px'},
        )
    ])
