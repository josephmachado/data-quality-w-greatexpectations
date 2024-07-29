-- Create raw_customer
CREATE TABLE raw_customer (
    customer_id INTEGER PRIMARY KEY,
    zipcode TEXT,
    city TEXT,
    state_code TEXT,
    datetime_created DATETIME,
    datetime_updated DATETIME
);

-- create base_customer
CREATE TABLE base_customer (
    customer_id INTEGER,
    zipcode TEXT,
    city TEXT,
    state_code TEXT,
    datetime_created DATETIME,
    datetime_updated DATETIME,
    etl_inserted DATETIME
);

-- create non_validated_base_customer
CREATE TABLE non_validated_base_customer (
    customer_id INTEGER,
    zipcode TEXT,
    city TEXT,
    state_code TEXT,
    datetime_created DATETIME,
    datetime_updated DATETIME,
    etl_inserted DATETIME
);

-- create raw_state
CREATE TABLE raw_state (
    state_id INTEGER PRIMARY KEY,
    state_code TEXT,
    state_name TEXT
);

-- create base_state
CREATE TABLE base_state (
    state_id INTEGER,
    state_code TEXT,
    state_name TEXT,
    etl_inserted DATETIME
);

-- create non_validated_base_state
CREATE TABLE non_validated_base_state (
    state_id INTEGER,
    state_code TEXT,
    state_name TEXT,
    etl_inserted DATETIME
);

-- create dim_customer
CREATE TABLE dim_customer (
    customer_id INTEGER,
    zipcode TEXT,
    city TEXT,
    state_code TEXT,
    state_name TEXT,
    datetime_created DATETIME,
    datetime_updated DATETIME,
    etl_inserted DATETIME
);

-- create non_validated_dim_customer
CREATE TABLE non_validated_dim_customer (
    customer_id INTEGER,
    zipcode TEXT,
    city TEXT,
    state_code TEXT,
    state_name TEXT,
    datetime_created DATETIME,
    datetime_updated DATETIME,
    etl_inserted DATETIME
);
