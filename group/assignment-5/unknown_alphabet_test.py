"""Unit tests for Assignment 5"""
import unittest
from unknown_alphabet import create_lexicon, get_alphabet

LEXICON = create_lexicon(["ART", "RAT", "CAT", "CAR", "MI"])

class TestUnknownAlphabet(unittest.TestCase):
    """Unit Test Class for Unkownn Alphabet.
    """

    def test_get_alphabet(self):
        """Test get alphabet: 
        test if the relative order of the letters is correct.
        """
        alphabet = get_alphabet(LEXICON)
        self.assertLess(alphabet.index('A'), alphabet.index('R'))
        self.assertLess(alphabet.index('T'), alphabet.index('R'))
        self.assertLess(alphabet.index('R'), alphabet.index('C'))
        self.assertLess(alphabet.index('C'), alphabet.index('M'))
