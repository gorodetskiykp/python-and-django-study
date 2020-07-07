"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.
Input: A string, that consist of digits.
Output: An Int.
Example:
    beginning_zeros('100') == 0
    beginning_zeros('001') == 2
    beginning_zeros('100100') == 0
    beginning_zeros('001001') == 2
    beginning_zeros('012345679') == 1
    beginning_zeros('0000') == 4
Precondition: 0-9
"""


def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))


# import re

# def beginning_zeros(number: str) -> int:
#     result = re.match(r'^(0+)', number)
#     return 0 if not result else len(result.group())


# beginning_zeros = lambda number: len(number) - len(number.lstrip('0'))


# import re
# def beginning_zeros(number: str) -> int:
#     return len(re.sub(r'[^0].*$', '', number))


# from itertools import takewhile
# beginning_zeros = lambda number: len(list(takewhile(lambda x: x=='0', number)))


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('0010'))

    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4