import requests
import pandas as pd


# response = requests.get(
#     'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')

# print(response)
# print(response.json())


# crypto_name = list()
# price = list()
# last_ath = list()
# crypto_symbole = list()
# market_cap = list()
# resp_json = response.json()
# for elem in resp_json:
#     crypto_name.append(elem['name'])
#     price.append(elem['current_price'])
#     last_ath.append(elem['ath_date'])
#     crypto_symbole.append(elem['symbol'])
#     market_cap.append(elem['market_cap_rank'])


# d = {'Symbol': crypto_symbole, 'Crypto': crypto_name,
#      'Current Price $': price, 'Date of All Time High': last_ath, 'Market Cap': market_cap}
# df = pd.DataFrame(data=d)
# print(df.head(20))

"""
table crypto 
id | nom | symbole | current_price |high_24h\low_24h |price_change_percentage_24h|ath\ market_cap |

"""


# response_2 = requests.get(
#     'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=01-06-202')

# print(response_2)
# print(response_2.json())

# import requests

# url = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?period_id=1MIN&time_start=2016-01-01T00:00:00'
# headers = {'X-CoinAPI-Key': '73034021-THIS-IS-SAMPLE-KEY'}
# response = requests.get(url, headers=headers)

# url = 'https://rest.coinapi.io/v1/ohlcv/BTC/USD/history?period_id=1MIN&time_start=2016-01-01T00:00:00'
# headers = {'X-CoinAPI-Key': '73034021-THIS-IS-SAMPLE-KEY'}
# response = requests.get(url, headers=headers)

# print(response)
