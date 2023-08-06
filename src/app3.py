# import pandas as pd
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# # Load the dataset
# file_path = "predicted_dataxgb_en_last.csv"
# df = pd.read_csv(file_path)

# # Convert 'created_at' to datetime and coerce errors
# df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')

# # Drop rows with NaT in 'created_at'
# df = df.dropna(subset=['created_at'])

# # Continue with the rest of the code...

# # Resample by day and count the number of tweets for each classification
# time_series_data_pivot = df.resample('D', on='created_at')['predicted_classification'].value_counts().unstack().fillna(0)
# time_series_data_pivot.to_csv('time_series_data.csv')

