"""
https://www.hackerrank.com/challenges/python-string-formatting/problem
"""


def print_formatted(number):
    size = len(bin(number)[2:])
    for item in range(1, number+1):
        print('{0:>{4}}{1:>{5}}{2:>{5}}{3:>{5}}'.
              format(item, oct(item)[2:], hex(item)[2:].upper(), bin(item)[2:], size, size+1))


if __name__ == '__main__':
    print_formatted(2)


# https://www.hackerrank.com/challenges/python-string-formatting/editorial
# def fun(N):
#     width = len(bin(N)) - 2
#     for i in range(1,N+1):
#         print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)
#
# n = input()
# fun(n)
#
#
# n = int(raw_input())
# spacing = len(bin(n)[2:])
#
# for i in range(1,n+1):
#     print str(i).rjust(spacing, ' '),str(oct(i)[1:]).rjust(spacing, ' '),str(hex(i)[2:].upper()).rjust(spacing, ' '),str(bin(i)[2:]).rjust(spacing, ' ')
