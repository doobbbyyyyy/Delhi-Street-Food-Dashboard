import pandas as pd
df = pd.read_csv(r'C:\Users\rohit\Downloads\DelhiNCR Restaurants.csv')
#df = pd.read_csv('DelhiNCR Restaurants.csv')

# Quick preview
print(df.head())
print(df.shape)  # Rows, columns
print(df.columns.tolist())  # Column names

# Basic overview
print("Dataset shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Data summary
print("\nData info:")
print(df.info())
print("\nStats summary:")
print(df.describe())

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# My Exact First 3 columns
print("YOUR EXACT COLUMNS:")
print(df.columns.tolist())
print("\nFirst 3 rows:")
print(df.head(3))
