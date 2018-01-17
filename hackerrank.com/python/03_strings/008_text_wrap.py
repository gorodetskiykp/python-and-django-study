"""
https://www.hackerrank.com/challenges/text-wrap/problem
"""


def wrap(st, max_width):
    result = []
    for i in range(0,len(st),max_width):
        result.append(st[i:i+max_width])
    return '\n'.join(result)
