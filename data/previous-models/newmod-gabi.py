# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the dataset
data_path = 'data/combined-data.csv'
data = pd.read_csv(data_path)

# Prepare the dataset
# Assuming the dataset has columns: Year, Month, Day, Hour, Temperature, Wind Speed, Precipitation, Stop, and Passengers
X = data[['Year', 'Month', 'Day', 'Hour', 'Average temperature', 'Wind speed', 'Precipitation', 'Stop']]
y = data['Passengers']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model using Mean Squared Error on the test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Model Mean Squared Error: {mse}")

# Function to predict future ferry busyness
def predict_traffic():
    
    # Create a DataFrame for the new input
    input_data = pd.DataFrame({
        'Year': [2025],
        'Month': [5],
        'Day': [15],
        'Hour': [7],
        'Temperature': [18],
        'Wind Speed': [3.3],
        'Precipitation': [20],
        'Stop': [99]
    })

    # Make the prediction
    predicted_passengers = model.predict(input_data)
    print(f"\nPredicted number of passengers: {int(predicted_passengers[0])}")

# Run the prediction function
predict_traffic()
