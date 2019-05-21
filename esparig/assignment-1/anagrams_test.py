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
        self.assertFalse(anagrams("Silent", "listen", case_insensitive=False))

    def test_case_insensitive(self):
        """Tests for case insensitive strings"""
        self.assertTrue(anagrams("Silent", "listen", case_insensitive=True))
        self.assertFalse(anagrams("silent", "listennn", case_insensitive=True))

    def test_case_sentences(self):
        """Tests for sentences"""
        self.assertTrue(anagrams("So dark the con of man", "Madonna of the Rocks",
                                 case_insensitive=True, is_sentence=True))
