import dash
from dash import html
from dash.dependencies import Input, Output
from dash import dcc
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
import plotly.graph_objects as go
from collections import defaultdict
import pmdarima as pm
import plotly.graph_objects as go
# import dash_core_components as dcc
from flask_caching import Cache
from pages.DescriptiveStatistics import DescriptiveStatistics
from pages.CrossCorrelation import CrossCorrelation
from pages.AutoCorrelation import AutoCorrelation
from pages.SentimentAnalysis import SentimentAnalysis
from pages.ARIMA import ARIMA
from pages.BERT import BERT
from pages.AboutResearchers import AboutWriter
from pages.ContactUs import ContactUs
from pages.Projectdetails import Projectdetails

app = dash.Dash(__name__, suppress_callback_exceptions=True)
# app = dash.Dash(__name__, )

# Initialize the cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
cache.clear()
########################      AutoCorrelation  ###############
# df = pd.read_csv("5g.csv")
# # Convert datetime_column to a datetime type
# df['created_at'] = pd.to_datetime(df['created_at'])
# # sort the DataFrame by the date_column
# df = df.sort_values('created_at').reset_index(drop=True)
# # Create a new date column
# df['date_column'] = df['created_at'].dt.date
# # Define the mapping from language codes to full names
# language_dict = {
#     'bg': 'Bulgarian',
#     'cs': 'Czech',
#     'da': 'Danish',
#     'nl': 'Dutch',
#     'en': 'English',
#     'et': 'Estonian',
#     'fr': 'French',
#     'tl': 'Filipino',
#     'es': 'Spanish',
#     'de': 'German',
#     'pt': 'Portuguese',
#     'it': 'Italian',
#     'in': 'Indonesian',
#     'eu': 'Basque',
#     'ht': 'Haitian Creole',
#     'vi': 'Vietnamese',
#     'sv': 'Swedish',
#     'hu': 'Hungarian',
#     'tr': 'Turkish',
#     'pl': 'Polish',
#     'ca': 'Catalan',
#     'hi': 'Hindi',
#     'no': 'Norwegian',
#     'fi': 'Finnish',
#     'el': 'Greek',
#     'lv': 'Latvian',
#     'lt': 'Lithuanian',
#     'ro': 'Romanian',
#     'sl': 'Slovenian',
#     'iw': 'Hebrew',
#     'und': 'Undefined'
# }

# # Replace the language codes with their full names
# df['lang'] = df['lang'].map(language_dict)

# # Define the list of languages to remove
# remove_langs = ['Bulgarian', 'Czech', 'Danish', 'Greek', 'Estonian', 'Hungarian', 'Hebrew', 'Latvian', 'Slovenian', 'English']

# # Filter out the languages in 'remove_langs' from the DataFrame
# df_filtered = df[~df['lang'].isin(remove_langs)]

# df_filtered['created_at'] = pd.to_datetime(df_filtered['created_at'])
# df_filtered['date_column'] = df_filtered['created_at'].dt.date

# # Assuming pivot_df is your dataframe with tweet counts for each language
# grouped_df =df_filtered.groupby(['lang', 'date_column']).size().reset_index(name='tweet_count')

# # Pivot the table to have languages as columns and dates as rows
# pivot_df = grouped_df.pivot_table(index='date_column', columns='lang', values='tweet_count', fill_value=0)####################################

# ################################ ARIMA #################################
# # Convert 'created_at' column to datetime
# df['created_at'] = pd.to_datetime(df['created_at'])

# # Set 'created_at' as the index
# df.set_index('created_at', inplace=True)

# # Resample the DataFrame to daily frequency by 'lang' and count the number of tweets
# tweets_per_day_by_lang = df.groupby('lang').resample('D').count()['id'].reset_index()

# # Group by language and resample to daily tweet count
# tweets_per_day_by_lang = df.groupby('lang').resample('D').count()['id'].reset_index()
#mangasha drive
df_arima=pd.read_csv("filtered_data.csv")

# group the data by language and compute the count of tweets for each language
lang_counts_arima = df_arima.groupby('lang').count()['original_text']

# # filter out the
# #  languages that have less than 100 tweets
# filtered_langs_arima = lang_counts_arima[lang_counts_arima >= 100].index

# # filter the dataframe to keep only the tweets in the filtered languages
# df_arima = df_arima[df_arima['lang'].isin(filtered_langs_arima)]

df_arima['created_at'] = pd.to_datetime(df_arima['created_at'])
df_arima.set_index('created_at', inplace=True)

# Group by language and resample to daily tweet count
tweets_per_day_by_lang = df_arima.groupby('lang').resample('D').count()['id'].reset_index()
tweets_per_day_by_lang.to_csv('tweets_per_day_by_lang.csv', index=False)

# pivot_df = pd.read_csv('pivot_df.csv')
# tweets_per_day_by_lang = pd.read_csv('tweets_per_day_by_lang.csv')
languages = tweets_per_day_by_lang['lang'].unique()
#################################################################
app.layout = html.Div([
    html.H1('5G Conspiracy Theory in Corona', style={'text-align': 'center'}),
    html.P('By Mengsha  Ataly and Yakir Attias', style={'text-align': 'center'}),
    dcc.Location(id='url', refresh=False),
    dcc.Tabs(id="tabs", value='/', children=[
        dcc.Tab(label='Home', value='/'),
        dcc.Tab(label='About the Writer', value='/about-writer'),
        dcc.Tab(label='Project Details', value='/project-details'),
        dcc.Tab(label='Contact Us', value='/contact-us'),
    ]),
    html.Div(id='tabs-content', className='site-container')
], className='site-container')

