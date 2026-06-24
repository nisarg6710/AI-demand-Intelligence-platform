USE demand_intelligence;

-- calender table:-

CREATE TABLE calendar_dim (

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

    snap_CA BOOLEAN,

    snap_TX BOOLEAN,

    snap_WI BOOLEAN
);

-- Price table:-

CREATE TABLE price_fact (

    id BIGINT AUTO_INCREMENT PRIMARY KEY,

    store_id VARCHAR(20),

    item_id VARCHAR(50),

    wm_yr_wk INT,

    sell_price FLOAT
);
