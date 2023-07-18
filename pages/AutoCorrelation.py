from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

text_1 = '''
Hypothesis: There is a correlation in the amount of tweets within a single time series.
Explanation of the index: unlike normal correlation, automatic correlation is a test of lag in the time series in the language itself - that is, 
the comparison is not between 2 languages, but between the same language at different times.
'''
text_2 = '''
A positive lagged correlation of 1 was found in all languages, indicating that the tweets discussing the conspiracy theory have some degree of dependence on the intensity of the previous day's tweets.
The strength of the aforementioned correlation varies between languages. For example, tweets in English (en) show the highest correlation at lag 1 (0.9163), while tweets in Hebrew (iw) show the lowest (0.1464). This indicates that the conversational dynamics and persistence of discussions The G5 conspiracy theory differs between different languages.

In most languages, the correlation values decrease as the lag increases, which is expected in time series data. However, some languages, such as Dutch (nl), show an increase in autocorrelation values after a lag of 2 (0.7410), peaking at a lag of 5 (0.7656).
'''
def AutoCorrelation(pivot_df):
    return html.Div([
        html.H3('AutoCorrelation'),
        html.P(text_1,style={'margin-top': '10px'}),
        html.P('choose the language to show the lags:'),
        dcc.Dropdown(
            id='language-dropdown',
            options=[{'label': i, 'value': i} for i in pivot_df.columns],
            value='Dutch'
        ),
        dcc.Graph(id='autocorrelation-graph'),
        html.H3('Conclusions from the analysis:'),
        html.P(text_2,style={'margin-top': '10px'}),

    ])


