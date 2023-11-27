import psycopg2
from portDetails import portEnv, assetsTable
import random

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

def add_geography_column(connection, cursor, table_name):
    try:
        # Check if the 'location' column already exists in the table
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}' AND column_name = 'location';")
        column_exists = cursor.fetchone()

        if column_exists == None:
            # Drop the existing 'location' column
            cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN IF EXISTS geometry;")

        # Add the new 'location' geography column
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN geometry GEOGRAPHY(Point, 4326);")

        # Commit the transaction
        connection.commit()

        print("Geography column added or replaced successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error adding geography column to PostgreSQL table:", error)

def generate_sample_data(num_samples, min_lat, max_lat, min_lon, max_lon):
    sample_data = []
    for _ in range(num_samples):
        title = "Sample Title"
        group = "Sample Group"
        address = "Sample Address"
        city = "Los Angeles"  # Sample City is Los Angeles
        latitude = round(random.uniform(min_lat, max_lat), 6)
        longitude = round(random.uniform(min_lon, max_lon), 6)
        email = "sample@email.com"
        sample_data.append((title, group, address, city, latitude, longitude, email))
    return sample_data

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

        # Define the table name where you want to add the entries
        table_name = assetsTable

        # Define the number of sample entries to generate
        num_samples = 10  # You can change this to generate more samples

        # Define latitude and longitude range for Los Angeles
        min_latitude = 33.6
        max_latitude = 34.1
        min_longitude = -118.6
        max_longitude = -118.1

        # Generate sample data with random coordinates around Los Angeles
        sample_data = generate_sample_data(num_samples, min_latitude, max_latitude, min_longitude, max_longitude)

        # Call the function to add the entries to the table
        for data in sample_data:
            add_entry_to_postgres(connection, cursor, table_name, data)

        # Call the function to add or replace the 'location' geography column
        add_geography_column(connection, cursor, table_name)

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
