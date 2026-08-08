USE demand_intelligence;

SHOW TABLES;

SELECT COUNT(*) FROM calendar_dim;

SELECT COUNT(*) FROM item_dim;

SELECT COUNT(*) FROM store_dim;

SELECT COUNT(*) FROM price_fact;

SELECT COUNT(*) FROM sales_fact;

SELECT * FROM forecast_experiments;

SELECT COUNT(*) FROM forecast_predictions;

SELECT *
FROM price_fact
LIMIT 10;

SELECT *
FROM sales_fact
LIMIT 10;

SELECT *
FROM sales_enriched
LIMIT 10;

-- now the following 2 commands will check the referntial integrity, both should return 0 rows.

SELECT *
FROM price_fact p
LEFT JOIN store_dim s
ON p.store_id = s.store_id
WHERE s.store_id IS NULL;

SELECT *
FROM price_fact p
LEFT JOIN item_dim i
ON p.item_id = i.item_id
WHERE i.item_id IS NULL;


-- join test on sales_fact
 SELECT
    s.item_id,
    s.store_id,
    c.date,
    s.sales
FROM sales_fact s
JOIN calendar_dim c
ON s.d = c.d
LIMIT 10;


USE demand_intelligence;
DESCRIBE forecast_predictions;


USE demand_intelligence;
SHOW Tables;

DESCRIBE sales_fact;

USE demand_intelligence;
DESCRIBE calendar_dim;

SELECT COUNT(*) FROM sales_enriched;

SELECT
    month,
    SUM(sales) AS total_sales
FROM sales_enriched
GROUP BY month;

SHOW TABLE STATUS LIKE 'sales_enriched';

SHOW CREATE VIEW sales_enriched;

SHOW INDEX FROM sales_fact;

SELECT COUNT(*) FROM calendar_dim;

SHOW VARIABLES LIKE 'innodb_buffer_pool_size';

SHOW VARIABLES LIKE 'max_allowed_packet'; 

-- some verifications
SELECT * FROM analytics_monthly_sales;
SELECT COUNT(*) FROM analytics_monthly_sales;

-- checking the table
DESCRIBE analytics_store_performance;

SELECT *
FROM analytics_store_performance
ORDER BY total_sales DESC;

SELECT *
FROM analytics_category_performance
ORDER BY total_sales DESC;

SELECT *
FROM analytics_department_performance
ORDER BY total_sales DESC;

USE demand_intelligence;
SHOW tables;

SELECT MAX(date) AS max_calendar_date
FROM calendar_dim;

SELECT MAX(d) AS max_sales_d
FROM sales_fact;

SELECT
    MAX(c.date) AS latest_joined_date,
    COUNT(*) AS matching_rows
FROM sales_fact s
JOIN calendar_dim c
    ON s.d = c.d;