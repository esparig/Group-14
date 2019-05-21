import unittest

from anagramchecker_extended import AnagramChecker


class AnagramCheckerTest(unittest.TestCase):
    def test_baseline_functionality(self):
        anagram_checker = AnagramChecker()
        self.assertTrue(anagram_checker.check_anagrams("stressed", "desserts"))
        self.assertFalse(anagram_checker.check_anagrams("stressed", "dessert"))

    def test_same_words(self):
        anagram_checker = AnagramChecker()
        self.assertTrue(anagram_checker.check_anagrams("listen", "silent"))
        self.assertFalse(anagram_checker.check_anagrams("listens", "silent"))

    def test_same_length(self):
        anagram_checker = AnagramChecker()
        self.assertTrue(anagram_checker.check_anagrams("cat", "act"))
        self.assertFalse(anagram_checker.check_anagrams("apple", "pabble"))

    def test_case_sensitive(self):
        anagram_checker = AnagramChecker(is_case_sensitive=True)
        self.assertTrue(anagram_checker.check_anagrams("CAt", "tAC"))
        self.assertFalse(anagram_checker.check_anagrams("CAT", "cat"))

    def test_not_case_sensitive(self):
        anagram_checker = AnagramChecker(is_case_sensitive=False)
        self.assertTrue(anagram_checker.check_anagrams("CAT", "cat"))
        self.assertTrue(anagram_checker.check_anagrams("CAT", "TAC"))

    def test_sentences(self):
        anagram_checker = AnagramChecker()
        self.assertTrue(anagram_checker.check_anagrams("astronomer", "moon starer"))

    def test_punctuation(self):
        anagram_checker = AnagramChecker()
        self.assertTrue(anagram_checker.check_anagrams("Jim Morrison", "Mr. Mojo Risin'"))

    def test_order_matters(self):
        anagram_checker = AnagramChecker(word_order_matters=True)
        self.assertTrue(anagram_checker.check_anagrams("study tar", "dusty rat"))
        self.assertFalse(anagram_checker.check_anagrams("a gentleman", "elegant man"))


if __name__ == '__main__':
    unittest.main()
