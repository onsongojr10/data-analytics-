import pandas as pd
import numpy as np

df = pd.read_csv("bakery_sales.csv")


print("Shape (rows, columns):", df.shape)
print("\nColumn names:", list(df.columns))

print("\nData types:")
print(df.dtypes)


print("\nFirst few rows:")
print(df.head())

average_price = np.mean(df["Unit_Price"])
print("\nAverage price:", average_price)

highest_item = df.loc[df["Unit_Price"].idxmax(), "Item"]
lowest_item = df.loc[df["Unit_Price"].idxmin(), "Item"]
print("Highest priced item:", highest_item, "-", df["Unit_Price"].max())
print("Lowest priced item:", lowest_item, "-", df["Unit_Price"].min())


total_units = np.sum(df["Units_Sold"])
print("\nTotal units sold:", total_units)

df["Revenue"] = df["Unit_Price"] * df["Units_Sold"]
print("\nRevenue per item:")
print(df[["Item", "Revenue"]])


total_revenue = np.sum(df["Revenue"])
average_revenue = np.mean(df["Revenue"])
print("\nTotal revenue:", total_revenue)
print("Average revenue:", average_revenue)