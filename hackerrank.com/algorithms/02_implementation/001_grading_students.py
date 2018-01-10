"""
https://www.hackerrank.com/challenges/grading/problem
"""

import sys


def solve(grades):
    for index in range(len(grades)):
        if grades[index] >= 38 and grades[index] % 5 > 2:
            grades[index] += 5 - grades[index] % 5
    return grades


# n = int(input().strip())
# grades = []
# grades_i = 0
# for grades_i in range(n):
#    grades_t = int(input().strip())
#    grades.append(grades_t)

n = 60
grades = []
for grade in range(1, 101):
    grades.append(grade)


result = solve(grades)
print ("\n".join(map(str, result)))