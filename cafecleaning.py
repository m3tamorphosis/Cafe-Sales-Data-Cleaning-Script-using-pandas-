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
