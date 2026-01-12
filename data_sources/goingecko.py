import json
import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/list"

def coin_list():
    response = requests.get(url)
    return response.json()

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1"
# params = {"ids":"bitcoin,ethereum,solana,dogecoin,cardano,ripple",
# "vs_currencies":"usd"}

response = requests.get(url)
df = pd.DataFrame(response.json())
df['last_updated'] = pd.to_datetime(df['last_updated'],errors="coerce")
# print(df.head())
# print(df.transpose().reset_index().rename(columns={'index':'asset_id'}).head())
print(df[['current_price', 'id', 'name']].head())
# print(df.columns)