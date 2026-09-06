import pandas as pd

# Load the dataset
df = pd.read_csv("dirty_business_sales.csv")
print(df)

# Check for duplicates
print("Duplicates:", df.duplicated().sum())

# Display the duplicate rows
print(df[df.duplicated()])

# Remove duplicate rows
df = df.drop_duplicates()

# Confirm that duplicates have been removed
print("Duplicates after cleaning:", df.duplicated().sum())

# Handle missing values
# Count missing values in each column
print(df.isnull().sum())

# Replace missing products with "Unknown"
df["Product"] = df["Product"].fillna("Unknown")

# Replace missing categories with "Unknown"
df["Category"] = df["Category"].fillna("Unknown")

# Replace missing customer names with "Unknown"
df["Customer"] = df["Customer"].fillna("Unknown")

# Replace missing prices with the average price
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Replace missing quantities with 0 (assume no sale recorded)
df["Quantity_Sold"] = df["Quantity_Sold"].fillna(0)

print("Missing values after cleaning:")
print(df.isnull().sum())

# Standardize text
df["Product"] = df["Product"].str.strip().str.title()
df["Category"] = df["Category"].str.strip().str.title()
df["Customer"] = df["Customer"].str.strip().str.title()

print(df)

# Save the cleaned dataset to a new file
df.to_csv("cleaned_business_sales.csv", index=False)
print("\nCleaned data saved to cleaned_business_sales.csv")
