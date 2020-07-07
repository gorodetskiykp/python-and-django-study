"""
Check is the given number is even or not. Your function shoudl return True if the number is even, andFalse if the number is odd.
Input: Int.
Output: Bool.
Example:
    is_even(2) == True
    is_even(5) == False
    is_even(0) == True
How it’s used: (math is used everywhere)
Precondition: both given ints should be between -1000 and 1000
"""


def is_even(num: int) -> bool:
    return num % 2 == 0


# def is_even(num: int) -> bool:
#     return not num%2


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
