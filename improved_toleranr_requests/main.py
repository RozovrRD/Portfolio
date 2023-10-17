# TODO создать библиотеку для получения каких-либо данных с какого-либо сайта

import requests
import random
from time import sleep

# def get(url, params=None, headers=None, type_response='text'):
#     number_of_code = 0
#     number_of_errors = 0
#     while number_of_code != 200:
#         try:
#             sleep(1)
#             tolerant_request = requests.get(url, params, headers=headers, timeout=5)
#             number_of_code = tolerant_request.status_code
#             if type_response == 'text':
#                 return tolerant_request.text
#             else:
#                 return tolerant_request.json()
#         except Exception as exc:   # ловит ошибку
#             number_of_errors += 1
#             if number_of_errors > 5:
#                 raise RuntimeError(f'>5mist: {exc}')  # записывает ошибку в строку вывода
#             else: pass
#
#
# def post(url, params=None, headers=None, type_response='text', data=None, json=None):
#     number_of_code = 0
#     number_of_errors = 0
#     while number_of_code != 200:
#         try:
#             sleep(1)
#             tolerant_request = requests.post(url=url, params=params, headers=headers, data=data, json=json)
#             number_of_code = tolerant_request.status_code
#             if type_response == 'text':
#                 return tolerant_request.text
#             else:
#                 return tolerant_request.json()
#         except Exception as exc:  # ловит ошибку
#             number_of_errors += 1
#             if number_of_errors > 5:
#                 raise RuntimeError(f'>5mist: {exc}')  # записывает ошибку в строку вывода
#             else:
#                 pass


def request (request_type, deley_time, url, params=None, headers=None, type_response='text', data=None, json=None):
    if request_type == 'get':
        number_of_code = 0
        for i in range(5):
            sleep(deley_time)
            tolerant_request = requests.get(url, params, headers=headers, timeout=5)
            number_of_code = tolerant_request.status_code
            if type_response == 'text' and number_of_code == 200:
                return tolerant_request.text
            elif type_response == 'json' and number_of_code == 200:
                return tolerant_request.json()
            elif i == 4 and number_of_code != 200:
                raise RuntimeError(f'status_code = {number_of_code}, returned_text: {tolerant_request.text}')
    elif request_type == 'post':
        number_of_code = 0
        for i in range(5):
            sleep(deley_time)
            tolerant_request = requests.post(url=url, params=params, headers=headers, data=data, json=json)
            number_of_code = tolerant_request.status_code
            if type_response == 'text' and number_of_code == 200:
                return tolerant_request.text
            elif type_response == 'json' and number_of_code == 200:
                return tolerant_request.json()
            elif i == 4 and number_of_code != 200:
                raise RuntimeError(f'status_code = {number_of_code}, returned_text: {tolerant_request.text}')
    else:
        raise RuntimeError("'", request_type, "'", " request doesn't exist in this library", sep='')




if __name__ == '__main__':
    print('ping: ', end='')
    print(request('get', 1, 'https://api.binance.com/api/v3/ping'))
    print(request('get', 2, 'https://api.binance.com/api/v3/time'))
    print('ETHBTC Kline/Candlestick data: ', end='')
    print(request('get', 0.1, 'https://api.binance.com/api/v3/klines', {'symbol': 'ETHBTC', 'interval': '1m'}))
    print(request('get', 0.1, 'https://api.binance.com/api/v3/ticker/24hr', {'symbol': 'ETHBTC', 'interval': '1m'}))




