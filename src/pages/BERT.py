from dash import html,dcc
import plotly.express as px 
import pandas as pd
text_bert_intro = "In our analysis of Twitter data, we employed advanced techniques to classify tweets and understand their underlying sentiment. Here's an overview of the methods we used:"

bert_methods = [
    ("1. CT-BERT Model for Twitter Tweets:", " Utilizing the specialized CT-BERT model, we accurately classified tweets by understanding their unique language structure."),
    ("2. SBERT Model for Sentence Embedding:", " We used SBERT to translate sentences into numerical forms, enabling efficient analysis of sentence meanings."),
    ("3. 5-Fold Validation:", " To evaluate our models' performance, we employed a 5-fold validation method, ensuring a balanced and comprehensive assessment."),
    ("4. Training and Test Data Division:", " Our approach included a careful division of data into training and test examples, allowing robust and real-world applicable results.")
]

text_bert_conclusion = "These sophisticated techniques allowed us to delve into Twitter data with precision, offering valuable insights into public sentiment and information spread during critical times."
############count predict ##################

time_series_data_pivot = pd.read_csv('time_series_data.csv')
classification_counts = time_series_data_pivot[['Neutral', 'Opponents', 'Supporters']].sum().reset_index()
classification_counts.columns = ['Classification', 'Count']
bar_fig = px.bar(classification_counts, x='Classification', y='Count', title='Counts of Predicted Classifications')

colors = ['blue', 'red', 'green']

bar_fig.update_traces(marker=dict(color=colors))
############ time seires graph #################

data = pd.read_csv("time_series_data_pivot_classification.csv", low_memory=False)

fig = px.line(data, x='created_at', y=['Neutral', 'Opponents', 'Supporters'], title='Tweets Over Time by Classification')
################################bar url ######################
df_URLs = pd.read_csv("With and Without URLs.csv")

fig_barurl = px.bar(df_URLs, x='predicted_classification', y='counts', color='has_url', title='Predicted Classifications: With and Without URLs')


###############################################
resampled_df=pd.read_csv('Sentiment Polarity by Predicted Classification.csv')
fig_resampled_df =px.line(resampled_df, x='created_at', y='sentiment_polarity', color='predicted_classification',
              title='Daily Average Sentiment Polarity by Predicted Classification',
              labels={'created_at': 'Date', 'sentiment_polarity': 'Sentiment Polarity'},
              template='plotly_dark')


def BERT():
    return html.Div([
        html.H3('Using CT-BERT and SBERT for Twitter Data Analysis'),
        html.P(text_bert_intro),
        html.Div([html.P([html.Strong(html.U(headline)), desc]) for (headline, desc) in bert_methods]),
        html.H3('Conclusion:'),
        html.P(text_bert_conclusion),
        html.Img(src='/assets/image/ct-bert-validation.jpg', width='800px', height='400px'),
        html.H1("The result of model:"),
        dcc.Graph(figure=bar_fig),
        dcc.Graph(figure=fig),
        dcc.Graph(figure=fig_barurl),
        dcc.Graph(figure=fig_resampled_df),
    ], style={'backgroundColor': 'white', 'color': 'black', 'padding': '15px'})
