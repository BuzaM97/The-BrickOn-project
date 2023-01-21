import requests
from bs4 import BeautifulSoup

import ad_class
HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}
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

#   Declare the website in the data_webiste variable
    data_website= "jofogas"

    return ad_class.AdObject(data_website, data_url,data_subject, price_value )


def get_set_vatera(set_num, set_name):
    # Correcting set num to be less long and too accurate
    corrected_set_num = set_num.split("-")
    corrected_set_name = set_name[:10]


    # make a GET request to the Vatera website
    response = requests.get(f'https://www.vatera.hu/listings/index.php?q=lego {corrected_set_num[0]} bontatlan&ob=2&obd=1&p=1')
    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # extract the data
    data = soup.find(class_="prod-inner-container")


    # Get the AD's url from the website
    data_url_tag = data.find("a", {"product_link": ""})
    data_url = data_url_tag.get("href")

    # Get the AD's price from the website
    price_value_tag = soup.find("div", {"class": "gtm-impression"})
    price_value = price_value_tag.get("data-gtm-price")
    # Get the AD's subject from the website
    data_subject_tag = data.find("a", {"class": "product_link"})
    data_subject = data_subject_tag.get("title")

#   Declare the website in the data_webiste variable
    data_website= "vatera"
    return ad_class.AdObject(data_website, data_url,data_subject, price_value )

def get_set_arukereso(set_num, set_name):
    # Correcting set num to be less long and too accurate
    corrected_set_num = set_num.split("-")
    corrected_set_name = set_name[:10]


    # make a GET request to the Vatera website
    response = requests.get(f'https://www.arukereso.hu/CategorySearch.php?st=lego+{corrected_set_num[0]}&start=0')
    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # extract the data
    data = soup.find(class_="product-box")

    # Get the AD's url from the website
    data_url_tag = data.find("a", {"ak-info": ""})
    data_url = data_url_tag.get("href")

    # Get the AD's price from the website
    price_value_tag = soup.find("a", {"class": "price"})
    price_value = price_value_tag.text

    # Get the AD's subject from the website
    data_subject = data.find('img')['alt']

    # Declare the website in the data_webiste variable
    data_website= "arukereso"
    return ad_class.AdObject(data_website, data_url,data_subject, price_value )

def get_set_amazon(set_num, set_name):
    # Correcting set num to be less long and too accurate
    corrected_set_num = set_num.split("-")
    corrected_set_name = set_name[:10]


    # make a GET request to the Vatera website
    "https://www.amazon.com/s?k=Lego+{corrected_set_num[0]}"
    response = requests.get(f'https://www.amazon.com/s?k=Lego+{corrected_set_num[0]}&ref=sr_pg_1', headers=HEADERS)
    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # extract the data
    data = soup.find(class_="s-widget-container")

    title = soup.find('span', {'class': "a-size-base-plus"}).text.strip()
    # # Get the AD's url from the website
    data_url_tag = soup.find('a', {'class': "a-link-normal"})
    data_url_href = data_url_tag.get("href")
    data_url=f"www.amazon.com{data_url_href}"

    # Get the AD's price from the website
    price_value_whole = soup.find('span', {'class': "a-price-whole"}).text.strip()
    price_value_fract = soup.find('span', {'class': "a-price-fraction"}).text.strip()
    price_value= str(f"{price_value_whole}{price_value_fract}")
    #
    # Get the AD's subject from the website
    data_subject = soup.find('span', {'class': "a-size-base-plus"}).text.strip()
    #
    # # Declare the website in the data_webiste variable
    data_website= "Amazon"
    return ad_class.AdObject(data_website, data_url,data_subject, price_value )
    #
