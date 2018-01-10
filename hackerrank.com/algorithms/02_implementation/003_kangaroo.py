"""
https://www.hackerrank.com/challenges/kangaroo/problem
"""

import sys


def kangaroo(x1, v1, x2, v2):
    dx = abs(x1 - x2)
    while True:
        dx = abs(x1 - x2)
        if dx == 0:
            return 'YES'
        x1 = x1 + v1
        x2 = x2 + v2
        if abs(x1 - x2) >= dx:
            return 'NO'


# x1, v1, x2, v2 = input().strip().split(' ')
# x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

x1, v1, x2, v2 = '0 3 4 2'.split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

result = kangaroo(x1, v1, x2, v2)
print(result)

x1, v1, x2, v2 = '0 2 5 3'.split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

result = kangaroo(x1, v1, x2, v2)
print(result)