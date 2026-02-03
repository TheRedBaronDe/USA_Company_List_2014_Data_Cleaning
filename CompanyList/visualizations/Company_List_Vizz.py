import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. load dataset
df = pd.read_csv('C:\\Users\\Yoro\\Documents\\SQLite\\DB Cleaning\\Company_List_2014.csv')

# 2. set a more professional style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))

# 3. show the top 10 industries in 2014
top_industries = df['industry'].value_counts().head(10)

sns.barplot(x=top_industries.values, y=top_industries.index, palette='viridis')

plt.title('Top 10 Fast Growing USA Industries in 2014', fontsize=16, fontweight='bold')
plt.xlabel('Number of Companies', fontsize=12)
plt.ylabel('Industry', fontsize=12)

# 4. show the top 10 USA states based on their growth
state_counts = df['state_s'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=state_counts.index, y=state_counts.values, palette='magma')

plt.title('Top 10 States by Growth', fontsize=14, fontweight='bold')
plt.xlabel('State', fontsize=12)
plt.ylabel('Number of Companies', fontsize=12)

# 5. visualize the charts
plt.show()
