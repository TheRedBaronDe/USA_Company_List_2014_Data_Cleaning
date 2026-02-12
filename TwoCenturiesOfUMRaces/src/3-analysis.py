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
df = pd.read_csv('C:\\Users\\User\\Documents\\PostgreSQL\\TWO_CENTURIES_OF_UM_RACES_CLEAN.csv', low_memory=False)

# Makes all column names lower case and divided by a underscore to avoid syntax errors
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(' ', '_')
      .str.replace('/', '_')
)

print(df.head()) # prints the first rows

# Print basic information about the dataset
print("\n===== BASIC INFO =====")
print(df.info()) # shows the column names and datatype

print("\n===== NULL VALUES =====")
print(df.isnull().sum().sort_values(ascending=False).head(15)) # sums the null values of each column and prints it in descending order 

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum()) # sums duplicated rows

print("\n===== DESCRIPTIVE STATS =====")
print(df.describe(include='all')) # prints the descriptive statatistics of each column

# Counts all unique values of the most important columns
total_races = df['event_name'].nunique() # counts all races
total_athletes = df['athlete_id'].nunique() # counts every athlete
total_results = len(df) # dataset length
countries = df['athlete_country'].nunique() # counts every country
years = df['year_of_event'].nunique() # counts all the years available

print("\n===== GLOBAL METRICS =====")
print(f"Total Races: {total_races:,}")
print(f"Total Athletes: {total_athletes:,}")
print(f"Total Results: {total_results:,}")
print(f"Countries: {countries}")
print(f"Years Covered: {years}")
