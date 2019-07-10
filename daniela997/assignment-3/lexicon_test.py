import unittest

from lexicon import Lexicon, LetterNode


class LexiconTest(unittest.TestCase):
    def test_letter_node(self):
        node = LetterNode()
        self.assertEqual(node.children, {})

    def test_child_index(self):
        lexicon = Lexicon()
        index = lexicon.get_child_index(child_character="C")
        self.assertEqual(2, index)

    def test_child_index_unique(self):
        lexicon = Lexicon()
        index1 = lexicon.get_child_index(child_character="C")
        index2 = lexicon.get_child_index(child_character="D")
        self.assertNotEqual(index1, index2)

    def test_is_word(self):
        lexicon = Lexicon()
        lexicon.add_words("CAT")
        self.assertTrue(lexicon.is_word("CAT"))
        self.assertFalse(lexicon.is_word("CA"))
        self.assertFalse(lexicon.is_word("DOG"))
        self.assertFalse(lexicon.is_word(""))

    def test_is_prefix(self):
        lexicon = Lexicon()
        lexicon.add_words("CAT")
        self.assertTrue(lexicon.is_prefix("CAT"))
        self.assertTrue(lexicon.is_prefix("CA"))
        self.assertFalse(lexicon.is_prefix("DOG"))
        self.assertFalse(lexicon.is_prefix(""))


if __name__ == '__main__':
    unittest.main()
