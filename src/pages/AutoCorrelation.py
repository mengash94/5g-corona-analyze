

from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Define text for each section
text_1 = '''
Our hypothesis here is that there might be a correlation within a single language's tweet volume over time. This is what we call 'autocorrelation'. Unlike normal correlation, autocorrelation doesn't compare two different variables. Instead, it examines one variable - in our case, the tweet volume in a single language - at different points in time.
'''
text_2 = '''
In autocorrelation, we look at 'lags' within the same language. For example, a lag of 1 would compare the tweet volume today with the tweet volume from yesterday.
'''

text_3 = '''
You can select a language from our data to explore its autocorrelation and understand how its tweet volume changes over time.
'''

text_4 = '''
Our analysis found a positive autocorrelation of 1 in all languages. This means that the intensity of tweets discussing the 5G conspiracy theory is somewhat dependent on the previous day's tweet volume.
'''

text_5 = '''
The strength of this correlation, however, varies between languages. For instance:

- English tweets show the highest correlation at a lag of 1 (0.9163).

- In contrast, Hebrew tweets have the lowest correlation at a lag of 1 (0.1464).

These findings suggest that the dynamics and persistence of 5G conspiracy theory discussions differ across languages.
'''

text_6 = '''
While most languages show decreasing correlation values as the lag increases (which is expected in time-series data), there are exceptions. For instance, Dutch tweets show an increase in autocorrelation values after a lag of 2, peaking at a lag of 5 (0.7656).
'''

def AutoCorrelation(pivot_df):
    return html.Div([
        html.H3('Exploring AutoCorrelation', style={'textAlign': 'left'}),
        html.P(text_1, style={'margin-right': '10px'}),

        html.H3('What is AutoCorrelation?', style={'textAlign': 'left'}),
        html.P(text_2, style={'margin-right': '10px'}),

        html.H3('Analyzing Lags within a Language', style={'textAlign': 'left'}),
        html.P(text_3, style={'margin-right': '10px'}),

        html.H3('Choose a Language to Analyze', style={'textAlign': 'left'}),
        dcc.Dropdown(
            id='language-dropdown',
            options=[{'label': i, 'value': i} for i in pivot_df.columns],
            value='Dutch'
        ),
        dcc.Graph(id='autocorrelation-graph'),

        html.H3('Conclusions', style={'textAlign': 'left'}),
        html.P(text_4, style={'margin-right': '10px'}),

        html.H3('Different Patterns Across Languages', style={'textAlign': 'left'}),
        html.P(text_5, style={'margin-right': '10px'}),

        html.H3('Interesting Findings', style={'textAlign': 'left'}),
        html.P(text_6, style={'margin-right': '10px'}),
    ])



