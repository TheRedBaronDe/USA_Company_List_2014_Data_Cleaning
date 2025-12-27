# Data_Cleaning
Repository used as portfolio for data cleaning skills and improvements.
This is my very first data cleaning repository.

I got this dataset from Tableau Public's library.
It's a big dataset containing information about the top 5.000 USA companies in 2014.
I used SQLite for all the data cleaning queries.

**Why clean it?**

It contained some irrelevant and repetitive columns, as well as a long and overly complicated name, which I shortened for practicality.
By cleaning this dataset, the data becomes much more readable and easier to query.

**What could be improved?**
It would be highly important if a "Month" column were added, so the dataset could be analysed by months and quarters, compare trends, holiday's seasons and more.

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
