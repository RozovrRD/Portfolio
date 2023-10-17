import sys
import math as m
import traceback
from random import*
from decimal import *
from functools import reduce


def test(a, b):
    print(a+b)


def greet(*args):
    l = list(args)
    if len(l) == 1:
        return 'Hello, {}!'.format(l[0])
    else:
        ans = 'Hello,'
        for i in l:
            ans = ans + ' ' + l[i] + 'and'
        ans += '!'
        return ans


def variables_errors():
    try:
        print(a)
    except Exception as exc:
        e = sys.exc_info()
        for i in e:
            print("\033[31m{}".format(i))

    print()

    try:
        с = 5
        c += 1
    except Exception as exp:
        e = sys.exc_info()
        for i in e:
            print("\033[31m{}".format(i))


def num_errors():
    try:
        a = 2 / 0
    except Exception as exc:
        e = sys.exc_info()
        for i in e:
            print("\033[31m{}".format(i))

    print()

    try:
        a = 2 + '5'
    except Exception as exc:
        e = sys.exc_info()
        for i in e:
            print("\033[31m{}".format(i))

    print()

    try:
        a = m.sqrt(-1)
    except Exception as exc:
        e = sys.exc_info()
        for i in e:
            print("\033[31m{}".format(i))

    print()

    try:
        a = 0 ** (-2)
    except Exception as exc:
        e = sys.exc_info()
        for i in e:
            print("\033[31m{}".format(i))

    print()


def different_errors():
    #colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange',
    #           'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None,
    #           'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac',
    #           'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
    #
    # result = {key, value for key, value in colors.items() if value} ошибка синтаксиса
    try:
        s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
        result = {int(i[0]): str(i[2:]) for i in s.strip()}
        print(result)
    except Exception as exc:
        print(traceback.format_exc())



    try:       # перенести сложение строки на одну сторону
        ip_addres = str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.'
        + str(randint(0, 255)) + '.' + str(randint(0, 255))
        print(ip_addres)
    except Exception as exc:
        print(traceback.format_exc())

    try: # вместо добавления set надо добавить неизменяемы тип данных например frozenset
        ans = set()
        while len(ans) < 100:
            s = set()

            while len(s) < 7:
                s.add(randint(1, 49))
            ans.add(sorted(s))
        for i in ans:
            print(*i)
    except Exception as exc:
        print(traceback.format_exc())


    try:
        s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62'
        l = list()
        for i in s:
            l.append(Decimal(i))
    except Exception as exc:
        print(traceback.format_exc())

    # try:
    #     test(a=10, 10)
    # except Exception as exc:
    #     print(traceback.format_exc())
    try:
        print(greet('Timur'))
        print(greet('Timur', 'Roman'))
        print(greet('Timur', 'Roman', 'Ruslan'))
    except Exception as exc:
        print(traceback.format_exc())

    # try:
    #     data = [['Tokyo', 35676000, 'primary'],
    #             ['New York', 19354922, 'nan']]
    #
    #     ll = list(filter(lambda inf: inf if inf[2] == 'primary' and inf[1] > 10000000 else None, data))
    #     ans = sorted(list(map(lambds item: item[0], ll)))
    #     print('Cities:', *ans)
    # except Exception as exc:
    #     print(traceback.format_exc())






print()

variables_errors()

print()

num_errors()

print()

different_errors()

