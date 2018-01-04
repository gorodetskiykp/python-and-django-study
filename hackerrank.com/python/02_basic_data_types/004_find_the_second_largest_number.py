"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

if __name__ == '__main__':
    # n = int(input())
    # arr = map(int, input().split())
    input_string = '2 3 6 6 5'
    arr = map(int, input_string.split())
    print(sorted(list(set(arr)))[-2])

