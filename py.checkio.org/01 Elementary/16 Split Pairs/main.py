"""
Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
Входные данные: Строка.
Входные данные: An iterable of strings.
Пример:
    split_pairs('abcd') == ['ab', 'cd']
    split_pairs('abc') == ['ab', 'c_']
Предварительное условие: 0<=len(str)<=100
"""


def split_pairs(a: str) -> list:
    return ["".join(pair) for pair in zip(a[::2], a[1::2]+"_")]


# from textwrap import wrap

# def split_pairs(a):
#     a = a + '_' if len(a) % 2 else a
#     return wrap(a, 2)


# import itertools, operator

# def split_pairs(a):
#     it = itertools.chain(a, '_')
#     return map(operator.add, it, it)


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(split_pairs('abcd')) == ['ab', 'cd']
    # assert list(split_pairs('abc')) == ['ab', 'c_']
    # assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    # assert list(split_pairs('a')) == ['a_']
    # assert list(split_pairs('')) == []
    # print("Coding complete? Click 'Check' to earn cool rewards!")

