DROP TABLE IF EXISTS public."TwoCenturiesOfUMRaces"; -- drops table from previous attempt to import the CSV data

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
