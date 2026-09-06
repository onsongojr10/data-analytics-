import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv("county_revenue.csv")

#total revenue for each county
#group by county and calculate the total revenue
county_total = df.groupby("County")["Revenue"].sum()
print("Total Revenue by County:", county_total)

#group by county and calculate the average revenue
county_average = df.groupby("County")["Revenue"].mean()
print("Average Revenue by County:", county_average)

#find the highest monthly revenue for each county
county_highest= df.groupby("County")["Revenue"].max()
print("Highest Monthly Revenue by County:", county_highest)

#find the lowest monthly revenue for each county
county_lowest = df.groupby("County")["Revenue"].min()
print("Lowest Monthly Revenue by County:", county_lowest)

#overall revenue statistics
total_revenue =np.sum(df["Revenue"])
print("Total Revenue for all counties:", total_revenue)

#bar chart for total revenue by county
plt.bar(county_total.index, county_total.values )
#Add labels and title to the bar chart
plt.title("Total Revenue by County")
#Add labels to the x-axis
plt.xlabel("County")
#Add labels to the y-axis
plt.ylabel("Revenue")
#display the bar chart
plt.show()


#line chart for average revenue by county
nairobi=df[df["County"]=="Nairobi"]
plt.plot(nairobi["Month"], nairobi["Revenue"])
plt.title("Nairobi Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

#pie chart for revenue distribution by county
plt.pie(
    county_total.values, 
    labels=county_total.index, 
    autopct='%1.1f%%'
    )
plt.title("Revenue share by County")
plt.show()

#scatter plot for revenue vs month for each county
data={
    "advertising_spend":[10000,15000,20000,25000,30000,35000],
    "sales":[50000,60000,72000,85000,95000,110000]
}
#convert the dict into a pandas DF
df_business=pd.DataFrame(data)
print(df_business)

plt.scatter(
    df_business["advertising_spend"],
    df_business["sales"]
    )
plt.title("Advertising Spend vs Sales")
plt.xlabel("Advertising Spend")
plt.ylabel("Sales")
plt.show()