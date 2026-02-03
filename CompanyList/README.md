# Data Cleaning – Inc. 5000 Companies (2014)
**Project Overview**

The goal was to improve readability, consistency, and query efficiency, enabling reliable exploratory and analytical work.


**Dataset**

Source: Tableau Public Library

Description: Information about the top 5,000 U.S. companies in 2014

Format: CSV imported into SQLite

Scope: Company metadata, rankings, and financial attributes


**Tools**

Cleaning: SQLite

Visualization: Sublime

Language: SQL, Python

Environment: Local database for data preparation and transformation


# Cleaning Process

The dataset required multiple cleaning steps before it could be effectively analyzed:

Renamed tables and columns to improve clarity and consistency
Removed irrelevant and duplicated columns
Standardized column naming conventions
Simplified overly long table and column names
Organized schema to improve query readability and maintainability

All transformations were performed using SQL queries.


**Outcomes**

The cleaned dataset is easier to explore and query
Improved schema readability during analysis
Queries are simpler, clearer, and less error-prone
Dataset is now suitable for downstream analysis and visualization

**Improvements**

The dataset does not include a time dimension (month or quarter)

Adding a date or month column would enable:
Trend analysis
Seasonal and quarterly comparisons
Holiday and period-based insights
This enhancement would significantly increase the analytical value of the dataset.

**Queries**

```sql
1. -- rename table.

ALTER TABLE Data Set- Inc5000 Company List_2014.csv to Company_List_2014;

2. -- irregular columns starting with a "_" to match the remaining collumns (Made it more organised).

ALTER TABLE Company_List_2014
RENAME COLUMN _num to num;


ALTER TABLE Company_List_2014
RENAME COLUMN _pageURL to pageURL;

3. -- search for null values. 

SELECT * FROM Company_List_2014
WHERE _id IS NULL;

4. -- delete repetitive and irrelevant columns (Made the dataset shorter and more relevant).

ALTER TABLE Company_List_2014
DROP COLUMN _id; -- (Only null values)

ALTER TABLE Company_List_2014
DROP COLUMN _widgetName; -- (All rows contained the same text, which was the dataset's title)

ALTER TABLE Company_List_2014
DROP COLUMN _source; -- (Identical to _widgetName)

ALTER TABLE Company_List_2014
DROP COLUMN _resultNumber; -- (Identical to num)
```
