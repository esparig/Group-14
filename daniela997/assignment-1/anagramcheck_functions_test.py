import unittest

import anagramcheck_functions as anagramcheck


class AnagramCheckerTest(unittest.TestCase):
    """Tests extended functionality from additional challenges.
    This is for functions-only implementation.
    """

    def test_baseline_functionality(self):
        self.assertTrue(anagramcheck.check_anagrams("stressed", "desserts"))
        self.assertFalse(anagramcheck.check_anagrams("stressed", "dessert"))

    def test_same_words(self):
        self.assertTrue(anagramcheck.check_anagrams("listen", "silent"))
        self.assertFalse(anagramcheck.check_anagrams("listens", "silent"))

    def test_same_length(self):
        self.assertTrue(anagramcheck.check_anagrams("cat", "act"))
        self.assertFalse(anagramcheck.check_anagrams("apple", "pabble"))

    def test_case_sensitive(self):
        self.assertTrue(anagramcheck.check_anagrams("CAt", "tAC", is_case_sensitive=True))
        self.assertFalse(anagramcheck.check_anagrams("CAT", "cat", is_case_sensitive=True))

    def test_not_case_sensitive(self):
        self.assertTrue(anagramcheck.check_anagrams("CAT", "cat", is_case_sensitive=False))
        self.assertTrue(anagramcheck.check_anagrams("CAT", "TAC", is_case_sensitive=False))

    def test_sentences(self):
        self.assertTrue(anagramcheck.check_anagrams("astronomer", "moon starer"))

    def test_punctuation(self):
        self.assertTrue(anagramcheck.check_anagrams("Jim Morrison", "Mr. Mojo Risin'"))

    def test_order_matters(self):
        self.assertTrue(anagramcheck.check_anagrams("study tar", "dusty rat", word_order_matters=True))
        self.assertFalse(anagramcheck.check_anagrams("a gentleman", "elegant man", word_order_matters=True))


if __name__ == '__main__':
    unittest.main()
