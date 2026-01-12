import requests

# def whales_alerts():
#     url = "https://api.whale-alert.io/v1/transactions"
#     params = {'api_key':'YOUR_API_KEY',
#               'min_value':500000,
#               'start':0}
#     data=requests.get(url,params=params).json()
#     print(data)
#     return data

import requests

url = "https://api.whale-alert.io/v1/status"
params = {"api_key": "YOUR_API_KEY"}

print(requests.get(url, params=params).json())


