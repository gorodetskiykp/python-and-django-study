"""
https://www.hackerrank.com/challenges/plus-minus/problem
"""

import sys


def plusMinus(arr):
    arr_size = len(arr)
    print('{:f}'.format(len([item for item in arr if item > 0]) / arr_size))
    print('{:f}'.format(len([item for item in arr if item < 0]) / arr_size))
    print('{:f}'.format(len([item for item in arr if item == 0]) / arr_size))


if __name__ == "__main__":
    # n = int(input().strip())
    # arr = list(map(int, input().strip().split(' ')))

    input_string = '-4 3 -9 0 4 1'
    arr = list(map(int, input_string.strip().split(' ')))

    plusMinus(arr)