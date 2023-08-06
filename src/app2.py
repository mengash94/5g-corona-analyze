# # # import pandas as pd
# # # # from textblob import TextBlob

# # # # # Read the CSV file

# # # # df = pd.read_csv("la5g-ym.csv")

# # # # # Convert the 'created_at' column to a datetime object and extract the date part
# # # # df['created_at'] = pd.to_datetime(df['created_at']).dt.date

# # # # # Function to analyze sentiment
# # # # def analyze_sentiment(text):
# # # #     analysis = TextBlob(str(text))
# # # #     return analysis.sentiment.polarity

# # # # # Apply sentiment analysis to the 'original_text' column
# # # # df['sentiment_polarity'] = df['original_text'].apply(analyze_sentiment)

# # # # # Group by 'lang' and 'created_at', then calculate the mean sentiment polarity
# # # # daily_sentiment_avg = df.groupby(['lang', 'created_at'])['sentiment_polarity'].mean().reset_index()

# # # # # Rename the columns for clarity
# # # # daily_sentiment_avg.columns = ['lang', 'date', 'average_sentiment_polarity']

# # # # # Save the daily sentiment averages to a CSV file
# # # # daily_sentiment_avg.to_csv('daily_sentiment_avg.csv', index=False)

# # # #Load the daily sentiment averages from the CSV file
# # # daily_sentiment_avg = pd.read_csv('daily_sentiment_avg1.csv')

# # # # # # Mapping of language codes to full names
# # # lang_mapping = {
# # #     'en': 'English',
# # #     'fr': 'French',
# # #     'pt': 'Portuguese',
# # #     'it': 'Italian',
# # #     'nl': 'Dutch',
# # #     'de': 'German',
# # #     'pl': 'Polish',
# # #     'fi': 'Finnish',
# # #     'cs': 'Czech',
# # #     'el': 'Greek',
# # #     'lt': 'Lithuanian',
# # #     'da': 'Danish',
# # #     'ro': 'Romanian',
# # #     'sl': 'Slovenian',
# # #     'bg': 'Bulgarian',
# # #     'iw': 'Hebrew',
# # #     'lv': 'Latvian',
# # #     'et': 'Estonian',
# # #     'es': 'Spanish',
# # #     'hu': 'Hungarian'
# # # }

# # # # # Create a list of language codes to keep
# # # # langs_to_keep = list(lang_mapping.keys())
# # # # daily_sentiment_avg = daily_sentiment_avg[daily_sentiment_avg['lang'].isin(langs_to_keep)]

# # # # daily_sentiment_avg.to_csv('daily_sentiment_avg.csv', index=False)
# # # # Add a new column with the full language name
# # # daily_sentiment_avg['lang'] = daily_sentiment_avg['lang'].map(lang_mapping)

# # # # # Save the updated DataFrame to the same CSV file
# # # daily_sentiment_avg.to_csv('daily_sentiment_avg.csv', index=False)
# # # Importing necessary libraries
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # # Loading the CSV file
# # data = pd.read_csv("la5g-ym.csv")

# # # Converting "created_at" to datetime format
# # data['created_at'] = pd.to_datetime(data['created_at'], utc=True)

# # # Resampling the data to get the count of tweets per day
# # daily_tweets = data.resample('D', on='created_at').size()

# # # Plotting the time series of daily tweet counts
# # plt.figure(figsize=(15, 6))
# # plt.plot(daily_tweets, label='Number of Tweets')
# # plt.title('Daily Tweet Counts')
# # plt.xlabel('Date')
# # plt.ylabel('Number of Tweets')
# # plt.legend()
# # plt.show()

# import pandas as pd
# import pmdarima as pm
# from sklearn.metrics import mean_squared_error
# from math import sqrt
# import pickle
# # # # # Mapping of language codes to full 
# df = pd.read_csv("la5g-ym.csv")
# lang_mapping = {
#     'en': 'English',
#     'fr': 'French',
#     'pt': 'Portuguese',
#     'it': 'Italian',
#     'nl': 'Dutch',
#     'de': 'German',
#     'pl': 'Polish',
#     'fi': 'Finnish',
#     'cs': 'Czech',
#     'el': 'Greek',
#     'lt': 'Lithuanian',
#     'da': 'Danish',
#     'ro': 'Romanian',
#     'sl': 'Slovenian',
#     'bg': 'Bulgarian',
#     'iw': 'Hebrew',
#     'lv': 'Latvian',
#     'et': 'Estonian',
#     'es': 'Spanish',
#     'hu': 'Hungarian'
# }

# # Create a list of language codes to keep
# langs_to_keep = list(lang_mapping.keys())
# df = df[df['lang'].isin(langs_to_keep)]
# df['lang'] = df['lang'].map(lang_mapping)


# df['created_at'] = pd.to_datetime(df['created_at'])
# df.set_index('created_at', inplace=True)

# # Group by language and resample to daily tweet count
# tweets_per_day_by_lang = df.groupby('lang').resample('D').count()['id']

# # Get unique languages
# languages = df['lang'].unique()
# # # Get the top 5 languages with the maximum number of days
# # top_5_languages = tweets_per_day_by_lang.groupby(level=0).size().nlargest(2).index

# # Number of days to forecast ahead (e.g., next month)
# forecast_days = 30

# # Loop through the top 5 languages and fit the Auto ARIMA model
# for lang in languages:
#     lang_series = tweets_per_day_by_lang[lang]

#     # Fill missing days with zeros
#     lang_series = lang_series.reindex(pd.date_range(start=lang_series.index.min(), end=lang_series.index.max()), fill_value=0)

#     # Split the data into training and testing sets (90% training, 10% testing)
#     split_point = int(len(lang_series) * 0.90)
#     train, test = lang_series[:split_point], lang_series[split_point:]

#     # Fit the Auto ARIMA model (with weekly seasonality)
#     model = pm.auto_arima(train, seasonal=False, m=7)

#     # Store the one-step-ahead forecasts
#     one_step_forecast = []
#     for t in test.index:
#         forecast = model.predict(n_periods=1)
#         one_step_forecast.append(forecast[0])
#         model.update(test[t])

#     # Calculate the RMSE
#     rmse = sqrt(mean_squared_error(test, one_step_forecast))

#     # Forecast the next month
#     future_forecast = model.predict(n_periods=forecast_days)
#     forecast_index = pd.date_range(start=test.index.min(), periods=forecast_days, freq='D')

#     # Save the data for this language as a pickle file
#     data_to_save = (train, test, future_forecast, forecast_index, rmse)
#     with open(f'autoarima/{lang}.pkl', 'wb') as file:
#         pickle.dump(data_to_save, file)

#     print(f"Data for language {lang} has been saved.")
