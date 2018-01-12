"""
https://www.hackerrank.com/challenges/string-validators/problem
"""

import unittest


def string_check(string):
    answers = [False for _ in range(5)]
    for sign in string:
        answers[0] = answers[0] or sign.isalnum()
        answers[1] = answers[1] or sign.isalpha()
        answers[2] = answers[2] or sign.isdigit()
        answers[3] = answers[3] or sign.islower()
        answers[4] = answers[4] or sign.isupper()
    # print('\n'.join(map(str, answers)))
    return answers


class Test(unittest.TestCase):

    def test_string_check(self):
        self.assertEqual(string_check('qA2'), [True, True, True, True, True])


if __name__ == '__main__':

    unittest.main()


# https://www.hackerrank.com/challenges/string-validators/editorial
# print any([char.isalnum() for char in S])
# print any([char.isalpha() for char in S])
# print any([char.isdigit() for char in S])
# print any([char.islower() for char in S])
# print any([char.isupper() for char in S])