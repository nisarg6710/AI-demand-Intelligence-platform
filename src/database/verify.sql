USE demand_intelligence;

SHOW TABLES;

SELECT COUNT(*) FROM calendar_dim;

SELECT COUNT(*) FROM item_dim;

SELECT COUNT(*) FROM store_dim;

SELECT COUNT(*) FROM price_fact;

SELECT COUNT(*) FROM sales_fact;

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




