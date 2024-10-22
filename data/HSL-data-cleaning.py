import pandas as pd

df = pd.read_csv('data/HSL-data.csv', delimiter=';', low_memory=False)

filtered_df = df[['VUOSI', 'KUUKAUSI', 'KUUKAUSIPÄIVÄ', 'TUNTI', 'PYSÄKKI', 'NOUSIJAT']]

for i in ['VUOSI', 'KUUKAUSI', 'KUUKAUSIPÄIVÄ', 'TUNTI', 'PYSÄKKI', 'NOUSIJAT']:
    filtered_df[i] = pd.to_numeric(filtered_df[i], errors='coerce').fillna(0).astype(int)

filtered_df.rename(columns={
    'VUOSI': 'Year',
    'KUUKAUSI': 'Month',
    'KUUKAUSIPÄIVÄ': 'Day',
    'TUNTI': 'Hour',
    'PYSÄKKI': 'Stop',
    'NOUSIJAT': 'Passengers'
}, inplace=True)

filtered_df = filtered_df[filtered_df['Stop'].isin([98, 99])]
filtered_df.to_csv('data/HSL-data-cleaned.csv', index=False)
