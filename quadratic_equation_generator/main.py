from random import randint

def create_coefficients(x1, x2, a, b):
    A = a*b
    B = -a*x2 -b*x1
    C = x1*x2
    return A, B, C


def create_roots_and_coef(count_of_equations):
    roots_coefficients = dict()
    while len(roots_coefficients) < count_of_equations:
        x1 = randint(-30, 30)
        x2 = randint(-30, 30)
        new_key = tuple([x1, x2])
        if new_key not in roots_coefficients.keys():
            a = randint(-10, 10)
            b = randint(-10, 10)
            roots_coefficients[new_key] = (a, b)
    return roots_coefficients


equation_count = int(input('Enter equations count: '))

equation_components = create_roots_and_coef(equation_count)

for key, value in equation_components.items():
    A, B, C = create_coefficients(key[0], key[1], value[0], value[1])
    if B >= 0:
        print(A, 'x^2 + ', B, 'x ', sep='', end='')
    else:
        print(A, 'x^2 ', B, 'x ', sep='', end='')
    if C >= 0:
        print('+', C, '= 0', 'roots:', key[0], key[1])
    else:
        print(C, '= 0', 'roots:', key[0], key[1])
