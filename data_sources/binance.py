import requests
import json
import pandas as pd
# def get_binance_price(symbol="BTCUSDT"):
url = f'https://api.bybit.com/v5/market/funding/history?category=linear&symbol=BTCUSDT'
# return requests.get(url).json()

df = pd.DataFrame(requests.get(url).json())
print(df)

