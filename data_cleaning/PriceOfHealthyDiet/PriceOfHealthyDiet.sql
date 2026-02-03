SELECT region,
AVG(cost_healthy_diet_ppp_usd) AS avg_cost
FROM public."PriceOfHealthyDiet"
GROUP BY region
ORDER BY avg_cost DESC;
