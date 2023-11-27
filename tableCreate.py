
import psycopg2
from portDetails import portEnv

def create_table_if_not_exists(connection, cursor, table_name, column_names, column_datatypes):
    try:
        # Construct the SQL statement to create a table if it does not exist
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        
        # Iterate over the column names and datatypes to construct the table schema
        for i, (col_name, col_dtype) in enumerate(zip(column_names, column_datatypes)):
            create_table_query += f"{col_name} {col_dtype}"
            if i < len(column_names) - 1:
                create_table_query += ', '
        
        create_table_query += ");"

        # Execute the SQL statement to create the table
        cursor.execute(create_table_query)

        # Commit the transaction to save the changes to the database
        connection.commit()

        print(f"Table '{table_name}' created or already exists.")

    except (Exception, psycopg2.Error) as error:
        print("Error creating table in PostgreSQL:", error)

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

        # Define table details: name, column names, and column datatypes
        table_name = "TEST"
        column_names = ["title", "org", "address", "city", "latitude", "longitude", "email"]
        column_datatypes = ["TEXT", "TEXT", "TEXT", "TEXT", "DOUBLE PRECISION", "DOUBLE PRECISION", "TEXT"]

        # Call the function to create the table if it does not exist
        create_table_if_not_exists(connection, cursor, table_name, column_names, column_datatypes)

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
