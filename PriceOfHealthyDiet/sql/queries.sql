/* Project: Price Of Healthy Diet (2017-2024) - Kaggle Dataset
Tools: pgAdmin 4
Author: Victoria Silva (TheRedBaronDe)

Objective: Make a exploratory data analysis of the dataset to identify data quality issues and ensure its consistency.
*/

-- Create matching columns with the correct data type so it's possible to import the dataset

CREATE TABLE public."PriceOfHealthyDiet" (
    country_code INT,
    country VARCHAR(255),
    region VARCHAR(255),
    year INT,
    cost_healthy_diet_ppp_usd DECIMAL,
    annual_cost_healthy_diet_usd DECIMAL,
    cost_vegetables_ppp_usd DECIMAL,
    cost_fruits_ppp_usd DECIMAL,
    total_food_components_cost DECIMAL,
    cost_category VARCHAR(255),
    data_quality VARCHAR(255)
);

-- Check if the data was correctly imported

SELECT COUNT(*) FROM public."PriceOfHealthyDiet"; -- count all the values imported

SELECT * FROM public."PriceOfHealthyDiet" 
LIMIT 5; -- show the first five rows

-- Check for null values

SELECT
COUNT(*) FILTER (WHERE country IS NULL) AS null_country,
COUNT(*) FILTER (WHERE year IS NULL) AS null_year,
COUNT(*) FILTER (WHERE cost_healthy_diet_ppp_usd IS NULL) AS null_cost
FROM public."PriceOfHealthyDiet";

-- Check the available years

SELECT DISTINCT year
FROM public."PriceOfHealthyDiet"
ORDER BY year; -- by ordering by year we can confirm that the dataset contains data from 2017 to 2024

-- Check for how many unique countries the dataset has

SELECT COUNT(DISTINCT country)
FROM public."PriceOfHealthyDiet";

-- Check for duplicated values in "country" and "year"

SELECT country, year, COUNT(*)
FROM public."PriceOfHealthyDiet"
GROUP BY country, year
HAVING COUNT(*) > 1; -- this query show us that there aren't any dupliated values in this column

-- Receive the first statistical analysis of the dataset
-- Calculate the min, max and average of the column "cost_healthy_diet_ppp_usd" 

SELECT
MIN(cost_healthy_diet_ppp_usd),
MAX(cost_healthy_diet_ppp_usd),
AVG(cost_healthy_diet_ppp_usd)
FROM public."PriceOfHealthyDiet";

-- Calculate the average cost of a healthy diet based on the "region" (continent)

SELECT region,
AVG(cost_healthy_diet_ppp_usd) AS avg_cost
FROM public."PriceOfHealthyDiet"
GROUP BY region
ORDER BY avg_cost DESC;
