"""Unit tests for optional 1 in Assignment 5"""
import unittest
from unknown_alphabet_optional_1 import get_alphabets

LEXICON = ["ART", "RAT", "CAT", "CAR", "MIK"]

class TestAllUnknownAlphabets(unittest.TestCase):
    """Unit Test Class for getting all possible unknown alphabets.
    """

    def test_len(self):
        """Test get alphabet:
        test if the relative order of the letters is correct.
        """
        alphabets = get_alphabets(LEXICON)
        self.assertEqual(len(alphabets), 84)
        self.assertIn(('T', 'A', 'R', 'C', 'I', 'M', 'K'), alphabets)
