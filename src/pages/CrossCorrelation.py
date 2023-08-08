from dash import html, dcc
import dash_table
import pandas as pd
import plotly.graph_objects as go


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

long_text = ''' Most of the lags we found were 0. This could be because global COVID-19 events trigger similar reactions across languages simultaneously, hinting at the world's increasing interconnectedness.
'''

conclusions = [
    "Italian and Portuguese tweets move almost hand-in-hand (correlation: 0.89).",
    "Spanish and Portuguese, and Spanish and Italian tweets also show strong correlations (0.88 and 0.79, respectively).",
    "English and Italian, as well as German and Italian, show a strong relationship (0.78).",
    "Intriguingly, German tweets today are strongly tied to Polish tweets from the previous day (correlation: 0.70, lag: 1)."
]

summary = "In summary, our study suggests that different languages show similar tweeting patterns over time, possibly reflecting shared sentiments or discussions around the pandemic."

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
                            html.H2('What Does Correlation Mean?', style={'textAlign': 'left'}),
                            html.P("A correlation of 1 means perfect positive correlation: as one variable goes up, so does the other."),
                            html.P("A correlation of -1 indicates perfect negative correlation: as one variable increases, the other decreases."),
                            html.P("A correlation of 0 suggests no linear relationship between the variables."),
                            html.H2('Lag in Time Series', style={'textAlign': 'left'}),
                            html.P(text_2),
                            html.H2('Our Findings', style={'textAlign': 'left'}),
                            html.P(long_text),
                            html.H3('Key Conclusions', style={'textAlign': 'left'}),
                            html.Ul([html.Li(item) for item in conclusions]),
                            html.P(summary),
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
