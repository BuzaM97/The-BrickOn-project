# Importing required libraries
from ebaysdk.finding import Connection  # Library for connecting to eBay API
import os  # Library for accessing environment variables
import ad_class  # Custom module for AdObject class
import exchange_rates  # Custom module for exchange rates conversion

# Setting the value of YOUR_APP_ID by fetching the value of EBAY_API_ID from environment variables
YOUR_APP_ID = (os.environ['EBAY_API_ID'])

# Creating an object of the Connection class from the eBay SDK
# Pass the value of appid as YOUR_APP_ID and config_file as None
api = Connection(appid=YOUR_APP_ID, config_file=None)

# Function to get information about an item from eBay
def get_set_ebay(set_num):
    # Splitting the set number using the "-" character
    corrected_set_num = set_num.split("-")

    # Setting the header for the API call
    header = {"Accept-Language": "de-AT de-DE"}

    # Executing the findItemsAdvanced method on the API object
    # Pass the keyword as 'LEGO {corrected_set_num[0]}', header as header, and itemFilter as a list of dictionaries
    response = api.execute('findItemsAdvanced', {'keywords': f'LEGO {corrected_set_num[0]}',
                                                 "header":header,
                                                 'itemFilter': [{'name': 'Condition', 'value': 'New'} ]})

    # Extracting the information about the first item from the response

    item_dict = response.dict()["searchResult"]["item"][0]

    # Setting the values for the data website, data URL, data subject, and price value
    data_website = "Ebay"
    data_url = item_dict["viewItemURL"]
    data_subject = item_dict["title"]
    price_value_us = item_dict["sellingStatus"]["currentPrice"]["value"]
    price_value = exchange_rates.change_currency(float(price_value_us), "US")

    # LOGO img URL availability
    logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/EBay_logo.svg/1280px-EBay_logo.svg.png"

    # Return an instance of the AdObject class from the ad_class module with the specified parameters
    return ad_class.AdObject(data_website, data_url,data_subject, price_value, logo )
