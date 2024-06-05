import psycopg2
import requests
from bs4 import BeautifulSoup

def create_table(headers,content):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname='Scrapper',
            user='postgres',
            password='Saisai@33',
            host='localhost',
            port='5432'
        )


        cur = conn.cursor()


        table_name = 'scraped_table'


        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        create_table_query += ", ".join([f'"{header}" varchar(200)' for  header in headers])
        create_table_query += ");"
        insert=", ".join([f'{header}' for  header in headers])

        cur.execute(create_table_query)

        print(f"Table '{table_name}' created successfully in the PostgreSQL database.")
        insert_data = 'INSERT INTO scraped_table  ("Basis", "LAN", "MAN", "WAN") VALUES (%s, %s, %s, %s)'
        print(insert_data)
        for item in content:
            print(item)
            insert_values = item
            cur.execute(insert_data, insert_values)
        conn.commit()
        print("added succesfully")

    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL:", e)

    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()


def scrape_website_table(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception if request fails
        soup = BeautifulSoup(r.text, "html.parser")

        tables = soup.find_all("table")
        if tables:
            table = tables[0]  # Assuming we want to scrape data from the first table
            rows = table.find_all("tr")
            headers = []
            content = []

            for row in rows:
                cells = row.find_all(["th", "td"])
                if cells:
                    row_data = [cell.text.strip() for cell in cells if cell.text.strip()]
                    if not headers:
                        headers = row_data
                    else:
                        content.append(row_data)

            if headers:
                create_table(headers,content)
                # insert_data('scraped_table', headers, content)
                print("Table headers:", headers)
                print("Data inserted into PostgreSQL table.")
            else:
                print("No headers found in the table.")

        else:
            print("No tables found on the webpage.")

    except requests.RequestException as e:
        print("Error fetching webpage:", e)


url = "https://www.geeksforgeeks.org/difference-between-lan-man-and-wan/"


scrape_website_table(url)
