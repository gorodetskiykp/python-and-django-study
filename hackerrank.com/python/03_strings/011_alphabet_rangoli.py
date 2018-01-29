"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""


def get_alphabet(limit):
    limit = limit if limit < 27 else 26
    alphabet = [chr(letter_code) for letter_code 
                                 in range(ord('a'), ord('a') + limit)]
    return alphabet


def print_rangoli(size):
    alphabet = get_alphabet(size)
    symmetry_alphabet = alphabet[::-1] + alphabet[1:]
    center_size = len(symmetry_alphabet)
    ragnoli_lists = []
    ragnoli_lists.append(symmetry_alphabet[:])
    
    for letter_index in range(size-1): 
        symmetry_alphabet.remove(alphabet[letter_index])
        symmetry_alphabet.remove(alphabet[letter_index+1])
        ragnoli_lists.append(symmetry_alphabet[:])
        ragnoli_lists.insert(0, symmetry_alphabet[:]) 
   
    for row in ragnoli_lists:
        print('{:-^{}}'.format('-'.join(row), center_size * 2 - 1))
    
    
if __name__ == '__main__':
    print_rangoli(20)


#https://www.hackerrank.com/challenges/alphabet-rangoli/editorial
#n = int(raw_input())
#for i in range(n):
#    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
#    print((s+s[::-1][1:]).center(n*4-3, '-'))
#
#for i in range(n-1):
#    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
#    print((s+s[::-1][1:]).center(n*4-3, '-'))
