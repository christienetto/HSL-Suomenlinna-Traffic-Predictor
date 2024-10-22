# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Assuming your merged ferry traffic and weather dataset is in 'data'
# 'data' is a DataFrame with the columns 'temperature', 'wind_speed', 'precipitation', 'ferry_traffic', etc.

df = pd.read_csv('data/combined-data.csv')

# Select the independent variables (weather features)
X = df[['Year', 'Month', 'Day', 'Hour', 'Average temperature', 'Wind speed', 'Precipitation']]  # Replace with actual column names

# Select the dependent variable (ferry traffic)
y = df[['Year', 'Month', 'Day', 'Hour', 'Passengers']]  # Replace with actual column name for ferry traffic

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