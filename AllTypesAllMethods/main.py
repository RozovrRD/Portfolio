import re

first_list_of_numbers = [1, -1, 2, -2, 3, -3, 11]
second_list_of_numbers = [1, -1, 2, -2, 3, -3, 11]

first_list_of_letters = list('lettersfortest')
second_list_of_letters = list('randomword')

first_list_of_numbers.append(3) # добавляет элемент в конец списка
first_list_of_numbers.extend(second_list_of_numbers) # добавляет все элементы 2 списка в первый
first_list_of_numbers.insert(0, 11) # заменяет первый элемент списка на 11
second_list_of_numbers.remove(11) # удаляет первый элемент списка со значением 11
second_list_of_numbers.pop() # удаляет последний элемент списка и возвращает его значение
second_list_of_numbers.pop(1) # удаляет элемент списка с индексом 1 и возвращает его значение
first_list_of_letters.index('e') #возвращает индекс первого попавшегося эоемента списка(ищет во всем списке)
first_list_of_letters.index('e', 4) #ищет индекс элемента после 4
first_list_of_letters.index('e', 1, 5) #ищет элемент в списке в указанном промежутке
second_list_of_letters.count('t') #считает количество элементов t в списке
first_list_of_numbers.sort() # сортирует числа по возрастанию
first_list_of_letters.sort() # сортирует в соответствии с алфавитом
second_list_of_letters.reverse() # реверсирует список
new_list_of_number = first_list_of_numbers.copy() # создает копию списка. Изменяя новый список-старый не поменяется
new_list_of_number.clear() # очищает список

tuple_of_one_element = (2, )
list_of_lists = [[1, 4], [2, 2], [1, 3]]
list_of_lists.sort(key=lambda item: item[1]) # сортирует список по лямда функции: item-элемент исходного списка




string_for_methods = 'jjjfhheu\nccdjje,dcd\t'
string_for_methods.find('e', 7, 10) # поиск первого совпавшего элемента в строке(либо во всей либо в указанном промежутке)
string_for_methods.rfind('e', 7, 10) # поиск последнего совпавшего элемента в строке(либо во всей либо в указанном промежутке)
string_for_methods.replace('jj', 'j') # заменяет подстроки по образцу(можно передать количество заменяемых подстрок)
string_for_methods.split(sep='j') # разделяет строку по разделителю и превращает в список
re.split('\n,', string_for_methods)
string_for_methods.isalpha() # проверяет состоит ли строка из букв
string_for_methods.isdigit() # проверяет состоит ли строка из цифр
string_for_methods.isalnum() # проеряет состоит ли строка из цифр или букв
string_for_methods.isspace() # проверяет состоит ли строка из пробелов табов и тд
string_for_methods.upper() # преобразует строку к верхнему регистру
string_for_methods.lower() # преобразует строку к нижнему регистру
string_for_methods.startswith('jjf') # начинается строка с подстроки
string_for_methods.endswith('\t') # заканчивается ли строка подстрокой
string_divisor = ','                # расширяет строку списком, добавляя элементы по разделителю
second_string_for_methods = string_divisor.join(first_list_of_letters)
string_for_methods.count('jj') # считает количество непересекающихся вхождений подстроки в строку
string_for_methods.strip() # удалит в начале и в конце строки лишние пробелы или подстроку, если ее указать в скобках
string_for_methods.rstrip() # удалит только в конце строки
string_for_methods.lstrip() # удалит только в начале строки



first_set = {1, 2, 3, 4, 5, 6}
second_set = {2, 3, 4}
# неизменяющие методы
print(3 in first_set) # есть ли 3 в первом множестве
first_set.isdisjoint(second_set) # проверяет пересекаются ли множества
first_set.issubset(second_set) # является ли первое множество подмножеством второго?
first_set.issuperset(second_set) # является ли второе множество подмножеством первого?
first_set.union(second_set) # объединение множеств
first_set.intersection(second_set) # пересечение множеств
first_set.difference(second_set) # множество всех элементов первого отличных от второго

# изменяющие методы
first_set.update(second_set) # пересечение множеств
first_set.intersection_update(second_set) # пересечение множеств
first_set.difference_update(second_set) # разность множеств
first_set.add(3) # добавление элемента в множество
first_set.remove(3) # удаляет элемент, возвращает keyerror если элемента нет
first_set.discard(3) # удаляет элемент, если он есть
first_set.update(second_set) # пересечение множеств
first_set.pop() # возвращает и удаляет случайный элемент



dict_for_methods = {(1, 1, 1):'a', (2, 2, 2):'b', (3, 3, 3):'c', 4:[1, 2, 3], 'str':'string'}
second_dict = {(1, 1, 1): 'e', 5:5}

dict_for_methods.copy() # копия словаря
new_dict = dict.fromkeys([1, 2, 3]) # создает словарь из последовательности с ключами-последовательности и значениями None
new_dict1 = dict.fromkeys([1, 2, 3], 'str') # создает словарь из последовательности с ключами-последовательности и значениями 'str'

new_dict2 = dict.fromkeys(dict_for_methods) # создает новый словарь с ключами как у указанного

print(new_dict2)

dict_for_methods.get((1, 1, 1)) # возвращает значение по ключу( если его нет - возвращает none
dict_for_methods.items() # возвращает пары [ключ, значение....]
dict_for_methods.keys() # возвращает ключи словаря
dict_for_methods.pop((1, 1, 1)) # удаляет ключ и элемент и возвращает значение
dict_for_methods.popitem() # удаляет и возвращает случайную пару ключ-значение
dict_for_methods.setdefault((1, 2, 3), 'h') # возвращает значение по ключу, а если его нет то создает ключ по указанному параметру c указанным значением
dict_for_methods.update(second_dict) # добавляет пары ключ-значение, если ключ уже есть - то значение перезаписывается
dict_for_methods.values() # возвращает значения в словаре
print(dict_for_methods)
dict_for_methods.clear() # очищает словарь

str_for_test = '25*x+y-15*6*7-8*7+5*z*6'
print(re.split("z|y|x", str_for_test))

