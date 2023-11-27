def add_geography_column(cursor, connection, table_name):
    try:

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # SQL command to add a geography column named 'location' to the table
        add_column_sql = f"""
        ALTER TABLE {table_name}
        ADD COLUMN IF NOT EXISTS location GEOGRAPHY(Point, 4326);
        """

        # Execute the SQL command
        cursor.execute(add_column_sql)

        # Commit the transaction
        connection.commit()

        print(f"Added 'location' geography column to the '{table_name}' table.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error adding geography column to PostgreSQL table: {error}")
