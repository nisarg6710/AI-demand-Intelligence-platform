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

-- changing the price_fact table

USE demand_intelligence;

DROP TABLE IF EXISTS price_fact;

CREATE TABLE price_fact (

    store_id VARCHAR(20),

    item_id VARCHAR(50),

    wm_yr_wk INT,

    sell_price DECIMAL(10, 2),

    PRIMARY KEY (
        store_id,
        item_id,
        wm_yr_wk
    ),

    FOREIGN KEY (store_id)
        REFERENCES store_dim(store_id),

    FOREIGN KEY (item_id)
        REFERENCES item_dim(item_id)
);

USE demand_intelligence;

CREATE TABLE IF NOT EXISTS sales_fact (

    item_id VARCHAR(50),

    store_id VARCHAR(20),

    d VARCHAR(10),

    sales INT,

    PRIMARY KEY (
        item_id,
        store_id,
        d
    ),

    FOREIGN KEY (item_id)
        REFERENCES item_dim(item_id),

    FOREIGN KEY (store_id)
        REFERENCES store_dim(store_id),

    FOREIGN KEY (d)
        REFERENCES calendar_dim(d)
);


CREATE OR REPLACE VIEW sales_enriched AS

SELECT

    s.item_id,
    i.dept_id,
    i.cat_id,

    s.store_id,
    st.state_id,

    c.date,
    c.weekday,
    c.month,
    c.year,

    c.event_name_1,
    c.event_type_1,
    c.event_name_2,
    c.event_type_2,

    c.snap_CA,
    c.snap_TX,
    c.snap_WI,

    s.sales

FROM sales_fact s

JOIN item_dim i
ON s.item_id = i.item_id

JOIN store_dim st
ON s.store_id = st.store_id

JOIN calendar_dim c
ON s.d = c.d;

show tables;