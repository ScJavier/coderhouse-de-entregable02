from psycopg2.extras import execute_batch

def load_df_to_db(df, table, conn, batch_size=100):
    """
    Load DataFrame data into a database table.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data to load.
        table (str): The name of the table to load the data into.
        conn (psycopg2.connection): The connection to the PostgreSQL database.
        batch_size (int, optional): The batch size for batch insertion. Defaults to 100.
    
    Returns:
        int: 1 if an error occurred during execution, otherwise None.
    """

    # Construct the DELETE query to remove existing data from the table
    delete_query = f"DELETE FROM {table}"
    
    # Construct the INSERT query for inserting new data into the table
    cols = ','.join(df.columns)
    insert_query = f"INSERT INTO {table} ({cols}) VALUES (%s, %s, %s)"

    # Generate data tuples from the DataFrame
    data_generator = ((row[0], row[1], row[2]) for row in df.itertuples(index=False))

    # Execute operations within a cursor context
    with conn.cursor() as cursor:
        try:
            # Execute the DELETE query to remove existing data
            cursor.execute(delete_query)
            print("Existing data deleted.")

            # Execute batch insertion of new data
            execute_batch(cursor, insert_query, data_generator, page_size=batch_size)
            conn.commit()
            print("Data insertion completed.")
        except psycopg2.DatabaseError as e:
            print(f"Error executing batch: {e}")
            conn.rollback()