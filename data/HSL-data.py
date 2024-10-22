import requests
import csv

base_url = "https://hsl.louhin.com/api/1.0/data/257001"

headers = {"Authorization": "LWS d59c041a-2ad1-4beb-b769-b9d7ea3a5628"}
params = {"offset": 545844}

response = requests.get(base_url, headers=headers, params=params)

if response.status_code == 200:
    csv_data = response.text
    with open('HSL-data.csv', 'w', newline='', encoding='utf-8') as file:
        file.write(csv_data)
