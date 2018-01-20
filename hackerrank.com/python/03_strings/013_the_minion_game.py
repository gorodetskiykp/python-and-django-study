"""
https://www.hackerrank.com/challenges/the-minion-game/problem
"""

import unittest

VOWELS = 'AEIOU'


def minion_game(string):
    string = string.upper()
    player_consonants_name = 'Stuart'
    player_vowels_name = 'Kevin'
    first_letter_score = sum(range(len(string), 0, -2))
    print(list(range(len(string), 0, -2)))
    second_letter_score = sum(range(len(string)-1, 0, -2))
    print(list(range(len(string)-1, 0, -2)))
    if string[0] in VOWELS:
        player_vowels_score, player_consonants_score = first_letter_score, second_letter_score
    else:
        player_vowels_score, player_consonants_score = second_letter_score, first_letter_score
    if player_consonants_score > player_vowels_score:
        return '{} {}'.format(player_consonants_name, player_consonants_score)
    elif player_consonants_score < player_vowels_score:
        return '{} {}'.format(player_vowels_name, player_vowels_score)
    else:
        return 'Draw'


class Test(unittest.TestCase):
    def test_minion_game(self):
        self.assertEqual(minion_game('CABARET'), 'Stuart 12')


if __name__ == '__main__':
    unittest.main()
