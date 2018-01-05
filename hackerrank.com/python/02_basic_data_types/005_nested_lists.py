"""
https://www.hackerrank.com/challenges/nested-list/problem
"""

if __name__ == '__main__':
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())

    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    names = list(zip(*students))[0]
    scores = list(zip(*students))[1]

    students = {}
    for i in range(5):
        name = names[i]
        score = scores[i]
        students[name] = score

    second_lowest_score = sorted(set([score for score in students.values()]))[1]

    second_lowest_score_students = sorted([student for student, score in students.items()
                                           if score == second_lowest_score])

    print(*second_lowest_score_students, sep='\n')
