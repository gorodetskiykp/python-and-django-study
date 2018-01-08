"""
https://www.hackerrank.com/challenges/python-string-split-and-join/problem
"""

import unittest


def split_and_join(line):
    return '-'.join(line.split())


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(split_and_join('this is a string'), 'this-is-a-string')


if __name__ == '__main__':

    unittest.main()
