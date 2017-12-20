"""
https://www.hackerrank.com/challenges/python-loops/problem

Task

Read an integer N. For all non-negative integers i < N, print i**2. See the sample for details.

Input Format

The first and only line contains the integer, N.

Constraints

1 <= N <= 20

Output Format

Print N lines, one corresponding to each i.

Sample Input

5

Sample Output

0
1
4
9
16
"""

import unittest
import random


def squares(n: int) -> list:
    return [i**2 for i in range(n)]


class Test(unittest.TestCase):

    def test_squares_2(self):
        self.assertEqual(squares(2), [0, 1])

    def test_squares_3(self):
        self.assertEqual(squares(3), [0, 1, 4])

    def test_squares_4(self):
        self.assertEqual(squares(4), [0, 1, 4, 9])


if __name__ == '__main__':
    n = int(input())

    for i in squares(n):
        print(i)


    unittest.main()
