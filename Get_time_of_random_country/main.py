# TODO вывести 10 случайных стран с дата, время, часовой пояс
import urllib.request
import requests
import random
from time import sleep

# with urllib.request.urlopen("https://developer.mozilla.org/") as url:
#     s = url.read()
#     print (s)
#     print(type(url))
number_of_code = 0
while number_of_code != 200:   # пока код сайта не 200 то есть 200 это нормальное состояние запроса
    try:     #ловим ошибку - если в коде блока try вылезает ошибка то код переклбчается на блок exept
        sleep(1)   # ставит прогарамму на паузу чтобы чайт не подумал что дудос
        site = requests.get('https://www.worldtimeapi.org/api/timezone', timeout=5)  # кусок данных с сайта о странах
        number_of_code = site.status_code
    except: pass   #pass ничего не делает и возвращается в цикл for

#site = requests.get('https://www.worldtimeapi.org/api/timezone/Europe/London') # кусок данных о конкретной стране
#print(site.json())

# number_of_country = random.randint(0, len(site.json()))     # выбираем случайный номер элемента site.json
# print(number_of_country)
# url_addres_for_get = 'https://www.worldtimeapi.org/api/timezone/' + site.json()[number_of_country]
# print(url_addres_for_get)

count_of_country = 10
while count_of_country != 0:      #для 10 случайных стран
    number_of_country = random.randint(0, len(site.json()))     # выбираем случайный номер элемента site.json
    if site.json()[number_of_country].count('/') == 2:
        continue
    url_addres_for_get = 'https://www.worldtimeapi.org/api/timezone/' + site.json()[number_of_country] # получание url строки для составление get запроса
    number_of_code = 0
    while number_of_code != 200:
        try:
            sleep(1)
            time_take = requests.get(url_addres_for_get, timeout=5) # получение куска данных о конкретной стране
            number_of_code = time_take.status_code
        except:
            pass
    info_about_time = time_take.json()['datetime']  # строка про дату и время для конкретной страны
    print('date of country', site.json()[number_of_country], info_about_time[0:10])
    print('time of country', site.json()[number_of_country], info_about_time[11:19])
    print('time_zone of country', site.json()[number_of_country], info_about_time[26:])
    count_of_country -= 1




