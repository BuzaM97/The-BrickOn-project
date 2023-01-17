import requests
from bs4 import BeautifulSoup
import json
import brickable

def get_set_jofogas(set_num, set_name):
    # Correcting set num to be less long and too accurate
    corrected_set_num = set_num.split("-")
    corrected_set_name = set_name[:10]


    # make a GET request to the Vatera website
    response = requests.get(f'https://www.jofogas.hu/magyarorszag?q=lego {corrected_set_num[0]} bontatlan&sp=1&o=1')
    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # extract the data
    data = soup.find(class_="contentArea")


    # Get the AD's url from the website
    data_url_tag = data.find("a", {"data-adview-url": ""})
    data_url = data_url_tag.get("href")

    # Get the AD's price from the website
    price_value_tag = soup.find("span", {"class": "price-value"})
    price_value = price_value_tag.get("content")

    # Get the AD's subject from the website
    data_subject_tag = data.find("a", {"class": "subject"})
    data_subject = data_subject_tag.text



