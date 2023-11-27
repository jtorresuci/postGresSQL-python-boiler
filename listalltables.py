import psycopg2

def list_current_database_and_tables(connection):
    try:
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Get the name of the current database
        cursor.execute("SELECT current_database();")
        current_database = cursor.fetchone()[0]

        # SQL query to fetch the names of all tables in the current database
        table_query = f"""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
        """

        # Execute the SQL query
        cursor.execute(table_query)

        # Fetch all table names
        table_names = [row[0] for row in cursor.fetchall()]

        return current_database, table_names

    except (Exception, psycopg2.Error) as error:
        print("Error listing database and tables from PostgreSQL:", error)

    finally:
        # Close the cursor (the connection is not closed here to allow further operations)
        if cursor:
            cursor.close()

# Function to list tables with numbers
def list_tables_with_numbers(table_names):
    if table_names:
        print("Tables in the database:")
        for i, table_name in enumerate(table_names, start=1):
            print(f"{i}. {table_name}")
    else:
        print("No tables found in the database.")

# Example usage
if __name__ == "__main__":
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="gisdatabase"
        )

        # Call the function to list the current database and tables
        current_db, table_names = list_current_database_and_tables(connection)

        # Call the function to list tables with numbers
        print("Current Database:["+current_db+"]")
        list_tables_with_numbers(table_names)

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

    finally:
        # Close the connection to the database
        if connection:
            connection.close()
