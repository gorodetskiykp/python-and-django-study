"""
https://www.hackerrank.com/challenges/mini-max-sum/problem
"""

import sys


def miniMaxSum(arr):
    print(sum(sorted(arr)[:-1]), sum(sorted(arr)[1:]))


if __name__ == "__main__":
    # arr = list(map(int, input().strip().split(' ')))

    input_string = '1 2 3 4 5'
    arr = list(map(int, input_string.strip().split(' ')))

    miniMaxSum(arr)
