"""
https://www.hackerrank.com/challenges/designer-door-mat/problem
"""

N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for row in range(0, N*2, 2):
    f = '.|.'*(row+1) if row/2 < N//2 else '.|.'*(N*2 - (row+1))
    if row+1 == N:
        f = 'WELCOME'
    print(f.center(N*3, '-'))
