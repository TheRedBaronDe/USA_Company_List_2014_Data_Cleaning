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
    df.columns.str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('/', '_')
)

# Convert numeric columns
df['athlete_year_of_birth'] = pd.to_numeric(df['athlete_year_of_birth'], errors='coerce') 
df['athlete_average_speed'] = pd.to_numeric(df['athlete_average_speed'], errors='coerce')
# "errors='coerce'" converts all invalid values into special missing values instead of returning an "error" message

# Calculate athlete's age and store it in a specific column
df['athlete_age'] = df['year_of_event'] - df['athlete_year_of_birth']

# Remove unrealistic ages
df.loc[(df['athlete_age'] < 10) | (df['athlete_age'] > 90), 'athlete_age'] = np.nan

# Create a random sample of the full dataset to avoid crashes, performance and memory issues
sample_df = df.sample(300_000, random_state=42)
# this sample uses 300.000 rows from the entire dataset
# setting an integer in "random_state=" makes sure the results always remain consistent

# Number of races over time
races_per_year = df.groupby('year_of_event')['event_name'].nunique()

plt.figure()
races_per_year.plot()
plt.title("Number of Ultra Marathon Races Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Races")
plt.tight_layout() # automatically adjusts parameters to avoid overlapping
plt.show()

# Athlete participation growth
athletes_per_year = df.groupby('year_of_event')['athlete_id'].nunique()

plt.figure()
athletes_per_year.plot()
plt.title("Number of Unique Athletes Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Athletes")
plt.tight_layout()
plt.show()

# Age distribution
plt.figure()
sns.histplot(sample_df['athlete_age'], bins=40) # divides the data into 40 intervals of equal width
plt.title("Athlete Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Speed x Age
plt.figure()
sns.scatterplot(
    data=sample_df,
    x='athlete_age',
    y='athlete_average_speed',
    alpha=0.3, # controls transparency
    s=10 # sets the size of the dots to "10"/small
)
plt.title("Athlete Speed x Age")
plt.xlabel("Age")
plt.ylabel("Speed (km/h)")
plt.tight_layout()
plt.show()

# Average speed by age
speed_by_age = (
    df.groupby('athlete_age')['athlete_average_speed']
    .mean()
    .dropna()
)

plt.figure()
speed_by_age.plot()
plt.title("Average Speed by Age")
plt.xlabel("Age")
plt.ylabel("Speed (km/h)")
plt.tight_layout()
plt.show()

# Top 15 countries by number of athletes
top_countries = (
    df['athlete_country']
    .value_counts()
    .head(15)
)

plt.figure()
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 15 Countries by Athlete Count")
plt.xlabel("Number of Athletes")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# Most popular race distances
top_distances = (
    df['event_distance_length']
    .value_counts()
    .head(15)
)

plt.figure()
sns.barplot(x=top_distances.values, y=top_distances.index)
plt.title("Most Common Race Distances")
plt.xlabel("Frequency")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()
