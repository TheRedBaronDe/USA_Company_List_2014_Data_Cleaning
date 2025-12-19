import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. load dataset
df = pd.read_csv('C:\\Users\\Yoro\\Documents\\Sublime\\Datasets\\netflix_titles_cleaned.csv')

# 2. set a professional style
sns.set_theme(style="white")
colors = ["#E50914", "#221F1F"]

# 3. content addition trends (setting the timeline)
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year

# 4. content addition trends (data by year and type)
trend_data = df[df['year_added'] >= 2008].groupby(['year_added', 'type']).size().reset_index(name='count')

# 5. content addition trends 
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")
sns.lineplot(data=trend_data, x='year_added', y='count', hue='type', marker='o', palette=['#E50914', '#221F1F'], linewidth=2.5)

plt.title('Netflix Content Addition Trends (2008 - 2021)', fontsize=16, fontweight='bold')
plt.xlabel('Year Added to Platform', fontsize=12)
plt.ylabel('Number of Titles Added', fontsize=12)
plt.legend(title='Content Type')

# 6. top 10 Content Producing Countries
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='Reds_r')
plt.title('Top 10 Content Producing Countries', fontsize=14, fontweight='bold')
plt.xlabel('Number of Titles')

# 7. visualize the charts
plt.show()