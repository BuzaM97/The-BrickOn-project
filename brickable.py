import json
import requests
# a module used for creating objects for lego sets.
import set_class
import os
import time
import sqlite3

ApiKey= (os.environ['BCA_API_KEY'])



# Communicate with rebrickable api to get the current lego database

def find_set(set_num):

    # making a GET request to the rebrickable api and passing the set_num and API key
    response = requests.get(f"https://rebrickable.com/api/v3/lego/sets/{set_num}/?key={ApiKey}")
    lego_set = response.text # get the response as text
    # creating a SetObject  and passing the json data to the constructor
    set_object= set_class.SetObject(json.loads(lego_set))

    return set_object

def find_all_set():
    # making a GET request to the rebrickable api and passing the API key
    list_of_setnums = []
    for year in range (1970, 2023):
        #maxyear = year+1
        print (year)
        #print (maxyear)
        response = requests.get(f"https://rebrickable.com/api/v3/lego/sets/?page_size=100000&min_year={year}&max_year={year}&key={ApiKey}")
        dict= json.loads(response.text)
        set_dict=dict['results']
        time.sleep(3)
        for x in range(len(set_dict)):
            list_of_setnums.append(dict['results'][x]['set_num'])
    print (list_of_setnums)
    file = open('items.txt', 'w')
    file.write(list_of_setnums)
    file.close()
    return list_of_setnums


def find_set_demo():
    conn = sqlite3.connect('lego_database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS your_table (
                        id INTEGER PRIMARY KEY,
                        column1 TEXT,
                        column2 TEXT,
                        column3 TEXT,
                        column4 TEXT,
                        column5 TEXT
                    )''')
    for year in range (1970, 2023):
        #maxyear = year+1
        print (year)
        #print (maxyear)
        response = requests.get(f"https://rebrickable.com/api/v3/lego/sets/?page_size=100000&min_year={year}&max_year={year}&key={ApiKey}")
        dict= json.loads(response.text)
        set_dict=dict['results']
        time.sleep(3)
        for x in range(len(set_dict)):
            print(dict['results'][x]['set_num'])
            column1_value = dict['results'][x]['set_num']
            column2_value = dict['results'][x]['name']
            column3_value = dict['results'][x]['year']
            column4_value = dict['results'][x]['theme_id']
            column5_value = dict['results'][x]['set_img_url']
        # Insert a new row into the table
            cursor.execute("INSERT INTO your_table (column1, column2, column3, column4, column5) VALUES (?, ?, ?, ?, ? )", (column1_value, column2_value, column3_value, column4_value, column5_value))
    conn.commit()
