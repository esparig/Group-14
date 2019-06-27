"""Unit tests for Assignment 3"""
import unittest

from word_search import create_lexicon, traverse_lexicon, words_from_grid


LEXICON = create_lexicon(["CAR", "CARD", "CART", "CAT"])
GRID = [['A', 'A', 'R'], ['T', 'C', 'D']]

class TestWordSearch(unittest.TestCase):
    """Unit Test Class for Binary Tree.
    """

    def test_create_lexicon(self):
        """Test create_lexicon and traverse_lexicon:
        - Using words.txt containing 235886 words.
        """
        with open("words.txt") as file:
            list_words = file.read().splitlines()
        my_lexicon = create_lexicon(list_words)
        new_list_words = []
        traverse_lexicon("", my_lexicon, new_list_words)
        self.assertEqual(list_words.sort(), new_list_words.sort())

    def test_is_word(self):
        """Test if a given word is in the lexicon
        """
        self.assertTrue(LEXICON.is_word("CAR"))
        self.assertTrue(LEXICON.is_word("CARD"))
        self.assertTrue(LEXICON.is_word("CART"))
        self.assertTrue(LEXICON.is_word("CAT"))

        self.assertFalse(LEXICON.is_word("DOG"))
        self.assertFalse(LEXICON.is_word("C"))
        self.assertFalse(LEXICON.is_word("CA"))
        self.assertFalse(LEXICON.is_word("CASH"))

    def test_is_prefix(self):
        """Test if a given word is in the lexicon
        """
        self.assertTrue(LEXICON.is_prefix("C"))
        self.assertTrue(LEXICON.is_prefix("CA"))

        self.assertFalse(LEXICON.is_prefix("DOG"))
        self.assertFalse(LEXICON.is_prefix("CAT"))

    def test_words_from_grid(self):
        """Test words from grid.
        """
        self.assertEqual(words_from_grid(LEXICON, GRID, 2, 3),
                         set(["CAT", "CAR", "CARD"]))
