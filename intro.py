import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronic", "Electronic", "Accessories", "Accessories", "Electronic"],
    "Price": [80000, 30000, 3000, 1500, 25000],
    "Quantity": [2, 5, 10, 15, 4]
}

# Creating a dataframe - like a table in excel
df = pd.DataFrame(data)
print(df)

# Viewing the first rows
print(df.head(3))

# df.head() for first rows and df.tail() for the last rows

# Checking the size of our dataset
print(df.shape)

# Getting column names
print(df.columns)

# Getting information about the dataset
print(df.info())

# Statistical summary
print(df.describe())

#Basic calculations and selscting one column
df["Price"]
print(df["Price"].mean())
print(df["Price"].max())
print(df["Price"].min())
print(df["Price"].sum())