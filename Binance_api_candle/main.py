import tolerant_requests as tr
import random as r
import csv

symbol_info = tr.get('https://api.binance.com/api/v3/exchangeInfo', type_response='json')
list_info_in_dicts = symbol_info.get('symbols')
list_of_symbols = list()
for item in list_info_in_dicts:
    list_of_symbols.append(item.get('symbol'))

random_symbol = list_of_symbols[r.randint(0, len(list_of_symbols))]
print(random_symbol)

kline_info_request = tr.get('https://api.binance.com/api/v3/klines', {'symbol': random_symbol, 'interval': '1m'}, type_response='json')
print(kline_info_request)

header_list = ["Kline open time",
                "Open price",
                "High price",
                "Low price",
                "Close price",
                "Volume",
                "Kline Close time",
                "Quote asset volume",
                "Number of trades",
                "Taker buy base asset volume",
                "Taker buy quote asset volume",
                "Unused field, ignore"]

data_for_write = [header_list]
for item in kline_info_request:
    data_for_write.append(item)

# csvfile = open("klines_info.csv", 'w')
# with csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data_for_write)
# print('successfully')

with open("klines_info1.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data_for_write)
print('successfully')






