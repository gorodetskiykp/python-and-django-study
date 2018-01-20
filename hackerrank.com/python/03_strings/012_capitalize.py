"""
https://www.hackerrank.com/challenges/capitalize/problem
"""

import unittest


def capitalize(string):
    # return ' '.join([word[0].upper() + word[1:].lower() for word in string.split()])
    names = []
    for index in range(len(string)):
        if index == 0 and string[index].isalpha():
            names.append(string[index].upper())
        elif string[index-1] == ' ' and string[index].isalpha():
            names.append(string[index].upper())
        else:
            names.append(string[index].lower())
    return ''.join(names)

class Test(unittest.TestCase):

    def test_mutate_string(self):
        self.assertEqual(capitalize('chris alan'), 'Chris Alan')


if __name__ == '__main__':
    unittest.main()


# https://www.hackerrank.com/challenges/capitalize/editorial
# print ' '.join(word.capitalize() for word in raw_input().split(' '))