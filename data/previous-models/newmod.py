# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('~/data/Suomenlinna-Traffic-Predictor/data/combined-data.csv')

# Select the independent variables (date, hour, weather features, and direction)
X = df[['Year', 'Month', 'Day', 'Hour', 'Average temperature', 'Wind speed', 'Precipitation', 'Stop']]  # Replace with actual column names

# Select the dependent variable (ferry traffic)
y = df['Passengers']  # Replace with actual column name for ferry traffic

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train) 

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Function to predict ferry traffic based on input date, hour, weather, and direction
def predict_traffic(year, month, day, hour, avg_temp, wind_speed, precipitation, stop):
    input_data = pd.DataFrame([[year, month, day, hour, avg_temp, wind_speed, precipitation, stop]], 
                              columns=['Year', 'Month', 'Day', 'Hour', 'Average temperature', 'Wind speed', 'Precipitation', 'Stop'])
    prediction = model.predict(input_data)
    return prediction[0]

# Example usage
year = 2024
month = 1
day = 15
hour = 5  # Example hour
avg_temp = 15.0  # Example temperature
wind_speed = 5.0  # Example wind speed
precipitation = 0.0  # Example precipitation
stop = 99  # Example direction

predicted_traffic = predict_traffic(year, month, day, hour, avg_temp, wind_speed, precipitation, stop)
print(f"Predicted ferry traffic: {predicted_traffic}")
