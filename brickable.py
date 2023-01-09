import json
import requests



ApiKey= "a8051c7afd62c5ed715c48fe45f58ec5"


# Communicate with rebrickable api to get the current lego database

def find_set(set_num):

    response = requests.get(f"https://rebrickable.com/api/v3/lego/sets/{set_num}/?key={ApiKey}")
    print(response.text)
    lego_set = response.text
    print(lego_set)

    return lego_set
