"""
https://www.hackerrank.com/challenges/swap-case/problem
"""

import unittest


def swap_string(input_string):
    return input_string.swapcase()


class Test(unittest.TestCase):

    def test_swap_1(self):
        self.assertEqual(swap_string('HackerRank.com presents "Pythonist 2".'), 'hACKERrANK.COM PRESENTS "pYTHONIST 2".')


if __name__ == '__main__':

    unittest.main()
