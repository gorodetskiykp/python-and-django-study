"""
https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

Task

Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Input Format

The first line contains the first integer, . The second line contains the second integer, .

Constraints

1 <= a <= 10**10
1 <= b <= 10**10

Output Format

Print the three lines as explained above.

Sample Input

3
2

Sample Output

5
1
6

Explanation

3 + 2 -> 5
3 - 2 -> 1
3 * 2 -> 6
"""

import unittest
import random


def summary(a: int, b: int) -> int:
    return a + b


def difference(a: int, b: int) -> int:
    return a - b


def product(a: int, b: int) -> int:
    return a * b


class Test(unittest.TestCase):

    def test_summary(self):
        for _ in range(100):
            a, b = (random.randint(1, 10**10), random.randint(1, 10**10))
            self.assertEqual(summary(a, b), a + b)

    def test_difference(self):
        for _ in range(100):
            a, b = (random.randint(1, 10**10), random.randint(1, 10**10))
            self.assertEqual(difference(a, b), a - b)

    def test_product(self):
        for _ in range(100):
            a, b = (random.randint(1, 10**10), random.randint(1, 10**10))
            self.assertEqual(product(a, b), a * b)


if __name__ == '__main__':
    # a = int(input())
    # b = int(input())
    # print(summary(a, b))
    # print(difference(a, b))
    # print(product(a, b))

    unittest.main()
