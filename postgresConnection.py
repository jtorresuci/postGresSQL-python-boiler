import psycopg2
from printStatments import connectionSuccess, modulePrint, mainScript, connectionClosed

def connect_to_postgres():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="gisdatabase"
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute a SQL query to fetch the PostgreSQL server version
        cursor.execute("SELECT version();")

        # Fetch and print the server version
        db_version = cursor.fetchone()
        print(connectionSuccess)
        print("PostgreSQL server version:", db_version[0])
        return connection, cursor

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)


def close_postgres_connection(connection):
    try:
        # Close the database connection
        if connection:
            connection.close()
            print(connectionClosed)

    except (Exception, psycopg2.Error) as error:
        print("Error closing PostgreSQL connection:", error)

# Example usage
if __name__ == "__main__":
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="gisdatabase"
        )

        # ... Perform database operations ...

        # Close the database connection when done
        close_postgres_connection(connection)

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

if __name__ == "__main__":
    print(mainScript)
    connect_to_postgres()
else:
    print(modulePrint)
