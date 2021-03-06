"""
Try to find out how many zeros a given number has at the end.
Input: A positive Int
Output: An Int.
Example:
end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
"""

def end_zeros(num: int) -> int:
    zeros = 0
    for digit in str(num)[::-1]:
        if digit == '0':
            zeros += 1 
        else: 
            return zeros
    return zeros


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2