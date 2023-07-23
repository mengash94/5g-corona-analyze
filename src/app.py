
import dash
from dash import html
from dash.dependencies import Input, Output
from dash import dcc
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
import plotly.graph_objects as go
import plotly.express as px
from collections import defaultdict
import pmdarima as pm
import plotly.graph_objects as go
# import dash_core_components as dcc
from flask_caching import Cache
from pages.DescriptiveStatistics import DescriptiveStatistics
from pages.CrossCorrelation import CrossCorrelation
from pages.AutoCorrelation import AutoCorrelation
from pages.SentimentAnalysis import avg_sentiment_scores
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
from pages.ARIMA import ARIMA
from pages.BERT import BERT
from pages.AboutResearchers import AboutResearchers
from pages.ContactUs import ContactUs
from pages.Projectdetails import Projectdetails
from pages.SentimentAnalysis import layout 
import dash_bootstrap_components as dbc


# ,external_stylesheets=[dbc.themes.CERULEAN]

app = dash.Dash(__name__, suppress_callback_exceptions=True)
# app = dash.Dash(__name__, )
server = app.server
# Initialize the cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
# cache.clear()
########################      AutoCorrelation  ###############

pivot_df = pd.read_csv('pivot_df.csv')
tweets_per_day_by_lang = pd.read_csv('tweets_per_day_by_lang.csv')

languages = tweets_per_day_by_lang['lang'].unique()
#################################################################
app.layout = html.Div([
    html.H1('5G Conspiracy Theory in Corona', style={'text-align': 'center','color': 'white'}),
    html.P('By Mengsha  Ataly and Yakir Attias', style={'text-align': 'center','color': 'white'}),
    dcc.Location(id='url', refresh=False),
    dcc.Tabs(id="tabs", value='/', children=[
        dcc.Tab(label='Home', value='/'),
        dcc.Tab(label='About the Researchers', value='/AboutResearchers'),
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
            html.H3('Short Explanation',style={'text-align': 'center','color': 'white'}),
            html.P('The 5G conspiracy theory in relation to the Corona pandemic suggests a false claim that 5G technology is somehow linked to the spread of the virus. This theory has gained traction in certain online communities despite being debunked by scientific evidence and experts.',style={'text-align': 'left','color': 'white'}),
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
    elif pathname == '/AboutResearchers':
        return AboutResearchers()
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
        return layout
    elif tab_value == 'nested-tab-5':
        return ARIMA(languages)
    elif tab_value == 'nested-tab-6':
        return BERT()

@app.callback(Output('url', 'pathname'),
              [Input('tabs', 'value')])
def update_url(tab_value):
    return tab_value

######################################### autocorrelation ################################
@app.callback(
    Output('autocorrelation-graph', 'figure'),
    Input('language-dropdown', 'value')
)
def update_graph(selected_language):
    lags = [1, 2, 3, 4, 5]
    autocorrelation_values = [pivot_df[selected_language].autocorr(lag=lag) for lag in lags]

    figure = go.Figure(data=go.Scatter(x=lags, y=autocorrelation_values))
    figure.update_layout(
        xaxis_title='Lag',
        yaxis_title='Autocorrelation',
        autosize=False,
        width=950,
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

@app.callback(
    Output('arima-summary-card', 'children'),
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
    

    
    summary = str(model.summary())

    # Replace newlines with line breaks for HTML
    summary_html = summary.replace('\n', '<br>')

    # Wrap the summary in a preformatted text tag to preserve spaces
    summary_html = f'<pre style="white-space: pre-wrap;">{summary_html}</pre>'
    card = dbc.Card([
        dbc.CardHeader("ARIMA Model Summary"),
        dbc.CardBody([
            DangerouslySetInnerHTML(summary_html)
        ])
    ])
    return card


############################################### sentiment ############################
@app.callback(
    Output('sentiment-pie-chart', 'figure'),
    Input('language-dropdown', 'value')
)
def update_pie_chart(selected_lang):
    # Load the data
    sentiment_counts = pd.read_csv('sentiment_counts.csv')

    if selected_lang == 'all':
        # Perform operation for all languages
        filtered_df = sentiment_counts
    else:
        # Filter data for the selected language
        filtered_df = sentiment_counts[sentiment_counts['lang'] == selected_lang]

    # Create a pie chart
    fig2 = px.pie(filtered_df, names='sentiment', values='count')

    # Update layout of the figure
    fig2.update_layout(
        title_text=f'Sentiment Distribution for {selected_lang}',
        autosize=False,
        width=700,
        height=960
    )

    return fig2



AutoCorrelation(pivot_df)
########################################################################## name
if __name__ == '__main__':
    app.run_server(debug=True)
    
