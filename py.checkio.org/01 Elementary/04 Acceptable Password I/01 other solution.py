"""
Необходимо создать функцию проверки пароля.
Условия проверки: длина пароля больше 6
Input: A string.
Output: A bool.
Пример:
is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == True
"""

def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False