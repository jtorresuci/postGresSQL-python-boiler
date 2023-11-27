import psycopg2
from postgresConnection import connect_to_postgres, close_postgres_connection
from printStatments import functionBanner
from addgeocol import add_geography_column


def main():
    try:
        # Open connection
        print(functionBanner)
        connection, cursor = connect_to_postgres()

        # Define your local PostgreSQL database connection details
        database_name = "g"
        # user = "your_username"
        # password = "your_password"

        # Replace 'your_table_name' with the name of your table
        table_name = "your_table_name"

        # Call the function to add the geography column
        add_geography_column(cursor,connection,"Assets")

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        # Always close the database connection, even if an exception occurred
        if connection:
            close_postgres_connection(connection)

        print(functionBanner)

if __name__ == "__main__":
    main()
