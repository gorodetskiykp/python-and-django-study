"""
https://www.hackerrank.com/challenges/whats-your-name/problem
"""

import unittest


def print_full_name(a, b):
    return 'Hello {} {}! You just delved into python.'.format(a, b)


class Test(unittest.TestCase):

    def test_print_full_name(self):
        self.assertEqual(print_full_name('Guido', 'Rossum'), 'Hello Guido Rossum! You just delved into python.')


if __name__ == '__main__':

    unittest.main()
