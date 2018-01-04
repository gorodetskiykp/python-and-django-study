"""
https://www.hackerrank.com/challenges/simple-array-sum/problem
"""

import sys


def simpleArraySum(n, ar):
    return sum(ar)


# n = int(input().strip())
# ar = list(map(int, input().strip().split(' ')))
n = 6
input_string = '1 2 3 4 10 11'
ar = list(map(int, input_string.strip().split(' ')))

result = simpleArraySum(n, ar)
print(result)
