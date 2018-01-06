"""
https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

import sys


def diagonalDifference(a):
    main_diagonal = []
    second_diagonal = []
    for row_number, row in enumerate(a):
        main_diagonal.append(row[row_number])
        second_diagonal.append(row[-row_number-1])
    return abs(sum(main_diagonal) - sum(second_diagonal))


if __name__ == "__main__":
    # n = int(input().strip())
    # a = []
    # for a_i in range(n):
    #    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    #    a.append(a_t)

    a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(a)
    print(result)


# https://www.hackerrank.com/challenges/diagonal-difference/editorial
# size = input()
# matrix = []
#
# # reading input
# for _ in xrange(size):
#     row = map(int, raw_input().split())
#     matrix.append(row)
#
# # initialize s1 for right diagonal and s2 for left diagonal
# s1, s2 = 0, 0
#
# # summing up together in just 1 loop, -ve index
# # (-x) in python is actually (size - x)
# for i in xrange(size):
#     s1 += matrix[i][i]
#     s2 += matrix[-i-1][i]
#
# # printing absolute difference
# print abs(s1 - s2)