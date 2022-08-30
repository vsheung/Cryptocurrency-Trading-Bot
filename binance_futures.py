import logging
import requests

logger = logging.getLogger()


# Returns current trading rules and symbol info
def get_tickers():
    tickers_url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
    response_object = requests.get(tickers_url)

    tickers = []

    for ticker in response_object.json()['symbols']:
        tickers.append(ticker['pair'])

    return tickers;
