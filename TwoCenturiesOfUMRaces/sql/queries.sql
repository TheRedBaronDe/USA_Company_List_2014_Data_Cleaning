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

-- Check for null values
