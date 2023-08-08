import dash
import dash_html_components as html

text_1 = "This project aims to understand the depth and distribution of false information on Twitter during the COVID-19 crisis, with a focus on European countries and Israel. The main goal is to enhance the accuracy and reliability of information disseminated on social media during global crises and emergencies."

methods = [
    ("1. Sentiment Analysis:", " We use the Vader sentiment analysis tool to quantify the emotion in each tweet related to COVID-19."),
    ("2. Data Visualization:", " We visualize the sentiment scores and tweet frequencies over time to understand trends in public opinion and discussion volume."),
    ("3. Text Preprocessing:", " We clean and preprocess tweet text to facilitate further analysis."),
    ("4. Word Clouds:", " We generate word clouds to visualize the most frequently used words in tweets across different languages."),
    ("5. Time Series Forecasting:", " We use ARIMA models to predict the future volume of COVID-19 related tweets in different languages."),
    ("6. Text Classification with BERT:", " We use BERT, a state-of-the-art language processing model, to classify the sentiment of tweets.")
]

text_3 = "The insights gained from this project can help social media platforms, public health organizations, and governments understand public sentiment during a crisis, monitor the spread of misinformation, and develop strategies to mitigate its impact. This project is a step towards ensuring the safety and well-being of individuals and communities by promoting the dissemination of accurate and reliable information during global crises and emergencies."

def Projectdetails():
    return html.Div([
        html.H3('Analyzing and Monitoring False Information on Twitter During the COVID-19 Crisis'),
        html.P(text_1),
        html.H3('Methods: We employ several data analysis techniques:'),
        html.Div([html.P([html.Strong(html.U(headline)), desc]) for (headline, desc) in methods]),
        html.H3('Findings:'),
        html.P(text_3)
    ], style={'backgroundColor': 'white', 'color': 'black', 'padding': '15px'})
