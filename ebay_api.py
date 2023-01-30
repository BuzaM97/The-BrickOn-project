from ebaysdk.finding import Connection
import os
import ad_class

YOUR_APP_ID= (os.environ['EBAY_API_ID'])
api = Connection(appid=YOUR_APP_ID, config_file=None)

def get_set_ebay(set_num):
    corrected_set_num = set_num.split("-")
    header = {"Accept-Language": "de-AT de-DE"}
    response = api.execute('findItemsAdvanced', {'keywords': f'LEGO {corrected_set_num[0]}',
                                                 "header":header,
                                                 'itemFilter': [{'name': 'Condition', 'value': 'New'} ]})
    item_dict=response.dict()["searchResult"]["item"][0]
    data_website="Ebay"
    data_url=item_dict["viewItemURL"]
    data_subject=item_dict["title"]
    price_value=item_dict["sellingStatus"]["currentPrice"]["value"]
    logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/EBay_logo.svg/1280px-EBay_logo.svg.png"
    return ad_class.AdObject(data_website, data_url,data_subject, price_value, logo )

