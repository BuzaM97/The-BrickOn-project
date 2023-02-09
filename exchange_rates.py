from easy_exchange_rates import API
from datetime import date

def change_currency(currency_amount, currency):
  today = str(date.today())
  api = API()
  currency_rate = api.get_exchange_rates(
    base_currency=currency,
    start_date= today,
    end_date=today,
    targets=["HUF"]
  )

  currency_change = currency_rate[today]['HUF']
  huf_price = currency_amount* currency_change
  return round(huf_price, 2)

