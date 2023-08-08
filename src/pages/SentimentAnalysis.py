
from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd
daily_sentiment_avg = pd.read_csv('daily_sentiment_avg.csv')

daily_sentiment_avg['date'] = pd.to_datetime(daily_sentiment_avg['date'])

dropdown = dcc.Dropdown(
    id='language-dropdown',
    options=[{'label': 'All', 'value': 'all'}] +
            [{'label': str(lang) if lang is not None else 'None', 'value': str(lang) if lang is not None else 'None'} for lang in daily_sentiment_avg['lang'].unique()],
    value='all'  
)


text1 = "Sentiment Analysis is a powerful technique that allows us to determine the emotional tone behind a piece of text. In our case, we're applying it to tweets about the 5G-COVID-19 conspiracy theory."
text2 = "By analyzing the text data in these tweets, we can identify and classify the opinions, attitudes, and emotions expressed by Twitter users. This gives us a better understanding of the overall sentiment towards the conspiracy theory."
text3 = "Is the prevailing sentiment positive, suggesting support for the theory? Or is it negative, indicating disbelief or criticism? Or perhaps it's neutral, neither endorsing nor rejecting the theory outright?"
text4 = "Through Sentiment Analysis, we can begin to answer these questions and gain a deeper understanding of public sentiment around this controversial issue."

layout = html.Div([
    html.H3('Sentiment Analysis', style={'textAlign': 'left', 'margin-right': '10px'}),
    html.P(text1 ),
    html.P(text2),
    html.P(text3),
    html.P(text4),
    dropdown, 
    dcc.Graph(id='sentiment-line-chart'),
], style={'margin': '10px'})
