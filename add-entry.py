import psycopg2
from portDetails import portEnv, assetsTable

def add_entry_to_postgres(connection, cursor, table_name, data):
    try:
        # SQL statement to insert data into the specified table
        insert_query = f"""
        INSERT INTO {table_name} (title, org, address, city, latitude, longitude, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        # Execute the SQL statement with the data
        cursor.execute(insert_query, data)

        # Commit the transaction to save the changes to the database
        connection.commit()

        print("Entry added successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error adding entry to PostgreSQL:", error)

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

        # Define the table name where you want to add the entry
        table_name = assetsTable

        # Define the data you want to insert as a tuple
        entry_data = (
            "Sample Title",
            "Sample Group",
            "Sample Address",
            "Sample City",
            123.456789,  # Sample latitude
            -12.345678,  # Sample longitude
            "sample@email.com"
        )

        # Call the function to add the entry to the table
        add_entry_to_postgres(connection, cursor, table_name, entry_data)

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
