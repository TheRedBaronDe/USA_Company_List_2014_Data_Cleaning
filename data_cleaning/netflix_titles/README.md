# Data Cleaning – Netflix Titles Dataset
**Project Overview**

This project focuses on cleaning and standardizing a media dataset to improve data quality and analytical reliability.
The objective was to correct inconsistent values, handle missing data, and prepare the dataset for downstream analysis.

**Dataset**

Source: Kaggle

Description: Netflix titles catalog including movies and TV shows

Format: CSV

Key Fields: Title, director, cast, country, rating, date_added, duration

**Tools & Technologies**

Language: Python

Library: Pandas

Environment: Local development (Sublime Text)

# Cleaning Process

The following steps were performed using Pandas:

Loaded and inspected the dataset

Identified and quantified missing values

Corrected incorrectly stored data

Standardized date formats

Prepared the dataset for reliable analysis and visualization

All cleaning steps are documented in code to ensure reproducibility.

**Issues Identified**

Several issues affected the usability of the dataset:

High volume of missing values across multiple columns

Incorrect data stored in categorical fields

Example: the rating column contained movie durations instead of rating values

Inconsistent and unformatted date values in the date_added column

Structural inconsistencies that limited temporal and categorical analysis

**Outcomes**

Improved data consistency and correctness

Cleaned categorical fields suitable for grouping and aggregation

Properly formatted date column enabling time-based analysis

Dataset is now ready for exploratory analysis and visualization

**Improvements**

Further enhancements could increase analytical depth:

Add a derived "Month" column for trend and seasonality analysis

Create a "Category" or genre classification to enable content segmentation

Perform enrichment with external metadata (e.g., IMDb ratings)

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
