import requests
import pandas as pd
import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def convert_timestamp_to_datetime(timestamp_ms):
    # Convert timestamp in milliseconds to datetime
    timestamp_seconds = timestamp_ms / 1000
    return datetime.datetime.fromtimestamp(timestamp_seconds)


# Define the API URL
url = (
    "https://api.polygon.io/v2/aggs/ticker/C:EURUSD/range/"
    "15/minute/2020-01-09/2023-01-20"
    "?adjusted=true&sort=asc&limit=1200000&"
    "apiKey=USGhqM149TAOaKXNbLratZdnuuTmJL9k"
)

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Extract the 'results' list from the JSON
results = data['results']

# Convert the 'results' list into a DataFrame
df = pd.DataFrame(results)

# Apply the timestamp conversion function to the 't' column
df['t'] = df['t'].apply(convert_timestamp_to_datetime)

# Drop irrelevant columns
df.drop(columns=['n'], inplace=True)

# Shift the 'c' column to create the target variable
df['next_close'] = df['c'].shift(-1)

# Drop rows with NaN (last row where 'next_close' is NaN)
df.dropna(inplace=True)

# Define features and target variable
X = df.drop(columns=['next_close', 't'])
y = df['next_close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = \
train_test_split(X, y, test_size=0.2, 
random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict the test set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
