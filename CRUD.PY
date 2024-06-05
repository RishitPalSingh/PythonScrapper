import psycopg2
#

# Reading the data from the databasefrom dotenv import load_dotenv
# # import os
# #
# # BASEDIR = os.path.abspath(os.path.dirname(_file_))
# # load_dotenv(os.path.join(BASEDIR, '.env'))
# #
# # user=os.getenv('user')
# # password=os.getenv('password')
# # host=os.getenv('host')
# # port=os.getenv('port')
# # database=os.getenv('database')
def fetch_data():
    try:
        connection = psycopg2.connect(
            dbname='Scrapper',
            user='postgres',
            password='Saisai@33',
            host='localhost',
            port='5432'
        )

        cursor = connection.cursor()

        # Execute a SELECT query to fetch data from the table
        cursor.execute("SELECT * FROM scraped_table")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print the data
        for row in rows:
            print(row)

    except (Exception, psycopg2.Error) as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# function to delete a particular row

def delete_row_by_Basis(Basis_to_delete):
    try:
        connection = psycopg2.connect(
            dbname='Scrapper',
            user='postgres',
            password='Saisai@33',
            host='localhost',
            port='5432'
        )

        cursor = connection.cursor()

        # Execute a DELETE query to remove the row with the specified year
        cursor.execute("DELETE FROM scraped_table WHERE \"Basis\" = %s", (Basis_to_delete,))

        # Commit the changes
        connection.commit()
        print(f"Row with year {Basis_to_delete} deleted successfully!")

    except (Exception, psycopg2.Error) as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# function to edit a row

def edit_winner_by_year(Basis_to_edit, new_man):
    try:
        connection = psycopg2.connect(
            dbname='Scrapper',
            user='postgres',
            password='Saisai@33',
            host='localhost',
            port='5432'
        )

        cursor = connection.cursor()

        # Execute an UPDATE query to modify the winner for the specified year
        cursor.execute("UPDATE scraped_table SET \"MAN\" = %s WHERE \"Basis\" = %s", (new_man, Basis_to_edit))

        # Commit the changes
        connection.commit()
        print(f"MAN for year {Basis_to_edit} updated to {new_man} successfully!")

    except (Exception, psycopg2.Error) as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# fetch_data()
delete_row_by_Basis("Transmission Speed")
# fetch_data()
# edit_winner_by_year("Congestion","Anything other than man full form")
fetch_data()