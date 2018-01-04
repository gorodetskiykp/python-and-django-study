"""
https://www.hackerrank.com/challenges/python-print/problem

Read an integer N.

Without using any string methods, try to print the following:

123...N

Note that "..." represents the values in between.

Input Format

The first line contains an integer N.

Output Format

Output the answer as explained in the task.

Sample Input

3

Sample Output

123
"""

import unittest


def print_numbers(numbers_limit):
    return ''.join([str(number) for number in range(1, numbers_limit+1)])


class Test(unittest.TestCase):

    def test_number_5(self):
        self.assertEqual(print_numbers(5), '12345')

    def test_number_10(self):
        self.assertEqual(print_numbers(10), '12345678910')


if __name__ == '__main__':

    unittest.main()
