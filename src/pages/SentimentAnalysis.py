
from dash import html, dcc
import plotly.graph_objects as go
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

# Define the text for the section
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
    dcc.Graph(figure=fig1),  # Display the bar chart
    dropdown,  # Display the dropdown
    dcc.Graph(id='sentiment-pie-chart'),  # Placeholder for the pie chart
], style={'margin': '10px'})
