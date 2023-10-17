# TODO создать библиотеку для получения каких-либо данных с какого-либо сайта

import requests
import random
from time import sleep

def get(url, params=None, headers=None, type_response='text'):
    number_of_code = 0
    number_of_errors = 0
    while number_of_code != 200:
        try:
            sleep(1)
            tolerant_request = requests.get(url, params, headers=headers, timeout=5)
            number_of_code = tolerant_request.status_code
            if type_response == 'text':
                return tolerant_request.text
            else:
                return tolerant_request.json()
        except Exception as exc:   # ловит ошибку
            number_of_errors += 1
            if number_of_errors > 5:
                raise RuntimeError(f'>5mist: {exc}')  # записывает ошибку в строку вывода
            else: pass


def post(url, params=None, headers=None, type_response='text', data=None, json=None):
    number_of_code = 0
    number_of_errors = 0
    while number_of_code != 200:
        try:
            sleep(1)
            tolerant_request = requests.post(url=url, params=params, headers=headers, data=data, json=json)
            number_of_code = tolerant_request.status_code
            if type_response == 'text':
                return tolerant_request.text
            else:
                return tolerant_request.json()
        except Exception as exc:  # ловит ошибку
            number_of_errors += 1
            if number_of_errors > 5:
                raise RuntimeError(f'>5mist: {exc}')  # записывает ошибку в строку вывода
            else:
                pass

#if __name__ == '__main__':
    # print('ping: ', end='')
    # get('https://api.binance.com/api/v3/ping')
    # 
    # get('https://api.binance.com/api/v3/time')
    # 
    # print('BNBBTC_symbol_info: ', end='')
    # get('https://api.binance.com/api/v3/exchangeInfo', {'symbol': 'BNBBTC'})
    # 
    # # print('MARGIN", "LEVERAGED_permission: ', end='')
    # # get('https://api.binance.com/api/v3/exchangeInfo', {'permissions': "[\"MARGIN\",\"LEVERAGED\"]"})
    # 
    # print('ETHBTC Market_data_endpoints: ', end='')
    # get('https://api.binance.com/api/v3/depth', {'symbol': 'ETHBTC', 'limit': 120})
    # 
    # print('ETHBTC Kline/Candlestick data: ', end='')
    # get('https://api.binance.com/api/v3/klines', {'symbol': 'ETHBTC', 'interval': '1m'})
    # 
    # print('ETHBTC Current average price: ', end='')
    # get('https://api.binance.com/api/v3/avgPrice', {'symbol': 'ETHBTC'})




