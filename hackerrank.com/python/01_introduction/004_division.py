"""
https://www.hackerrank.com/challenges/python-division/problem

Task

Read two integers and print two lines. The first line should contain integer division,  // . The second line should
contain float division,  / .

You don't need to perform any rounding or formatting operations.

Input Format

The first line contains the first integer, . The second line contains the second integer, .

Output Format

Print the two lines as described above.

Sample Input

4
3

Sample Output

1
1.3333333333333333
"""

import unittest
import random


def integer_division(a: int, b: int) -> int:
    return a // b


def float_division(a: int, b: int) -> float:
    return a / b


class Test(unittest.TestCase):

    def test_integer_division(self):
        for _ in range(100):
            a, b = (random.randint(1, 10**10), random.randint(1, 10**10))
            self.assertEqual(integer_division(a, b), a // b)

    def test_float_division(self):
        for _ in range(100):
            a, b = (random.randint(1, 10**10), random.randint(1, 10**10))
            self.assertEqual(float_division(a, b), a / b)


if __name__ == '__main__':
    # a = int(input())
    # b = int(input())
    # print(integer_division(a, b))
    # print(float_division(a, b))

    unittest.main()
