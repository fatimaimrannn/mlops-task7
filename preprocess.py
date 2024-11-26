import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load the raw data
raw_data_file = "raw_data.csv"
df = pd.read_csv(raw_data_file)

# Step 2: Handle missing values (only for numeric columns)
numeric_cols = ['Temperature', 'Humidity', 'Wind Speed']
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Step 3: Normalize/Standardize numerical fields (Temperature and Wind Speed)
scaler = MinMaxScaler()

# Normalize 'Temperature' and 'Wind Speed' columns
df[['Temperature', 'Wind Speed']] = scaler.fit_transform(df[['Temperature', 'Wind Speed']])

# Step 4: Save the preprocessed data to a new CSV file
processed_data_file = "processed_dataa.csv"
df.to_csv(processed_data_file, index=False)

# Print the first few rows of the preprocessed data
print(df.head())
