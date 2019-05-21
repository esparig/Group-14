import unittest

from anagrams import *

class TestAnagrams(unittest.TestCase):

    def test_case_sensitive(self):
        self.assertTrue(anagrams("silent", "listen"))
        self.assertFalse(anagrams("silent", "listennn"))
        self.assertFalse(anagrams("silentt", "listen"))
        self.assertFalse(anagrams("Silent", "listen", case_insensitive=False))

        

    def test_case_insensitive(self):
        self.assertTrue(anagrams("Silent", "listen", case_insensitive=True))
        self.assertFalse(anagrams("silent", "listennn", case_insensitive=True))
    
