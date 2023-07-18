from dash import html, dcc
import dash_table
import pandas as pd
import plotly.graph_objects as go

# Create a dataframe from your data
data = {
    'Pair': ['Lithuanian vs Portuguese', 'Spanish vs Portuguese', 'Spanish vs Lithuanian', 'English vs Italian', 'German vs Italian', 'Italian vs Polish', 'English vs Romanian', 'German vs Polish', 'Greek vs Dutch', 'English vs Polish'],
    'Correlation': [0.89, 0.88, 0.79, 0.78, 0.78, 0.74, 0.70, 0.70, 0.70, 0.70],
    'Lag': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
}
df = pd.DataFrame(data)

text_1  = '''
Hypothesis: There is a relationship or pattern between the languages ​​over time in terms of the amount of tweets
Explanation of the index- Correlation is a statistical measure showing the extent to which two variables move in relation to each other
'''

text_2  = '''
Lag in time series analysis for a certain period of time the number of tweets in a certain language lags behind another language.
For example, if a lag of 1 is found, it means today's amount of tweets in one language is perfectly correlated with yesterday's amount of tweets in the other language.
'''

long_text = ''' In our study, it was found that almost all lags are 0, the reason why we see maximum correlations at lag 0 may be because the tweets in different languages respond to the same global events related to the corona virus, which will cause increases in tweets in all languages at the same time, this confirms the assumption that the world is undergoing globalization.
Key conclusions from the analysis:
The tweets in Italian ('lt') and Portuguese ('pt') show the strongest correlation (0.89), meaning that the tweeting patterns about COVID-19 in these languages move very similarly over time.
Tweets in Spanish ('es') and Portuguese ('pt') also show a very strong correlation (0.88), as do Spanish and Italian tweets (0.79)
Tweets in English ('en') and Italian ('it') and German ('de') and Italian show strong correlations (0.78).
Interestingly, German and Polish tweets ('pl') also show a correlation of 0.70, but with a lag of 1, this means that the German tweets today are most strongly related to the Polish tweets from the previous day.
Our analysis showed that tweets in different languages tend to show similar patterns over time, especially between Lithuanian and Portuguese, and between Spanish and Portuguese. This could indicate similar feelings or identical discussions about the corona virus in these languages.

'''

def CrossCorrelation():
    return html.Div(
        className='page-container',
        children=[
            html.Div(
                className='content-container',
                children=[
                    html.H1('Cross Correlation', style={'textAlign': 'center'}),
                    html.Div(
                        className='text-container',
                        children=[
                            html.P(text_1),
                            html.P("A correlation of 1 means that the two variables are perfectly correlated, if one variable increases, the other variable also increases."),
                            html.P("A correlation of -1 (negative correlation) means that the two variables are completely inversely correlated. If one increases, the other decreases."),
                            html.P("A correlation of 0 means that there is no linear relationship between the variables."),
                            html.P(text_2),
                            html.P(long_text),
                        ],
                    ),
                ],
            ),
            html.Div(
                className='table-container',
                children=[
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in df.columns],
                        data=df.to_dict('records'),
                        style_cell={'textAlign': 'center'},
                        style_table={'height': 'auto', 'width': 'auto', 'overflow': 'auto'},
                    ),
                ],
            ),
        ],
    )
