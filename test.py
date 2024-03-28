import requests


def get_data():
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    content = float(response.json()['price'])
    return round(content, 1)


print(get_data())
