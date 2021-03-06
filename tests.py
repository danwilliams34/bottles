#In this file we shall test bottles.py
import unittest
import bottles

class tests (unittest.TestCase):
    def test1(self):
        song_expected_last_word = 'floor \n'
        song_actual_last_word = bottles.song[-7:]
        self.assertEquals(song_expected_last_word, song_actual_last_word, "last word is wrong, Test 1 fails")
    
    def test2(self):
        index_of_10 = bottles.song.index('10')
        index_of_9 = bottles.song.index('9')
        index_of_5 = bottles.song.index('5')
        index_of_4 = bottles.song.index('4')
        assert index_of_10 < index_of_9 #"10 does not come before 9, Test 2 fails"
        assert index_of_5 > index_of_9 #"5 Does not come after 9, Test 2 Fails"
        assert index_of_5 <index_of_4 #5 does not come before 4, Test 2 fails"
    
    def test3(self):
        assert ('\n0' in bottles.song) #0 is not in bottles.song, Test 3 fails
    
    def test4(self):
        assert ('\n' in bottles.song) #There are no line breaks, Test 4 Fails
        
    def test5(self):
        assert ('\n1 bottles' not in bottles.song) # 1  bottle should not be plural
        assert ('\n1 bottle' in bottles.song) # 1 bottle should be singular
        assert ('\n2 bottles' in bottles.song) #2 bottles should be plural

if __name__ == '__main__':
    unittest.main()
    