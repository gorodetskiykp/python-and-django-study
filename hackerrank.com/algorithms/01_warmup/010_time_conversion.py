"""
https://www.hackerrank.com/challenges/time-conversion/problem
"""

import sys


def timeConversion(s):
    if s[-2:] == 'PM':
        if s[:2] == '12':
            return s[:-2]
        else:
            return '{}{}'.format(int(s[:2])+12, s[2:-2])
    else:
        if s[:2] == '12':
            return '{}{}'.format('00', s[2:-2])
        else:
            return s[:-2]


# s = input().strip()
s = '07:05:45PM'

result = timeConversion(s)
print(result)
