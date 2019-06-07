"""Unit tests for Assignment 3"""
import unittest
from typing import List
from word_search import Lexicon

class TestWordSearch(unittest.TestCase):
    """Unit Test Class for Binary Tree.
    """

    def setUp(self):
        
        def create_lexicon(words: List[str]) -> Lexicon:
            dummy_head = Lexicon(None, False, [])
            for word in words:
                lexicon = dummy_head
                for w in word:
                    if len(lexicon.next) == 0:
                        elem = Lexicon(w, False, [])
                        lexicon.next.append(elem)
                    else:
                        found = False
                        for elem in lexicon.next:
                            if w == elem.chr:
                                found = True
                                break
                        if not found:
                            elem = Lexicon(w, False, [])          
                            lexicon.next.append(elem)
                    lexicon = elem
                lexicon.ends = True
            return dummy_head
        
        self.my_lexicon = create_lexicon(["CAR", "CARD", "CART", "CAT"])
        print(self.my_lexicon.chr, self.my_lexicon.next[0].chr, self.my_lexicon.next[0].next[0].chr) 
        
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
        
    def test_is_preffix(self):
        """Test if a given word is in the lexicon
        """
        self.assertTrue(self.my_lexicon.is_preffix("C"))
        self.assertTrue(self.my_lexicon.is_preffix("CA"))
        
        self.assertFalse(self.my_lexicon.is_preffix("DOG"))
        self.assertFalse(self.my_lexicon.is_preffix("CAS"))
