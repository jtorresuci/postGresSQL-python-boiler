import psycopg2
from psycopg2 import sql
from psycopg2.extensions import adapt
from shapely.geometry import Point
from shapely.wkt import dumps

def create_geometry_point(connection, cursor, table_name, name, latitude, longitude):
    try:
        # Create a Shapely Point object
        point = Point(longitude, latitude)

        # Convert the Point object to Well-Known Text (WKT) format
        wkt = dumps(point)

        # Use SQL to insert the geometry point into the specified table
        insert_query = sql.SQL("""
            INSERT INTO {} (name, location)
            VALUES (%s, ST_GeomFromText(%s, 4326))
        """).format(sql.Identifier(table_name))

        # Execute the SQL statement with the data
        cursor.execute(insert_query, (name, wkt))

        # Commit the transaction to save the changes to the database
        connection.commit()

        print("Geometry point added successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error adding geometry point to PostgreSQL:", error)

# Example usage
if __name__ == "__main__":
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            port=5432,  # Change to your PostgreSQL port if needed
            database="your_database_name",
            user="your_username",
            password="your_password"
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the table name where you want to add the geometry point
        table_name = "points"

        # Define the attributes for the geometry point
        name = "Point 1"
        latitude = 34.0522  # Example latitude
        longitude = -118.2437  # Example longitude

        # Call the function to create the geometry point
        create_geometry_point(connection, cursor, table_name, name, latitude, longitude)

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
