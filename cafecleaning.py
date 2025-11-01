import pandas as pd


df = pd.read_csv('A:/Dataset/Cafe-Sales-Data-Cleaning-Script-using-pandas-/dirty_cafe_sales.csv')


print("Initial Data Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

df = df.dropna()
df = df[~df.apply(lambda row: row.astype(str).str.strip().eq('').any(), axis=1)]
df = df[~df.apply(lambda row: row.astype(str).str.upper().isin(['UNKNOWN', 'ERROR']).any(), axis=1)]

df.replace(['ERROR', 'UNKNOWN'], pd.NA, inplace=True)


df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

df = df.dropna()

df['Total Spent'] = df['Total Spent'].fillna(df['Quantity'] * df['Price Per Unit'])

df['Location'].fillna('Unknown', inplace=True)
df['Payment Method'].fillna('Unknown', inplace=True)
df['Item'].fillna('Unknown Item', inplace=True)

df.dropna(subset=['Total Spent', 'Quantity'], inplace=True)

df.drop_duplicates(subset=['Transaction ID'], inplace=True)

df = df[df['Total Spent'] > 0] 
df = df[df['Quantity'] > 0]

df.reset_index(drop=True, inplace=True)

print("\nCleaned Data Info:")
print(df.info())
print("\nFirst 5 Rows of Cleaned Data:")
print(df.head())
print(f"\nTotal Rows After Cleaning: {len(df)}")
print(f"Total Sales: ${df['Total Spent'].sum():.2f}")


df.to_csv('cleaned_cafe_sales_drop_rows.csv', index=False)

