import sqlite3
import random


def getrandomsets ():
    # Connect to the SQLite database
    conn = sqlite3.connect('lego_database.db')
    cursor = conn.cursor()

    # Execute the SQL query to select 8 random rows
    cursor.execute("SELECT * FROM your_table WHERE year BETWEEN 2005 AND 2020 ORDER BY RANDOM() LIMIT 8")

    # Fetch the selected rows
    selected_rows = cursor.fetchall()

    # Close the database connection
    conn.close()
    return selected_rows
