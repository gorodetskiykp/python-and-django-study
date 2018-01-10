"""
https://www.hackerrank.com/challenges/find-a-string/problem
"""

import unittest


def count_substring(string, sub_string):
    contains = 0
    for index in range(len(string) - len(sub_string) + 1):
        if sub_string == string[index:index+len(sub_string)]:
            contains += 1
    return contains


class Test(unittest.TestCase):

    def test_mutate_string(self):
        self.assertEqual(count_substring('ABCDCDC', 'CDC'), 2)


if __name__ == '__main__':

    unittest.main()


# https://www.hackerrank.com/challenges/find-a-string/editorial
# import re
# a = raw_input()
# b = raw_input()
# match = re.findall('(?='+b+')',a)
# print len(match)