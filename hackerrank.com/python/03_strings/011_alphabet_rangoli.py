"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""


def get_alphabet(limit):
    limit = limit if limit < 27 else 26
    alphabet = [chr(letter_code) for letter_code in range(ord('a'), ord('a') + limit)]
    return alphabet


def print_rangoli(size):
    alphabet = get_alphabet(size)
    symmetry_alphabet = alphabet[::-1] + alphabet[1:]
    rangoli_size = len(symmetry_alphabet) * 2 - 1
    print(alphabet)
    for row in range(1, size+1):
        print(row, alphabet[-row:])
    center_string = '-'.join(alphabet)
    center_string_size = len(center_string)
    for row in range(1, size+1):
        print('{:-^{}}'.format('-'.join(alphabet[-row:]), center_string_size))
    print('-'.join(alphabet))


if __name__ == '__main__':
    print_rangoli(3)

