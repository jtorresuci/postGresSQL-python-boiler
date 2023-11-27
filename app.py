import psycopg2
from postgresConnection import connect_to_postgres, close_postgres_connection
from printStatments import functionBanner
from addgeocol import add_geography_column

from tableCreate import create_table_if_not_exists

from portDetails import portEnv

from createGeoPoint import create_geometry_point
import random

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

def main():
    print(functionBanner)
    # Define your local PostgreSQL database connection details
    host_name = "localhost"
    database_name = "gisdatabase"
    table_name = "assets"

    try:
        # Open connection
        connection, cursor = connect_to_postgres(host_name,portEnv,database_name)

        # Define the number of sample entries to generate
        num_samples = 10  # You can change this to generate more samples

        # Define latitude and longitude range for Los Angeles
        min_latitude = 33.6
        max_latitude = 34.1
        min_longitude = -118.6
        max_longitude = -118.1

        # Generate sample data with random coordinates around Los Angeles
        sample_data = generate_sample_data(num_samples, min_latitude, max_latitude, min_longitude, max_longitude)        # create_geometry_point(connection,cursor,table_name,)

        print(sample_data)
    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        # Always close the database connection, even if an exception occurred
        if connection:
            close_postgres_connection(connection)

        print(functionBanner)

if __name__ == "__main__":
    main()


