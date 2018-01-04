"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""

import sys


def solve(*args):
    score = [0, 0]
    for position in range(3):
        if args[position] > args[position+3]:
            score[0] += 1
        elif args[position] < args[position+3]:
            score[1] += 1
    return score


# a0, a1, a2 = input().strip().split(' ')
# a0, a1, a2 = [int(a0), int(a1), int(a2)]
# b0, b1, b2 = input().strip().split(' ')
# b0, b1, b2 = [int(b0), int(b1), int(b2)]

input_string = '5 6 7'
a0, a1, a2 = input_string.strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
input_string = '3 6 10'
b0, b1, b2 = input_string.strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))


# https://www.hackerrank.com/challenges/compare-the-triplets/editorial
# a_triplet = map(int, input().split())
# b_triplet = map(int, input().split())
# alice_points = 0
# bob_points = 0
# for a_val, b_val in zip(a_triplet, b_triplet):
#     if a_val < b_val:
#         bob_points += 1
#     elif a_val > b_val:
#         alice_points += 1
# print(alice_points, bob_points)