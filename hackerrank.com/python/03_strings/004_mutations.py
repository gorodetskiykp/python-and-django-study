"""
https://www.hackerrank.com/challenges/python-mutations/problem
"""

import unittest


def mutate_string(string, position, character):
    return '{}{}{}'.format(string[:position], character, string[position + 1:])


class Test(unittest.TestCase):

    def test_mutate_string(self):
        self.assertEqual(mutate_string('abracadabra', 5, 'k'), 'abrackdabra')


if __name__ == '__main__':

    unittest.main()
