import json
import requests
# a module used for creating objects for lego sets.
import set_class


ApiKey= "a8051c7afd62c5ed715c48fe45f58ec5"


# Communicate with rebrickable api to get the current lego database

def find_set(set_num):
    # making a GET request to the rebrickable api and passing the set_num and API key
    response = requests.get(f"https://rebrickable.com/api/v3/lego/sets/{set_num}/?key={ApiKey}")
    lego_set = response.text # get the response as text
    # creating a SetObject  and passing the json data to the constructor
    set_object= set_class.SetObject(json.loads(lego_set))
    return set_object
