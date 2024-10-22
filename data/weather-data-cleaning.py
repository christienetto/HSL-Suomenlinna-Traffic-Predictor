import pandas as pd

file_path = 'data/weather-data.csv'
df = pd.read_csv(file_path)
df['Time [Local time]'] = df['Time [Local time]'].apply(lambda x: x.split(':')[0])

df.rename(columns={'Time [Local time]': 'Hour'}, inplace=True)
df.rename(columns={'Average temperature [°C]': 'Average temperature'}, inplace=True)
df.rename(columns={'Wind speed [m/s]': 'Wind speed'}, inplace=True)
df.rename(columns={'Precipitation [mm]': 'Precipitation'}, inplace=True)

df["Hour"] = pd.to_numeric(df["Hour"], errors='coerce').fillna(0).astype(int)
df.drop(columns=['Observation station'], inplace=True)

output_file_path = 'weather-data-cleaned.csv' 
df.to_csv(output_file_path, index=False)
