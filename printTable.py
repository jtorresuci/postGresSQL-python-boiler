import psycopg2
from portDetails import assetsTable

def print_table(connection, table_name):
    try:
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # SQL statement to select all rows from the specified table
        select_query = f"SELECT * FROM {table_name};"

        # Execute the SQL statement
        cursor.execute(select_query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the table header (column names)
        column_names = [desc[0] for desc in cursor.description]
        print("\t".join(column_names))

        # Print the table data
        for row in rows:
            print("\t".join(map(str, row)))

    except (Exception, psycopg2.Error) as error:
        print("Error printing table from PostgreSQL:", error)

    finally:
        # Close the cursor (the connection is not closed here to allow further operations)
        if cursor:
            cursor.close()

# Example usage
if __name__ == "__main__":
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="gisdatabase"
        )

        # Define the table name you want to print
        table_name_to_print = assetsTable

        # Call the function to print the table
        print_table(connection, table_name_to_print)

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

    finally:
        # Close the connection to the database
        if connection:
            connection.close()
