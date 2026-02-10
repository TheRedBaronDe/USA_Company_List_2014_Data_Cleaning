/* Project: Two Centuries Of Ultra Marathon Races (1798-2022) - Kaggle Dataset
Tools: pgAdmin 4
Author: Victoria Silva (TheRedBaronDe)

Objective: Make a exploratory data analysis of the dataset to identify data quality issues and ensure its consistency.
*/

DROP TABLE IF EXISTS public."TwoCenturiesOfUMRaces"; -- drops table from previous attempt to import the CSV data

-- Create matching columns with the correct data type so it's possible to import the dataset

CREATE TABLE public."TwoCenturiesOfUMRaces" ( -- creates new table
    year_of_event            INTEGER,
    event_dates              TEXT,
    event_name               TEXT,
    event_distance_length    TEXT,
    event_number_of_finishers   INTEGER,
    athlete_performance      TEXT,
    athlete_club             TEXT,
    athlete_country          TEXT,
    athlete_year_of_birth    DOUBLE PRECISION,
    athlete_gender           TEXT,
    athlete_age_category     TEXT,
    athlete_average_speed    TEXT,
    athlete_id               BIGINT
); 

-- Check if the data was correctly imported

SELECT COUNT(*) FROM public."TwoCenturiesOfUMRaces"; -- count all the values imported

SELECT * FROM public."TwoCenturiesOFUMRaces" 
LIMIT 5; -- show the first five rows

-- Check for null values in the most important columns

SELECT
    COUNT(*) FILTER (WHERE year_of_event IS NULL) AS null_year,
    COUNT(*) FILTER (WHERE event_name IS NULL) AS null_event,
    COUNT(*) FILTER (WHERE athlete_id IS NULL) AS null_athlete,
    COUNT(*) FILTER (WHERE athlete_gender IS NULL) AS null_gender,
    COUNT(*) FILTER (WHERE athlete_country IS NULL) AS null_country,
    COUNT(*) FILTER (WHERE athlete_average_speed IS NULL) AS null_avg_speed
FROM public."TwoCenturiesOfUMRaces";

-- Check the available years

SELECT DISTINCT year_of_event
FROM public."TwoCenturiesOfUMRaces"
ORDER BY year_of_event; -- this query returns 146 different values (years)

-- Check how many unique countries the dataset has

SELECT COUNT(DISTINCT athlete_country)
FROM public."TwoCenturiesOfUMRaces"; -- this query returns 209 distinct values (countries)

-- Checks if an athlete was recorded more than once on the same event and on the same year

SELECT
    year_of_event,
    event_name,
    athlete_id,
    COUNT(*)
FROM public."TwoCenturiesOfUMRaces"
GROUP BY
    year_of_event,
    event_name,
    athlete_id
HAVING COUNT(*) > 1; -- it returns various values, but that's expected since we're dealing with athletes racing on very long marathons

-- Check for real duplicates by comparing the athlete's performance and checking if all rows look identical

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT (
        year_of_event,
        event_name,
        athlete_id,
        athlete_performance,
        athlete_average_speed
    )) AS distinct_rows
FROM public."TwoCenturiesOfUMRaces";

-- it returned:    Total Rows: 7,461,195 - Distinct Rows: 7,460,935
-- a 260 difference in values, meaning there are 260 identical (most likely duplicated) values
-- this makes up for 0.00348469649% of the total dataset, making it insignificant
