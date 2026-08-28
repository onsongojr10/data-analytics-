import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("small_business_sales.csv")

# Numpy calculations
# Calculate average price
average_price = np.mean(df["Price"])
print("Average price:", average_price)

# Find the highest price
highest_price = np.max(df["Price"])
print("Highest price:", highest_price)

# Find the lowest price
lowest_price = np.min(df["Price"])
print("Lowest price:", lowest_price)

# calculate total quantity sold
total_quantity = np.sum(df["Quantity_Sold"])
print("Total Quantity:", total_quantity)

# Standard deviation - how spread out the prices are
price_std = np.std(df["Price"])
print("Price standard deviation:", price_std)

#Business Analysis
#calculate revenue for each product
df["Revenue"]=df["Price"]*df["Quantity_Sold"]
print(df)

# calculate total revenue
total_revenue = np.sum(df["Revenue"])
print("Total Revenue for 2025:", total_revenue)

# calculate average revenue
average_revenue = np.mean(df["Revenue"])
print("Average Revenue for 2025:", average_revenue)