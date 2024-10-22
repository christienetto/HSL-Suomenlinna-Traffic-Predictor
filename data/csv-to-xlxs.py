import pandas as pd

csv_file = 'data/combined-data.csv'
data = pd.read_csv(csv_file)

excel_file = 'data/combined-data.xlsx' 
data.to_excel(excel_file, index=False)
