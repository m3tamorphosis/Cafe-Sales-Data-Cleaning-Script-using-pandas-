import pandas as pd
# Load the CSV file

df = pd.read_csv('A:/Dataset/Cafe-Sales-Data-Cleaning-Script-using-pandas-/dirty_cafe_sales.csv')

# Inspect initial data
print("Initial Data Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Replace 'ERROR' and 'UNKNOWN' with NaN for easier handling
df.replace(['ERROR', 'UNKNOWN'], pd.NA, inplace=True)

# Convert columns to appropriate data types
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')