from random import randint

letters_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
paths_dict = {(0, 1): 0, (0, 2): 0, (0, 3): 0, (1, 2): 0, (1, 4): 0, (2, 3): 0, (3, 4): 0,
              (1, 0): 0, (2, 0): 0, (2, 1): 0, (3, 0): 0, (3, 2): 0, (4, 1): 0, (4, 3): 0}

def print_table(paths):
    print('\t', 'A', '\t', 'B', '\t', 'C', '\t', 'D', '\t', 'E')
    for line in range(5):
        print(letters_dict[line], end='')
        for column in range(5):
            if column != line and column + line != 4 and column + line != 6:
                print('\t', paths[(line, column)], end='')
            else:
                print('\t', '.', end='')
        print()


def path_generate(paths_dict):
    lines = list()
    while len(lines) < 7:
        path = randint(1, 10)
        if path not in lines:
            lines.append(path)
    for key in paths_dict.keys():
        symmetric_key = list(key)
        symmetric_key.reverse()
        symmetric_key = tuple(symmetric_key)
        paths_dict[key] = lines[0]
        paths_dict[symmetric_key] = lines[0]
        del lines[0]
        if len(lines) < 1:
            break
    return paths_dict


count_of_exc = int(input('Enter the number of tasks: '))
for i in range(count_of_exc):
    print("№", i+1)
    dict_of_path = path_generate(paths_dict)
    print_table(dict_of_path)
    print()
