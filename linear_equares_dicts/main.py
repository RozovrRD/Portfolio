def terms_to_left(equ_str):
    term_list = equ_str.split('=')
    returned_string = term_list[0]
    right_side_string = term_list[-1].replace('-', '+-')
    equ_right_side = right_side_string.split('+')
    for term in equ_right_side:
        returned_string += '-' + term
    returned_string = returned_string.replace('--', '+')
    return returned_string


def string_to_dict(equ_str):
    returned_dict = dict()
    for char in equ_str:
        if char.isalpha():
            returned_dict.setdefault(char, 0)
    returned_dict.setdefault('free_koef', 0)
    return returned_dict


def coefficients_counting(equ_dict, equ_str):
    equ_str = equ_str.replace('-', '+-')
    list_of_terms = equ_str.split('+')
    list_of_numeric_terms = list_of_terms.copy()
    for term in list_of_terms:
        coefficient = 1
        if not any(key in term for key in equ_dict.keys()):
            multipliers = term.split('*')
            for multiplier in multipliers:
                if len(multiplier) > 0:
                    coefficient *= int(multiplier)
            equ_dict['free_koef'] = equ_dict.get('free_koef') + coefficient
        else:
            for key in equ_dict.keys():
                if key in term:
                    multipliers_string = term.replace(key, '')
                    multipliers_string = multipliers_string.replace('**', '*')
                    multipliers = multipliers_string.split('*')
                    for multiplier in multipliers:
                        if len(multiplier) > 0:
                            coefficient *= int(multiplier)
                    equ_dict[key] = equ_dict.get(key) + coefficient


def create_dict(equ_str):
    returned_dict = dict()
    for char in equ_str:
        if char.isalpha():
            returned_dict.setdefault(char, {'terms': list(), 'coeff': list(), 'result': 0})
    returned_dict['free_koef'] = {'terms': list(), 'coeff': list(), 'result': 0}
    return returned_dict


def create_coefficients(equ_dict: dict, equ_str: str):
    print(equ_str + '\n')
    equ_str = equ_str.replace('-', '+-')
    list_of_terms = equ_str.split('+')
    list_of_numeric_terms = list_of_terms.copy()

    for term in list_of_terms:
        for key in equ_dict.keys():
            if key in term:
                equ_dict[key]['terms'].append(term)
                list_of_numeric_terms.remove(term)
    equ_dict['free_koef']['terms'] = list_of_numeric_terms

    for key, value in equ_dict.items():
        print(value['terms'])
        for term in value['terms']:
            term = term.replace(key, '').replace('**', '*')
            coefficient = 1
            multipliers = term.split('*')
            for multiplier in multipliers:
                if len(multiplier) > 0:
                    coefficient *= int(multiplier)
            value['coeff'].append(coefficient)
        print(f'{value["coeff"]}\n')
        for coefficient in value['coeff']:
            value['result'] += coefficient


def print_equation(equ_dict):
    for key, value in equ_dict.items():
        if key == 'free_koef':
            print(value['result'], '=0', sep='')
        elif value['result'] > 0:
            print('+', value['result'], key, sep='', end='')
        else:
            print(value['result'], key, sep='', end='')


if __name__ == '__main__':
    equation_string = '25*x*5*1 +1-8* 7 -8y*9+5*z*11-8x*16-12*2*x = 15x - 7*y*8 + 11z*2 - 11'.replace(' ', '')
    equation_string = terms_to_left(equation_string)
    # equation_dict = string_to_dict(equation_string)
    # coefficients_counting(equation_dict, equation_string)
    equation_dict = create_dict(equation_string)
    create_coefficients(equation_dict, equation_string)
    print_equation(equation_dict)



