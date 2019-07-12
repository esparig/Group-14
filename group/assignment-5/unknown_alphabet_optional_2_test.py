"""Unit tests for Assignment 5"""
import unittest
from unknown_alphabet import get_alphabet

LEXICON = ["ART", "BIT", "ANT"]

class TestUnknownAlphabet(unittest.TestCase):
    """Unit Test Class for Unkownn Alphabet.
    """

    def test_detect_contradictory_rules(self):
        """Test get alphabet: 
        test if the relative order of the letters is correct.
        """
        alphabet = get_alphabet(LEXICON)
        self.assertContains(alphabet, "Lexicon has inconsistent rules:")
        self.assertContains(alphabet, "A comes before B")
        self.assertContains(alphabet, "B comes before A")
