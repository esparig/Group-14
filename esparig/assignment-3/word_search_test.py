"""Unit tests for Assignment 3"""
import unittest
from typing import List
from word_search import Lexicon, words_from_grid


class TestWordSearch(unittest.TestCase):
    """Unit Test Class for Binary Tree.
    """

    def setUp(self):

        def create_lexicon(words: List[str]) -> Lexicon:
            """Initialize a lexicon.
            """
            dummy_head = Lexicon(None, False, [])
            for word in words:
                lexicon = dummy_head
                for char in word:
                    if not lexicon.next:
                        elem = Lexicon(char, False, [])
                        lexicon.next.append(elem)
                    else:
                        found = False
                        for elem in lexicon.next:
                            if char == elem.chr:
                                found = True
                                break
                        if not found:
                            elem = Lexicon(char, False, [])
                            lexicon.next.append(elem)
                    lexicon = elem
                lexicon.ends = True
            return dummy_head

        self.my_lexicon = create_lexicon(["CAR", "CARD", "CART", "CAT"])
        self.my_grid = [['A', 'A', 'R'], ['T', 'C', 'D']]

    def test_is_word(self):
        """Test if a given word is in the lexicon
        """
        self.assertTrue(self.my_lexicon.is_word("CAR"))
        self.assertTrue(self.my_lexicon.is_word("CARD"))
        self.assertTrue(self.my_lexicon.is_word("CART"))
        self.assertTrue(self.my_lexicon.is_word("CAT"))

        self.assertFalse(self.my_lexicon.is_word("DOG"))
        self.assertFalse(self.my_lexicon.is_word("C"))
        self.assertFalse(self.my_lexicon.is_word("CA"))
        self.assertFalse(self.my_lexicon.is_word("CASH"))

    def test_is_prefix(self):
        """Test if a given word is in the lexicon
        """
        self.assertTrue(self.my_lexicon.is_prefix("C"))
        self.assertTrue(self.my_lexicon.is_prefix("CA"))

        self.assertFalse(self.my_lexicon.is_prefix("DOG"))
        self.assertFalse(self.my_lexicon.is_prefix("CAT"))

    def test_words_from_grid(self):
        """Test words from grid.
        """
        self.assertEqual(words_from_grid(self.my_lexicon, self.my_grid, 2, 3),
                         set(["CAT", "CAR", "CARD"]))
