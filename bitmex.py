import requests

# Returns current trading rules and symbol info
def get_tickers():
    tickers_url = "https://www.bitmex.com/api/v1/instrument/active"
    response_object = requests.get(tickers_url)

    tickers = []

    for ticker in response_object.json():
        tickers.append(ticker['symbol'])

    return tickers

