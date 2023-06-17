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
def getselectedsets (set_data):
    # Connect to the SQLite database
    conn = sqlite3.connect('lego_database.db')
    cursor = conn.cursor()
    set_data = "%" + set_data + "%"
    try:
        # Execute the SQL query to select 8 random rows
        cursor.execute(f'SELECT * FROM your_table WHERE set_num LIKE  "{set_data}" OR set_name LIKE  "{set_data}"')
        # Fetch the selected rows

        selected_rows = cursor.fetchall()
        # except no result
        print(selected_rows)
        if selected_rows == []:
            conn.close()

            return "No result"
    #except worng format
    except:
        conn.close()

        return "No result"

    conn.close()

    # Close the database connection
    print(selected_rows)
    return selected_rows