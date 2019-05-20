import unittest

from anagrams import anagrams0, anagrams1, anagrams2

class TestAnagrams(unittest.TestCase):

    def test_case_sensitive_v0(self):
        self.assertTrue(anagrams0("silent", "listen"))
        self.assertFalse(anagrams0("silent", "listennn"))
        self.assertFalse(anagrams0("silentt", "listen"))
        
    def test_case_sensitive_v1(self):
        self.assertTrue(anagrams1("silent", "listen"))
        self.assertFalse(anagrams1("silent", "listennn"))
        self.assertFalse(anagrams1("silentt", "listen"))

    def test_case_insensitive_v2(self):
        self.assertTrue(anagrams2("Silent", "listen", case_insensitive=True))
        self.assertFalse(anagrams2("Silent", "listen", case_insensitive=False))
        self.assertFalse(anagrams2("silent", "listennn"))
        self.assertFalse(anagrams2("silent", "listennn", case_insensitive=True))
        self.assertFalse(anagrams2("silentt", "listen"))
    
