import pandas as pd

hsl_data = pd.read_csv('data/HSL-data-cleaned.csv')
weather_data = pd.read_csv('data/weather-data-cleaned.csv')

merge_keys = ['Year', 'Month', 'Day', 'Hour']
merged_data = pd.merge(hsl_data, weather_data, on=merge_keys, how='inner')

for i in ['Average temperature', 'Wind speed', 'Precipitation']:
    merged_data[i] = pd.to_numeric(merged_data[i], errors='coerce').fillna(0).astype(float)

merged_data.to_csv('data/combined-data.csv', index=False)
