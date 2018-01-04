"""
https://www.hackerrank.com/challenges/write-a-function/problem

We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to
the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300
and 2500 are NOT leap years. Source - http://www.timeanddate.com/date/leapyear.html

Task

You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

Input Format

Read y, the year that needs to be checked.

Constraints

1900 <= y <= 10**5

Output Format

Output is taken care of by the template. Your function must return a boolean value (True/False)

Sample Input

1990

Sample Output

False

Explanation

1990 is not a multiple of 4 hence it's not a leap year.
"""

import unittest


def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True

    return leap


# def is_leap(year):
#     return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


class Test(unittest.TestCase):

    def test_is_leap_1900(self):
        self.assertEqual(is_leap(1900), False)

    def test_is_leap_2000(self):
        self.assertEqual(is_leap(2000), True)

    def test_is_leap_2400(self):
        self.assertEqual(is_leap(2400), True)

    def test_is_leap_1800(self):
        self.assertEqual(is_leap(1800), False)


if __name__ == '__main__':

    unittest.main()
