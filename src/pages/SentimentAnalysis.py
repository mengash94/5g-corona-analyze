from dash import html, dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Load the data
avg_sentiment_scores = pd.read_csv('avg_sentiment_scores.csv')

# Create a bar chart with languages on x-axis and average sentiment scores on y-axis
fig1 = go.Figure(data=[
    go.Bar(x=avg_sentiment_scores['lang'], y=avg_sentiment_scores['sentiment_polarity'])
])

# Update layout of the figure
fig1.update_layout(title_text='Average Sentiment Scores by Language')

# Create a dropdown for selecting language
dropdown = dcc.Dropdown(
    id='language-dropdown',
    options=[{'label': 'All', 'value': 'all'}] +
            [{'label': str(lang) if lang is not None else 'None', 'value': str(lang) if lang is not None else 'None'} for lang in avg_sentiment_scores['lang'].unique()],
    value='all'  # Default value
)


layout = html.Div([
    html.H3('Sentiment Analysis'),
    html.P('Sentiment Analysis is a technique used to determine the sentiment or emotional tone expressed in a piece of text. It involves analyzing text data to identify and classify opinions, attitudes, and emotions conveyed by individuals. The goal of sentiment analysis is to understand the overall sentiment behind a given text, whether it is positive, negative, or neutral.'),
    dcc.Graph(figure=fig1),  # Display the bar chart
    dropdown,  # Display the dropdown
    dcc.Graph(id='sentiment-pie-chart'),  # Placeholder for the pie chart
]),

sentiment_analysis_layout = html.Div([
    html.H3('Sentiment Analysis'),
    html.P('This is the Sentiment Analysis page.'),
    dcc.Graph(figure=fig1),  # Display the bar chart
    dropdown,  # Display the dropdown
    dcc.Graph(id='sentiment-pie-chart'),  # Placeholder for the pie chart
])