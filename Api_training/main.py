# TODO зайти на любую вк страницу пользователя и вывести имя пользователя

import tolerant_requests as tr
import re

headers = {        # достаются из network-> headers из твоего запроса на страницу (преимущественно из первого запроса)
"Accept-Encoding": 'gzip, deflate, br',
"Accept-Language": 'ru-RU,ru;q=0.9',
"Cache-Control": 'max-age=0',
"Cookie": 'remixlang=0; remixstlid=9094563434675135167_UMxBVF8Tb99OBqxqp3Qtrn05CZxCNtwOfuRc0ADMmZH; remixua=41%7C-1%7C195%7C1384047604; remixbdr=1; remixstid=567681454_nsu5hQRMhlTyUJ9BjGRXdqGTEZjVAe3eA3A4G9eCe5s; remixlgck=0ee7668396dfe4d66c; remixrefkey=40868000181cfd8cf0; remixnp=0; remixscreen_width=1600; remixscreen_height=900; remixscreen_dpr=1; remixscreen_depth=24; remixscreen_orient=1; remixscreen_winzoom=1; remixdark_color_scheme=0; remixcolor_scheme_mode=auto; remixdt=0; remixgp=22f143f4c900de6a8b69cf1a32862adf; tmr_lvid=d298acd81c06b1178e6d5be21420724b; tmr_lvidTS=1690388357351; remixuas=YzMwYThhYmYzOWY4YTZiYmU4ZjI5ZTVi; tmr_detect=0%7C1690388373558',
"Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
"Sec-Ch-Ua-Mobile": '?0',
"Sec-Ch-Ua-Platform": '"Windows"',
"Sec-Fetch-Dest": 'document',
"Sec-Fetch-Mode": 'navigate',
"Sec-Fetch-Site": 'none',
"Sec-Fetch-User": '?1',
"Upgrade-Insecure-Requests": '1',
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}


url = 'https://vk.com/snowshine96'
html_text = tr.get(url, headers=headers)
#print(html_text)

with open('html_file.html', 'w') as h_file: # создаем файл чтобы прочесть, который в случае чего точно закроется
    h_file.write(html_text)


result = re.search(r'<meta name="description" content=".+"', html_text)
print(result[0])
answer_string = result[0].split('content="')[1].split(',')[0]
print(answer_string)