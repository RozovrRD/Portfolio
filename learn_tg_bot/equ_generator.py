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
            a = 1
            b = 1
            roots_coefficients[new_key] = (a, b)
    return roots_coefficients


def print_equation():
    equation_components = create_roots_and_coef(1)
    for key, value in equation_components.items():
        A, B, C = create_coefficients(key[0], key[1], value[0], value[1])
        if B == 1:
            answer_str = 'x^2 + x '
        elif B == -1:
            answer_str = 'x^2 - x '
        elif B >= 0 and B > 1:
            answer_str = 'x^2 + ' + str(B) + 'x '
        else:
            answer_str = 'x^2 ' + '- ' + str(abs(B)) + 'x '
        if C >= 0:
            answer_str = answer_str + '+ ' + str(C) + ' = 0'
        else:
            answer_str = answer_str + '- ' + str(abs(C)) + ' = 0'
        return answer_str, key[0], key[1]

