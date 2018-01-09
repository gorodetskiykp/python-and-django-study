"""
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
"""

import sys


def birthdayCakeCandles(n, ar):
    return ar.count(max(ar))


# n = int(input().strip())
# ar = list(map(int, input().strip().split(' ')))

n = 4
input_string = '3 2 1 3'
ar = list(map(int, input_string.strip().split(' ')))

result = birthdayCakeCandles(n, ar)
print(result)