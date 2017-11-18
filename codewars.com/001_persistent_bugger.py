"""
http://www.codewars.com/kata/persistent-bugger/python

python_version: 2.7.6

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                      # and 4 has only one digit.

persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                      # 1*2*6 = 12, and finally 1*2 = 2.

persistence(4) => 0   # Because 4 is already a one-digit number.
"""


import unittest
from functools import reduce


def persistence(n):
    steps = 0
    while True:
        if n / 10.0 < 1:
            return steps
        else:
            steps += 1
            numbers_list = map(int, str(n))
            n = reduce(lambda a, b: a * b, numbers_list)


"""
Some solutions

http://www.codewars.com/kata/reviews/55c7dba2ea4fa879c4000015/groups/55c81e198daa9ba951000040
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

http://www.codewars.com/kata/reviews/55c7dba2ea4fa879c4000015/groups/55cce4e83ecaf850ac00001a    
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist

http://www.codewars.com/kata/reviews/55c7dba2ea4fa879c4000015/groups/5704aea446edc2e5c4000864
from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1
"""


class Test(unittest.TestCase):
    def test_persistence(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(25), 2)
        self.assertEqual(persistence(999), 4)


if __name__ == "__main__":
    unittest.main()
