# Data manipulation
import pandas as pd
import numpy as np 

# Visualization
import matplotlib.pyplot as plt 
import seaborn as sns

# Statistical analysis
from scipy import stats
from scipy.stats import pearsonr, spearmanr

# Set visualization style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', '{:.2f}'.format)

# Load the cleaned dataset
df = pd.read_csv('C:\\Users\\User\\Documents\\PostgreSQL\\price_of_healthy_diet_clean.csv')

global_trend = df.groupby("year")["cost_healthy_diet_ppp_usd"].mean()

# Show how the cost of a healthy diet changed from 2017 to 2024
plt.figure()
plt.plot(global_trend.index, global_trend.values)
plt.title("Average Cost of Healthy Diet Over Time")
plt.xlabel("Year")
plt.ylabel("Cost (PPP USD)")
plt.show()

# Compare the cost of a healthy diet by continents from 2017 to 2024
region_trend = df.groupby(["year", "region"])["cost_healthy_diet_ppp_usd"].mean().unstack()

region_trend.plot()
plt.title("Healthy Diet Cost Trend by Region")
plt.xlabel("Year")
plt.ylabel("Cost (PPP USD)")
plt.show()

# Average cost of a healthy diet by continent
region_avg = df.groupby("region")["cost_healthy_diet_ppp_usd"].mean().sort_values()

plt.figure()
region_avg.plot(kind="bar")
plt.title("Average Healthy Diet Cost by Region")
plt.ylabel("Cost (PPP USD)")
plt.show()

# Show the top 10 most expensive countries for a healthy diet
latest_year = df[df["year"] == df["year"].max()]

top_countries = latest_year.sort_values(
    "cost_healthy_diet_ppp_usd", ascending=False
).head(10)

plt.figure()
plt.bar(top_countries["country"], top_countries["cost_healthy_diet_ppp_usd"])
plt.xticks(rotation=45)
plt.title("Top 10 Most Expensive Countries for Healthy Diet")
plt.show()

# Show the top 10 cheapest countries for a healthy diet
latest_year = df[df["year"] == df["year"].max()]

top_countries = latest_year.sort_values(
    "cost_healthy_diet_ppp_usd", ascending=True
).head(10)

plt.figure()
plt.bar(top_countries["country"], top_countries["cost_healthy_diet_ppp_usd"])
plt.xticks(rotation=45)
plt.title("Top 10 Cheapest Countries for Healthy Diet")
plt.show()

# Distribution of a healthy diet by region
plt.figure()
sns.boxplot(data=df, x="region", y="cost_healthy_diet_ppp_usd")
plt.title("Distribution of Healthy Diet Cost by Region")
plt.show()

# Annual and daily cost
plt.figure()
plt.scatter(
    df["cost_healthy_diet_ppp_usd"],
    df["annual_cost_healthy_diet_usd"]
)
plt.xlabel("Daily Cost")
plt.ylabel("Annual Cost")
plt.title("Daily vs Annual Healthy Diet Cost")
plt.show()
