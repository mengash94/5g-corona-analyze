
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
import plotly.express as px 

lang_mapping = {
    'en': 'English',
    'fr': 'French',
    'pt': 'Portuguese',
    'it': 'Italian',
    'nl': 'Dutch',
    'de': 'German',
    'pl': 'Polish',
    'fi': 'Finnish',
    'cs': 'Czech',
    'el': 'Greek',
    'lt': 'Lithuanian',
    'da': 'Danish',
    'ro': 'Romanian',
    'sl': 'Slovenian',
    'bg': 'Bulgarian',
    'iw': 'Hebrew',
    'lv': 'Latvian',
    'et': 'Estonian',
    'es': 'Spanish',
    'hu': 'Hungarian'
}

text1 = "ARIMA, which stands for AutoRegressive Integrated Moving Average, is a forecasting technique used to analyze and predict future trends in time series data."
text2 = "In our study, we use ARIMA to predict future volumes of tweets in different languages. Here's how it works:"
text3 = "<u><b>Autoregressive (AR) Part:</b></u> This examines the relationship between an observation and a certain number of lagged observations (i.e., previous observations)."
text4 = "<u><b>Integrated (I) Part:</b></u> This uses differencing to make the time series stationary—meaning that its properties don't change over time."
text5 = "<u><b>Moving Average (MA) Part:</b></u> This involves modeling the error term as a combination of previous error terms."
text6 = "By understanding these patterns and relationships in our data, ARIMA helps us forecast what the tweet volumes might look like in the future."


def ARIMA(languages):
    return html.Div([
        html.H3("ARIMA", style={'textAlign': 'left'}),
        DangerouslySetInnerHTML(f'<p style="margin-right: 10px">{text1}</p>'),
        DangerouslySetInnerHTML(f'<p style="margin-right: 10px">{text2}</p>'),
        DangerouslySetInnerHTML(f'<p style="margin-right: 10px">{text3}</p>'),
        DangerouslySetInnerHTML(f'<p style="margin-right: 10px">{text4}</p>'),
        DangerouslySetInnerHTML(f'<p style="margin-right: 10px">{text5}</p>'),
        DangerouslySetInnerHTML(f'<p style="margin-right: 10px">{text6}</p>'),
        dcc.Dropdown(
            id='language-dropdown',
            options=[{'label': lang, 'value': lang} for lang in languages],
            value=languages[0]  
                ),

        dcc.Loading(
            id="loading",
            type="cube",
            children=[
                dcc.Graph(id='forecast-plot'),
                html.Div(id='forecast-values')
            ],
            style={'height': '300px', 'width': '500px'},
        )
    ])
