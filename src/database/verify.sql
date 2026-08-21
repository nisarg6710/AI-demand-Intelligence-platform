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

SHOW TABLES LIKE 'analytics%';

DESCRIBE analytics_sales_summary;

SELECT *
FROM analytics_sales_summary;

ALTER TABLE analytics_sales_summary
MODIFY average_sales DECIMAL(18,6);

ALTER TABLE analytics_sales_summary
ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

UPDATE analytics_sales_summary
SET average_sales = CAST(total_sales AS DECIMAL(18,6)) / total_records
WHERE id = 1;

DESCRIBE analytics_sales_summary;

SELECT
    total_records,
    total_sales,
    total_sales / total_records AS calculated_average,
    CAST(
        total_sales / total_records
        AS DECIMAL(18,6)
    ) AS calculated_average_6dp,
    average_sales
FROM analytics_sales_summary
WHERE id = 1;

SELECT
    CAST(total_sales AS DECIMAL(18,6)) /
    CAST(total_records AS DECIMAL(18,6)) AS calculated_average
FROM analytics_sales_summary
WHERE id = 1;

SELECT *
FROM analytics_sales_summary
WHERE id = 1;

SELECT COUNT(*)
FROM analytics_product_performance;

SELECT *
FROM analytics_product_performance
ORDER BY total_sales DESC
LIMIT 10;

ALTER TABLE analytics_product_performance
ADD INDEX idx_product_sales (total_sales);

SELECT *
FROM analytics_weekday_sales;

SELECT COUNT(*)
FROM analytics_weekday_sales;

ALTER TABLE analytics_weekday_sales
ADD INDEX idx_weekday_sales (total_sales);

DESCRIBE analytics_price_summary;

ALTER TABLE analytics_price_summary
ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

UPDATE analytics_price_summary
SET average_price = (
    SELECT CAST(AVG(sell_price) AS DECIMAL(18,6))
    FROM price_fact
)
WHERE id = 1;

SELECT
    id,
    average_price,
    minimum_price,
    maximum_price
FROM analytics_price_summary
WHERE id = 1;

DESCRIBE analytics_sales_distribution;

ALTER TABLE analytics_sales_distribution
MODIFY average_sales DECIMAL(18,6);

ALTER TABLE analytics_sales_distribution
ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

-- verification
SELECT
    id,
    total_transactions,
    average_sales,
    sales_stddev,
    minimum_sales,
    maximum_sales
FROM analytics_sales_distribution
WHERE id = 1;

DESCRIBE analytics_category_performance;

SELECT *
FROM analytics_category_performance
ORDER BY total_sales DESC;

ALTER TABLE analytics_category_performance
ADD INDEX idx_category_sales (total_sales);

DESCRIBE analytics_department_performance;

SELECT *
FROM analytics_department_performance
ORDER BY total_sales DESC;

ALTER TABLE analytics_department_performance
ADD INDEX idx_department_sales (total_sales);

SHOW TABLES LIKE 'forecast%';

SELECT
    model_name,
    mae,
    rmse,
    mape
FROM forecast_experiments
ORDER BY mape ASC;

SELECT
    model_name,
    COUNT(*) AS prediction_rows
FROM forecast_predictions
GROUP BY model_name
ORDER BY prediction_rows DESC;

SELECT *
FROM forecast_predictions
LIMIT 10;

SELECT
    model_name,
    MIN(forecast_date) AS first_date,
    MAX(forecast_date) AS last_date,
    COUNT(*) AS prediction_count
FROM forecast_predictions
GROUP BY model_name
ORDER BY model_name;

SELECT
    MIN(forecast_date) AS first_date,
    MAX(forecast_date) AS last_date
FROM forecast_predictions
WHERE model_name = 'ProphetModel';