"""
https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

import sys

def appleAndOrange(s, t, a, b, apple, orange):
    fall_on_house = [0, 0]
    for app in apple:
        if s <= a + app <= t:
            fall_on_house[0] += 1
    for ora in orange:
        if s <= b + ora <= t:
            fall_on_house[1] += 1
    return fall_on_house

if __name__ == "__main__":
    # s, t = input().strip().split(' ')
    # s, t = [int(s), int(t)]
    # a, b = input().strip().split(' ')
    # a, b = [int(a), int(b)]
    # m, n = input().strip().split(' ')
    # m, n = [int(m), int(n)]
    # apple = list(map(int, input().strip().split(' ')))
    # orange = list(map(int, input().strip().split(' ')))

    s, t = '7 11'.split(' ')
    s, t = [int(s), int(t)]
    a, b = '5 15'.split(' ')
    a, b = [int(a), int(b)]
    m, n = '3 2'.split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, '-2 2 1'.split(' ')))
    orange = list(map(int, '5 -6'.split(' ')))

    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))