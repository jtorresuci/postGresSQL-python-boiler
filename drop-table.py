import psycopg2
from portDetails import portEnv



def drop_table(connection, cursor, table_name):
    try:
        # SQL statement to drop a table
        drop_table_query = f"DROP TABLE IF EXISTS {table_name};"

        # Execute the SQL statement to drop the table
        cursor.execute(drop_table_query)

        # Commit the transaction to save the changes to the database
        connection.commit()

        print(f"Table '{table_name}' dropped successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error dropping table in PostgreSQL:", error)

# Example usage
if __name__ == "__main__":
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            port=portEnv,
            database="gisdatabase"
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the table name you want to drop
        table_name_to_drop = "TEST"

        # Call the function to drop the table
        drop_table(connection, cursor, table_name_to_drop)

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
