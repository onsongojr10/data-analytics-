import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("bakery_sales.csv")

# 1. First few rows and column names
print("First few rows:")
print(df.head())

# 2. Average price of items
average_price = np.mean(df["Unit_Price"])
print("Average price:", average_price)

# 3. Highest and lowest priced item
highest_price = np.max(df["Unit_Price"].max())
Lowest_price = np.max(df["Unit_Price"].min())
print("Highest priced item:", highest_price)
print("Lowest priced item:", Lowest_price)

# 4. Total units sold across all items
total_units = np.sum(df["Units_Sold"])
print("Total units sold:", total_units)

# 5. Revenue per item (price x units sold)
df["Revenue"] = df["Unit_Price"] * df["Units_Sold"]
print("Revenue per item:")
print(df[["Item", "Revenue"]])

# 6. Total and average revenue for the bakery
total_revenue = np.sum(df["Revenue"])
average_revenue = np.mean(df["Revenue"])
print("Total revenue:", total_revenue)
print("Average revenue:", average_revenue)