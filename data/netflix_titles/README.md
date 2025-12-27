# Data Cleaning

I got this dataset from the available Kaggle datasets.
I used the Pandas library for all the cleaning done, all that using Sublime.

**Why clean it?**

The dataset contained lots of null values and some wrong stored data.
The "rating" column for the director "Louis C.K" was filled with the durations of his movies. 
It also lacked a date formatting for its "date_added" column.

**What could be improved?**

A "Month" column could be added for further trends analysis, as well as a "Category" column.

```python

import pandas as pd

# 1. load data 
df = pd.read_csv('C:\\Users\\Yoro\\Documents\\SQLite\\CSV\\netflix_titles.csv')

# 2. find null values and count them

print(df.isnull().sum()) # "director" column has 2634 null values, "cast" has 825, "country" has 831, "data_added" has 10, "rating" has 4, and "duration" has 3 null values.

# 3. find the percentage of null values for each column

print(df.isnull().sum()/len(df)*100) # the "director" column represents 29% of all null values.


# 4. fill null values with a "no data available" warning

df['director'] = df['director'].fillna('No Director Specified')
df['cast'] = df['cast'].fillna('No Cast Listed')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('No Ratings Available')

# 5. fix input added to wrong column (the "rating" column for the director "Louis C.K" was filled with the durations of his movies)

df.loc[df['director'] == 'Louis C.K.', 'duration'] = df['rating']
df.loc[df['director'] == 'Louis C.K.', 'rating'] = 'No Ratings Available' # moved the duration of each move to "duration" while leaving the missing ratings with its default message "No Ratings Available"

# 6. fix date formatting

df['date_added'] = df.loc[:, 'date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# 7. drop remaining null values

df = df.dropna(subset=['date_added', 'duration'])

# 8. save cleaned dataset

df.to_csv('netflix_titles_cleaned.csv', index=False)

``` 
