import sqlite3

def write_non_validated_base_state(db_cursor):
    db_cursor.execute(
        """
        INSERT INTO non_validated_base_state (state_id, state_code, state_name)
        SELECT
            CAST(state_id AS INTEGER) AS state_id,
            CAST(state_code AS TEXT) AS state_code,
            CAST(state_name AS TEXT) AS state_name
        FROM raw_state;
        """
    )

def publish_base_state(db_cursor):
    db_cursor.execute(
        """
        INSERT INTO base_state (state_id, state_code, state_name, etl_inserted)
        SELECT
            state_id,
            state_code,
            state_name,
            datetime('now') AS etl_inserted
        FROM non_validated_base_state;
        """
    )   

def write_non_validated_base_customer(db_cursor):
    db_cursor.execute(
        """
        INSERT INTO non_validated_base_customer (customer_id, zipcode, city, state_code, datetime_created, datetime_updated)
        SELECT
            customer_id,
            zipcode,
            city,
            state_code,
            datetime_created AS datetime_created,
            datetime_updated AS datetime_updated
        FROM raw_customer;
        """
    )

def publish_base_customer(db_cursor):
    db_cursor.execute(
        """
        INSERT INTO base_customer (customer_id, zipcode, city, state_code, datetime_created, datetime_updated, etl_inserted)
        SELECT
            customer_id,
            zipcode,
            city,
            state_code,
            datetime_created,
            datetime_updated,
            datetime('now')
        FROM non_validated_base_customer;
        """
    )

def write_non_validated_dim_customer(db_cursor):
    db_cursor.execute(
        """
        INSERT INTO non_validated_dim_customer (customer_id, zipcode, city, state_code, state_name, datetime_created, datetime_updated)
        SELECT
            c.customer_id,
            c.zipcode,
            c.city,
            c.state_code,
            s.state_name,
            c.datetime_created,
            c.datetime_updated
        FROM base_customer AS c
        INNER JOIN base_state AS s ON c.state_code = s.state_code;
        """
    )

def publish_dim_customer(db_cursor):
    db_cursor.execute(
        """
        INSERT INTO dim_customer(customer_id, zipcode, city, state_code, state_name, datetime_created, datetime_updated, etl_inserted)
        SELECT
            c.customer_id,
            c.zipcode,
            c.city,
            c.state_code,
            s.state_name,
            c.datetime_created,
            c.datetime_updated,
            datetime('now')
        FROM base_customer AS c
        LEFT JOIN base_state AS s ON c.state_code = s.state_code;
        """
    )
    pass

def audit(expectation_suite_to_check):
    print(expectation_suite_to_check)
    pass

def check_audit_failures(expectation_suite_to_check):
    print(expectation_suite_to_check)
    return True 

def run():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    # # NOTE: transform -> non_validated_table -> Validate -> table
    write_non_validated_base_customer(cursor)
    audit('non_validated_base_customer')
    if check_audit_failures('non_validated_base_customer'):
        publish_base_customer(cursor)

    write_non_validated_base_state(cursor)
    audit('non_validated_base_state')
    if check_audit_failures('non_validated_base_state'):
        publish_base_state(cursor)

    write_non_validated_dim_customer(cursor)
    audit('non_validated_dim_customer')
    if check_audit_failures('non_validated_dim_customer'):
        publish_dim_customer(cursor)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    run()
