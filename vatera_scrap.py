import requests
from bs4 import BeautifulSoup
import exchange_rates
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

    logo="https://insiderblog.hu/wp-content/uploads/2020/01/jofogas_logo.jpg"
    if "Lepin" in data_subject or "LEPIN" in data_subject or "lepin" in data_subject:
        # Need another search to skip fake lego
        pass
    else:
        return ad_class.AdObject(data_website, data_url,data_subject, price_value, logo)


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


    logo="data:image/png;base64,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"
    if "Lepin" in data_subject or "LEPIN" in data_subject:
        # Here need to add another search to skip the fake lego
        pass
    else:
        return ad_class.AdObject(data_website, data_url,data_subject, price_value, logo )

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
    price= price_value_tag.text
    price_value=price.split(" ")[0]

    # Get the AD's subject from the website
    data_subject = data.find('img')['alt']



    # Declare the website in the data_webiste variable
    data_website= "arukereso"

    logo = "http://pr.arukereso.hu/wp-content/uploads/2019/01/arukereso-hu-logo-color.png"
    return ad_class.AdObject(data_website, data_url,data_subject, price_value, logo )

def get_set_amazon(set_num, set_name):
    # Correcting set num to be less long and too accurate
    corrected_set_num = set_num.split("-")
    corrected_set_name = set_name[:10]


    # make a GET request to the Vatera website
    response = requests.get(f'https://www.amazon.de/s?k=Lego+{corrected_set_num[0]}&ref=sr_pg_1', headers=HEADERS)
    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # extract the data
    data = soup.find(class_="a-section a-spacing-base")
    title = soup.find('span', {'class': "a-size-base-plus"}).text.strip()
    # Get the AD's url from the website
    data_url_tag = data.find('a', {'class': "a-link-normal"})
    data_url_href = data_url_tag.get("href")


    data_url=f"https://www.amazon.de/{data_url_href}"

    # Get the AD's price from the website
    price_value_eur = soup.find('span', {'class': "a-price-whole"}).text.strip()

    price_value = exchange_rates.change_currency(float(price_value_eur.replace(",","")), "EUR")

    # Get the AD's subject from the website
    data_subject = soup.find('span', {'class': "a-size-base-plus"}).text.strip()


    # Declare the website in the data_webiste variable
    data_website= "Amazon"

    logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqu8nsOXBapqDEySzTkg1UFncYxh-JSgCegA&usqp=CAU"
    # Check if the searched set's name is in the AD's subject
    if corrected_set_name in data_subject:
        return ad_class.AdObject(data_website, data_url, data_subject, price_value, logo)
    # If the searched set's name is not in the AD's subject return none
    elif corrected_set_name not in data_subject:
        return None

    #
