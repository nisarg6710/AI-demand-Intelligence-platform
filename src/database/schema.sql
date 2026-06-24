USE demand_intelligence;

CREATE TABLE IF NOT EXISTS calendar_dim (
    d VARCHAR(10) PRIMARY KEY,
    date DATE,
    wm_yr_wk INT,
    weekday VARCHAR(20),
    wday INT,
    month INT,
    year INT,
    event_name_1 VARCHAR(100),
    event_type_1 VARCHAR(100),
    event_name_2 VARCHAR(100),
    event_type_2 VARCHAR(100),
    snap_CA TINYINT,
    snap_TX TINYINT,
    snap_WI TINYINT
);

CREATE TABLE IF NOT EXISTS store_dim (
    store_id VARCHAR(20) PRIMARY KEY,
    state_id VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS item_dim (
    item_id VARCHAR(50) PRIMARY KEY,
    dept_id VARCHAR(50),
    cat_id VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS price_fact (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    store_id VARCHAR(20),
    item_id VARCHAR(50),
    wm_yr_wk INT,
    sell_price FLOAT,

    FOREIGN KEY (store_id)
        REFERENCES store_dim(store_id),

    FOREIGN KEY (item_id)
        REFERENCES item_dim(item_id)
);

SHOW Tables;

USE demand_intelligence;
SELECT COUNT(*)
FROM calendar_dim;

SELECT *
FROM calendar_dim
LIMIT 5;