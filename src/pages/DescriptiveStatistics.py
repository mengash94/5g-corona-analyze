
from dash import html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
from dash import dash_table
from plotly.graph_objs import Figure
import plotly.graph_objects as go


df_description = pd.read_csv('df_description.csv', index_col=0)
tweet_counts = pd.read_csv('tweet_counts.csv')
tweets_over_time = pd.read_csv('tweets_over_time.csv')
url_counts = pd.read_csv('url_counts.csv')
tweet_distribution = pd.read_csv('tweet_distribution.csv')
tweet_counts_no_en = pd.read_csv('tweet_counts_no_en.csv')
def DescriptiveStatistics():
    desc_table = dash_table.DataTable(
        data=df_description.reset_index().to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df_description.reset_index().columns],
        style_cell={'textAlign': 'left'},
        style_table={'height': '300px', 'width': '500px'},
    )

    # Create a bar chart of the tweet counts by language
    tweet_counts_fig = px.bar(tweet_counts, x='lang', y='count', title='Tweet Counts by Language')
    tweet_counts_fig.update_layout(autosize=False, width=900, height=400)
    
    tweets_over_time['created_at'] = pd.to_datetime(tweets_over_time['created_at'])
    tweets_over_time.set_index('created_at', inplace=True)

    tweets_over_time_fig = go.Figure()

    for lang in tweets_over_time['lang'].unique():
        df_lang = tweets_over_time[tweets_over_time['lang'] == lang]
        tweets_over_time_fig.add_trace(go.Scatter(x=df_lang.index, y=df_lang['count'], mode='lines', name=lang))
    
    # Create a pie chart
    url_pie_fig = px.pie(url_counts, names=['Contains URL', 'Does not contain URL'], title='Distribution of Tweets Containing URLs')
    url_pie_fig.update_layout(autosize=False, width=900, height=300)

    # Create a pie chart of the distribution of tweets across languages 
    tweet_pie_fig = px.pie(tweet_distribution, names='lang', values='count', title='Distribution of Tweets Across Languages')     
    tweet_pie_fig.update_layout(autosize=False, width=900, height=700)
############################## no en #####################################
    # Create a bar chart of the tweet counts by language (excluding English)
    tweet_counts_fig_no_en = px.bar(tweet_counts_no_en, x='lang', y='count', title='Tweet Counts by Language (excluding English)')
    tweet_counts_fig_no_en.update_layout(autosize=False, width=900, height=300)

    return html.Div(
    children=[
        html.H2('Descriptive Statistics', style={'text-align': 'center'}),
        desc_table,
        dcc.Loading(
            id="tweet-counts-loading",
            type="cube",
            children=[dcc.Graph(figure=tweet_counts_fig)],
        ),
        dcc.Loading(
            id="tweet-counts-no-en-loading",
            type="cube",
            children=[dcc.Graph(figure=tweet_counts_fig_no_en)],
        ),
        html.P('You can filter by clicking on the language (when languages ​​are displayed on the side)', style={'text-align': 'center'}),
        dcc.Loading(
            id="tweets-over-time-loading",
            type="cube",
            children=[dcc.Graph(figure=tweets_over_time_fig)],
        ),
        dcc.Loading(
            id="url-pie-loading",
            type="cube",
            children=[dcc.Graph(figure=url_pie_fig)],
        ),
        dcc.Loading(
            id="tweet-pie-loading",
            type="cube",
            children=[dcc.Graph(figure=tweet_pie_fig)],
        ),
       
    ],
)
