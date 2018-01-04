"""
https://www.hackerrank.com/challenges/py-if-else/problem

Task

Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format

A single line containing a positive integer, n.

Constraints

1 <= n <= 100

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3

Sample Output 0

Weird

Sample Input 1

24

Sample Output 1

Not Weird

Explanation

Sample Case 0: n = 3
n is odd and odd numbers are weird, so we print Weird.

Sample Case 1: n = 24
n > 20 and n is even, so it isn't weird. Thus, we print Not Weird.
"""

import unittest


def find_weird(n):
    if (n % 2 == 1) or (6 <= n <= 20):
        return 'Weird'
    return 'Not Weird'


class Test(unittest.TestCase):
    def test_find_weird(self):
        for n in (n for n in range(1, 101) if n % 2 == 1):
            self.assertEqual(find_weird(n), 'Weird')
        for n in (n for n in range(2, 6) if n % 2 == 0):
            self.assertEqual(find_weird(n), 'Not Weird')
        for n in (n for n in range(6, 21) if n % 2 == 1):
            self.assertEqual(find_weird(n), 'Weird')
        for n in (n for n in range(21, 101) if n % 2 == 0):
            self.assertEqual(find_weird(n), 'Not Weird')


if __name__ == '__main__':
    # n = int(input())
    # print(find_weird(n))

    unittest.main()