@app.callback(Output('tabs-content', 'children'),
              [Input('url', 'pathname')])
def render_content(pathname):
    if pathname == '/':
        return html.Div([
            html.H3('Short Explanation'),
            html.P('The 5G conspiracy theory in relation to the Corona pandemic suggests a false claim that 5G technology is somehow linked to the spread of the virus. This theory has gained traction in certain online communities despite being debunked by scientific evidence and experts.'),
            html.Div(id='tabs-and-content', children=[
                dcc.Tabs(id='nested-tabs', value='nested-tab-1',vertical=True, children=[
                    dcc.Tab(label='Descriptive Statistics', value='nested-tab-1'),
                    dcc.Tab(label='Cross Correlation', value='nested-tab-2'),
                    dcc.Tab(label='Auto Correlation', value='nested-tab-3'),
                    dcc.Tab(label='Sentiment Analysis', value='nested-tab-4'),
                    dcc.Tab(label='ARIMA', value='nested-tab-5'),
                    dcc.Tab(label='BERT', value='nested-tab-6'),
                ]),
            html.Div(id='nested-tabs-content')
            ])
        ])
    elif pathname == '/about-writer':
        return AboutWriter()
    elif pathname == '/project-details':
        return Projectdetails()
    elif pathname == '/contact-us':
        return ContactUs()

@app.callback(Output('nested-tabs-content', 'children'),
              [Input('nested-tabs', 'value')])
@cache.memoize()  # Use the cache to store the results of this function
def render_nested_content(tab_value):
    if tab_value == 'nested-tab-1':
        return DescriptiveStatistics()
    elif tab_value == 'nested-tab-2':
        return CrossCorrelation()
    elif tab_value == 'nested-tab-3':
        return AutoCorrelation(pivot_df)
    elif tab_value == 'nested-tab-4':
        return SentimentAnalysis()
    elif tab_value == 'nested-tab-5':
        return ARIMA(languages)
    elif tab_value == 'nested-tab-6':
        return BERT()

@app.callback(Output('url', 'pathname'),
              [Input('tabs', 'value')])
def update_url(tab_value):
    return tab_value
@app.callback(
    Output('autocorrelation-graph', 'figure'),
    Input('language-dropdown', 'value')
)
def update_graph(selected_language):
    lags = [1, 2, 3, 4, 5]
    autocorrelation_values = [pivot_df[selected_language].autocorr(lag=lag) for lag in lags]

    figure = go.Figure(data=go.Scatter(x=lags, y=autocorrelation_values))
    figure.update_layout(
        autosize=False,
        width=700,
        height=300
    )

    return figure

#################################### ARIMA #################################
def fit_auto_arima(series, forecast_periods=10):
    try:
        model = pm.auto_arima(series, suppress_warnings=True, seasonal=False, stepwise=True)
        forecast, conf_int = model.predict(n_periods=forecast_periods, return_conf_int=True)
        return model, forecast, conf_int
    except Exception as e:
        print(f"Failed to fit model: {e}")
        return None, None, None

@app.callback(
    Output('arima-graph', 'figure'),
    [Input('arima-language-dropdown', 'value')]  # changed id
)

def update_arima_graph(selected_lang_arima):
    lang_data = tweets_per_day_by_lang[tweets_per_day_by_lang['lang'] == selected_lang_arima]
    lang_data.set_index('created_at', inplace=True)
    lang_series = lang_data['id']


    # We'll use 80% of our data for training, 20% for testing
    split_point = int(len(lang_series) * 0.8)
    train, test = lang_series[:split_point], lang_series[split_point:]

    model, _, _ = fit_auto_arima(train, forecast_periods=len(test))

    # Generate predictions for the dates in the test set
    forecast = model.predict(n_periods=len(test))
    # Create the plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=test.index, y=test, mode='lines', name='Actual'))
    fig.add_trace(go.Scatter(x=test.index, y=forecast, mode='lines', name='Predicted'))
    fig.update_layout(title=f"ARIMA Model Forecast vs Actuals for Language: {selected_lang_arima}",
                    xaxis_title='Date',
                    yaxis_title='Tweet Count',
                    )
    fig.update_layout(
        autosize=False,
        width=700,
        height=300
    )


    return fig

# Callback to update the ARIMA summary
@app.callback(
    Output('arima-summary', 'children'),
    [Input('arima-language-dropdown', 'value')]
)
def update_arima_summary(selected_lang_arima):
    lang_data = tweets_per_day_by_lang[tweets_per_day_by_lang['lang'] == selected_lang_arima]
    lang_data.set_index('created_at', inplace=True)
    lang_series = lang_data['id']


    # We'll use 80% of our data for training, 20% for testing
    split_point = int(len(lang_series) * 0.8)
    train, test = lang_series[:split_point], lang_series[split_point:]

    model, _, _ = fit_auto_arima(train, forecast_periods=len(test))

    # Generate predictions for the dates in the test set
    forecast = model.predict(n_periods=len(test))
    return str(model.summary())


######################################################## Arima ###############################
# When calling the AutoCorrelation function, pass the pivot_df dataframe as a parameter
AutoCorrelation(pivot_df)

if __name__ == '__main__':
    app.run_server(debug=True)



