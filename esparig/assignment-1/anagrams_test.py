"""Unit tests for first assignment"""
import unittest

from anagrams import anagrams

class TestAnagrams(unittest.TestCase):
    """Unit Test Class for Anagrams"""

    def test_case_sensitive(self):
        """Tests for case sensitive strings"""
        self.assertTrue(anagrams("silent", "listen"))
        self.assertFalse(anagrams("silent", "listennn"))
        self.assertFalse(anagrams("silentt", "listen"))
        self.assertFalse(anagrams("Silent", "listen", case_sensitive=True))

    def test_case_insensitive(self):
        """Tests for case insensitive strings"""
        self.assertTrue(anagrams("Silent", "listen", case_sensitive=False))
        self.assertFalse(anagrams("silent", "listennn", case_sensitive=False))

    def test_case_sentences(self):
        """Tests for sentences"""
        self.assertTrue(anagrams("So dark the con of man", "Madonna of the Rocks",
                                 case_sensitive=False, is_sentence=True))
        self.assertFalse(anagrams("So dark the con of man", "Madonna of the Rocks",
                                  case_sensitive=True, is_sentence=True))
        self.assertFalse(anagrams("So dark the con of man", "Madonna of the Rocks",
                                  case_sensitive=False,
                                  is_sentence=True, corresponding_words=True))
        self.assertTrue(anagrams("Elvis cried", "Lives cider",
                                 case_sensitive=False, is_sentence=True, corresponding_words=True))
