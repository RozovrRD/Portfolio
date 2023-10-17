import re
from datetime import date, time, datetime

# with open('file.txt', 'r', encoding='utf-8') as file:
#     s = file.read()
#     file.seek(0)
#     sws = re.sub(r'[^\w\s\d]','', s)
#     sl = sws.replace(' ', '')
#     ans = file.readlines()
#     print('Input file contains:')
#     print(len([i for i in s if i.isalpha()]))
#     print(len(sws.split()), 'words')
#     print(len(ans), 'lines')



# with open("test.txt") as file:    # открть и прочитать уже созданный файл
#     info = file.read()
#     print(info)


# with open("test1.txt", 'w') as file:
#     file.write('test1')
#
#
# with open("test1.txt") as file:
#     info = file.read()
#     print(info)
#
#
# info_str = 'Try to learn how to deal with strings and files!'
#
# with open("text1.txt", 'w') as file:
#     for i in info_str:
#         file.write(i)
#
# with open("text1.txt") as file:
#     info = file.readlines()
#     print(info)

# выводит строки максимальной длины
# with open('lines.txt', 'r', encoding='utf-8') as file:
#     l = [line.rstrip() for line in file.readlines()]
#     trig = len(max(l, key=len))
#     for line in l:
#         if len(line) == trig:
#             print(line)


# with open('population.txt', 'r') as file:
#     for line in file:
#         info = [item.rstrip() for item in line.split('\t')]
#         if info[0][0] == 'G' and int(info[1]) > 500000:
#             print(info[0])


#
# def read_csv():
#     with open('data.csv', 'r') as file:
#         keys = file.readline().replace('\n', '').split(',')
#         answer = list()
#         for line in file:
#             values = line.replace('\n', '').split(',')
#             answer.append(dict(zip(keys, values)))
#         return answer



# with open('class_scores.txt', 'r', encoding='utf-8') as file,open('new_scores.txt', 'w', encoding='utf-8') as nfile:
#     ans = list()
#     for line in file:
#         new_mark = int(line.split()[1])
#         if new_mark < 95:
#             ans.append(line.split()[0]+' ' + str(new_mark+5)+'\n')
#         else:
#             ans.append(line.split()[0]+' ' + '100'+'\n')
#
#     print(ans)
#     nfile.writelines(ans)

# with open('goats.txt', 'r', encoding='utf-8') as file, open('answer.txt', 'w', encoding='utf-8') as nfile:
#     file.readline()
#     answer = list()
#     ans = list()
#     colors = dict()
#     while 1:
#         s = file.readline()
#         if s == 'GOATS\n':
#             break
#         colors.setdefault(s.rstrip().split()[0], 0)
#     for line in file:
#         colors[line.rstrip().split()[0]] += 1
#     for key, value in colors.items():
#         if value * 100 > 7 * sum(colors.values()):
#             answer.append(key)
#     answer.sort()
#     print(answer)
#     for i in answer:
#         ans.append(i + ' goat' + '\n')
#     print(ans)
#     nfile.writelines(ans)

# with open('logfile.txt', 'r', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as o_f:
#     for line in file:
#         s = line.split(',')
#         s[1].rstrip()
#         s[2].rstrip()
#         time1 = [int(i) for i in s[1].split(':')]
#         time2 = [int(i) for i in s[2].split(':')]
#         if (time2[0]*60+time2[1]) - (time1[0]*60+time1[1]) >= 60:
#             o_f.write(s[0]+'\n')


# with open('words.txt', 'r', encoding='utf-8') as file:
#     l = file.read().split()
#     etalon = len(max(map(str.rstrip, l), key=len))
#     for i in l:
#         if len(i) == etalon:
#             print(i)



# with open('for.txt', 'r', encoding='utf-8') as file:
#     l = file.readlines()
#     if len(l) <=10:
#         print(*l)
#     else:
#         print(*l[-10:], sep='')



# ans = list()
# with open('last.txt', 'r', encoding='utf-8') as file:
#     l = file.readlines()
#     for i in range(1, len(l)):
#         if i == 1 and 'def' in l[0]:
#             ans.append(l[0][4:l[0].index('(')])
#         if 'def' in l[i] and '#' not in l[i-1]:
#             ans.append(l[i][4:l[i].index('(')])
# if len(ans) == 0:
#     print('Best Programming Team')
# else:
#     print(*ans, sep='\n')


# with open('files.txt', 'r', encoding='utf-8') as file:
#     ans = dict()
#     size_file = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
#     files_volume = dict()
#     for line in file:
#         info = line.split()
#         volume = int(info[1]) * size_file[info[2]]
#         keyy = info[0].split('.')[1]
#         value = info[0]
#         ans[keyy] = ans.get(keyy, []) + [value]
#         files_volume[keyy] = files_volume.get(keyy, 0) + volume
#     for key in sorted(ans.keys()):
#         for fn in sorted(ans[key]):
#             print(fn)
#         print('----------')
#         vol = files_volume[key]
#         ed = ''
#         if vol > 1023:
#             vol = round(vol / 1024)
#             ed = 'KB'
#             if vol > 1023:
#                 vol = round(vol / 1024)
#                 ed = 'MB'
#                 if vol > 1023:
#                     vol = round(vol / 1024)
#                     ed = 'GB'
#         print('Summary:', vol, ed)
#         print()

# with open('diary.txt', 'r', encoding='utf-8') as file:
#     info = file.read().split('\n\n')
#     answer = dict()
#     for l in info:
#         line = l[:17]
#         date_str, time_str = line.split('; ')
#
#         date_info = [int(i) for i in date_str.split('.')]
#         time_info = [int(i) for i in time_str.split(':')]
#
#         abzats_datetime = datetime(date_info[2], date_info[1], date_info[0], time_info[0], time_info[1])
#         answer.setdefault(abzats_datetime, l)
#
#     for key in sorted(answer.keys()):
#         print(answer[key])
#         answer.pop(key)
#         break
#
#     for key in sorted(answer.keys()):
#         print()
#         print(answer[key])


for a in range(1000):
    if all(((x < a) or (y < a)) and ((y < x-5) or (y<2*x-15)) for x in range(1000) for y in range(1000)):
        print(a)
        break


