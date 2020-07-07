"""
Cоздать функцию, которая получает массив(tuple) и возвращает набор с 3 элементами - первым, третьим, вторым с конца.
Входные данные: Набор длинной не менее 3 элементов.
Выходные данные: Набор элементов.
Пример:
easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
easy_unpack((6, 3, 7)) == (6, 7, 3)
"""

def easy_unpack(elements: tuple) -> tuple:
    return elements[0], elements[2], elements[-2]


if __name__ == '__main__':
    print("Example:")
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
    
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)