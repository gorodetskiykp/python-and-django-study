"""
https://www.hackerrank.com/challenges/between-two-sets/problem
"""

import sys

def getTotalX(a, b):
    x_list = []
    for x in range(max(a), min(b)+1, min(a)):
        if not any([x % a_item for a_item in a]) and not any([b_item % x for b_item in b]):
            x_list.append(x)
    return len(x_list)

if __name__ == "__main__":
    # n, m = input().strip().split(' ')
    # n, m = [int(n), int(m)]
    # a = list(map(int, input().strip().split(' ')))
    # b = list(map(int, input().strip().split(' ')))

    n, m = '2 3'.strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, '2 4'.strip().split(' ')))
    b = list(map(int, '16 32 96'.strip().split(' ')))

    total = getTotalX(a, b)
    print(total)