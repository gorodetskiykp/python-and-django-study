"""
https://www.hackerrank.com/domains/algorithms/implementation
"""

import sys


def breakingRecords(score):
    highest_scores = [score[0]]
    lowest_scores = [score[0]]
    for points in score[1:]:
        if points > highest_scores[-1]:
            highest_scores.append(points)
        elif points < lowest_scores[-1]:
            lowest_scores.append(points)
    return len(highest_scores[1:]), len(lowest_scores[1:])


if __name__ == "__main__":
    # n = int(input().strip())
    # score = list(map(int, input().strip().split(' ')))

    n = 9
    score = list(map(int, '10 5 20 20 4 5 2 25 1'.strip().split(' ')))

    result = breakingRecords(score)
    print (" ".join(map(str, result)))

    n = 10
    score = list(map(int, '3 4 21 36 10 28 35 5 24 42'.strip().split(' ')))

    result = breakingRecords(score)
    print (" ".join(map(str, result)))


# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/editorial
# n = int(raw_input().strip())
# score = map(int, raw_input().strip().split(' '))
#
# max_score = score[0]
# min_score = score[0]
#
# ans1 = 0
# ans2 = 0
# for val in score:
#     if val > max_score:
#         max_score = val
#         ans1 = ans1 + 1
#     if val < min_score:
#         min_score = val
#         ans2 = ans2 + 1
# print ans1, ans2