"""
Наибольшее произведение идущих подряд чисел
Найти наибольшее произведение 13 идущих подряд чисел. Функция должна возвращать максимальное произведение.
На вход подается строка из чисел.
"""

def solution(A):
    multi_list = []

    for index in range(len(A)):
        A13 = A[index:13+index]
        if len(A13) < 13:
            break
        multi13 = 1
        for i in A13:
            multi13 *= int(i)
        multi_list.append(multi13)

    return max(multi_list)

if __name__ == '__main__':
    A = '123456789123443256435232543'
    print(solution(A))

