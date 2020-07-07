"""
You have a positive integer. Try to find out how many digits it has?
Input: A positive Int
Output: An Int.
Example:
number_length(10) == 2
number_length(0) == 1
"""

# def number_length(a: int) -> int:
#     return len(str(a))

number_length = lambda a: len(str(a))

if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2