"""
Напишите функцию, которая будет получать 2 числа и возвращать результат произведения этих чисел.
Входные данные: Два аргумента. Оба int
Выходные данные: Int.
Пример:
mult_two(2, 3) == 6
mult_two(1, 0) == 0
"""

def mult_two(a: int, b: int) -> int:
    return a * b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))
    
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0