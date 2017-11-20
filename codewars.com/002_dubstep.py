"""
http://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python

Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he
has decided to take a couple of old songs and make dubstep remixes from them.

Let's assume that a song consists of some number of words. To make the dubstep remix of this song, Polycarpus inserts a
certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the
number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues
together all the words, including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform
into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out
what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

Input

The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length
doesn't exceed 200 characters

Output

Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
# =>  WE ARE THE CHAMPIONS MY FRIEND
"""


import unittest


def song_decoder(song):
    return ' '.join([word for word in song.split('WUB') if word != ''])


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
    def test_song_decoder(self):
        self.assertEqual(song_decoder("AWUBBWUBC"), "A B C")
        self.assertEqual(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C")
        self.assertEqual(song_decoder("WUBAWUBBWUBCWUB"), "A B C")
        self.assertEqual(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"),
                         "WE ARE THE CHAMPIONS MY FRIEND")


if __name__ == "__main__":
    unittest.main()
