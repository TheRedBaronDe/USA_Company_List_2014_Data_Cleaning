# Price Of Healthy Diet (2017-2014)
**Project Overview**

The goal was to improve readability, consistency, and query efficiency, enabling reliable exploratory and analytical work.

**Dataset**

Source: Kaggle (https://www.kaggle.com/datasets/ibrahimshahrukh/global-price-of-healthy-diet-dataset/code)

Description: What is the cost of a healthy diet around the world?* This comprehensive dataset answers that question with official data from the Food and Agriculture Organization (FAO) covering 175 countries from 2017 to 2024.

Format: CSV imported into pgAdmin 4

Scope: World health and economy analysis

**This analysis aims to answer:**

How has the cost of a healthy diet evolved globally between 2017–2024?

Which regions have the highest average costs?

Which countries show extreme values?

**What is PPP (Purchasing Power Parity)?**

PPP adjusts for differences in price levels between countries, making costs internationally comparable. A PPP dollar represents the same purchasing power in every country, unlike regular exchange rates.

Example: $3.50 PPP per day in India represents the same basket of goods as $3.50 PPP per day in the United States.

**Cost Categories**

Countries are classified based on their 2024 healthy diet costs:

Low Cost: < $2.00 PPP per day

Medium Cost: $2.00 - $3.50 PPP per day

High Cost: > $3.50 PPP per day

**Global Trends (2017-2024)**

Rising Costs: Average global cost increased from $3.14 (2017) to $4.46 (2024) - a 42% increase

Regional Disparities: Costs range from $2.56 to $8.39 per day in 2024

Accelerating Growth: Largest increases occurred 2021-2024, likely due to inflation and supply chain disruptions

Most Expensive: European and high-income countries generally have higher costs

Affordability Crisis: In many low-income countries, a healthy diet costs more than the poverty line

**Tools**

Cleaning: pgAdmin 4

Visualization: Sublime, Tableau (https://public.tableau.com/app/profile/vicsilva42/viz/PriceOfAHealthyDiet-GlobalOverview/Dashboard2)

Language: SQL, Python

Environment: Local database for data preparation and transformation
