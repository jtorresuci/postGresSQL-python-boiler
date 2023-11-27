import psycopg2

from postgresConnection import connect_to_postgres, close_postgres_connection
from printStatments import functionBanner


def main():
    try:
        # Open connection
        print(functionBanner)
        connection, cursor = connect_to_postgres()

        # Perform database operations here
        

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        # Always close the database connection, even if an exception occurred
        if connection:
            close_postgres_connection(connection)

        print(functionBanner)




main()