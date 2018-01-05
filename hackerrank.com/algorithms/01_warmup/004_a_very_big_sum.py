"""
https://www.hackerrank.com/challenges/a-very-big-sum/problem
"""

import sys


def aVeryBigSum(n, ar):
    return sum(ar)

# n = int(input().strip())
# ar = list(map(int, input().strip().split(' ')))

n = 5
input_string = '1000000001 1000000002 1000000003 1000000004 1000000005'
ar = list(map(int, input_string.strip().split(' ')))

result = aVeryBigSum(n, ar)
print(result)