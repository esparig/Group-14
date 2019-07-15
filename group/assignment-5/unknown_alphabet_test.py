"""Unit tests for optional 1 in Assignment 5"""
import unittest
from unknown_alphabet_all import get_alphabets

LEXICON = ["ART", "RAT", "CAT", "CAR", "MIK"]
BAD_LEXICON = ["ART", "BIT", "ANT"]

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
        alphabets = get_alphabets(BAD_LEXICON)
        self.assertEqual(len(alphabets), 0)
        
    def test_get_precedency_rules(self):
        """Test get alphabet: 
        test if the relative order of the letters is correct.
        """
        alphabets = get_alphabets(LEXICON)
        for alphabet in alphabets:
            self.assertLess(alphabet.index('A'), alphabet.index('R'))
            self.assertLess(alphabet.index('T'), alphabet.index('R'))
            self.assertLess(alphabet.index('R'), alphabet.index('C'))
            self.assertLess(alphabet.index('C'), alphabet.index('M'))
